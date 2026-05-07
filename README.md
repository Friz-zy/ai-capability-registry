# AI Capability Registry

Curated AI skills, MCP servers, workflows, and agent integrations for secure multi-agent development.

This repository turns AI-agent capability sprawl into a reproducible GitOps-style registry. It downloads upstream sources as pinned submodules, inventories every discovered skill, and generates a cascading skill map organized by roles and tags for dynamic agent capability routing.

## Setup

```bash
git clone --recurse-submodules <repo-url>
cd ai-capability-registry
./scripts/bootstrap.sh
```

The bootstrap script will:
1. Sync external submodules to correct commits
2. Validate registry configuration
3. Generate skill maps in `generated/`

## How Agents Use This Registry

Point your agent to the generated skills index:

```
<path-to-registry>/generated/skills.md
```

For example:

```bash
REGISTRY_ROOT=$(PWD)
echo "Skills index: $REGISTRY_ROOT/generated/skills.md"
echo "" >> AGENTS.md
echo "Read also instructions from $REGISTRY_ROOT/generated/skills.md" >> AGENTS.md
```

## Navigation

All paths in generated files are absolute — ready to use on any machine.

```
generated/skills.md           (root index - all roles)
  → generated/roles/<role>/skills.md  (role catalog - delegates to tags)
  → generated/tags/<tag>/skills.md    (tag catalog - lists skills)
  → <absolute-path>/SKILL.md         (actual skill file)
```

## Generated Structure

```
generated/
├── skills.md              # Root index (point your agent here)
├── roles/                 # 22 role catalogs
│   └── <role-id>/skills.md
└── tags/                  # Tag catalogs
    └── <tag>/skills.md
```

## Trust Levels

- `trusted`: Official vendor or reputable security-reviewed source. Used by default.
- `reviewed`: Manually reviewed source from a known maintainer. Available on request.
- `candidate`: Discovery-only sources. Not installed by default.

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

## Scripts

| Script | What It Does |
| --- | --- |
| `scripts/bootstrap.sh` | Full setup: sync submodules, validate, generate skill maps |
| `scripts/update-external.py` | Sync external/ submodules with skills.yaml config |
| `scripts/validate-registry.py` | Validate registry YAML structure and policies |
| `scripts/discover-skills.py` | Generate cascading skill maps by roles and tags |

## Regenerate Skill Maps

If you modify `registry/skills.yaml` or update submodules:

```bash
./scripts/bootstrap.sh
```

This regenerates `generated/` with absolute paths.

## Policy

- Use **trusted** or **reviewed** sources only
- Prefer Docker/hosted MCP
- Never execute untrusted scripts
- Load skills dynamically — only when relevant to current task
