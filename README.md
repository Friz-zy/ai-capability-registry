# AI Capability Registry

> **Warning**
> Connecting this registry through `AGENTS.md.template` makes agents read routing indexes and selected capability guides at runtime. This can use substantially more model context and tokens than a minimal static agent setup. Prefer task-, role-, keyword-, or project-specific subsets when context budget matters.

AI Capability Registry is an experiment in dynamic capability routing for AI agents: load the right skills, MCP servers, workflows, and integration instructions only when the current task needs them.

Instead of stuffing every agent with a huge static prompt, a random pile of tools, or every available MCP server, this repository treats agent capabilities as versioned infrastructure. An agent can resolve the user's request by task, role, and keywords, then progressively load only the relevant skill instructions or MCP connection guidance.

This is not the theoretical optimum for every setup. A carefully hand-tuned agent with the smallest possible set of skills and MCP servers for one specific task will usually be simpler, faster, and easier to reason about. The registry is meant for the more common middle ground: teams and users who run many agents across many tasks and need something better than enabling a broad list of skills and MCP servers for every agent "just in case". Many agent tools make that broad attachment path easy; this project explores a more explicit routing layer between fully minimal per-agent configuration and everything-enabled-by-default capability sprawl.

You can also use the registry as a starting point for minimal static setups. A user can ask their AI assistant to inspect the shared registry and assemble the smallest useful set of skills and MCP servers for a specific role, task, or agent configuration. In that mode, the registry is not the runtime layer itself; it is the common source of reviewed capabilities from which task-specific agent setups are derived.

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

For shared use across multiple repositories, keep this registry at `~/.ai-registry`:

```bash
git clone --recurse-submodules <repo-url> ~/.ai-registry
cd ~/.ai-registry
./scripts/bootstrap.sh
```

The bootstrap script will:
1. Sync external submodules to correct commits
2. Validate registry configuration
3. Sync provider chunks under `skill-catalog.d/` with discovered skills
4. Generate the workflow routing index from `registry/workflows.yaml`
5. Generate the combined `skills/` routing catalogs and symlink packs from `skill-catalog.d/`
6. Generate MCP routing catalogs from `mcp-catalog.d/`

## How Agents Use This Registry

Agents can use this registry in two ways: dynamic routing at runtime or a minimal static setup derived from the registry for a specific agent, role, or task.

### AGENTS.md Template

Use `AGENTS.md.template` to connect another repository to a shared registry stored at `~/.ai-registry`:

```bash
cp ~/.ai-registry/AGENTS.md.template /path/to/project/AGENTS.md
```

The template is intentionally only a bootloader. It tells agents to read and follow `capability-routing.md`, `workflows/workflows.md`, `skills/skills.md`, and `mcp/mcp.md` from the shared registry, while allowing more specific local repository instructions to override shared guidance.

If the registry is installed somewhere else, edit the paths in the copied `AGENTS.md`.

### Workflows

Use the generated workflow routing index when the agent should choose process guidance before loading concrete skills or MCP servers:

```
<path-to-registry>/workflows/workflows.md
```

For cross-repository use, prefer installing `AGENTS.md.template` rather than adding partial workflow-only instructions.

Workflow routing should be read before skill routing. Workflows answer how to approach a task; skills provide concrete task, tool, or domain instructions.

### Skills

Use the generated skill routing index when the agent should dynamically choose skills per request:

```
<path-to-registry>/skills/skills.md
```

For dynamic routing, agents should reach this file through `AGENTS.md.template` or an equivalent bootloader that also includes `capability-routing.md`, workflows, and MCP routing.

For direct agent configuration, attach one generated pack instead of the whole registry when you want a narrower static setup:

```
<path-to-registry>/skills/packs/roles/<role-id>/
<path-to-registry>/skills/packs/tasks/<task-id>/
<path-to-registry>/skills/packs/keywords/<keyword>/
```

`skills/packs/all/` exists, but it is mainly useful for inspection or experiments. Prefer task, role, keyword, or custom minimal packs for real agents.

### MCP

Use the generated MCP routing index when the agent should choose MCP servers only when a task needs them:

```
<path-to-registry>/mcp/mcp.md
```

For dynamic routing, agents should reach this file through `AGENTS.md.template` or an equivalent bootloader that also includes `capability-routing.md`, workflows, and skills routing.

For direct agent configuration, adapt the generated connection metadata to your agent's MCP config schema:

```
<path-to-registry>/mcp/servers/<server-id>/connection.json
<path-to-registry>/mcp/servers/<server-id>/SKILL.md
```

Hosted MCP servers should follow `mcp/web.md`. Docker MCP servers should follow `mcp/docker.md` and must avoid privileged containers, host networking, Docker socket mounts, unrestricted host mounts, SSH key mounts, and cloud credential directory mounts.

## Registry Map

Editable source chunks:

| Path | Purpose |
| --- | --- |
| `registry/skills.yaml` | Upstream skills discovery source configuration |
| `registry/mcp-sources.yaml` | Upstream MCP discovery source configuration |
| `registry/workflows.yaml` | Workflow routing source configuration |
| `skill-catalog.d/*.yaml` | Source of truth for discovered skills |
| `mcp-catalog.d/*.yml` | Source of truth for MCP servers |

Generated outputs:

| Path | Purpose |
| --- | --- |
| `skills/skills.md` | Root skill routing index |
| `skills/catalog/tasks/<task>/skills.md` | Skill task routing indexes |
| `skills/catalog/roles/<role>/skills.md` | Skill role routing indexes |
| `skills/catalog/keywords/<keyword>/skills.md` | Skill keyword routing indexes |
| `skills/packs/` | Symlink packs for direct agent inclusion |
| `workflows/workflows.md` | Root workflow routing index |
| `workflows/<workflow>.md` | Workflow guide files referenced by the workflow index |
| `mcp/mcp.md` | Root MCP routing index |
| `mcp/catalog/tasks/<task>/servers.md` | MCP task routing indexes |
| `mcp/catalog/roles/<role>/servers.md` | MCP role routing indexes |
| `mcp/catalog/keywords/<keyword>/servers.md` | MCP keyword routing indexes |
| `mcp/servers/<server-id>/SKILL.md` | Generated MCP usage wrapper |
| `mcp/servers/<server-id>/connection.json` | Generated MCP connection metadata |
| `skill-catalog.md` and `mcp-catalog.md` | Generated human-readable catalog views |

Do not edit generated files directly. Edit source chunks, then regenerate.

## Catalog Editing

For skills, edit only `enabled` and `keywords` in `skill-catalog.d/*.yaml`. New discovered skills are added disabled by default, and removed upstream skills remain with `exists: false`.

For MCP, keep hand-curated entries in `mcp-catalog.d/manual.yml`. Auto-discovered entries from `official-mcp-registry.yml` and `docker-mcp-registry.yml` should stay disabled until reviewed, assigned useful keywords, and explicitly promoted with `enabled: true`.

Important MCP fields are `enabled`, `exists`, `trust`, `runtime`, `transport.type`, `default_mode`, and `keywords`.

## Regeneration

| Command | Use |
| --- | --- |
| `./scripts/bootstrap.sh` | Full sync, validation, workflow generation, skills generation, and MCP generation |
| `./scripts/generate-workflows.py` | Regenerate `workflows/workflows.md` from `registry/workflows.yaml` |
| `./scripts/discover-skills.py` | Regenerate skill catalogs and packs from `skill-catalog.d/` |
| `./scripts/discover-mcp.py` | Import disabled candidate MCP entries from configured upstream sources |
| `./scripts/generate-mcp.py` | Regenerate `mcp/` and `mcp-catalog.md` from `mcp-catalog.d/` |
| `./scripts/validate-registry.py` | Validate registry YAML structure and policy constraints |

## Trust And Policy

Trust levels: `trusted` for official or reputable security-reviewed sources, `reviewed` for manually reviewed known maintainers, and `candidate` for discovery-only entries.

Policy defaults:

- Use trusted or reviewed capabilities by default.
- Keep discovered candidates disabled until reviewed.
- Prefer hosted MCP or constrained Docker MCP.
- Deny direct `node`, `npx`, `python`, `pip`, and `uvx` MCP runners.
- Never use `curl | sh`, privileged Docker, host networking, Docker socket mounts, or unrestricted host mounts.
- Load skills and MCP servers only when they are relevant to the current task.

Trusted skill sources currently include Anthropic skills and knowledge-work plugins, OpenAI skills, Vercel Agent Skills, the Agent Skills specification, Superpowers development methodology skills, Trail of Bits security workflows, and Kilo Marketplace skills.
