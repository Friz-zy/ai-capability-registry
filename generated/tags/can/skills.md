# can

## Skills
Load skill file when task matches.

### cli-creator
Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

File: `../external/openai-skills/skills/.curated/cli-creator/SKILL.md`

### configure
Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord bot token, asks to configure Discord, asks "how do I set this up" or "who can reach me," or wants to check channel status.

File: `../external/anthropic-claude-plugins-official/external_plugins/discord/skills/configure/SKILL.md`

### configure
Check iMessage channel setup and review access policy. Use when the user asks to configure iMessage, asks "how do I set this up" or "who can reach me," or wants to know why texts aren't reaching the assistant.

File: `../external/anthropic-claude-plugins-official/external_plugins/imessage/skills/configure/SKILL.md`

### configure
Set up the Telegram channel — save the bot token and review access policy. Use when the user pastes a Telegram bot token, asks to configure Telegram, asks "how do I set this up" or "who can reach me," or wants to check channel status.

File: `../external/anthropic-claude-plugins-official/external_plugins/telegram/skills/configure/SKILL.md`

### plugin-creator
Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders you can edit before publishing or testing. Use when Codex needs to create a new local plugin, add optional plugin structure, or generate or update repo-root `.agents/plugins/marketplace.json` entries for plugin ordering and availability metadata.

File: `../external/openai-skills/skills/.system/plugin-creator/SKILL.md`

### policy-lookup
Find and explain company policies in plain language. Trigger with "what's our PTO policy", "can I work remotely from another country", "how do expenses work", or any plain-language question about benefits, travel, leave, or handbook rules.

File: `../external/anthropic-knowledge-work-plugins/human-resources/skills/policy-lookup/SKILL.md`

### process-optimization
Analyze and improve business processes. Trigger with "this process is slow", "how can we improve", "streamline this workflow", "too many steps", "bottleneck", or when the user describes an inefficient process they want to fix.

File: `../external/anthropic-knowledge-work-plugins/operations/skills/process-optimization/SKILL.md`

### theme-factory
Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.

File: `../external/anthropic-skills/skills/theme-factory/SKILL.md`

### triage-nda
Rapidly triage an incoming NDA and classify it as GREEN (standard approval), YELLOW (counsel review), or RED (full legal review). Use when a new NDA arrives from sales or business development, when screening for embedded non-solicits, non-competes, or missing carveouts, or when deciding whether an NDA can be signed under standard delegation.

File: `../external/anthropic-knowledge-work-plugins/legal/skills/triage-nda/SKILL.md`
