# AI Capability Registry

Curated AI skills, MCP servers, workflows, and agent integrations for secure multi-agent development.

This repository turns AI-agent capability sprawl into a reproducible GitOps-style registry. It downloads upstream sources as pinned submodules, inventories every discovered skill, and generates a cascading skill map organized by roles and tags for dynamic agent capability routing.

## What You Get

- 7 trusted skill/plugin sources indexed (all with pinned commits)
- 9 MCP servers cataloged
- 22 role-based profiles
- 370+ skills organized into tag catalogs
- Cascading skill map: Roles → Tags → Skills
- Agent bootstrap template for dynamic capability routing

## Quick Start

```bash
git clone --recurse-submodules <repo-url>
cd ai-capability-registry
./scripts/bootstrap.sh
```

## Core Model

```
external/      Pinned upstream sources (trusted only)
registry/      Source metadata, trust levels, tag categories, profiles, policies
generated/     Generated skill maps (roles/, tags/, skills.md, agents.md.template)
```

## How Agents Use This Registry

The registry uses a cascading navigation model:

```
generated/agents.md.template
  → generated/skills.md           (root index - all roles)
  → generated/roles/<role>/skills.md  (role catalog - delegates to tags)
  → generated/tags/<tag>/skills.md    (tag catalog - lists skills with paths)
  → external/<source>/<path>/SKILL.md (actual skill file)
```

Agents read `generated/agents.md.template` to understand how to navigate the registry, then dynamically load only the skills relevant to their current task.

## Generated Output

| Path | Purpose |
| --- | --- |
| `generated/skills.md` | Root index listing all roles |
| `generated/agents.md.template` | Bootstrap template for agents with navigation instructions |
| `generated/roles/<id>/skills.md` | Role catalog delegating to tag catalogs |
| `generated/tags/<tag>/skills.md` | Tag catalog listing skills with full paths |

## Trust Levels

- `trusted`: Official vendor or reputable security-reviewed source. Used by default.
- `reviewed`: Manually reviewed source from a known maintainer. Available on request.
- `candidate`: Discovery-only sources. Not installed by default.

Only `trusted` and `reviewed` sources are indexed in the skill maps.

## Profiles (Roles)

Each profile defines which tag categories are relevant:

| Profile | Categories |
| --- | --- |
| `personal-assistant` | core, research |
| `software-engineer` | core, engineering, backend, frontend, qa |
| `security-engineer` | security |
| `devops-platform-engineer` | devops, sre, security |
| `data-analyst` | data, research, product |
| `ai-engineer` | ai_ml, engineering, security, research |
| ... | Full list in `generated/skills.md` |

## External Sources (Trusted)

| Source | Description |
| --- | --- |
| `anthropic-skills` | Official Anthropic skill catalog |
| `anthropic-claude-plugins-official` | Anthropic Claude plugin marketplace |
| `anthropic-knowledge-work-plugins` | Anthropic knowledge-work plugins |
| `openai-skills` | OpenAI skills for Codex |
| `agentskills-spec` | Portable skill specification |
| `trailofbits-skills` | Security research and audit workflows |
| `trailofbits-skills-curated` | Trail of Bits curated marketplace |

All sources use pinned commits verified in CI.

## Scripts

| Script | What It Does |
| --- | --- |
| `scripts/bootstrap.sh` | Full bootstrap: sync submodules, validate registry, generate skill maps |
| `scripts/update-external.py` | Sync external/ submodules with skills.yaml config |
| `scripts/validate-registry.py` | Validates registry YAML structure and policies |
| `scripts/discover-skills.py` | Generates cascading skill maps by roles and tags |

### update-external.py

This script ensures external/ submodules always match the skills.yaml configuration:

1. **Reads** `registry/skills.yaml` to get all enabled sources with pinned commits
2. **Adds** new submodules if they don't exist
3. **Removes** old submodules if they're no longer in config or not trusted/reviewed
4. **Updates** all submodules to the correct pinned commit
5. **Verifies** all submodules are at the correct commit after sync

Run this script independently to synchronize submodules:

```bash
./scripts/update-external.py
```

## Skill Resolution Example

```
Task: Review Terraform configuration for AWS security

1. Read generated/agents.md.template
2. Navigate to generated/skills.md
3. Select role: devops-platform-engineer
4. Read generated/roles/devops-platform-engineer/skills.md
5. Find relevant tag: terraform, security, cloud, aws
6. Read generated/tags/terraform/skills.md
7. Read generated/tags/security/skills.md
8. Access specific skill files in external/
```

## Philosophy

AGENTS.md should be an **orchestration bootstrap layer**, not a dump of all instructions.

Agents receive:
- Navigation instructions (this registry)
- Policy rules (trust, execution)
- Dynamic skill loading (cascading maps)

Agents decide:
- Which role to use
- Which tags are relevant
- Which specific skills to load

This enables scalable, composable, and portable agent configurations.
