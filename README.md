# AI Capability Registry

> **Warning**
> Connecting this registry through `AGENTS.full-registry.md.template` makes agents read routing indexes and selected capability guides at runtime. This can use substantially more model context and tokens than a minimal static agent setup. Prefer task-, role-, keyword-, or project-specific subsets when context budget matters.

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
git clone --recurse-submodules --jobs 8 <repo-url> ai-capability-registry
cd ai-capability-registry
```

For shared use across multiple repositories, keep this registry at `~/.ai-registry`:

```bash
git clone --recurse-submodules --jobs 8 <repo-url> ~/.ai-registry
cd ~/.ai-registry
```

The `--recurse-submodules` flag clones all pinned upstream capability sources. Use the generation commands below when you need to refresh derived catalogs after editing registry source files.

## How Agents Use This Registry

Agents can use this registry in 3 ways: static setup for agents cli with roles, dynamic routing at runtime or a minimal static setup derived from the registry for a specific agent, role, or task.

### Generate CLI Role Agent Configs

Generate role-level agent configs for a CLI from `registry/profiles.yaml` and `registry/model-tiers.yaml`.

```bash
# generate ~/.codex/roles/*.toml using the CLI default preset
python scripts/generate-agent-configs.py --cli codex --output ~/.codex --templates-path "$PWD"

# generate ~/.claude/agents/*.md using the CLI default preset
python scripts/generate-agent-configs.py --cli claude-code --output ~/.claude --templates-path "$PWD"

# generate ~/.config/kilo/agent/*.md and ~/.config/kilo/kilo.jsonc using the CLI default preset
python scripts/generate-agent-configs.py --cli kilo-code --output ~/.config/kilo --templates-path "$PWD"

# generate ~/.config/opencode/agents/*.md and ~/.config/opencode/opencode.json using the CLI default preset
python scripts/generate-agent-configs.py --cli opencode --output ~/.config/opencode --templates-path "$PWD"

# generate ~/.kiro/agents/*.json using the CLI default preset and single role levels
python scripts/generate-agent-configs.py --cli amazon-kiro --output ~/.kiro --templates-path "$PWD"

# collapse each profile to one generated agent id instead of tiered level ids
python scripts/generate-agent-configs.py --cli codex --output ~/.codex --role-levels single --preset none --templates-path "$PWD"
```

The generator defaults to `tiered` role levels for Codex, Claude Code, Kilo Code, and OpenCode, which creates one ready-to-use agent per role seniority level, for example `backend-engineer-middle`, `qa-engineer-senior`, and `orchestrator-senior`. Amazon Kiro defaults to `single` role levels, which collapses each profile into one agent id such as `backend-engineer`, `qa-engineer`, and `orchestrator`. Single mode requires `--preset none` or `--preset ""` so generated configs omit model fields, and it removes role-level labels from the rendered prompt and description. It also writes a compact `roles.md` catalog in the output root for fallback role selection. Cleanup removes stale generated agent files for both role-level modes inside the selected output tree, but it leaves unrelated files alone. Codex writes `config.toml` when no main config exists and `config.override.toml` when it does. Kilo Code writes `kilo.jsonc` when no main config exists and `kilo.override.jsonc` when it does; OpenCode follows the same main-or-override pattern with `opencode.json` and `opencode.override.json`. Claude Code and Amazon Kiro do not generate override note files.

For `kilo-code` and `opencode`, generated agent models use a three-part catalog id: `<outer-provider>/<model-provider>/<model-name>`. Defaults are `kilo` for `kilo-code` and `opencode-go` for `opencode`, so preset model `gpt-5.5` becomes `kilo/openai/gpt-5.5` or `opencode-go/openai/gpt-5.5`. Override the outer provider with `--model-prefix openrouter`, or disable only the outer provider with `--model-prefix ""`.

The default presets are `openai` for Codex, `anthropic` for Claude Code, `opencode` for Kilo Code, `opencode` for OpenCode, and `none` for Amazon Kiro.

Use `--preset none` or `--preset ""` when you want the generator to omit every `model` field from the rendered templates.

Use `--role-levels single` when you want one generated agent per profile instead of one agent per role seniority level.

### AGENTS.md Templates

Use `AGENTS.full-registry.md.template` to connect another repository to a shared registry stored at `~/.ai-registry` with the recommended workflow-first setup:

```bash
cp ~/.ai-registry/AGENTS.full-registry.md.template /path/to/project/AGENTS.md
```

The full-registry template is intentionally only a bootloader. It tells agents to read and follow `capability-routing.md`, start with `workflows/workflow.md`, use `workflows/routing.md` only when workflow selection is needed, load workflow-selected roles from `roles/`, then let those roles route to skills and MCP only when needed. More specific local repository instructions still override shared guidance.

Root templates are available for narrower setups:

| Template | Use |
| --- | --- |
| `AGENTS.full-registry.md.template` | Recommended workflow-first full-registry setup with role-mediated skills and MCP. |
| `AGENTS.workflows.md.template` | Workflow orchestration and roles only. |
| `AGENTS.skills.md.template` | Skill routing only. |
| `AGENTS.mcp.md.template` | MCP routing only. |
| `AGENTS.workflows-skills.md.template` | Workflow orchestration and role-mediated skills, without MCP routing by default. |

If the registry is installed somewhere else, edit the paths in the copied `AGENTS.md`.

### Workflows

Use the generated workflow runtime instructions when the agent should choose process guidance before loading concrete skills or MCP servers:

```
<path-to-registry>/workflows/workflow.md
```

For full workflow routing when no workflow scope is assigned, use:

```
<path-to-registry>/workflows/routing.md
```

For cross-repository use, prefer installing `AGENTS.full-registry.md.template` or `AGENTS.workflows.md.template` rather than adding partial workflow-only instructions.

Workflow routing should be read before skill routing. Workflows answer how to approach a task, which roles should participate, which stages and gates apply, and which artifacts are expected. Roles then decide which skills to load for their part of the workflow.

### Skills

Use the generated skill runtime instructions when the agent should dynamically choose skills per request:

```
<path-to-registry>/skills/skills.md
```

For full role and task capability routing when no registry scope is assigned, use:

```
<path-to-registry>/skills/routing.md
```

For dynamic routing, agents should usually reach `skills/skills.md` through workflow-selected role prompts. Direct skill-only use is still supported through `AGENTS.skills.md.template` or an equivalent bootloader.

For direct agent configuration, attach one generated pack instead of the whole registry when you want a narrower static setup:

```
<path-to-registry>/skills/packs/roles/<role-id>/
<path-to-registry>/skills/packs/tasks/<task-id>/
<path-to-registry>/skills/packs/keywords/<keyword>/
```

`skills/packs/all/` exists, but it is mainly useful for inspection or experiments. Prefer task, role, keyword, or custom minimal packs for real agents.

### MCP

Use the generated MCP runtime instructions when the agent should choose MCP servers only when a task needs them:

```
<path-to-registry>/mcp/mcp.md
```

For full role and task capability routing when no registry scope is assigned, use:

```
<path-to-registry>/mcp/routing.md
```

For dynamic routing, agents should usually reach `mcp/mcp.md` through workflow-selected role prompts or workflow stage guidance. Direct MCP-only use is still supported through `AGENTS.mcp.md.template` or an equivalent bootloader.

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
| `registry/profiles.yaml` | Role/profile source configuration used by workflow role matching |
| `skill-catalog.d/*.yaml` | Source of truth for discovered skills |
| `mcp-catalog.d/*.yml` | Source of truth for MCP servers |

Generated outputs:

| Path | Purpose |
| --- | --- |
| `skills/skills.md` | Skill runtime instructions and scoped selection protocol |
| `skills/routing.md` | Full skill role and task routing index |
| `skills/catalog/tasks/<task>/skills.md` | Skill task routing indexes |
| `skills/catalog/roles/<role>/skills.md` | Skill role routing indexes |
| `skills/catalog/keywords/<keyword>/skills.md` | Skill keyword routing indexes |
| `skills/packs/` | Symlink packs for direct agent inclusion |
| `workflows/workflow.md` | Generated workflow runtime instructions and coordination protocol |
| `workflows/routing.md` | Generated root workflow routing index |
| `workflows/catalog/tasks/<task>/workflows.md` | Generated workflow task routing indexes |
| `workflows/catalog/roles/<role>/workflows.md` | Generated workflow role routing indexes |
| `workflows/catalog/categories/<category>/workflows.md` | Generated workflow category routing indexes |
| `workflows/catalog/tags/<tag>/workflows.md` | Generated workflow tag routing indexes |
| `workflows-catalog.md` | Generated human-readable workflow catalog view |
| `workflows/<category>/<workflow>/workflow.md` | Workflow guide files referenced by workflow routing |
| `workflows/<category>/<workflow>/workflow.yaml` | Workflow manifests with stages, roles, gates, and acceptance criteria |
| `roles/<role-id>.md` | Runtime role prompts loaded by workflow stages |
| `mcp/mcp.md` | MCP runtime instructions, transport guidance, and safety rules |
| `mcp/routing.md` | Full MCP role and task routing index |
| `mcp/catalog/tasks/<task>/servers.md` | MCP task routing indexes |
| `mcp/catalog/roles/<role>/servers.md` | MCP role routing indexes |
| `mcp/catalog/keywords/<keyword>/servers.md` | MCP keyword routing indexes |
| `mcp/servers/<server-id>/SKILL.md` | Generated MCP usage wrapper |
| `mcp/servers/<server-id>/connection.json` | Generated MCP connection metadata |
| `skill-catalog.md`, `workflows-catalog.md`, and `mcp-catalog.md` | Generated human-readable catalog views |

Do not edit generated files directly. Edit source chunks, then regenerate.

## Catalog Editing

For skills, edit only `enabled` and `keywords` in `skill-catalog.d/*.yaml`. New discovered skills are added disabled by default, and removed upstream skills remain with `exists: false`.

For MCP, keep hand-curated entries in `mcp-catalog.d/manual.yml`. Auto-discovered entries from `official-mcp-registry.yml` and `docker-mcp-registry.yml` should stay disabled until reviewed, assigned useful keywords, and explicitly promoted with `enabled: true`.

Important MCP fields are `enabled`, `exists`, `trust`, `runtime`, `transport.type`, `default_mode`, and `keywords`.

## Regeneration

| Command | Use |
| --- | --- |
| `./scripts/generate-workflows.py` | Regenerate `workflows/workflow.md`, `workflows/routing.md`, `workflows-catalog.md`, and workflow catalogs from `registry/workflows.yaml` |
| `./scripts/discover-skills.py` | Regenerate skill catalogs and packs from `skill-catalog.d/` |
| `./scripts/discover-mcp.py` | Import disabled candidate MCP entries from configured upstream sources |
| `./scripts/generate-mcp.py` | Regenerate `mcp/` and `mcp-catalog.md` from `mcp-catalog.d/` |
| `python scripts/generate-agent-configs.py --cli <cli> --output configs/<cli> --templates-path "$PWD"` | Generate CLI-specific role agent configs from `registry/profiles.yaml` and `registry/model-tiers.yaml` using the CLI default preset; Codex, Kilo Code, and OpenCode write a main config when absent and an override when the main config already exists |
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
