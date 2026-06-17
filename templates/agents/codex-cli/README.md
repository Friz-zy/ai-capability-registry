# Codex CLI Configuration Templates

## Where to Place Files

| File | Global | Project | Managed (enterprise) |
|------|--------|---------|----------------------|
| `config.toml` | `~/.codex/config.toml` | `.codex/config.toml` | `/etc/codex/config.toml` |
| `agent-role.toml` | Path referenced by `config_file` in `[agents.<name>]` | Same | — |
| `SKILL.md` | `~/.agents/skills/<name>/SKILL.md` | `.agents/skills/<name>/SKILL.md` | — |
| `AGENTS.md` | `~/.codex/AGENTS.md` | `<project-root>/AGENTS.md` (hierarchical) | — |

Profiles: `~/.codex/<name>.config.toml` (selected with `--profile <name>`)

### File Placement Details

#### `config.toml` — Main configuration

```
# Global (applies to all projects)
~/.codex/config.toml

# Project (applies only to this project)
my-project/.codex/config.toml

# Profile-specific (selected with --profile <name>)
~/.codex/code-review.config.toml
~/.codex/security.config.toml

# Managed/enterprise (system-wide, enforced)
/etc/codex/config.toml
```

Override the config directory with `CODEX_HOME` env var.

#### `agent-role.toml` — Agent role definition

```
# Place anywhere and reference from config.toml via config_file:
#   [agents.reviewer]
#   config_file = "./agents/reviewer.toml"
my-project/.codex/agents/reviewer.toml
my-project/.codex/agents/researcher.toml
my-project/.codex/agents/tester.toml
```

The `config_file` path is relative to the config file that contains it.

#### `SKILL.md` — Skill definition

```
# Global (available in all projects)
~/.agents/skills/code-review/SKILL.md
~/.agents/skills/security-audit/SKILL.md

# Project (available only in this project)
my-project/.agents/skills/deploy-check/SKILL.md
my-project/.agents/skills/db-migration/SKILL.md
```

Enable/disable in config:
```toml
[[skills.config]]
path = ".agents/skills/my-skill"
enabled = true
```

#### `AGENTS.md` — Project instructions

```
# Global instructions (applies to all projects)
~/.codex/AGENTS.md

# Project root (applies to the entire project)
my-project/AGENTS.md

# Nested (overrides parent for this subtree)
my-project/src/AGENTS.md
my-project/tests/AGENTS.md
```

Nested `AGENTS.md` files override parent ones for their directory subtree. Precedence: nested > parent > global.

## How to Use

### 1. Main config (`config.toml`)

Copy to `~/.codex/config.toml` for global settings, or `.codex/config.toml` in your project root. Edit the sections you need and remove the rest.

Key sections:
- **model** — Pick your model, e.g. `model = "o3"`
- **model_providers** — Add custom providers (Anthropic, local LLM, etc.)
- **agents** — Define named roles; each can reference an external `config_file`
- **mcp_servers** — Connect external tool servers (stdio or HTTP)
- **features** — Toggle experimental features (`multi_agent`, `hooks`, `memories`, etc.)
- **skills.config** — Register skill directories

### 2. Agent role (`agent-role.toml`)

Create a separate TOML file for each agent role. Reference it from the main config:

```toml
# In config.toml:
[agents.reviewer]
description = "Reviews code for quality and security"
config_file = "./agents/reviewer.toml"
```

### 3. Skills (`SKILL.md`)

Place in a `<skill-name>/` directory. The directory name becomes the skill identifier. Enable in config:

```toml
[[skills.config]]
path = ".agents/skills/my-skill"
enabled = true
```

### 4. Instructions (`AGENTS.md`)

Place at project root. Nested `AGENTS.md` files in subdirectories override the root file for their subtree.

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `CODEX_HOME` | Override config directory |
| `OPENAI_API_KEY` | API key for OpenAI models |

## Useful Commands

```bash
codex write-config-schema   # Generate JSON Schema for config.toml
codex mcp add <name>        # Add an MCP server interactively
codex mcp list              # List configured MCP servers
codex mcp remove <name>     # Remove an MCP server
codex features enable <name>  # Enable a feature flag
codex features disable <name> # Disable a feature flag
```