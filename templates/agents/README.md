# AI Agent Configuration Templates

Full configuration file templates for each CLI agent tool referenced in `ai-agents.md`.

## Directory Structure

| Tool | Directory | Format |
|------|-----------|--------|
| Codex CLI | `codex-cli/` | TOML |
| Claude Code | `claude-code/` | JSON + Markdown (YAML frontmatter) |
| Kilo Code | `kilo-code/` | JSONC + Markdown (YAML frontmatter) |
| OpenCode | `opencode/` | JSON + Markdown (YAML frontmatter) |
| Amazon Kiro | `amazon-kiro/` | JSON + Markdown (YAML frontmatter) |

## Template Files by Tool

### Codex CLI (`codex-cli/`)

| File | Purpose |
|------|---------|
| `config.toml` | Full project/global config: model, providers, agents, MCP, features, skills, hooks, permissions |
| `agent-role.toml` | Agent role definition (referenced via `config_file` in `[agents.<name>]`) |
| `SKILL.md` | Skill template with TOML-compatible YAML frontmatter |
| `AGENTS.md` | Project instructions (hierarchical by directory) |

<details>
<summary>File placement details</summary>

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

#### `AGENTS.md` — Project instructions

```
# Global (applies to all projects)
~/.codex/AGENTS.md

# Project root (applies to the entire project)
my-project/AGENTS.md

# Nested (overrides parent for this subtree)
my-project/src/AGENTS.md
my-project/tests/AGENTS.md
```

Nested files override parent ones. Precedence: nested > parent > global.

</details>

---

### Claude Code (`claude-code/`)

| File | Purpose |
|------|---------|
| `settings.json` | Project settings: permissions, hooks |
| `settings.local.json` | Local overrides (gitignored) |
| `.mcp.json` | MCP server configuration |
| `agent.md` | Agent definition (YAML frontmatter + markdown body) |
| `SKILL.md` | Skill template with YAML frontmatter |
| `command.md` | Slash command template |
| `CLAUDE.md` | Project instructions |
| `rule.md` | Path-scoped rule template |

<details>
<summary>File placement details</summary>

#### `settings.json` — Project settings

```
# Global (applies to all projects)
~/.claude/settings.json

# Project (applies only to this project)
my-project/.claude/settings.json

# Local overrides (gitignored, personal only)
my-project/.claude/settings.local.json

# Managed/enterprise (system-wide, enforced, overrides everything)
~/.claude/managed-settings.json
```

Precedence: managed-settings > local > project > global.

#### `.mcp.json` — MCP server configuration

```
# Global (inside ~/.claude.json, mcpServers key)
~/.claude.json

# Project (standalone file at project root)
my-project/.mcp.json
```

#### `agent.md` — Agent definition

```
# Global (available in all projects)
~/.claude/agents/code-reviewer.md
~/.claude/agents/security-auditor.md

# Project (available only in this project)
my-project/.claude/agents/backend-specialist.md
```

The filename (minus `.md`) becomes the agent name.

#### `SKILL.md` — Skill definition

```
# Global
~/.claude/skills/deploy-check/SKILL.md

# Project
my-project/.claude/skills/db-migration/SKILL.md
```

The directory name becomes the slash command: `/deploy-check`, `/db-migration`.

#### `command.md` — Slash command

```
# Global → /user:<command-name>
~/.claude/commands/deploy.md
~/.claude/commands/review.md

# Project → /project:<command-name>
my-project/.claude/commands/migrate.md
```

#### `CLAUDE.md` — Project instructions

```
# Global
~/.claude/CLAUDE.md

# Project root
my-project/CLAUDE.md

# Project .claude/ directory (takes precedence)
my-project/.claude/CLAUDE.md

# Local overrides (gitignored)
my-project/CLAUDE.local.md
```

Precedence: `.claude/CLAUDE.md` > root `CLAUDE.md` > `~/.claude/CLAUDE.md`.

#### `rule.md` — Path-scoped rules

```
# Project-level only, always active
my-project/.claude/rules/python-style.md
my-project/.claude/rules/security-standards.md
```

</details>

---

### Kilo Code (`kilo-code/`)

| File | Purpose |
|------|---------|
| `kilo.jsonc` | Full project config: model, providers, agents, MCP, permissions, commands, references |
| `agent.md` | Agent definition (YAML frontmatter + markdown body) |
| `SKILL.md` | Skill template with YAML frontmatter |
| `AGENTS.md` | Project instructions (hierarchical) |
| `command.md` | Slash command template |

<details>
<summary>File placement details</summary>

#### `kilo.jsonc` — Main configuration (JSON with comments)

```
# Global (applies to all projects)
~/.config/kilo/kilo.jsonc

# Project — primary location (preferred)
my-project/kilo.jsonc

# Project — alternative location
my-project/.kilo/kilo.jsonc

# Managed/enterprise (system-wide, enforced)
/etc/kilo/kilo.json
```

Override config path with `KILO_CONFIG` env var, or inline with `KILO_CONFIG_CONTENT`.

#### `agent.md` — Agent definition (Markdown + YAML frontmatter)

```
# Global (available in all projects)
~/.config/kilo/agent/code-reviewer.md
~/.config/kilo/agent/security-auditor.md

# Project (available only in this project)
my-project/.kilo/agent/backend-dev.md
my-project/.kilo/agent/db-migrator.md

# Also scans compat directory:
my-project/.opencode/agents/<name>.md
```

The filename (minus `.md`) becomes the agent name. Nested directories create namespaced names: `.kilo/agent/backend/sql.md` → agent `backend/sql`.

#### `SKILL.md` — Skill definition

```
# Global
~/.config/kilo/skills/deploy-check/SKILL.md

# Project
my-project/.kilo/skills/db-migration/SKILL.md

# Compat directories also scanned:
my-project/.claude/skills/<name>/SKILL.md
my-project/.agents/skills/<name>/SKILL.md
```

#### `AGENTS.md` — Project instructions (hierarchical)

```
# Config-based global instructions:
#   In kilo.jsonc: "instructions": ["AGENTS.md", "docs/style.md"]

# Project root
my-project/AGENTS.md

# Per-directory (overrides parent for this subtree)
my-project/src/AGENTS.md
my-project/tests/AGENTS.md
```

Precedence: agent.prompt > config `instructions` > AGENTS.md (nested > parent).

#### `command.md` — Slash command

```
# Global
~/.config/kilo/command/deploy.md
~/.config/kilo/command/review.md

# Project
my-project/.kilo/command/migrate.md
```

The filename (minus `.md`) becomes the command name.

</details>

---

### OpenCode (`opencode/`)

| File | Purpose |
|------|---------|
| `opencode.json` | Full project config: model, providers, agents, MCP, permissions, plugins, references |
| `agent.md` | Agent definition (YAML frontmatter + markdown body) |
| `SKILL.md` | Skill template with YAML frontmatter |
| `AGENTS.md` | Project instructions |

<details>
<summary>File placement details</summary>

#### `opencode.json` — Main configuration

```
# Global (applies to all projects)
~/.config/opencode/opencode.json

# Project (applies only to this project)
my-project/opencode.json

# Managed/enterprise (MDM)
<managed>.mobileconfig
```

Override config path with `OPENCODE_CONFIG`, inline with `OPENCODE_CONFIG_CONTENT`, or directory with `OPENCODE_CONFIG_DIR`.

#### `agent.md` — Agent definition (Markdown + YAML frontmatter)

```
# Global
~/.config/opencode/agents/code-reviewer.md
~/.config/opencode/agents/security-auditor.md

# Project
my-project/.opencode/agents/backend-dev.md
my-project/.opencode/agents/db-migrator.md
```

Agents can also be defined inline in `opencode.json` under the `agent` key. Use `"prompt": "{file:./prompts/my-prompt.txt}"` to reference external prompt files.

#### `SKILL.md` — Skill definition

```
# Global
~/.config/opencode/skills/deploy-check/SKILL.md

# Project
my-project/.opencode/skills/db-migration/SKILL.md

# Compat directories also scanned:
my-project/.claude/skills/<name>/SKILL.md
my-project/.agents/skills/<name>/SKILL.md
```

#### `AGENTS.md` — Project instructions

```
# Config-based global instructions:
#   In opencode.json: "instructions": ["AGENTS.md", "docs/style.md"]

# Project root
my-project/AGENTS.md
```

Precedence: agent.prompt > config `instructions` > AGENTS.md.

</details>

---

### Amazon Kiro (`amazon-kiro/`)

| File | Purpose |
|------|---------|
| `agent.json` | Full agent config: tools, MCP, hooks, resources, model, keyboard shortcut |
| `mcp.json` | MCP server configuration (project or global) |
| `SKILL.md` | Skill template with YAML frontmatter |
| `steering-always.md` | Steering file: always active |
| `steering-conditional.md` | Steering file: activated by glob pattern |
| `steering-manual.md` | Steering file: activated by `#name` reference |
| `AGENTS.md` | Project instructions (always active) |

<details>
<summary>File placement details</summary>

#### `agent.json` — Agent configuration

```
# Global (available in all projects)
~/.kiro/agents/general-assistant.json
~/.kiro/agents/code-reviewer.json

# Project (available only in this project)
my-project/.kiro/agents/dev-agent.json
my-project/.kiro/agents/aws-specialist.json
```

When both locations have an agent with the same name, the project one takes precedence (with a warning).

#### `mcp.json` — MCP server configuration

```
# Global (applies to all projects)
~/.kiro/settings/mcp.json

# Project (applies only to this project)
my-project/.kiro/settings/mcp.json
```

Agent configs can also define per-agent MCP servers via the `mcpServers` field, and control merging with `includeMcpJson`.

#### `SKILL.md` — Skill definition

```
# Global
~/.kiro/skills/aws-patterns/SKILL.md
~/.kiro/skills/api-design/SKILL.md

# Project
my-project/.kiro/skills/db-migration/SKILL.md
my-project/.kiro/skills/deploy-check/SKILL.md
```

Skills use progressive loading — metadata loaded at startup, full content loaded on demand. Reference from agent config:

```json
"resources": ["skill://.kiro/skills/**/SKILL.md"]
```

#### `steering-*.md` — Steering files (instruction modes)

```
# Global
~/.kiro/steering/coding-standards.md       # mode: always
~/.kiro/steering/security-rules.md          # mode: always
~/.kiro/steering/typescript-rules.md        # condition: "*.ts"

# Project
my-project/.kiro/steering/project-style.md  # mode: always
my-project/.kiro/steering/python-rules.md    # condition: "*.py"
my-project/.kiro/steering/deploy-check.md   # mode: manual → #deploy-check
```

Four modes: `always` (always loaded), `conditional` (glob match), `manual` (`#name` reference), `auto` (description match).

Precedence: workspace steering > global steering.

#### `AGENTS.md` — Project instructions

```
# Project root only (always active, no frontmatter needed)
my-project/AGENTS.md
```

Unlike steering files, `AGENTS.md` is always loaded into context (equivalent to `mode: always`).

</details>

---

## Key Differences

| Feature | Codex CLI | Claude Code | Kilo Code | OpenCode | Amazon Kiro |
|---------|-----------|-------------|-----------|----------|-------------|
| Config format | TOML | JSON / YAML fm | JSONC / YAML fm | JSON / YAML fm | JSON / YAML fm |
| Multi-provider | No (OpenAI) | No (Anthropic) | Yes (75+) | Yes (75+) | No (AWS Bedrock) |
| Agent definition | TOML `[agents.<name>]` + role file | `.claude/agents/<name>.md` | `.kilo/agent/<name>.md` or config | `.opencode/agents/<name>.md` or config | `.kiro/agents/<name>.json` |
| MCP transport | stdio + HTTP | stdio + HTTP + SSE + WS | stdio (local) + HTTP (remote) | stdio (local) + HTTP (remote) | stdio + streamable HTTP |
| Spec-driven dev | No | No | No | No | Yes (steering) |
| Hooks | Yes | Yes (pre/post tool) | No | Yes (via plugins) | Yes (lifecycle hooks) |
| Plugins | Early stage | Mature | No | TS/JS | No |
| Profiles | Yes (`--profile`) | No | No | No | No |

## Global vs Project Config Precedence

| Tool | Global | Project | Local/Private | Managed |
|------|--------|---------|---------------|---------|
| Codex CLI | `~/.codex/config.toml` | `.codex/config.toml` | — | `/etc/codex/config.toml` |
| Claude Code | `~/.claude/settings.json` | `.claude/settings.json` | `.claude/settings.local.json` (gitignored) | `managed-settings.json` |
| Kilo Code | `~/.config/kilo/kilo.jsonc` | `kilo.jsonc` / `.kilo/kilo.jsonc` | — | `/etc/kilo/kilo.json` |
| OpenCode | `~/.config/opencode/opencode.json` | `opencode.json` | — | MDM `.mobileconfig` |
| Amazon Kiro | `~/.kiro/agents/`, `~/.kiro/settings/`, `~/.kiro/steering/` | `.kiro/agents/`, `.kiro/settings/`, `.kiro/steering/` | — | MDM/Group Policy → `~/.kiro/steering/` |