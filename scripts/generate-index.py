#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict

from registry_lib import GENERATED_DIR, load_all, write_json, write_text


def yn(value: bool) -> str:
    return "yes" if value else "no"


def generate_skills(skills: list[dict]) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for skill in skills:
        categories = skill.get("category") or ["uncategorized"]
        grouped[categories[0]].append(skill)

    lines = ["# Global Skills Registry", "", "Generated from `registry/skills.yaml`.", ""]
    for category in sorted(grouped):
        lines.extend([f"## {category.title()}", ""])
        for skill in sorted(grouped[category], key=lambda item: item["id"]):
            trust = skill.get("trust", {}).get("level", "unknown")
            compat = ", ".join(skill.get("compatibility", []))
            status = "enabled" if skill.get("enabled") else "manual/index-only"
            lines.append(f"- **{skill['name']}** (`{skill['id']}`): {skill.get('description', '')}")
            lines.append(f"  Trust: `{trust}`. Status: `{status}`. Compatibility: {compat}.")
        lines.append("")
    return "\n".join(lines)


def generate_skills_readme(skills: list[dict]) -> str:
    lines = ["# Skills Catalog", "", "This catalog is generated. Edit `registry/skills.yaml` instead.", ""]
    lines.append("| ID | Name | Trust | Enabled | Source |")
    lines.append("| --- | --- | --- | --- | --- |")
    for skill in sorted(skills, key=lambda item: item["id"]):
        source = skill.get("source", {}).get("repo", "")
        trust = skill.get("trust", {}).get("level", "unknown")
        lines.append(f"| `{skill['id']}` | {skill['name']} | `{trust}` | {yn(skill.get('enabled'))} | {source} |")
    return "\n".join(lines)


def generate_mcp(servers: list[dict]) -> str:
    lines = ["# MCP Catalog", "", "Generated from `registry/mcp.yaml`.", ""]
    lines.append("| ID | Name | Trust | Runtime | Default Mode | Enabled |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for server in sorted(servers, key=lambda item: item["id"]):
        lines.append(
            f"| `{server['id']}` | {server['name']} | `{server.get('trust')}` | "
            f"`{server.get('runtime')}` | `{server.get('default_mode')}` | {yn(server.get('enabled'))} |"
        )
    lines.extend(["", "## Security Defaults", ""])
    for server in sorted(servers, key=lambda item: item["id"]):
        security = server.get("security", {})
        lines.append(f"- **{server['name']}**: {server.get('description', '')}")
        lines.append(f"  Data risk: `{security.get('data_risk', 'unknown')}`. Permission default: `{security.get('permission_default', server.get('default_mode'))}`.")
    return "\n".join(lines)


def generate_workflows(workflows: list[dict]) -> str:
    lines = ["# Workflow Catalog", "", "Generated from `registry/workflows.yaml`.", ""]
    for workflow in sorted(workflows, key=lambda item: item["id"]):
        lines.extend([f"## {workflow['name']}", "", workflow.get("description", ""), ""])
        lines.append("Steps:")
        for step in workflow.get("steps", []):
            lines.append(f"- `{step}`")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    registry = load_all()
    write_text(GENERATED_DIR / "skills.md", generate_skills(registry["skills"]))
    write_text(GENERATED_DIR / "README.skills.md", generate_skills_readme(registry["skills"]))
    write_text(GENERATED_DIR / "mcp-catalog.md", generate_mcp(registry["mcp_servers"]))
    write_text(GENERATED_DIR / "workflows.md", generate_workflows(registry["workflows"]))
    write_json(GENERATED_DIR / "registry.json", registry)
    print("Generated catalog artifacts in generated/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
