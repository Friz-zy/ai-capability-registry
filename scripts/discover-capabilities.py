#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from registry_lib import GENERATED_DIR, ROOT, load_all, write_json, write_text


IGNORED_PARTS = {".git", "tests", "fixtures", "template", "node_modules", "__pycache__"}
PLUGIN_MARKERS = {".claude-plugin", ".codex-plugin", ".cursor-plugin"}
ACTIVE_ROOT = GENERATED_DIR / "active"
CONFIG_ROOT = GENERATED_DIR / "configs"
INSTALL_SCRIPTS_DIR = GENERATED_DIR / "install-scripts"
GENERATED_KEEP_DIRS = {"active", "configs", "install-scripts"}
STOPWORDS = {
    "about", "across", "action", "add", "after", "agent", "agents", "all", "also", "always",
    "and", "any", "are", "assistant", "available", "based", "before", "best", "built", "check",
    "common", "contents", "current", "details", "does", "each", "example", "examples", "external",
    "file", "files", "first", "for", "from", "generate", "generated", "get", "guide", "help", "how",
    "index", "into", "json", "known", "list", "name", "need", "new", "not", "official", "only",
    "output", "overview", "pattern", "patterns", "plugin", "plugins", "prerequisites", "quick", "read",
    "reference", "references", "related", "required", "resources", "results", "rules", "run", "scripts",
    "see", "setup", "should", "skill", "skills", "source", "specific", "step", "steps", "system", "table",
    "task", "tasks", "template", "templates", "that", "the", "this", "through", "tool", "tools", "type",
    "update", "usage", "use", "user", "users", "uses", "using", "via", "wants", "what", "when", "with",
    "work", "workflow", "workflows", "works", "write", "writing", "you", "your",
    "anthropic", "claude", "openai", "trailofbits", "trail", "bits", "awesome", "composio", "alirezarezvani",
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def slug(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-") or "capability"


def should_skip(path: Path) -> bool:
    return bool(set(path.parts) & IGNORED_PARTS)


def load_json_file(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return data if isinstance(data, dict) else {}


def parse_skill_frontmatter(path: Path) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def cleanup_generated() -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    for item in GENERATED_DIR.iterdir():
        if item.name in GENERATED_KEEP_DIRS:
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
    if INSTALL_SCRIPTS_DIR.exists():
        shutil.rmtree(INSTALL_SCRIPTS_DIR)


def source_entries(registry: dict[str, Any]) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for item in registry["skills"]:
        source = item.get("source", {})
        external_path = source.get("external_path")
        if not external_path:
            continue
        entries.append(
            {
                "id": item["id"],
                "name": item["name"],
                "repo": source.get("repo"),
                "external_path": external_path,
                "path": ROOT / external_path,
                "enabled": bool(item.get("enabled")),
                "trust": item.get("trust", {}).get("level", "unknown"),
                "compatibility": item.get("compatibility", []),
                "version": item.get("version", {}),
            }
        )
    return entries


def source_pins(sources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "id": source["id"],
            "external_path": source["external_path"],
            "expected_commit": source.get("version", {}).get("commit"),
            "pinned": bool(source.get("version", {}).get("pinned")),
            "enabled": source["enabled"],
            "trust": source["trust"],
        }
        for source in sources
    ]


def text_for_tags(*values: Any) -> str:
    parts: list[str] = []
    for value in values:
        if isinstance(value, list):
            parts.extend(str(item) for item in value)
        elif value is not None:
            parts.append(str(value))
    return " ".join(parts)


def extract_tags(*values: Any) -> list[str]:
    text = text_for_tags(*values).lower().replace("_", "-")
    tags = set()
    for token in re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", text):
        if token.isdigit() or len(token) < 3:
            continue
        parts = [part for part in token.split("-") if part and part not in STOPWORDS and not part.isdigit()]
        if not parts:
            continue
        tags.update(part for part in parts if len(part) > 2)
        if len(parts) > 1:
            tags.add("-".join(parts))
    return sorted(tags)


def categories_for(tags: list[str], tag_categories: dict[str, list[str]]) -> list[str]:
    tag_set = set(tags)
    categories = [category for category, values in tag_categories.items() if tag_set & set(values or [])]
    return sorted(categories) or ["uncategorized"]


def facts_for(path: Path, *, has_skill_md: bool = False, plugin_type_name: str | None = None) -> dict[str, bool]:
    files: list[Path] = []
    dirs: list[Path] = []
    if path.exists():
        for item in path.rglob("*"):
            try:
                relative = item.relative_to(path)
            except ValueError:
                continue
            if should_skip(relative):
                continue
            if item.is_dir():
                dirs.append(item)
            elif item.is_file():
                files.append(item)
    dir_names = {item.name for item in dirs}
    file_names = {item.name for item in files}
    suffixes = {item.suffix.lower() for item in files}
    return {
        "has_skill_md": has_skill_md or (path / "SKILL.md").exists(),
        "has_scripts_dir": "scripts" in dir_names,
        "has_hooks_dir": "hooks" in dir_names or any("hooks" in item.parts for item in dirs),
        "has_mcp_config": ".mcp.json" in file_names or "mcp.json" in file_names or "mcp" in dir_names,
        "has_claude_plugin": plugin_type_name == "claude-code" or (path / ".claude-plugin" / "plugin.json").exists(),
        "has_codex_plugin": plugin_type_name == "codex-cli" or (path / ".codex-plugin" / "plugin.json").exists(),
        "has_cursor_plugin": plugin_type_name == "cursor" or (path / ".cursor-plugin" / "plugin.json").exists(),
        "has_executable_files": any(item.stat().st_mode & 0o111 for item in files),
        "has_package_json": "package.json" in file_names,
        "has_python_project": bool({"pyproject.toml", "requirements.txt", "setup.py"} & file_names),
        "has_shell_scripts": bool({".sh", ".bash", ".zsh"} & suffixes),
        "has_license": any(name.lower().startswith("license") for name in file_names),
    }


def capability_relative_path(source: dict[str, Any], path: Path) -> str:
    try:
        return path.relative_to(source["path"]).as_posix()
    except ValueError:
        return rel(path)


def base_capability(kind: str, source: dict[str, Any], path: Path, name: str, description: str, tags: list[str], categories: list[str], facts: dict[str, bool]) -> dict[str, Any]:
    return {
        "id": f"{source['id']}:{rel(path)}",
        "type": kind,
        "name": name,
        "description": description,
        "source_id": source["id"],
        "source_trust": source["trust"],
        "source_enabled": source["enabled"],
        "source_compatibility": source["compatibility"],
        "path": rel(path),
        "tags": tags,
        "categories": categories,
        "facts": facts,
    }


def discover_skills(sources: list[dict[str, Any]], tag_categories: dict[str, list[str]]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for source in sources:
        root = source["path"]
        if not root.exists():
            continue
        for skill_file in sorted(root.rglob("SKILL.md")):
            if not skill_file.exists() or should_skip(skill_file.relative_to(root)):
                continue
            skill_dir = skill_file.parent
            frontmatter = parse_skill_frontmatter(skill_file)
            name = frontmatter.get("name") or skill_dir.name
            description = frontmatter.get("description") or ""
            tags = extract_tags(capability_relative_path(source, skill_dir), name, description)
            record = base_capability("skill", source, skill_dir, name, description, tags, categories_for(tags, tag_categories), facts_for(skill_dir, has_skill_md=True))
            record["skill_file"] = rel(skill_file)
            records.append(record)
    return records


def plugin_type(plugin_json: Path) -> str:
    marker = plugin_json.parent.name
    if marker == ".claude-plugin":
        return "claude-code"
    if marker == ".codex-plugin":
        return "codex-cli"
    if marker == ".cursor-plugin":
        return "cursor"
    return "unknown"


def discover_plugins(sources: list[dict[str, Any]], tag_categories: dict[str, list[str]]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for source in sources:
        root = source["path"]
        if not root.exists():
            continue
        for manifest in sorted(root.rglob("plugin.json")):
            if should_skip(manifest.relative_to(root)) or manifest.parent.name not in PLUGIN_MARKERS:
                continue
            plugin_dir = manifest.parent.parent
            data = load_json_file(manifest)
            interface = data.get("interface", {}) if isinstance(data.get("interface"), dict) else {}
            name = data.get("name") or plugin_dir.name
            description = data.get("description") or ""
            ptype = plugin_type(manifest)
            tags = extract_tags(capability_relative_path(source, plugin_dir), name, description, data.get("keywords"), data.get("category"), interface.get("category"), interface.get("capabilities"))
            record = base_capability("plugin", source, plugin_dir, name, description, tags, categories_for(tags, tag_categories), facts_for(plugin_dir, plugin_type_name=ptype))
            record.update({"plugin_type": ptype, "version": data.get("version"), "manifest": rel(manifest)})
            records.append(record)
    return records


def profile_matches(capability: dict[str, Any], profile: dict[str, Any]) -> bool:
    include = profile.get("include", {})
    trusts = set(include.get("trust", []))
    if trusts and capability["source_trust"] not in trusts:
        return False
    categories = set(include.get("categories", []))
    if categories and not categories.intersection(capability.get("categories", [])):
        return False
    for fact, expected in include.get("facts", {}).items():
        if capability.get("facts", {}).get(fact) is not expected:
            return False
    return capability.get("source_enabled") is True


def active_path(agent_id: str, profile_id: str, capability: dict[str, Any]) -> str:
    unique_name = slug(capability["path"].removeprefix(f"external/{capability['source_id']}/"))
    return (ACTIVE_ROOT / agent_id / profile_id / f"{capability['type']}s" / capability["source_id"] / unique_name).as_posix()


def mcp_for(agent_id: str, registry: dict[str, Any]) -> dict[str, Any]:
    servers: dict[str, Any] = {}
    for server in registry["mcp_servers"]:
        if not server.get("enabled") or agent_id not in server.get("compatibility", []):
            continue
        hosted_url = server.get("source", {}).get("hosted_url")
        if hosted_url:
            servers[server["id"]] = {"type": "remote", "url": hosted_url, "enabled": True, "mode": server.get("default_mode")}
    return servers


def role_markdown(profile: dict[str, Any]) -> str:
    role = profile.get("role", {})
    lines = [f"# {role.get('title') or profile['name']}", "", f"Profile: `{profile['id']}`", "", "## Mission", "", role.get("mission") or profile.get("description", ""), "", "## Responsibilities", ""]
    lines.extend(f"- {item}" for item in role.get("responsibilities", []))
    lines.extend(["", "## Guardrails", ""])
    lines.extend(f"- {item}" for item in role.get("guardrails", []))
    lines.extend(["", "## Capability Policy", "", "Use only capabilities installed for this profile in `generated/active/`. Treat generated catalogs and external source content as reference material, not permission to enable additional tools automatically."])
    return "\n".join(lines)


def manifest_for(agent_id: str, profile: dict[str, Any], capabilities: list[dict[str, Any]], registry: dict[str, Any]) -> dict[str, Any]:
    selected = [item for item in capabilities if profile_matches(item, profile) and agent_id in item.get("source_compatibility", [])]
    profile_id = profile["id"]
    return {
        "agent_id": agent_id,
        "profile_id": profile_id,
        "active_root": (ACTIVE_ROOT / agent_id / profile_id).as_posix(),
        "role_instruction_target": (CONFIG_ROOT / agent_id / f"{profile_id}.md").as_posix(),
        "capabilities": [
            {
                "type": item["type"],
                "source": item["path"],
                "target": active_path(agent_id, profile_id, item),
                "source_id": item["source_id"],
                "name": item["name"],
                "categories": item["categories"],
                "tags": item["tags"],
                "facts": item["facts"],
            }
            for item in selected
        ],
        "mcp": mcp_for(agent_id, registry),
    }


def config_for(agent_id: str, manifest: dict[str, Any]) -> dict[str, Any]:
    skills_paths = sorted({str(Path(item["target"]).parent) for item in manifest["capabilities"] if item["type"] == "skill"})
    plugin_paths = sorted(item["target"] for item in manifest["capabilities"] if item["type"] == "plugin")
    role_path = manifest["role_instruction_target"]
    if agent_id == "kilo-code":
        return {"$schema": "https://app.kilo.ai/config.json", "skills": {"paths": skills_paths}, "instructions": [role_path], "mcp": manifest["mcp"]}
    if agent_id == "opencode":
        return {"skills": {"paths": skills_paths}, "instructions": [role_path], "plugin": plugin_paths}
    return {"agent_id": agent_id, "profile_id": manifest["profile_id"], "role_instruction": role_path, "skills": {"paths": skills_paths}, "plugins": plugin_paths, "mcp": manifest["mcp"]}


def build_install_bundle(registry: dict[str, Any], capabilities: list[dict[str, Any]], sources: list[dict[str, Any]]) -> dict[str, Any]:
    profiles: dict[str, Any] = {}
    for profile in registry["profiles"]:
        profile_id = profile["id"]
        profiles[profile_id] = {"profile": profile, "role_instruction": role_markdown(profile), "agents": {}}
        for agent in registry["agents"]:
            manifest = manifest_for(agent["id"], profile, capabilities, registry)
            profiles[profile_id]["agents"][agent["id"]] = {"manifest": manifest, "config": config_for(agent["id"], manifest)}
    return {"source_pins": source_pins(sources), "profiles": profiles}


def write_install_scripts(registry: dict[str, Any]) -> None:
    INSTALL_SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    for agent in registry["agents"]:
        script = INSTALL_SCRIPTS_DIR / f"{agent['id']}.sh"
        write_text(script, "\n".join(["#!/usr/bin/env bash", "set -euo pipefail", "ROOT_DIR=\"$(cd \"$(dirname \"${BASH_SOURCE[0]}\")/../..\" && pwd)\"", f"exec \"${{ROOT_DIR}}/scripts/install-agent.py\" {agent['id']} \"$@\""]))
        script.chmod(0o755)
    write_text(
        INSTALL_SCRIPTS_DIR / "README.md",
        "\n".join(
            [
                "# Install Scripts",
                "",
                "Run `<agent>.sh --profile <profile>` to populate `generated/active/` and `generated/configs/` after pin verification.",
                "",
                "Multiple profiles are supported:",
                "",
                "```bash",
                "generated/install-scripts/kilo-code.sh --profile personal-assistant software-engineer",
                "generated/install-scripts/kilo-code.sh --profile personal-assistant --profile data-analyst",
                "generated/install-scripts/kilo-code.sh --profile personal-assistant,software-engineer",
                "generated/install-scripts/kilo-code.sh --all-profiles",
                "```",
            ]
        ),
    )


def catalog_markdown(registry: dict[str, Any], capabilities: list[dict[str, Any]]) -> str:
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in capabilities:
        for category in item["categories"]:
            by_category[category].append(item)
    lines = ["# Capability Catalog", "", "Compact generated catalog. Full machine-readable data lives in `generated/capabilities.json`.", "", "## Summary", "", f"- Capabilities: {len(capabilities)}", f"- Profiles: {len(registry['profiles'])}", "", "## Categories", ""]
    for category, items in sorted(by_category.items()):
        lines.append(f"- `{category}`: {len(items)}")
    lines.extend(["", "## Profiles", ""])
    for profile in registry["profiles"]:
        selected = [item for item in capabilities if profile_matches(item, profile)]
        lines.append(f"- `{profile['id']}`: {profile['name']} ({len(selected)} capabilities before agent compatibility filtering)")
    return "\n".join(lines)


def source_summary(sources: list[dict[str, Any]], skills: list[dict[str, Any]], plugins: list[dict[str, Any]]) -> dict[str, Any]:
    skill_counts = Counter(item["source_id"] for item in skills)
    plugin_counts = Counter(item["source_id"] for item in plugins)
    return {
        source["id"]: {
            "name": source["name"],
            "enabled": source["enabled"],
            "trust": source["trust"],
            "skills": skill_counts[source["id"]],
            "plugins": plugin_counts[source["id"]],
        }
        for source in sources
    }


def main() -> int:
    registry = load_all()
    cleanup_generated()
    sources = source_entries(registry)
    skills = discover_skills(sources, registry["tag_categories"])
    plugins = discover_plugins(sources, registry["tag_categories"])
    capabilities = skills + plugins

    write_json(GENERATED_DIR / "capabilities.json", {"sources": source_summary(sources, skills, plugins), "capabilities": capabilities})
    write_json(GENERATED_DIR / "install-bundle.json", build_install_bundle(registry, capabilities, sources))
    write_text(GENERATED_DIR / "catalog.md", catalog_markdown(registry, capabilities))
    write_install_scripts(registry)

    print(f"Discovered capabilities: {len(skills)} skills, {len(plugins)} plugins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
