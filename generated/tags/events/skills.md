# events

## Skills
Load skill file when task matches.

### build-zoom-phone-integration
Reference skill for Zoom Phone. Use after routing to a phone workflow when implementing OAuth, Phone APIs, webhooks, Smart Embed events, URI schemes, CRM or CTI dialers, or call handling automation.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/phone/SKILL.md`

### hook-development
This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API.

File: `../external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development/SKILL.md`

### openai-sentry
Use when the user asks to inspect Sentry issues or events, summarize recent production errors,

File: `../external/trailofbits-skills-curated/plugins/openai-sentry/skills/openai-sentry/SKILL.md`

### sentry
Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; perform read-only queries using the `sentry` command.

File: `../external/openai-skills/skills/.curated/sentry/SKILL.md`
