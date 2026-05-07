# AI Capability Registry

Curated AI skills, MCP servers, workflows, and agent integrations for secure multi-agent development.

This repository turns AI-agent capability sprawl into a reproducible GitOps-style registry. It downloads upstream sources as pinned submodules, inventories every discovered skill/plugin, classifies them with deterministic tags, and installs selected profiles into a repo-local active cache.

## What You Get

- 13 skill/plugin sources indexed, with 7 enabled as usable sources and 6 kept candidate/index-only.
- 9 MCP servers cataloged, with 8 enabled by conservative defaults.
- 7 agent installers generated from the same registry metadata.
- 22 install profiles for safer activation.
- Full generated inventory of every discovered `SKILL.md` and plugin manifest.
- Deterministic category/tag catalogs without AI calls in CI.

## Quick Start

```bash
git clone --recurse-submodules <repo-url>
cd ai-capability-registry
./scripts/bootstrap.sh
generated/install-scripts/kilo-code.sh --profile core
```

Installers write under this checkout's `generated/` directory, not to a hardcoded home directory:

```text
generated/active/<agent>/<profile>/
generated/configs/<agent>/<profile>.json
```

## Core Model

```text
external/      raw pinned upstream cache; never loaded directly by agents
registry/      source metadata, trust, tag categories, profiles, policies
generated/     compact catalog, capability bundle, install bundle, install scripts
generated/active/
               repo-local runtime cache populated by install scripts
```

Updating a submodule does not update active agent skills. Install scripts verify enabled source commits against `registry/skills.yaml` before copying anything into the active cache.

## Trust And Activation

- `candidate`: downloaded/indexed for inspection only; not installed.
- `reviewed`: manually reviewed; can be included by profiles.
- `trusted`: official or reputable source; can be included by default profiles when pinned.
- Source `enabled: true` means a source may be used, not that every discovered skill is automatically active.
- Profiles decide which tagged categories/facts become active.

## Generated Output

| Path | Purpose |
| --- | --- |
| `generated/catalog.md` | Compact human-readable category/profile summary. |
| `generated/capabilities.json` | Single machine-readable inventory of sources and discovered skills/plugins. |
| `generated/install-bundle.json` | Single install bundle with source pins, role instructions, manifests, and agent config snippets. |
| `generated/install-scripts/` | Per-agent installer wrappers. |
| `generated/active/` | Ignored runtime install output populated by install scripts. |
| `generated/configs/` | Ignored runtime config snippets written by install scripts. |

## Tags, Categories, And Facts

No AI call is required for normal generation. `scripts/discover-capabilities.py` extracts deterministic tags from names, descriptions, paths, and plugin metadata. `registry/tag-categories.yaml` maps tags to categories.

Facts are observed file-structure booleans, not security scores: `has_scripts_dir`, `has_hooks_dir`, `has_mcp_config`, `has_executable_files`, `has_package_json`, `has_python_project`, `has_shell_scripts`, and related flags. Profiles may use facts to select content-only or lower-complexity capabilities.

## Profiles

- `personal-assistant` default: Personal productivity, research, summarization, planning, notes, and lightweight coordination.
- `founder-ceo`: Strategy, company planning, fundraising preparation, product narrative, hiring priorities, and executive synthesis.
- `cto-engineering-lead`: Architecture, engineering strategy, technical planning, code review, delivery, and platform decisions.
- `product-manager`: Product discovery, requirements, roadmap, metrics, sprint planning, and customer-informed prioritization.
- `software-engineer`: General software implementation, debugging, refactoring, testing, and code review.
- `backend-engineer`: APIs, services, databases, backend frameworks, integration work, and server-side quality.
- `frontend-engineer`: UI implementation, frontend architecture, accessibility, design systems, and web app testing.
- `mobile-engineer`: Mobile SDKs, native platforms, React Native, app UX, and mobile integration workflows.
- `qa-engineer`: Test strategy, regression coverage, web app testing, Playwright, and quality workflows.
- `security-engineer`: Application security, threat modeling, static analysis, fuzzing, dependency review, and audit workflows.
- `devops-platform-engineer`: CI, deployment, infrastructure, containers, cloud, platform automation, and release workflows.
- `sre-incident-manager`: Reliability, incident response, observability, capacity planning, and operational readiness.
- `data-analyst`: SQL, dashboards, metrics review, data validation, visualization, and statistical analysis.
- `ai-engineer`: LLM apps, MCP, prompts, model integrations, embeddings, AI workflows, and agent capability design.
- `designer`: UX, UI, accessibility, design critique, design systems, handoff, and research synthesis.
- `marketing-growth`: Brand, campaigns, lifecycle email, SEO, ads, copywriting, growth, and conversion workflows.
- `sales-account-executive`: Account research, call prep, outreach, competitive intelligence, pipeline review, and sales planning.
- `customer-success-support`: Customer support, knowledge base articles, account prep, issue summaries, and success workflows.
- `finance-ops`: Financial statements, close management, audit support, journal entries, SOX testing, and finance workflows.
- `legal-ops`: Contract review support, NDA triage, legal risk assessment, and legal operations workflows.
- `people-ops-recruiting`: Hiring, org planning, performance review support, people operations, and recruiting workflows.
- `operations-manager`: Vendor review, change requests, capacity planning, process documentation, and operational coordination.

Install a profile for an agent:

```bash
generated/install-scripts/kilo-code.sh --profile core
generated/install-scripts/opencode.sh --profile content-only
generated/install-scripts/claude-code.sh --profile security-audit --dry-run
```

## Supported Agents

- **Aider** (`aider`): repo_context, bootstrap_prompt. Installer: `generated/install-scripts/aider.sh`
- **Amazon Kiro** (`amazon-kiro`): specs, steering, mcp. Installer: `generated/install-scripts/amazon-kiro.sh`
- **Claude Code** (`claude-code`): skills, plugins, mcp, project_instructions. Installer: `generated/install-scripts/claude-code.sh`
- **Codex CLI** (`codex-cli`): skills, mcp, bootstrap_prompt. Installer: `generated/install-scripts/codex-cli.sh`
- **Cursor** (`cursor`): project_rules, plugins, mcp, docs. Installer: `generated/install-scripts/cursor.sh`
- **Kilo Code** (`kilo-code`): skills, mcp, project_instructions, custom_agents. Installer: `generated/install-scripts/kilo-code.sh`
- **OpenCode** (`opencode`): skills, plugins, project_instructions, mcp. Installer: `generated/install-scripts/opencode.sh`

## Scripts

| Script | What It Does |
| --- | --- |
| `scripts/bootstrap.sh` | Runs submodule init, registry validation, source catalogs, capability discovery, install-plan generation, and README generation. |
| `scripts/validate-registry.py` | Validates registry structure, trust levels, compatibility IDs, candidate enablement, and MCP policy constraints. |
| `scripts/discover-capabilities.py` | Scans real upstream files, extracts tags/facts, writes compact generated bundles, and creates install scripts. |
| `scripts/install-agent.py` | Used by generated install scripts to verify pins and copy profile-selected capabilities into the repo-local active cache. |
| `scripts/generate-readme.py` | Regenerates this README. |
| `scripts/update-submodules.sh` | Runs `git submodule update --init --recursive`. |

## Verify Generation

```bash
rm -rf generated
./scripts/bootstrap.sh
./scripts/validate-registry.py
git status --short
```

Expected generated files: `catalog.md`, `capabilities.json`, `install-bundle.json`, and `install-scripts/`. Runtime installs create ignored `generated/active/` and `generated/configs/`.
