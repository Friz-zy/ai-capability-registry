# configuration

## Skills
Load skill and **use it** when task matches.

### cowork-plugin-customizer
Customize a Claude Code plugin for a specific organization's tools and workflows. Use when: customize plugin, set up plugin, configure plugin, tailor plugin, adjust plugin settings, customize plugin connectors, customize plugin skill, tweak plugin, modify plugin configuration.

File: `external/anthropic-knowledge-work-plugins/cowork-plugin-management/skills/cowork-plugin-customizer/SKILL.md`

### devcontainer-setup
Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configuring sandboxed Claude Code workspaces.

File: `external/trailofbits-skills/plugins/devcontainer-setup/skills/devcontainer-setup/SKILL.md`

### insecure-defaults
Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling.

File: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults/SKILL.md`

### migrate-to-codex
Migrate supported instruction files, skills, agents, and MCP config into Codex project and global files.

File: `external/openai-skills/skills/.curated/migrate-to-codex/SKILL.md`

### skill-installer
Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).

File: `external/openai-skills/skills/.system/skill-installer/SKILL.md`

### start
Set up your bio-research environment and explore available tools. Use when first getting oriented with the plugin, checking which literature, drug-discovery, or visualization MCP servers are connected, or surveying available analysis skills before starting a new project.

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/start/SKILL.md`

### start
Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your existing task list, or decoding the shorthand (nicknames, acronyms, project codenames) you use in your todos.

File: `external/anthropic-knowledge-work-plugins/productivity/skills/start/SKILL.md`
