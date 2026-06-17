# OpenCode Configuration Templates

## Where to Place Files

| File | Global | Project |
|------|--------|---------|
| `opencode.json` | `~/.config/opencode/opencode.json` | `opencode.json` in project root |
| `agent.md` | `~/.config/opencode/agents/<name>.md` | `.opencode/agents/<name>.md` |
| `SKILL.md` | `~/.config/opencode/skills/<name>/SKILL.md` | `.opencode/skills/<name>/SKILL.md` |
| `AGENTS.md` | Config `instructions` key | `<project-root>/AGENTS.md` |

Managed config: MDM `.mobileconfig` (enterprise)

### File Placement Details

#### `opencode.json` — Main configuration

```
# Global (applies to all projects)
~/.config/opencode/opencode.json

# Project (applies only to this project)
my-project/opencode.json
```

Override config path with `OPENCODE_CONFIG` env var, or inline with `OPENCODE_CONFIG_CONTENT`, or directory with `OPENCODE_CONFIG_DIR`.

#### `agent.md` — Agent definition (Markdown + YAML frontmatter)

```
# Global (available in all projects)
~/.config/opencode/agents/code-reviewer.md
~/.config/opencode/agents/security-auditor.md

# Project (available only in this project)
my-project/.opencode/agents/backend-dev.md
my-project/.opencode/agents/db-migrator.md
```

The filename (minus `.md`) becomes the agent name. Agents can also be defined inline in `opencode.json` under the `agent` key. Use `"prompt": "{file:./prompts/my-prompt.txt}"` to reference external prompt files.

#### `SKILL.md` — Skill definition

```
# Global (available in all projects)
~/.config/opencode/skills/deploy-check/SKILL.md
~/.config/opencode/skills/api-review/SKILL.md

# Project (available only in this project)
my-project/.opencode/skills/db-migration/SKILL.md

# Compat directories also scanned:
my-project/.claude/skills/<name>/SKILL.md
my-project/.agents/skills/<name>/SKILL.md
```

Skills can also be registered via config:
```json
"skills": {
  "paths": [".opencode/skills", "/abs/path/to/skills"],
  "urls": ["https://example.com/.well-known/skills/"]
}
```

#### `AGENTS.md` — Project instructions

```
# Global instructions (via config key "instructions")
# In opencode.json:
#   "instructions": ["AGENTS.md", "docs/style.md"]

# Project root
my-project/AGENTS.md
```

Precedence: agent.prompt > config `instructions` > AGENTS.md.

## How to Use

### 1. Main config (`opencode.json`)

Copy to `opencode.json` in the project root (or `~/.config/opencode/opencode.json` for global). Edit sections you need; remove the rest.

Key sections:
- **model** / **small_model** — Default and fast models in `provider/model-id` format
- **provider** — API keys (`"env:VAR_NAME"`) and endpoints
- **agent** — Define or override agents (inline in config or markdown files)
- **mcp** — MCP servers: `type: "local"` (stdio) or `type: "remote"` (HTTP)
- **permission** — Global tool permissions (`allow`/`ask`/`deny` + glob patterns)
- **skills** — Register skill directories and remote URLs
- **command** — Slash commands with prompts
- **plugin** — TS/JS plugin packages or local paths
- **references** — Codebase references for context
- **lsp** / **formatter** — Enable/disable LSP and formatter

### 2. Agents (`agent.md`)

Save as `.opencode/agents/<name>.md`. The **filename** (minus `.md`) becomes the agent name. YAML frontmatter defines metadata; the markdown body is the system prompt.

Frontmatter fields:
- `description` — Shown for delegation
- `mode` — `primary`, `subagent`, or `all`
- `model` — Model override (`provider/model-id`)
- `prompt` — Inline prompt (or use body)
- `permission` — Per-agent tool permissions
- `hidden` — Hide from UI
- `license` / `compatibility` / `metadata` — Skill packaging metadata

You can also define agents inline in `opencode.json` under the `agent` key. Use `"prompt": "{file:./prompts/my-prompt.txt}"` to reference external prompt files.

### 3. Skills (`SKILL.md`)

Place in `.opencode/skills/<skill-name>/SKILL.md`. Compat directories `.claude/skills/` and `.agents/skills/` are also scanned.

Frontmatter:
- `name` / `description` — Identity and auto-invoke matching
- `license` — License identifier
- `compatibility` — Version constraint (`>=0.1.0`)
- `metadata` — Add metadata (author, tags, etc.)

### 4. Permissions

Permissions use glob patterns with three actions: `allow`, `ask`, `deny`. Rules are evaluated in order; **last match wins**.

```yaml
permission:
  edit:
    "*.md": "allow"
    "*": "deny"
  bash:
    "*": "ask"
    "git *": "allow"
```

Skill-level permissions:
```yaml
permission:
  skill:
    "*": "allow"
    "internal-*": "deny"
    "experimental-*": "ask"
```

### 5. Instructions (`AGENTS.md`)

Place at project root. Precedence: agent.prompt > config `instructions` > AGENTS.md

### 6. Plugins

Add TS/JS plugins in the `plugin` array:

```json
"plugin": [
  "opencode-gemini-auth",
  "opencode-foo@1.2.3",
  "./local-plugin.ts",
  ["opencode-bar", { "option": "value" }]
]
```

### 7. LSP

OpenCode has built-in LSP support (no plugin needed). Set `"lsp": true` in config to enable.

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `OPENCODE_CONFIG` | Override config file path |
| `OPENCODE_CONFIG_CONTENT` | Inline config content |
| `OPENCODE_CONFIG_DIR` | Override config directory |

## Useful Commands

```bash
opencode mcp add <name>         # Add an MCP server
opencode mcp add <name> --local # Add stdio-based MCP server
opencode mcp list                # List configured MCP servers
```

## Schema Validation

Use `"$schema": "https://opencode.ai/config.json"` in your `opencode.json` for IDE autocompletion and validation.