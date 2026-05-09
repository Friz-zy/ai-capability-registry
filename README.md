# AI Capability Registry

Curated AI skills, MCP servers, workflows, and agent integrations for secure multi-agent development.

This repository turns AI-agent capability sprawl into a reproducible GitOps-style registry. It downloads upstream sources as pinned submodules, inventories every discovered skill, and generates a cascading skill map organized by roles and keywords for dynamic agent capability routing.

## Setup

```bash
git clone --recurse-submodules <repo-url>
cd ai-capability-registry
./scripts/bootstrap.sh
```

The bootstrap script will:
1. Sync external submodules to correct commits
2. Validate registry configuration
3. Sync provider chunks under `skill-catalog.d/` with discovered skills
4. Generate the combined `skills/` routing indexes and symlink directories from `skill-catalog.d/`

## How Agents Use This Registry

Agents can consume skills in either of two ways:

1. Point the agent to the generated routing index:

```
<path-to-registry>/skills/skills.md
```

2. Attach a whole generated skill directory:

```
<path-to-registry>/skills/roles/<role-id>/
<path-to-registry>/skills/tasks/<task-id>/
<path-to-registry>/skills/keywords/<keyword>/
<path-to-registry>/skills/all/
```

For example:

```bash
REGISTRY_ROOT="path to your skills registry"
echo "Skills index: $REGISTRY_ROOT/skills/skills.md"
echo "Frontend role skills: $REGISTRY_ROOT/skills/roles/frontend-engineer"
echo "" >> AGENTS.md
echo "Read also instructions from $REGISTRY_ROOT/skills/skills.md" >> AGENTS.md
```

## Navigation

Skill entries inside `skills/roles/`, `skills/tasks/`, `skills/keywords/`, and `skills/all/` are symlinks back to skill directories under `external/`.

```
skill-catalog.d/<provider>.yaml       (source of truth for enabled/disabled skills)
  → skills/skills.md               (root index - all roles)
    → skills/roles/<role>/skills.md    (role catalog plus matching skill symlinks)
    → skills/tasks/<task>/skills.md    (task catalog plus matching skill symlinks)
    → skills/keywords/<keyword>/skills.md  (keyword catalog plus matching skill symlinks)
    → <absolute-path>/SKILL.md          (actual skill file)
  → skills/all/                         (all enabled skills once)
```

## Skill Catalog and Generated Structure

`skill-catalog.d/<provider>.yaml` files are the editable source of truth for discovered skills. The generation script keeps discovered entries in sync while preserving existing `enabled` and `keywords` values. Newly discovered skills are added with `enabled: false` and auto-filled `keywords`. After that first insertion, `keywords` are manual and are not overwritten by the script.

Removed upstream skills remain in the catalog with `exists: false`; the generated `skills/` tree only uses entries where both `exists: true` and `enabled: true`.

Edit only `enabled` and `keywords` manually:

```yaml
skills:
  - id: "external/source/path/to/skill"
    exists: true
    enabled: true
    name: "skill-name"
    description: "Human-readable skill description"
    keywords:
      - "manual-or-initial-keyword"
```

Generated outputs:

```
skills/
├── skills.md              # Root index (point your agent here)
├── all/                   # Every existing enabled skill once, as symlinks
├── roles/                 # Role catalogs and symlinks from registry/profiles.yaml
│   └── <role-id>/
│       ├── skills.md
│       └── <source>-<skill> -> external/...
├── tasks/                 # Task catalogs and symlinks from registry/tasks.yaml
│   └── <task-id>/
│       ├── skills.md
│       └── <source>-<skill> -> external/...
└── keywords/              # Keyword catalogs and symlinks from registry/keyword-categories.yaml
    └── <keyword>/
        ├── skills.md
        └── <source>-<skill> -> external/...
```

`skill-catalog.md` is generated as a human-readable view of `skill-catalog.d/`; do not edit it directly.

## Trust Levels

- `trusted`: Official vendor or reputable security-reviewed source. Used by default.
- `reviewed`: Manually reviewed source from a known maintainer. Available on request.
- `candidate`: Discovery-only sources. Not installed by default.

## External Sources (Trusted)

| Source | Description |
| --- | --- |
| `anthropic-skills` | Official Anthropic skill catalog |
| `anthropic-claude-plugins-official` | Anthropic Claude plugin marketplace (disabled by default; plugin-dependent skills should be enabled explicitly after review) |
| `anthropic-knowledge-work-plugins` | Anthropic knowledge-work plugins |
| `openai-skills` | OpenAI skills for Codex |
| `agentskills-spec` | Portable skill specification |
| `trailofbits-skills` | Security research and audit workflows |
| `trailofbits-skills-curated` | Trail of Bits curated marketplace |
| `kilo-marketplace-skills` | Kilo Marketplace skills from `skills/` |

## Scripts

| Script | What It Does |
| --- | --- |
| `scripts/bootstrap.sh` | Full setup: sync submodules, validate, sync catalog, generate the combined skills tree |
| `scripts/update-external.py` | Sync external/ submodules with skills.yaml config |
| `scripts/validate-registry.py` | Validate registry YAML structure and policies |
| `scripts/discover-skills.py` | Sync `skill-catalog.d/`, generate `skills/`, and generate `skill-catalog.md` |
| `scripts/generate-collections-all.py` | Regenerate `skills/all` from enabled entries in `skill-catalog.d/` |

## Regenerate Skills Tree

If you modify `registry/skills.yaml`, `skill-catalog.d/`, keyword categories, tasks, profiles, or update submodules:

```bash
./scripts/bootstrap.sh
```

For generation only:

```bash
./scripts/discover-skills.py
```

This syncs `skill-catalog.d/`, then regenerates `skills/` and `skill-catalog.md` from the catalog.

## Policy

- Use **trusted** or **reviewed** sources only
- Prefer Docker/hosted MCP
- Never execute untrusted scripts
- Load skills dynamically — only when relevant to current task
