#!/usr/bin/env python3
from __future__ import annotations

from registry_lib import ROOT, load_all, write_text


def main() -> int:
    registry = load_all()
    skills = registry["skills"]
    mcp_servers = registry["mcp_servers"]
    agents = registry["agents"]
    policies = registry["policies"]

    trusted_skills = [item for item in skills if item.get("trust", {}).get("level") == "trusted"]
    enabled_mcp = [item for item in mcp_servers if item.get("enabled")]

    lines = [
        "# AI Capability Registry",
        "",
        "Curated AI skills, MCP servers, workflows, and agent integrations for secure multi-agent development.",
        "",
        "This repository is a GitOps-style capability registry. Registry YAML is the source of truth; generated Markdown and agent configs are derived artifacts.",
        "",
        "## Security Model",
        "",
        "- Everything can be indexed, almost nothing is auto-enabled.",
        "- Trusted or reviewed capabilities are promoted into active profiles only after manual review.",
        "- MCP runtimes must be hosted HTTPS/OAuth or Docker-isolated.",
        "- Random `npx`, `curl | sh`, unknown Python servers, arbitrary shell MCP, and unrestricted filesystem MCP are denied.",
        "- Read-only or ask-before-write defaults are preferred for all integrations.",
        "",
        "## Repository Layout",
        "",
        "```text",
        "registry/      Declarative source of truth",
        "skills/        Local category anchors and generated references",
        "mcp/           Docker/hosted MCP templates and generated references",
        "adapters/      Agent-specific install/bootstrap helpers",
        "scripts/       Validation and generation tooling",
        "generated/     Generated catalogs and configs",
        "external/      Pinned upstream sources as submodules or indexes",
        "```",
        "",
        "## Current Catalog",
        "",
        f"- Skills indexed: {len(skills)}",
        f"- Trusted skills: {len(trusted_skills)}",
        f"- MCP servers indexed: {len(mcp_servers)}",
        f"- MCP servers enabled by default: {len(enabled_mcp)}",
        f"- Agent adapters: {len(agents)}",
        "",
        "## Supported Agents",
        "",
    ]

    for agent in sorted(agents, key=lambda item: item["id"]):
        supports = ", ".join(agent.get("supports", []))
        lines.append(f"- **{agent['name']}** (`{agent['id']}`): {supports}")

    lines.extend([
        "",
        "## Generated Catalogs",
        "",
        "- `generated/skills.md`",
        "- `generated/README.skills.md`",
        "- `generated/mcp-catalog.md`",
        "- `generated/workflows.md`",
        "- `generated/agent-configs/`",
        "",
        "## Bootstrap",
        "",
        "```bash",
        "./scripts/bootstrap.sh",
        "```",
        "",
        "Bootstrap validates registry metadata, regenerates indexes, refreshes adapter configs, and creates local symlink references when pinned external sources exist.",
        "",
        "## Manual Commands",
        "",
        "```bash",
        "./scripts/validate-registry.py",
        "./scripts/generate-index.py",
        "./scripts/generate-agent-configs.py",
        "./scripts/generate-readme.py",
        "./scripts/link-artifacts.py",
        "```",
        "",
        "## Trust Levels",
        "",
    ])

    for trust_id, trust in policies.get("trust_levels", {}).items():
        actions = ", ".join(trust.get("allowed_actions", [])) or "none"
        lines.append(f"- `{trust_id}`: {trust.get('description')} Actions: {actions}.")

    lines.extend([
        "",
        "## Update Workflow",
        "",
        "1. Add or update registry YAML.",
        "2. Pin upstream source tag and commit when enabling installable content.",
        "3. Run validation and generation scripts.",
        "4. Review generated diffs.",
        "5. Promote only reviewed capabilities into active profiles.",
    ])

    write_text(ROOT / "README.md", "\n".join(lines))
    print("Generated README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
