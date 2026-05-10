#!/usr/bin/env python3
"""Generate MCP routing indexes from templates/mcp."""

from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Any

from registry_lib import ROOT, load_all, write_text

MCP_DIR = ROOT / "mcp"
MCP_SERVERS_DIR = MCP_DIR / "servers"
MCP_CATALOG_MD = ROOT / "mcp-catalog.md"
TEMPLATES_DIR = ROOT / "templates" / "mcp"


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9._-]+", "-", value.lower()).strip("-") or "unknown"


def template(name: str) -> str:
    return (TEMPLATES_DIR / name).read_text(encoding="utf-8").rstrip()


def render(name: str, values: dict[str, Any]) -> str:
    text = template(name)
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", str(value))
    unresolved = re.findall(r"\{\{[a-zA-Z0-9_]+\}\}", text)
    if unresolved:
        raise ValueError(f"Unresolved placeholder(s) in {name}: {', '.join(sorted(set(unresolved)))}")
    return text


def join_blocks(blocks: list[str]) -> str:
    return "\n\n".join(block for block in blocks if block)


def keywords(server: dict[str, Any]) -> list[str]:
    raw = server.get("keywords", [])
    if isinstance(raw, list):
        return [slug(str(item)) for item in raw if str(item)]
    return []


def runtime_bucket(server: dict[str, Any]) -> list[str]:
    runtime = str(server.get("runtime") or "")
    buckets = []
    if "hosted" in runtime:
        buckets.append("hosted")
    if "docker" in runtime:
        buckets.append("docker")
    return buckets or ["other"]


def enabled_servers(servers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [server for server in servers if server.get("enabled") is True and server.get("exists", True) is not False]


def hosted_url(server: dict[str, Any]) -> str | None:
    source = server.get("source", {})
    if isinstance(source, dict) and source.get("hosted_url"):
        return str(source["hosted_url"])
    return None


def docker_config(server: dict[str, Any]) -> dict[str, Any] | None:
    source = server.get("source", {})
    if not isinstance(source, dict):
        return None
    docker = source.get("docker")
    return docker if isinstance(docker, dict) else None


def source_auth(server: dict[str, Any]) -> str:
    source = server.get("source", {})
    if isinstance(source, dict) and source.get("authentication"):
        return str(source["authentication"])
    if "oauth" in str(server.get("runtime") or ""):
        return "OAuth"
    docker = docker_config(server)
    if docker:
        args = docker.get("args", [])
        if isinstance(args, list) and "-e" in [str(arg) for arg in args]:
            return "Environment variables"
    return "Open or unspecified"


def string_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item)]
    if isinstance(value, str) and value:
        return [value]
    return []


def bullet_list(values: list[str]) -> str:
    return "\n".join(f"- {item}" for item in values)


def inline_keywords(values: list[str]) -> str:
    return ", ".join(f"`{item}`" for item in values)


def yaml_keywords(values: list[str]) -> str:
    return "\n".join(f"  - {item}" for item in values)


def json_section(title: str, data: Any) -> str:
    return f"### {title}\n\n```json\n{json.dumps(data, indent=2, ensure_ascii=False)}\n```"


def markdown_section(title: str, content: str) -> str:
    return f"## {title}\n\n{content}"


def connection_config(server: dict[str, Any]) -> dict[str, Any]:
    server_id = slug(str(server.get("id") or "unknown"))
    url = hosted_url(server)
    docker = docker_config(server)
    if url:
        transport_type = "sse" if str(server.get("transport", {}).get("type")) == "sse" else "streamable_http"
        return {"mcpServers": {server_id: {"type": transport_type, "url": url}}}
    if docker:
        return {"mcpServers": {server_id: {"command": docker.get("command"), "args": docker.get("args", [])}}}
    return {"mcpServers": {server_id: {}}}


def skill_content(server: dict[str, Any]) -> str:
    server_id = str(server.get("id") or "unknown")
    skill = server.get("skill", {}) if isinstance(server.get("skill"), dict) else {}
    security = server.get("security", {}) if isinstance(server.get("security"), dict) else {}
    connection_sections = []
    url = hosted_url(server)
    docker = docker_config(server)
    if url:
        connection_sections.append(json_section("Hosted endpoint", {"type": "sse" if str(server.get("transport", {}).get("type")) == "sse" else "streamable_http", "url": url}))
    if docker:
        connection_sections.append(json_section("Docker stdio", {"command": docker.get("command"), "args": docker.get("args", [])}))
    docker_notes = bullet_list(string_list(skill.get("docker")))
    references = bullet_list(string_list(skill.get("references")))
    return render(
        "SKILL.md",
        {
            "server_id": server_id,
            "description_json": json.dumps(str(server.get("description") or "No description."), ensure_ascii=False),
            "description": str(server.get("description") or "No description."),
            "server_name": str(server.get("name") or server_id),
            "keywords": yaml_keywords(keywords(server)[:12]),
            "when_to_use": bullet_list(string_list(skill.get("when_to_use"))),
            "connection_sections": join_blocks(connection_sections),
            "skill_instructions": bullet_list(string_list(skill.get("instructions"))),
            "docker_notes_section": markdown_section("Docker launch notes", docker_notes) if docker_notes else "",
            "references_section": markdown_section("References", references) if references else "",
            "trust": server.get("trust", "unknown"),
            "default_mode": server.get("default_mode", "manual_review"),
            "permission_default": security.get("permission_default", "manual_review"),
            "authentication": source_auth(server),
        },
    )


def server_line(server: dict[str, Any]) -> str:
    sid = str(server.get("id") or "unknown")
    name = str(server.get("name") or sid)
    runtime = str(server.get("runtime") or "unknown")
    trust = str(server.get("trust") or "unknown")
    description = str(server.get("description") or "No description.")
    return f"- **{name}** (`{sid}`) — `{runtime}`, `{trust}`: {description}"


def write_server_list(path: Path, title: str, servers: list[dict[str, Any]]) -> None:
    server_items = [server_line(server) for server in sorted(servers, key=lambda item: str(item.get("name") or item.get("id")))]
    write_text(path, render("server-list.md", {"title": title, "servers": "\n".join(server_items) if server_items else "No enabled MCP servers found."}))


def get_keywords_for_categories(categories: list[str], keyword_categories: dict[str, list[str]]) -> list[str]:
    keys: set[str] = set()
    for category in categories:
        keys.update(str(keyword) for keyword in keyword_categories.get(category, []))
    return sorted(keys)


def task_keywords(task: dict[str, Any], keyword_categories: dict[str, list[str]]) -> list[str]:
    raw = task.get("keywords", [])
    explicit = {slug(str(keyword)) for keyword in raw if str(keyword)} if isinstance(raw, list) else set()
    categories = task.get("categories", [])
    category_keywords = set(get_keywords_for_categories(categories if isinstance(categories, list) else [], keyword_categories))
    return sorted(explicit | category_keywords)


def keyword_items(keys: list[str], by_keyword: dict[str, list[dict[str, Any]]], empty_template: str) -> str:
    if not keys:
        return "No enabled MCP servers match this task." if empty_template == "task" else "No enabled MCP servers match this role."
    return "\n".join(f"- **{key}**: {len(by_keyword[key])} server(s) — `mcp/catalog/keywords/{key}/servers.md`" for key in keys)


def generate_task_servers_md(task: dict[str, Any], keyword_categories: dict[str, list[str]], by_keyword: dict[str, list[dict[str, Any]]]) -> str:
    keys = [keyword for keyword in task_keywords(task, keyword_categories) if by_keyword.get(keyword)]
    categories = task.get("categories", []) if isinstance(task.get("categories"), list) else []
    return render(
        "task.md",
        {
            "name": str(task["name"]),
            "description": str(task.get("description") or ""),
            "categories": "\n".join(f"- `{category}`" for category in categories),
            "keywords": keyword_items(keys, by_keyword, "task"),
        },
    )


def generate_role_servers_md(profile: dict[str, Any], keyword_categories: dict[str, list[str]], by_keyword: dict[str, list[dict[str, Any]]]) -> str:
    categories = profile.get("include", {}).get("categories", [])
    if not isinstance(categories, list):
        categories = []
    keys = [keyword for keyword in get_keywords_for_categories(categories, keyword_categories) if by_keyword.get(keyword)]
    return render(
        "role.md",
        {
            "name": str(profile.get("role", {}).get("title") or profile["name"]),
            "keywords": keyword_items(keys, by_keyword, "role"),
        },
    )


def generate_catalog_md(all_servers: list[dict[str, Any]]) -> None:
    enabled_count = sum(1 for server in all_servers if server.get("enabled") is True)
    entries = []
    for server in sorted(all_servers, key=lambda item: str(item.get("id") or "")):
        server_keywords = keywords(server)[:12]
        entries.append(
            "\n".join(
                [
                    f"## {server.get('name') or server.get('id')}",
                    "",
                    str(server.get("description") or "No description."),
                    "",
                    f"**ID:** `{server.get('id') or 'unknown'}`",
                    f"**Enabled:** `{str(server.get('enabled') is True).lower()}`",
                    f"**Runtime:** `{server.get('runtime') or 'unknown'}`",
                    f"**Trust:** `{server.get('trust') or 'unknown'}`",
                    f"**Keywords:** {inline_keywords(server_keywords) if server_keywords else 'none'}",
                ]
            )
        )
    write_text(
        MCP_CATALOG_MD,
        render(
            "mcp-catalog.md",
            {"total": len(all_servers), "enabled": enabled_count, "disabled": len(all_servers) - enabled_count, "servers": join_blocks(entries)},
        ),
    )


def root_roles(profiles: list[dict[str, Any]], keyword_categories: dict[str, list[str]], by_keyword: dict[str, list[dict[str, Any]]]) -> str:
    items = []
    for profile in profiles:
        categories = profile.get("include", {}).get("categories", [])
        if not isinstance(categories, list):
            categories = []
        available = [keyword for keyword in get_keywords_for_categories(categories, keyword_categories) if by_keyword.get(keyword)]
        if available:
            role = profile.get("role", {}).get("title") or profile["name"]
            items.append(f"- **{role}**: `mcp/catalog/roles/{profile['id']}/servers.md` -> {inline_keywords(available[:12])}")
    return "\n".join(items)


def root_tasks(tasks: list[dict[str, Any]], keyword_categories: dict[str, list[str]], by_keyword: dict[str, list[dict[str, Any]]]) -> str:
    items = []
    for task in tasks:
        available = [keyword for keyword in task_keywords(task, keyword_categories) if by_keyword.get(keyword)]
        if available:
            items.append(f"- **{task['name']}**: `mcp/catalog/tasks/{task['id']}/servers.md` -> {inline_keywords(available[:12])}")
    return "\n".join(items)


def runtime_catalogs(by_runtime: dict[str, list[dict[str, Any]]]) -> str:
    labels = {
        "hosted": ("Hosted HTTPS", "public HTTPS endpoints using Streamable HTTP or SSE"),
        "docker": ("Docker stdio", "OCI images launched via `docker run --rm -i`"),
        "other": ("Other", "non-standard runtimes requiring manual review"),
    }
    items = []
    for bucket in ["hosted", "docker", "other"]:
        servers = by_runtime.get(bucket, [])
        count = f"{len(servers)} server(s)" if servers else "no enabled servers"
        label, description = labels.get(bucket, (bucket.title(), ""))
        items.append(f"- **{label}** ({description}): `mcp/catalog/runtime/{bucket}/servers.md` — {count}")
    return "\n".join(items)


def main() -> int:
    registry = load_all()
    all_servers = registry["mcp_servers"]
    servers = enabled_servers(all_servers)
    if MCP_DIR.exists():
        shutil.rmtree(MCP_DIR)
    for path in ["catalog/roles", "catalog/tasks", "catalog/runtime", "catalog/keywords", "servers"]:
        (MCP_DIR / path).mkdir(parents=True, exist_ok=True)

    by_runtime: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_keyword: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for server in servers:
        for bucket in runtime_bucket(server):
            by_runtime[bucket].append(server)
        for key in keywords(server):
            by_keyword[key].append(server)
        server_dir = MCP_SERVERS_DIR / slug(str(server.get("id") or "unknown"))
        write_text(server_dir / "SKILL.md", skill_content(server))
        write_text(server_dir / "connection.json", render("connection.json", {"connection_json": json.dumps(connection_config(server), indent=2, ensure_ascii=False)}))

    write_text(MCP_DIR / "mcp.md", render("mcp.md", {"roles": root_roles(registry["profiles"], registry["keyword_categories"], by_keyword), "tasks": root_tasks(registry["tasks"], registry["keyword_categories"], by_keyword), "runtime_catalogs": runtime_catalogs(by_runtime)}))

    for bucket in ["hosted", "docker", "other"]:
        write_server_list(MCP_DIR / "catalog" / "runtime" / bucket / "servers.md", f"{bucket.title()} MCP Servers", by_runtime.get(bucket, []))
    for profile in registry["profiles"]:
        write_text(MCP_DIR / "catalog" / "roles" / str(profile["id"]) / "servers.md", generate_role_servers_md(profile, registry["keyword_categories"], by_keyword))
    for task in registry["tasks"]:
        write_text(MCP_DIR / "catalog" / "tasks" / str(task["id"]) / "servers.md", generate_task_servers_md(task, registry["keyword_categories"], by_keyword))
    for key, items in sorted(by_keyword.items()):
        write_server_list(MCP_DIR / "catalog" / "keywords" / key / "servers.md", f"{key} MCP Servers", items)

    generate_catalog_md(all_servers)
    print(f"Generated MCP registry: {len(servers)} enabled / {len(all_servers)} total")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
