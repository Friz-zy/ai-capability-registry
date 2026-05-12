# AI Capability Registry

AI Capability Registry is an experiment in dynamic capability routing for AI agents: load the right skills, MCP servers, workflows, and integration instructions only when the current task needs them.

Instead of stuffing every agent with a huge static prompt, a random pile of tools, or every available MCP server, this repository treats agent capabilities as versioned infrastructure. An agent can resolve the user's request by task, role, and keywords, then progressively load only the relevant skill instructions or MCP connection guidance.

This is not the theoretical optimum for every setup. A carefully hand-tuned agent with the smallest possible set of skills and MCP servers for one specific task will usually be simpler, faster, and easier to reason about. The registry is meant for the more common middle ground: teams and users who run many agents across many tasks and need something better than enabling a broad list of skills and MCP servers for every agent "just in case". Many agent tools make that broad attachment path easy; this project explores a more explicit routing layer between fully minimal per-agent configuration and everything-enabled-by-default capability sprawl.

The goal is to make AI-agent capability management more modular, reproducible, and reviewable:

- discover and curate skills, MCP servers, workflows, and agent integrations from upstream sources;
- organize capabilities by tasks, roles, and keywords for runtime routing;
- keep enabled capabilities explicit in Git rather than hidden in local agent state;
- separate trusted, reviewed, and candidate capabilities;
- prefer safer MCP runtimes such as hosted endpoints or constrained Docker containers;
- let multi-agent setups share the same capability registry instead of duplicating prompt/tool configuration.

This repository turns AI-agent capability sprawl into a reproducible GitOps-style registry. It downloads upstream sources as pinned submodules, inventories every discovered skill and MCP entry, and generates routing catalogs plus symlink packs organized by roles, tasks, and keywords.

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
4. Generate the combined `skills/` routing catalogs and symlink packs from `skill-catalog.d/`
5. Generate MCP routing catalogs from `mcp-catalog.d/`

## How Agents Use This Registry

Agents can consume skills in either of two ways:

1. Point the agent to the generated routing index:

```
<path-to-registry>/skills/skills.md
```

2. Attach a whole generated skill pack:

```
<path-to-registry>/skills/packs/roles/<role-id>/
<path-to-registry>/skills/packs/tasks/<task-id>/
<path-to-registry>/skills/packs/keywords/<keyword>/
<path-to-registry>/skills/packs/all/
```

For example:

```bash
REGISTRY_ROOT="path to your skills registry"
echo "Skills index: $REGISTRY_ROOT/skills/skills.md"
echo "Frontend role pack: $REGISTRY_ROOT/skills/packs/roles/frontend-engineer"
echo "" >> AGENTS.md
echo "Read also instructions from $REGISTRY_ROOT/skills/skills.md" >> AGENTS.md
```

## Navigation

Skill routing catalogs live under `skills/catalog/`. Skill entries inside `skills/packs/` are symlinks back to skill directories under `external/`. MCP routing catalogs live under `mcp/` and are generated from `mcp-catalog.d/*.yml`.

```
skill-catalog.d/<provider>.yaml                 (source of truth for enabled/disabled skills)
  -> skills/skills.md                            (root routing index)
    -> skills/catalog/tasks/<task>/skills.md     (task routing catalog)
    -> skills/catalog/roles/<role>/skills.md     (optional role routing catalog)
    -> skills/catalog/keywords/<keyword>/skills.md  (keyword catalog with skill descriptions)
    -> external/<source>/<path>/SKILL.md         (actual skill file)
  -> skills/packs/                               (symlink packs for direct config inclusion)

mcp-catalog.d/<source>.yml           (source of truth for MCP servers)
  -> mcp/mcp.md                                  (root MCP routing index with resolution protocol)
  -> mcp/web.md                                  (HTTPS/SSE MCP connector guide)
  -> mcp/docker.md                               (Docker MCP connector guide)
  -> mcp/common.md                               (general MCP concepts and diagnostics)
  -> mcp/catalog/tasks/<task>/servers.md         (task routing catalog)
  -> mcp/catalog/roles/<role>/servers.md         (optional role routing catalog)
  -> mcp/catalog/runtime/<runtime>/servers.md    (runtime routing catalogs)
  -> mcp/catalog/keywords/<keyword>/servers.md   (keyword routing catalogs)
  -> mcp/servers/<server>/SKILL.md               (generated MCP usage wrapper)
  -> mcp/servers/<server>/connection.json        (generated MCP connection config)
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
├── skills.md                    # Root routing index (point your agent here)
├── catalog/                     # Routing-only indexes for progressive disclosure
│   ├── roles/<role-id>/skills.md
│   ├── tasks/<task-id>/skills.md
│   └── keywords/<keyword>/skills.md
└── packs/                       # Symlink packs for direct agent config inclusion
    ├── all/                     # Every existing enabled skill once
    ├── roles/<role-id>/
    ├── tasks/<task-id>/
    └── keywords/<keyword>/
```

`skill-catalog.md` is generated as a human-readable view of `skill-catalog.d/`; do not edit it directly.

## MCP Catalog

`mcp-catalog.d/*.yml` files are the editable source of truth for MCP servers. `registry/mcp.yaml` has been intentionally removed so MCP entries can be split by source, just like skill provider chunks.

The manual chunk is:

```
mcp-catalog.d/manual.yml
```

Keep `manual.yml` only for curated entries that are not discoverable from configured upstream sources. Auto-discovered sources should write source-specific chunks such as `official-mcp-registry.yml` or `docker-mcp-registry.yml`; imported entries must remain `enabled: false` until reviewed.

Allowed MCP runtimes:

- public HTTPS endpoints using Streamable HTTP or SSE;
- Docker/OCI images launched only through `docker run --rm`.

Denied MCP runtimes:

- direct `node`, `npx`, `python`, `pip`, or `uvx`;
- `curl | sh`;
- Docker host escape modes such as `--privileged`, `--network=host`, or unrestricted host mounts.

Generate MCP indexes with:

```bash
./scripts/generate-mcp.py
```

Optionally discover candidates from configured upstream sources with:

```bash
./scripts/discover-mcp.py
```

`mcp-catalog.md` is generated as a human-readable view of `mcp-catalog.d/`; do not edit it directly.

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
| `scripts/discover-mcp.py` | Import disabled candidate MCP entries from allowed upstream registries into `mcp-catalog.d/` |
| `scripts/generate-mcp.py` | Generate `mcp/` routing indexes, MCP skill wrappers, and `mcp-catalog.md` from `mcp-catalog.d/` |
| `scripts/generate-collections-all.py` | Regenerate `skills/packs/all` from enabled entries in `skill-catalog.d/` |

## Regenerate Skills Tree

If you modify `registry/skills.yaml`, `skill-catalog.d/`, `mcp-catalog.d/`, keyword categories, tasks, profiles, or update submodules:

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
