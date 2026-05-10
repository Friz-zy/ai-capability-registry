#!/usr/bin/env python3
"""Discover MCP servers into mcp-catalog.d chunks from configurable sources.

The importer is intentionally conservative: imported entries are disabled by
default and must be manually reviewed/promoted before use. It only keeps
remote HTTPS endpoints and OCI/Docker packages; npm/pypi/node/python direct
runners are ignored by policy.
"""

from __future__ import annotations

import json
import os
import re
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from registry_lib import ROOT, RegistryError, load_yaml, write_text

MCP_CATALOG_DIR = ROOT / "mcp-catalog.d"
SOURCES_FILE = ROOT / "registry" / "mcp-sources.yaml"


def parse_yaml_text(content: str) -> dict[str, Any] | None:
    try:
        import yaml  # type: ignore
    except ImportError:
        yaml = None
    if yaml is not None:
        data = yaml.safe_load(content)
        return data if isinstance(data, dict) else None
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".yaml", delete=False) as temp:
        temp.write(content)
        temp_path = Path(temp.name)
    try:
        data = load_yaml(temp_path)
    except RegistryError:
        return None
    finally:
        temp_path.unlink(missing_ok=True)
    return data if isinstance(data, dict) else None


def fetch_json(url: str) -> Any:
    request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "ai-capability-registry"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"Accept": "text/plain", "User-Agent": "ai-capability-registry"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8")


def fetch_html(url: str) -> str:
    request = urllib.request.Request(url, headers={"Accept": "text/html", "User-Agent": "ai-capability-registry"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8")


def slug(value: str) -> str:
    value = value.strip().lower().replace("/", "-")
    value = re.sub(r"[^a-z0-9._-]+", "-", value).strip("-")
    return value or "unknown"


def keywords_for(*values: Any) -> list[str]:
    text = " ".join(str(value or "") for value in values).lower()
    words = set(re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", text.replace("_", "-")))
    stop = {"mcp", "server", "servers", "model", "context", "protocol", "official", "the", "and", "for", "with"}
    return sorted(word for word in words if len(word) > 2 and word not in stop)[:12]


def docker_args(image: str, env_names: list[str] | None = None, extra_args: list[str] | None = None) -> list[str]:
    args = ["run", "--rm", "-i"]
    for name in env_names or []:
        args.extend(["-e", name])
    args.append(image)
    args.extend(extra_args or [])
    return args


def allow_type(import_policy: dict[str, Any], runtime: str) -> bool:
    allow_list = import_policy.get("allow", [])
    deny_list = import_policy.get("deny", [])
    if allow_list:
        return runtime in allow_list
    if deny_list:
        return runtime not in deny_list
    return True


class SourceHandler:
    def __init__(self, source: dict[str, Any]):
        self.source = source
        self.id = str(source.get("id") or "unknown")
        self.name = str(source.get("name") or self.id)
        self.trust = str(source.get("trust") or "candidate")
        self.import_policy = source.get("import_policy", {})

    def discover(self) -> list[dict[str, Any]]:
        raise NotImplementedError

    def write_chunk(self, entries: list[dict[str, Any]], existing_path: Path) -> list[dict[str, Any]]:
        from copy import deepcopy
        previous = self.load_existing_entries(existing_path)
        seen: set[str] = set()
        for entry in entries:
            entry_id = str(entry.get("id") or "")
            seen.add(entry_id)
            prior = previous.get(entry_id)
            if prior:
                for key in ("enabled", "trust", "default_mode", "keywords", "skill"):
                    if key in prior:
                        entry[key] = prior[key]
                if isinstance(prior.get("security"), dict):
                    security = dict(entry.get("security", {}))
                    prior_security = prior["security"]
                    for key in ("reviewed", "data_risk", "permission_default", "disabled_by_default", "deny"):
                        if key in prior_security:
                            security[key] = prior_security[key]
                    entry["security"] = security
        for entry_id, prior in previous.items():
            if entry_id not in seen:
                entries.append(prior)
        entries = sorted(entries, key=lambda item: str(item.get("id") or ""))
        self.write_yaml_chunk(existing_path, entries)
        return entries

    def load_existing_entries(self, path: Path) -> dict[str, dict[str, Any]]:
        if not path.exists():
            return {}
        try:
            data = load_yaml(path)
        except Exception:
            return {}
        if not isinstance(data, dict):
            return {}
        entries: dict[str, dict[str, Any]] = {}
        for item in data.get("mcp_servers", []):
            if isinstance(item, dict) and isinstance(item.get("id"), str):
                entries[str(item["id"])] = item
        return entries

    def yaml_scalar(self, value: Any) -> str:
        if value is True:
            return "true"
        if value is False:
            return "false"
        if value is None:
            return "null"
        return json.dumps(str(value), ensure_ascii=False)

    def is_empty_value(self, value: Any) -> bool:
        return value is None or value == "" or value == [] or value == {}

    def append_yaml(self, lines: list[str], key: str, value: Any, indent: int = 0) -> None:
        prefix = " " * indent
        if self.is_empty_value(value):
            return
        if isinstance(value, dict):
            if not value:
                return
            lines.append(f"{prefix}{key}:")
            for child_key, child_value in value.items():
                self.append_yaml(lines, child_key, child_value, indent + 2)
        elif isinstance(value, list):
            if not value:
                return
            lines.append(f"{prefix}{key}:")
            for item in value:
                if isinstance(item, dict):
                    lines.append(f"{prefix}  -")
                    for child_key, child_value in item.items():
                        self.append_yaml(lines, child_key, child_value, indent + 4)
                else:
                    lines.append(f"{prefix}  - {self.yaml_scalar(item)}")
        else:
            lines.append(f"{prefix}{key}: {self.yaml_scalar(value)}")

    def write_yaml_chunk(self, path: Path, entries: list[dict[str, Any]]) -> None:
        lines = [
            "# Auto-synced by scripts/discover-mcp.py.",
            "# Imported entries are disabled by default; promote manually after review.",
            f"source: {self.yaml_scalar(self.id)}",
            "mcp_servers:",
        ]
        for entry in entries:
            entry_id = entry.get("id")
            lines.append(f"  - id: {self.yaml_scalar(entry_id)}")
            for key, value in entry.items():
                if key == "id":
                    continue
                self.append_yaml(lines, key, value, 4)
        write_text(path, "\n".join(lines))


class RestApiHandler(SourceHandler):
    def __init__(self, source: dict[str, Any]):
        super().__init__(source)
        self.url = str(source.get("url") or "")

    def discover(self) -> list[dict[str, Any]]:
        entries: dict[str, dict[str, Any]] = {}
        cursor = None
        for _ in range(20):
            params = {"limit": "100"}
            if cursor:
                params["cursor"] = cursor
            url = self.url + ("?" + urllib.parse.urlencode(params) if "?" not in self.url else "&" + urllib.parse.urlencode(params))
            try:
                data = fetch_json(url)
            except urllib.error.URLError:
                break
            for record in data.get("servers", []):
                entry = self.official_entry(record)
                if entry:
                    entries[entry["id"]] = entry
            cursor = data.get("metadata", {}).get("nextCursor")
            if not cursor:
                break
        return sorted(entries.values(), key=lambda item: item["id"])

    def official_entry(self, record: dict[str, Any]) -> dict[str, Any] | None:
        server = record.get("server", {})
        meta = record.get("_meta", {}).get("io.modelcontextprotocol.registry/official", {})
        if meta.get("status") != "active" or meta.get("isLatest") is not True:
            return None

        remotes = [remote for remote in server.get("remotes", []) if str(remote.get("url", "")).startswith("https://") and remote.get("type") in {"streamable-http", "sse"}]
        docker_packages = [pkg for pkg in server.get("packages", []) if pkg.get("registryType") == "oci" and pkg.get("identifier")]
        if not remotes and not docker_packages:
            return None

        name = str(server.get("name") or "")
        title = str(server.get("title") or name.rsplit("/", 1)[-1])
        description = str(server.get("description") or "No description.")
        hosted_url = str(remotes[0]["url"]) if remotes else None
        image = str(docker_packages[0]["identifier"]) if docker_packages else None
        env_names = [str(env.get("name")) for env in docker_packages[0].get("environmentVariables", []) if env.get("name")] if docker_packages else []

        if hosted_url and not allow_type(self.import_policy, "hosted_https"):
            hosted_url = None
        if image and not allow_type(self.import_policy, "docker_oci"):
            image = None

        if not hosted_url and not image:
            return None

        runtime = "hosted_or_docker" if hosted_url and image else "hosted_https" if hosted_url else "docker"
        transport = "streamable_http_or_stdio" if hosted_url and image else "streamable_http" if hosted_url else "stdio"
        source_type = runtime

        source: dict[str, Any] = {
            "type": source_type,
            "provider": self.id,
            "registry_url": self.url,
        }
        if hosted_url:
            source["hosted_url"] = hosted_url
        if image:
            source["image"] = image
            source["docker"] = {"command": "docker", "args": docker_args(image, env_names)}
        repo = server.get("repository", {})
        if isinstance(repo, dict) and repo.get("url"):
            source["repo"] = str(repo["url"])

        return {
            "id": slug(name),
            "exists": True,
            "enabled": False,
            "name": title,
            "description": description,
            "source": source,
            "security": {
                "local_code_execution": False if hosted_url else "isolated_container_only",
                "sandboxed": bool(image) or bool(hosted_url),
                "reviewed": False,
                "data_risk": "unknown_until_reviewed",
                "permission_default": "manual_review",
            },
            "transport": {"type": transport},
            "keywords": keywords_for(name, title, description),
            "trust": self.trust,
            "runtime": runtime,
            "default_mode": "manual_review",
        }


class GithubYamlHandler(SourceHandler):
    def __init__(self, source: dict[str, Any]):
        super().__init__(source)
        self.repo = str(source.get("repo") or "")
        self.catalog_path = str(source.get("catalog_path") or "")
        self.catalog_pattern = str(source.get("catalog_pattern") or "*.yaml")
        self.raw_base = f"https://raw.githubusercontent.com/{self.repo.split('github.com/', 1)[-1].strip('/').replace('/', '/', 1)}/main"

    def github_api(self, path: str) -> Any:
        api_url = f"https://api.github.com/repos/{self.repo.split('github.com/', 1)[-1].strip('/')}/contents/{path}"
        request = urllib.request.Request(api_url, headers={"Accept": "application/json", "User-Agent": "ai-capability-registry"})
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))

    def discover(self) -> list[dict[str, Any]]:
        entries: dict[str, dict[str, Any]] = {}
        repo_path = self.repo.split("github.com/", 1)[-1].strip("/")
        api_url = f"https://api.github.com/repos/{repo_path}/contents/{self.catalog_path}"
        try:
            listing = fetch_json(api_url)
        except urllib.error.URLError:
            return []
        processed = 0
        for item in listing:
            if item.get("type") != "dir" or not item.get("name"):
                continue
            server_name = item["name"]
            file_url = f"https://raw.githubusercontent.com/{repo_path}/main/{self.catalog_path}/{server_name}/server.yaml"
            try:
                content = fetch_text(file_url)
            except urllib.error.URLError:
                continue
            data = parse_yaml_text(content)
            if isinstance(data, dict):
                entry = self.docker_registry_entry(server_name, data)
                if entry:
                    entries[entry["id"]] = entry
            processed += 1
        return sorted(entries.values(), key=lambda item: item["id"])

    def docker_registry_entry(self, name: str, data: dict[str, Any]) -> dict[str, Any] | None:
        image = data.get("image")
        if not image:
            return None
        if not allow_type(self.import_policy, "docker_oci"):
            return None
        title = str(data.get("about", {}).get("title") or data.get("name") or name)
        description = str(data.get("about", {}).get("description") or "No description.")
        config_secrets = data.get("config", {}).get("secrets", [])
        env_names = [str(secret.get("env")) for secret in config_secrets if isinstance(secret, dict) and secret.get("env")]
        run_command = data.get("run", {}).get("command", [])
        extra_args = [str(arg) for arg in run_command] if isinstance(run_command, list) else []
        source = {
            "type": "docker",
            "provider": self.id,
            "registry_url": f"{self.repo}/tree/main/{self.catalog_path}/{name}",
            "image": str(image),
            "docker": {"command": "docker", "args": docker_args(str(image), env_names, extra_args)},
        }
        project = data.get("source", {}).get("project")
        commit = data.get("source", {}).get("commit")
        if project:
            source["repo"] = str(project)
        if commit:
            source["commit"] = str(commit)
        allow_hosts = data.get("run", {}).get("allowHosts", [])
        tags = data.get("meta", {}).get("tags", [])
        return {
            "id": slug(str(data.get("name") or name)),
            "exists": True,
            "enabled": False,
            "name": title,
            "description": description,
            "source": source,
            "security": {
                "local_code_execution": "isolated_container_only",
                "sandboxed": True,
                "reviewed": self.trust == "reviewed",
                "data_risk": "unknown_until_reviewed",
                "permission_default": "manual_review",
                "network_allow_hosts": allow_hosts if isinstance(allow_hosts, list) else [],
            },
            "transport": {"type": "stdio"},
            "keywords": sorted(set(keywords_for(title, description) + [str(tag) for tag in tags if tag])),
            "trust": self.trust,
            "runtime": "docker",
            "default_mode": "manual_review",
        }


class GithubReadmeTableHandler(SourceHandler):
    def discover(self) -> list[dict[str, Any]]:
        try:
            content = fetch_text(f"https://raw.githubusercontent.com/{self.repo.split('github.com/', 1)[-1].strip('/')}/main/README.md")
        except urllib.error.URLError:
            return []
        return self.parse_readme_table(content)

    def parse_readme_table(self, content: str) -> list[dict[str, Any]]:
        entries: list[dict[str, Any]] = []
        lines = content.split("\n")
        in_table = False
        table_headers: list[str] = []

        for line in lines:
            line = line.strip()
            if line.startswith("|") and "|---" in line:
                in_table = True
                continue
            if not in_table:
                continue
            if not line.startswith("|"):
                in_table = False
                break
            cells = [cell.strip() for cell in line.split("|")[1:-1]]
            if not table_headers:
                header_map = {cell.lower(): idx for idx, cell in enumerate(cells)}
                if not all(k in header_map for k in ("name", "url", "authentication")):
                    break
                table_headers = cells
                continue
            if len(cells) < len(table_headers):
                continue
            entry = self.parse_table_row(cells, table_headers)
            if entry:
                entries.append(entry)
        return entries

    def parse_table_row(self, cells: list[str], headers: list[str]) -> dict[str, Any] | None:
        header_map = {h.lower(): idx for idx, h in enumerate(headers)}
        name_idx = header_map.get("name", -1)
        url_idx = header_map.get("url", -1)
        auth_idx = header_map.get("authentication", -1)
        category_idx = header_map.get("category", -1)
        maintainer_idx = header_map.get("maintainer", -1)

        if name_idx < 0 or url_idx < 0:
            return None

        name = cells[name_idx] if name_idx < len(cells) else ""
        url = cells[url_idx] if url_idx < len(cells) else ""
        auth = cells[auth_idx] if auth_idx < len(cells) else ""
        category = cells[category_idx] if category_idx < len(cells) and category_idx < len(cells) else ""
        maintainer = cells[maintainer_idx] if maintainer_idx < len(cells) and maintainer_idx < len(cells) else ""

        if not name or not url:
            return None
        if not url.startswith("https://"):
            return None
        if not allow_type(self.import_policy, "hosted_https"):
            return None

        server_id = slug(name)
        transport_type = "sse" if "/sse" in url else "streamable_http"

        return {
            "id": server_id,
            "exists": True,
            "enabled": False,
            "name": name,
            "description": f"{category} MCP server{(' by ' + maintainer) if maintainer else ''}.".strip(),
            "source": {
                "type": "hosted_https",
                "provider": self.id,
                "hosted_url": url,
                "authentication": auth,
                "repo": self.repo,
            },
            "security": {
                "local_code_execution": False,
                "sandboxed": True,
                "reviewed": self.trust == "reviewed",
                "data_risk": "unknown_until_reviewed",
                "permission_default": "manual_review",
            },
            "transport": {"type": transport_type},
            "keywords": keywords_for(name, category, maintainer),
            "trust": self.trust,
            "runtime": "hosted_https",
            "default_mode": "manual_review",
        }


HANDLERS: dict[str, type[SourceHandler]] = {
    "rest_api": RestApiHandler,
    "github_yaml": GithubYamlHandler,
    "github_readme_table": GithubReadmeTableHandler,
}


def load_sources() -> list[dict[str, Any]]:
    data = load_yaml(SOURCES_FILE)
    return data.get("mcp_sources", [])


def main() -> int:
    MCP_CATALOG_DIR.mkdir(parents=True, exist_ok=True)

    sources = load_sources()
    seen_ids: set[str] = set()
    total_discovered = 0

    for source in sources:
        if not source.get("enabled", False):
            continue
        source_type = str(source.get("source_type") or "")
        handler_class = HANDLERS.get(source_type)
        if not handler_class:
            print(f"Unknown source_type '{source_type}' for source {source.get('id')}")
            continue

        handler = handler_class(source)
        catalog_path = MCP_CATALOG_DIR / f"{handler.id}.yml"

        entries = handler.discover()

        unique_entries = []
        duplicates = 0
        for entry in entries:
            entry_id = str(entry.get("id") or "")
            if entry_id in seen_ids:
                duplicates += 1
                continue
            seen_ids.add(entry_id)
            unique_entries.append(entry)

        if duplicates > 0:
            print(f"Source '{handler.id}': {len(unique_entries)} entries ({duplicates} deduplicated)")

        preserved = handler.write_chunk(unique_entries, catalog_path)

        count = len(preserved)
        print(f"Source '{handler.id}': {count} entries")
        total_discovered += count

    print(f"Total unique MCP servers discovered: {len(seen_ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
