# AI Capability Registry

Curated AI skills, MCP servers, workflows, and agent integrations for secure multi-agent development.

This repository is a GitOps-style capability registry. Registry YAML is the source of truth; generated Markdown and agent configs are derived artifacts.

## Security Model

- Everything can be indexed, almost nothing is auto-enabled.
- Trusted or reviewed capabilities are promoted into active profiles only after manual review.
- MCP runtimes must be hosted HTTPS/OAuth or Docker-isolated.
- Random `npx`, `curl | sh`, unknown Python servers, arbitrary shell MCP, and unrestricted filesystem MCP are denied.
- Read-only or ask-before-write defaults are preferred for all integrations.

## Repository Layout

```text
registry/      Declarative source of truth
skills/        Local category anchors and generated references
mcp/           Docker/hosted MCP templates and generated references
adapters/      Agent-specific install/bootstrap helpers
scripts/       Validation and generation tooling
generated/     Generated catalogs and configs
external/      Pinned upstream sources as submodules or indexes
```

## Current Catalog

- Skills indexed: 14
- Trusted skills: 8
- MCP servers indexed: 8
- MCP servers enabled by default: 7
- Agent adapters: 7

## Supported Agents

- **Aider** (`aider`): repo_context, bootstrap_prompt
- **Amazon Kiro** (`amazon-kiro`): specs, steering, mcp
- **Claude Code** (`claude-code`): skills, mcp, project_instructions
- **Codex CLI** (`codex-cli`): skills, mcp, bootstrap_prompt
- **Cursor** (`cursor`): project_rules, mcp, docs
- **Kilo Code** (`kilo-code`): skills, mcp, project_instructions, custom_agents
- **OpenCode** (`opencode`): project_instructions, mcp

## Generated Catalogs

- `generated/skills.md`
- `generated/README.skills.md`
- `generated/mcp-catalog.md`
- `generated/workflows.md`
- `generated/agent-configs/`

## Bootstrap

```bash
./scripts/bootstrap.sh
```

Bootstrap validates registry metadata, regenerates indexes, refreshes adapter configs, and creates local symlink references when pinned external sources exist.

## Manual Commands

```bash
./scripts/validate-registry.py
./scripts/generate-index.py
./scripts/generate-agent-configs.py
./scripts/generate-readme.py
./scripts/link-artifacts.py
```

## Trust Levels

- `trusted`: Official vendor or reputable security-reviewed source. Actions: index, install, enable_by_default.
- `reviewed`: Manually reviewed source from a known maintainer or curated marketplace. Actions: index, install, enable_manually.
- `candidate`: Useful discovery source that is not trusted for direct installation. Actions: index_only.
- `denied`: Unsafe execution model, unknown maintainer, or known risky behavior. Actions: none.
- `trusted_runtime_layer`: Infrastructure layer used to isolate allowlisted capabilities. Actions: index, install, route_allowlisted_only.

## Update Workflow

1. Add or update registry YAML.
2. Pin upstream source tag and commit when enabling installable content.
3. Run validation and generation scripts.
4. Review generated diffs.
5. Promote only reviewed capabilities into active profiles.
