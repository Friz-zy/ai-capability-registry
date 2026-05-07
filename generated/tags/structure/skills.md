# Tag: structure

Skills with tag `structure`:

## agent-development

This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/agent-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/agent-development/SKILL.md`
- **Tags**: `asks`, `autonomous`, `code`, `colors`, `conditions`, `create`, `description`, `dev`, `development`, `frontmatter`, `guidance`, `needs`, `practices`, `prompts`, `structure`, `subagent`, `triggering`, `used`

## command-development

This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in commands, user interaction patterns, or command development best practices for Claude Code.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/command-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/command-development/SKILL.md`
- **Tags**: `arguments`, `asks`, `askuserquestion`, `bash`, `code`, `command`, `command-development`, `commands`, `create`, `custom`, `define`, `dev`, `development`, `dynamic`, `execution`, `fields`, `frontmatter`, `guidance`, `interaction`, `interactive`, `needs`, `organize`, `practices`, `slash`, `structure`, `used`, `yaml`

## figma-use

**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-use`
- **Skill file**: `external/openai-skills/skills/.curated/figma-use/SKILL.md`
- **Tags**: `auto`, `auto-layout`, `bind`, `build`, `call`, `causes`, `components`, `context`, `create`, `curated`, `debug`, `delete`, `directly`, `edit`, `every`, `execution`, `failures`, `figma`, `fills`, `hard`, `hard-to-debug`, `inspect`, `invoke`, `javascript`, `layout`, `loading`, `mandatory`, `modify`, `must`, `never`, `nodes`, `perform`, `prerequisite`, `programmatically`, `properties`, `requires`, `set`, `skipping`, `structure`, `tokens`, `trigger`, `unique`, `variables`, `variants`, `whenever`, `without`

## org-planning

Headcount planning, org design, and team structure optimization. Trigger with "org planning", "headcount plan", "team structure", "reorg", "who should we hire next", or when the user is thinking about team size, reporting structure, or organizational design.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/human-resources/skills/org-planning`
- **Skill file**: `external/anthropic-knowledge-work-plugins/human-resources/skills/org-planning/SKILL.md`
- **Tags**: `design`, `headcount`, `hire`, `human`, `next`, `optimization`, `org`, `org-planning`, `organizational`, `plan`, `planning`, `reorg`, `reporting`, `size`, `structure`, `team`, `thinking`, `trigger`, `who`

## performance-review

Structure a performance review with self-assessment, manager template, and calibration prep. Use when review season kicks off and you need a self-assessment template, writing a manager review for a direct report, prepping rating distributions and promotion cases for calibration, or turning vague feedback into specific behavioral examples.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/human-resources/skills/performance-review`
- **Skill file**: `external/anthropic-knowledge-work-plugins/human-resources/skills/performance-review/SKILL.md`
- **Tags**: `assessment`, `behavioral`, `calibration`, `cases`, `direct`, `distributions`, `feedback`, `human`, `kicks`, `manager`, `off`, `performance`, `performance-review`, `prep`, `prepping`, `promotion`, `rating`, `report`, `review`, `season`, `self`, `self-assessment`, `structure`, `turning`, `vague`

## plugin-creator

Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders you can edit before publishing or testing. Use when Codex needs to create a new local plugin, add optional plugin structure, or generate or update repo-root `.agents/plugins/marketplace.json` entries for plugin ordering and availability metadata.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.system/plugin-creator`
- **Skill file**: `external/openai-skills/skills/.system/plugin-creator/SKILL.md`
- **Tags**: `availability`, `baseline`, `can`, `codex`, `create`, `creator`, `directories`, `edit`, `entries`, `folders`, `local`, `marketplace`, `metadata`, `needs`, `optional`, `ordering`, `placeholders`, `publishing`, `repo`, `repo-root`, `root`, `scaffold`, `structure`, `testing`

## plugin-structure

This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure/SKILL.md`
- **Tags**: `architecture`, `asks`, `auto`, `auto-discovery`, `code`, `commands`, `component`, `components`, `configuration`, `configure`, `conventions`, `create`, `dev`, `directory`, `discovery`, `guidance`, `hooks`, `layout`, `manifest`, `naming`, `needs`, `organization`, `organize`, `practices`, `root`, `scaffold`, `set`, `structure`, `understand`, `used`

## skill-development

This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/skill-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/skill-development/SKILL.md`
- **Tags**: `code`, `content`, `create`, `description`, `dev`, `development`, `disclosure`, `guidance`, `improve`, `needs`, `organize`, `practices`, `progressive`, `structure`, `used`
