# Kilo Code Configuration Templates

## Where to Place Files

| File | Global | Project |
|------|--------|---------|
| `kilo.jsonc` | `~/.config/kilo/kilo.jsonc` | `kilo.jsonc` or `.kilo/kilo.jsonc` |
| `agent.md` | `~/.config/kilo/agent/<name>.md` | `.kilo/agent/<name>.md` |
| `SKILL.md` | `~/.config/kilo/skills/<name>/SKILL.md` | `.kilo/skills/<name>/SKILL.md` |
| `AGENTS.md` | Config `instructions` key | `<project-root>/AGENTS.md` (hierarchical, per-dir) |
| `command.md` | `~/.config/kilo/command/<name>.md` | `.kilo/command/<name>.md` |

Managed config: `/etc/kilo/kilo.json` (enterprise, MDM)

### File Placement Details

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
```

The filename (minus `.md`) becomes the agent name. Nested directories create namespaced names: `.kilo/agent/backend/sql.md` → agent `backend/sql`. Also supports `.opencode/agents/` directory as compat path.

#### `SKILL.md` — Skill definition

```
# Global (available in all projects)
~/.config/kilo/skills/deploy-check/SKILL.md
~/.config/kilo/skills/api-review/SKILL.md

# Project (available only in this project)
my-project/.kilo/skills/db-migration/SKILL.md

# Compat directories also scanned (in order):
my-project/.claude/skills/<name>/SKILL.md
my-project/.agents/skills/<name>/SKILL.md
```

Skills can also be registered via config:
```jsonc
"skills": {
  "paths": [".kilo/skills", "/abs/path/to/skills"],
  "urls": ["https://example.com/.well-known/skills/"]
}
```

#### `AGENTS.md` — Project instructions (hierarchical)

```
# Global instructions (via config key "instructions")
# In kilo.jsonc:
#   "instructions": ["AGENTS.md", "docs/style.md"]

# Project root
my-project/AGENTS.md

# Per-directory (overrides parent for this subtree)
my-project/src/AGENTS.md
my-project/tests/AGENTS.md
```

Precedence: agent.prompt > config `instructions` > AGENTS.md (nested > parent).

#### `command.md` — Slash command

```
# Global (available in all projects)
~/.config/kilo/command/deploy.md
~/.config/kilo/command/review.md

# Project (available only in this project)
my-project/.kilo/command/migrate.md
my-project/.kilo/command/test-coverage.md
```

The filename (minus `.md`) becomes the command name, accessible as `/migrate`, `/test-coverage`, etc.

## Template Files

| File | Description |
|------|-------------|
| `kilo.jsonc` | Full config reference with all fields and section comments (JSONC — supports `//` comments) |
| `agent.md` | Full agent definition with all frontmatter fields |
| `SKILL.md` | Skill definition template with frontmatter fields |
| `AGENTS.md` | Project instructions template |
| `command.md` | Slash command template |

## How to Use

### 1. Main config (`kilo.jsonc`)

Copy to `kilo.jsonc` in the project root (or `.kilo/kilo.jsonc`). Edit sections you need; remove the rest. The file is JSONC (JSON with comments), so `//` comments are valid.

Key sections:
- **model** / **small_model** — Default and fast models in `provider/model-id` format
- **provider** — API keys and endpoints (`"env:VAR_NAME"` for env vars)
- **agent** — Define or override agents (both inline and as markdown files)
- **mcp** — MCP servers: `type: "local"` (stdio) or `type: "remote"` (HTTP)
- **permission** — Global tool permissions (`allow`/`ask`/`deny` + glob patterns)
- **skills** — Register skill directories and remote URLs
- **command** — Slash commands with prompts

### 2. Agents (`agent.md`)

Save as `.kilo/agent/<name>.md` or `~/.config/kilo/agent/<name>.md`. The **filename** (minus `.md`) becomes the agent name. YAML frontmatter defines metadata; the markdown body is the system prompt.

Frontmatter fields:
- `description` — Shown to orchestrator for delegation
- `mode` — `primary` (user-facing), `subagent` (delegated), `all` (both, default)
- `model` — Model override (`provider/model-id`)
- `prompt` — Inline prompt (or use body as prompt)
- `temperature` / `top_p` — Sampling parameters
- `permission` — Per-agent tool permissions (glob patterns for bash, file patterns for edit)
- `steps` — Max agentic iterations before text-only fallback
- `hidden` — Hide from UI (subagents only)
- `color` — Hex color or theme keyword for UI

You can also define agents inline in `kilo.jsonc` under the `agent` key. Use `"prompt": "{file:./prompts/my-prompt.txt}"` to reference external prompt files from JSON config.

### 3. Skills (`SKILL.md`)

Place in `.kilo/skills/<skill-name>/SKILL.md`. The directory name becomes the skill identifier. Compat directories `.claude/skills/` and `.agents/skills/` are also scanned.

Frontmatter:
- `name` / `description` — Identity and auto-invoke matching

### 4. Permissions

Permissions use glob patterns with three actions: `allow`, `ask`, `deny`. Rules are evaluated in order; **last match wins**.

```yaml
permission:
  edit:
    "*.md": "allow"    # Allow editing markdown
    "*": "deny"        # Deny everything else (last match wins)
  bash:
    "*": "ask"         # Ask for all commands
    "git *": "allow"   # But allow git commands (later rule)
```

Subagent delegation control:
```yaml
permission:
  task:
    "*": "deny"
    "code-reviewer": "allow"
```

### 5. Instructions (`AGENTS.md`)

Place at project root. Nested `AGENTS.md` files apply to their directory subtree. Precedence: agent.prompt > config `instructions` > AGENTS.md

### 6. Commands (`command.md`)

Place in `.kilo/command/<name>.md`. Accessed as a slash command by filename.

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `KILO_CONFIG` | Override config file path |
| `KILO_CONFIG_CONTENT` | Inline config content (overrides file) |
| `KILO_DISABLE_EXTERNAL_SKILLS` | Disable remote skill URLs |

## Useful Commands

```bash
kilo agent list                # List all agents
kilo agent create              # Create agent interactively
kilo mcp add <name>            # Add an MCP server (UI)
```