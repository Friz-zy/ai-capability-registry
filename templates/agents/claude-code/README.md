# Claude Code Configuration Templates

## Where to Place Files

| File | Global | Project |
|------|--------|---------|
| `settings.json` | `~/.claude/settings.json` | `.claude/settings.json` |
| `settings.local.json` | — | `.claude/settings.local.json` (gitignored) |
| `.mcp.json` | `~/.claude.json` (inline `mcpServers` key) | `.mcp.json` (project root) |
| `agent.md` | `~/.claude/agents/<name>.md` | `.claude/agents/<name>.md` |
| `SKILL.md` | `~/.claude/skills/<name>/SKILL.md` | `.claude/skills/<name>/SKILL.md` |
| `command.md` | `~/.claude/commands/<name>.md` | `.claude/commands/<name>.md` |
| `CLAUDE.md` | `~/.claude/CLAUDE.md` | `CLAUDE.md` or `.claude/CLAUDE.md` |
| `rule.md` | — | `.claude/rules/<name>.md` |

Managed settings: `managed-settings.json` (enterprise, overrides everything)

### File Placement Details

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

#### `settings.local.json` — Local overrides (gitignored)

```
# Only project-level, never global
my-project/.claude/settings.local.json
```

Use for personal settings like local API keys that should not be committed.

#### `.mcp.json` — MCP server configuration

```
# Global (applies to all projects)
# The mcpServers key inside ~/.claude.json
~/.claude.json

# Project (applies only to this project)
my-project/.mcp.json
```

#### `agent.md` — Agent definition

```
# Global (available in all projects)
~/.claude/agents/code-reviewer.md
~/.claude/agents/security-auditor.md

# Project (available only in this project)
my-project/.claude/agents/backend-specialist.md
my-project/.claude/agents/db-migrator.md
```

The filename (minus `.md`) becomes the agent name.

#### `SKILL.md` — Skill definition

```
# Global (available in all projects)
~/.claude/skills/deploy-check/SKILL.md
~/.claude/skills/api-review/SKILL.md

# Project (available only in this project)
my-project/.claude/skills/db-migration/SKILL.md
```

The directory name becomes the slash command: `/deploy-check`, `/db-migration`.

#### `command.md` — Slash command

```
# Global → accessed as /user:<command-name>
~/.claude/commands/deploy.md
~/.claude/commands/review.md

# Project → accessed as /project:<command-name>
my-project/.claude/commands/migrate.md
my-project/.claude/commands/test-coverage.md
```

#### `CLAUDE.md` — Project instructions

```
# Global (applies to all projects)
~/.claude/CLAUDE.md

# Project root (primary project instructions)
my-project/CLAUDE.md

# Project .claude/ directory (takes precedence over root CLAUDE.md)
my-project/.claude/CLAUDE.md

# Local overrides (gitignored, personal only)
my-project/CLAUDE.local.md
```

Precedence: `.claude/CLAUDE.md` > root `CLAUDE.md` > `~/.claude/CLAUDE.md`.

#### `rule.md` — Path-scoped rules

```
# Only project-level, always active
my-project/.claude/rules/python-style.md
my-project/.claude/rules/security-standards.md
my-project/.claude/rules/no-mutation.md
```

Rules are always loaded into context (no glob-based activation like Kiro steering).

## Template Files

| File | Description |
|------|-------------|
| `settings.json` | Minimal working settings (permissions + hooks) |
| `settings.json.example` | Full reference with all fields commented (JSON — delete `//` keys before use) |
| `settings.local.json` | Minimal local overrides example (gitignored, personal) |
| `.mcp.json` | Minimal MCP server configuration |
| `.mcp.json.example` | Full MCP reference with all server types (JSON — delete `//` keys before use) |
| `agent.md` | Full agent definition with all frontmatter fields |
| `SKILL.md` | Skill definition template with frontmatter fields |
| `command.md` | Slash command template |
| `CLAUDE.md` | Project instructions template |
| `rule.md` | Path-scoped rule template |

## How to Use

### 1. Settings (`settings.json`)

Copy to `~/.claude/settings.json` (global) or `.claude/settings.json` (project). Edit the permissions and hooks you need. For a complete reference of all fields, see `settings.json.example`.

Key sections:
- **permissions.allow** / **permissions.deny** — Tool access rules with glob patterns
- **hooks.PostToolUse** / **hooks.PreToolUse** — Run commands on tool events

`settings.local.json` is the same format but gitignored — use for personal overrides like local API keys.

### 2. MCP servers (`.mcp.json`)

Place at project root. Each key under `mcpServers` defines one server with `command`, `args`, `env`. Supports env var expansion like `${MY_API_KEY}`. For all server types (stdio, HTTP, SSE, WebSocket, OAuth), see `.mcp.json.example`.

### 3. Agents (`agent.md`)

Save as `.claude/agents/<name>.md`. The **filename** (minus `.md`) becomes the agent name. The YAML frontmatter defines metadata; the markdown body is the system prompt.

Required frontmatter fields:
- `description` — When to use this agent (used for auto-delegation)
- `model` — `inherit` or a specific model name

Optional:
- `tools` — Restrict available tools
- `hidden` — Hide from agent picker
- `color` — UI color (`blue`, `green`, `red`, `cyan`, `magenta`, `yellow`)

### 4. Skills (`SKILL.md`)

Place in `.claude/skills/<skill-name>/SKILL.md`. The **directory name** becomes the slash command: `/skill-name`.

Key frontmatter:
- `name` / `description` — Identity and auto-invoke matching
- `disable-model-invocation: true` — Manual-only skill
- `allowed-tools` — Restrict which tools the skill can use
- `model` — Override model for this skill
- `context: fork` + `agent:` — Fork conversation context

### 5. Commands (`command.md`)

Place in `.claude/commands/<name>.md`. Accessed as `/project:<name>` (project) or `/user:<name>` (global).

Frontmatter:
- `description` — What the command does
- `argument-hint` — Argument usage hint
- `allowed-tools` — Restrict tools for this command
- `model` — Model override

Body uses `$1`, `$2`, `$ARGUMENTS` for arguments and `@path/to/file` for file references.

### 6. Instructions (`CLAUDE.md`)

Place at project root (or `.claude/CLAUDE.md`). Local overrides go in `CLAUDE.local.md` (gitignored).

Precedence: `.claude/CLAUDE.md` > root `CLAUDE.md` > `~/.claude/CLAUDE.md`

### 7. Rules (`rule.md`)

Place in `.claude/rules/<name>.md`. Rules are always active and loaded into context. Use for persistent coding standards, security requirements, etc.

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `ANTHROPIC_API_KEY` | API key for Anthropic models |
| `ANTHROPIC_BASE_URL` | Override API base URL |
| `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` | Extra dirs for CLAUDE.md |
| `ENABLE_CLAUDEAI_MCP_SERVERS` | Enable MCP servers from claude.ai |
| `ENABLE_TOOL_SEARCH` | Enable tool search feature |
| `CLAUDE_CODE_USE_POWERSHELL_TOOL` | Use PowerShell instead of Bash |
| `CLAUDE_PROJECT_DIR` | Override project directory for MCP |

## Useful Commands

```bash
claude mcp add <name>              # Add an MCP server interactively
claude mcp list                    # List configured MCP servers
claude mcp remove <name>           # Remove an MCP server
claude plugin install <url>        # Install a plugin
claude /reload-plugins             # Reload plugins after changes
/mcp                               # Show loaded MCP servers (in session)
```