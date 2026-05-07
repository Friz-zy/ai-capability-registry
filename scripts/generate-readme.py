#!/usr/bin/env python3
from __future__ import annotations

from registry_lib import ROOT, load_all, write_text


def main() -> int:
    registry = load_all()
    skills = registry["skills"]
    mcp_servers = registry["mcp_servers"]
    agents = registry["agents"]
    profiles = registry["profiles"]
    enabled_sources = [item for item in skills if item.get("enabled")]
    candidate_sources = [item for item in skills if item.get("trust", {}).get("level") == "candidate"]
    enabled_mcp = [item for item in mcp_servers if item.get("enabled")]

    lines = [
        "# AI Capability Registry",
        "",
        "Curated AI skills, MCP servers, workflows, and agent integrations for secure multi-agent development.",
        "",
        "This repository turns AI-agent capability sprawl into a reproducible GitOps-style registry. It downloads upstream sources as pinned submodules, inventories every discovered skill/plugin, classifies them with deterministic tags, and installs selected profiles into a repo-local active cache.",
        "",
        "## What You Get",
        "",
        f"- {len(skills)} skill/plugin sources indexed, with {len(enabled_sources)} enabled as usable sources and {len(candidate_sources)} kept candidate/index-only.",
        f"- {len(mcp_servers)} MCP servers cataloged, with {len(enabled_mcp)} enabled by conservative defaults.",
        f"- {len(agents)} agent installers generated from the same registry metadata.",
        f"- {len(profiles)} install profiles for safer activation.",
        "- Full generated inventory of every discovered `SKILL.md` and plugin manifest.",
        "- Deterministic category/tag catalogs without AI calls in CI.",
        "",
        "## Quick Start",
        "",
        "```bash",
        "git clone --recurse-submodules <repo-url>",
        "cd ai-capability-registry",
        "./scripts/bootstrap.sh",
        "generated/install-scripts/kilo-code.sh --profile core",
        "```",
        "",
        "Installers write under this checkout's `generated/` directory, not to a hardcoded home directory:",
        "",
        "```text",
        "generated/active/<agent>/<profile>/",
        "generated/configs/<agent>/<profile>.json",
        "```",
        "",
        "## Core Model",
        "",
        "```text",
        "external/      raw pinned upstream cache; never loaded directly by agents",
        "registry/      source metadata, trust, tag categories, profiles, policies",
        "generated/     compact catalog, capability bundle, install bundle, install scripts",
        "generated/active/",
        "               repo-local runtime cache populated by install scripts",
        "```",
        "",
        "Updating a submodule does not update active agent skills. Install scripts verify enabled source commits against `registry/skills.yaml` before copying anything into the active cache.",
        "",
        "## Trust And Activation",
        "",
        "- `candidate`: downloaded/indexed for inspection only; not installed.",
        "- `reviewed`: manually reviewed; can be included by profiles.",
        "- `trusted`: official or reputable source; can be included by default profiles when pinned.",
        "- Source `enabled: true` means a source may be used, not that every discovered skill is automatically active.",
        "- Profiles decide which tagged categories/facts become active.",
        "",
        "## Generated Output",
        "",
        "| Path | Purpose |",
        "| --- | --- |",
        "| `generated/catalog.md` | Compact human-readable category/profile summary. |",
        "| `generated/capabilities.json` | Single machine-readable inventory of sources and discovered skills/plugins. |",
        "| `generated/install-bundle.json` | Single install bundle with source pins, role instructions, manifests, and agent config snippets. |",
        "| `generated/install-scripts/` | Per-agent installer wrappers. |",
        "| `generated/active/` | Ignored runtime install output populated by install scripts. |",
        "| `generated/configs/` | Ignored runtime config snippets written by install scripts. |",
        "",
        "## Tags, Categories, And Facts",
        "",
        "No AI call is required for normal generation. `scripts/discover-capabilities.py` extracts deterministic tags from names, descriptions, paths, and plugin metadata. `registry/tag-categories.yaml` maps tags to categories.",
        "",
        "Facts are observed file-structure booleans, not security scores: `has_scripts_dir`, `has_hooks_dir`, `has_mcp_config`, `has_executable_files`, `has_package_json`, `has_python_project`, `has_shell_scripts`, and related flags. Profiles may use facts to select content-only or lower-complexity capabilities.",
        "",
        "## Profiles",
        "",
    ]
    for profile in profiles:
        default = " default" if profile.get("default") else ""
        lines.append(f"- `{profile['id']}`{default}: {profile.get('description', '')}")

    lines.extend([
        "",
        "Install a profile for an agent:",
        "",
        "```bash",
        "generated/install-scripts/kilo-code.sh --profile core",
        "generated/install-scripts/opencode.sh --profile content-only",
        "generated/install-scripts/claude-code.sh --profile security-audit --dry-run",
        "```",
        "",
        "## Supported Agents",
        "",
    ])
    for agent in sorted(agents, key=lambda item: item["id"]):
        supports = ", ".join(agent.get("supports", []))
        lines.append(f"- **{agent['name']}** (`{agent['id']}`): {supports}. Installer: `{agent['install_script']}`")

    lines.extend([
        "",
        "## Scripts",
        "",
        "| Script | What It Does |",
        "| --- | --- |",
        "| `scripts/bootstrap.sh` | Runs submodule init, registry validation, source catalogs, capability discovery, install-plan generation, and README generation. |",
        "| `scripts/validate-registry.py` | Validates registry structure, trust levels, compatibility IDs, candidate enablement, and MCP policy constraints. |",
        "| `scripts/discover-capabilities.py` | Scans real upstream files, extracts tags/facts, writes compact generated bundles, and creates install scripts. |",
        "| `scripts/install-agent.py` | Used by generated install scripts to verify pins and copy profile-selected capabilities into the repo-local active cache. |",
        "| `scripts/generate-readme.py` | Regenerates this README. |",
        "| `scripts/update-submodules.sh` | Runs `git submodule update --init --recursive`. |",
        "",
        "## Verify Generation",
        "",
        "```bash",
        "rm -rf generated",
        "./scripts/bootstrap.sh",
        "./scripts/validate-registry.py",
        "git status --short",
        "```",
        "",
        "Expected generated files: `catalog.md`, `capabilities.json`, `install-bundle.json`, and `install-scripts/`. Runtime installs create ignored `generated/active/` and `generated/configs/`.",
    ])

    write_text(ROOT / "README.md", "\n".join(lines))
    print("Generated README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
