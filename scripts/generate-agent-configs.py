#!/usr/bin/env python3
from __future__ import annotations

from registry_lib import GENERATED_DIR, load_all, write_json, write_text


def markdown_config(agent: dict, registry: dict) -> str:
    skills = [skill for skill in registry["skills"] if agent["id"] in skill.get("compatibility", [])]
    mcp_servers = [server for server in registry["mcp_servers"] if agent["id"] in server.get("compatibility", [])]
    lines = [f"# {agent['name']} Registry Bootstrap", "", f"Generated config reference for `{agent['id']}`.", ""]
    lines.extend(["## Load Generated Artifacts", "", "- `generated/skills.md`", "- `generated/mcp-catalog.md`", "- `generated/workflows.md`", ""])
    lines.extend(["## Compatible Skills", ""])
    for skill in sorted(skills, key=lambda item: item["id"]):
        status = "enabled" if skill.get("enabled") else "manual/index-only"
        lines.append(f"- `{skill['id']}`: {skill['name']} ({status})")
    lines.extend(["", "## Compatible MCP Servers", ""])
    for server in sorted(mcp_servers, key=lambda item: item["id"]):
        lines.append(f"- `{server['id']}`: {server['name']} (`{server.get('default_mode')}`)")
    return "\n".join(lines)


def kilo_config(agent: dict, registry: dict) -> dict:
    return {
        "registry": "~/.ai-capability-registry/generated",
        "skills_registry": "~/.ai-capability-registry/generated/skills.md",
        "mcp_catalog": "~/.ai-capability-registry/generated/mcp-catalog.md",
        "workflows": "~/.ai-capability-registry/generated/workflows.md",
        "policy": {
            "default_enablement": "manual_review",
            "deny_arbitrary_local_execution": True,
            "prefer_read_only": True,
        },
        "compatible_skills": [
            skill["id"] for skill in registry["skills"] if agent["id"] in skill.get("compatibility", [])
        ],
        "compatible_mcp_servers": [
            server["id"] for server in registry["mcp_servers"] if agent["id"] in server.get("compatibility", [])
        ],
    }


def main() -> int:
    registry = load_all()
    out_dir = GENERATED_DIR / "agent-configs"
    for agent in registry["agents"]:
        if agent["id"] == "kilo-code":
            write_json(out_dir / "kilo-code.json", kilo_config(agent, registry))
        else:
            write_text(out_dir / f"{agent['id']}.md", markdown_config(agent, registry))
    print("Generated agent configs in generated/agent-configs/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
