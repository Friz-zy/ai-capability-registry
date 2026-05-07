# driven

## Skills
Load skill file when task matches.

### hook-development
This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API.

File: `../external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development/SKILL.md`

### setup-zoom-webhooks
Reference skill for Zoom webhooks. Use after routing to an event-driven workflow when implementing subscriptions, signature verification, delivery handling, retries, or event-type selection.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/webhooks/SKILL.md`

### vector-forge
Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

File: `../external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`

### virtual-agent/web
Zoom Virtual Agent SDK for web embeds. Use for campaign or entry ID chat launch, event-driven controls, user context updates, and CSP-safe deployment.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/web/SKILL.md`
