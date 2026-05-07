# Tag: they

Skills with tag `they`:

## build-mcp-app

This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`
- **Tags**: `already`, `app`, `apps`, `build`, `build-mcp-app`, `build-mcp-server`, `chat`, `components`, `confirmation`, `context`, `conversation`, `dashboard`, `deployment`, `dev`, `dialog`, `form`, `has`, `inline`, `interactive`, `knows`, `make`, `mcp`, `mcp-server-dev`, `mentions`, `model`, `picker`, `render`, `sdk`, `server`, `settled`, `shows`, `they`, `used`, `want`, `widgets`

## claude-automation-recommender

Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`
- **Tags**: `analyze`, `asks`, `automation`, `automation-recommender`, `automations`, `code`, `codebase`, `features`, `hooks`, `improving`, `know`, `mcp`, `mentions`, `optimize`, `project`, `recommend`, `recommendations`, `recommender`, `servers`, `set`, `subagents`, `their`, `they`

## pptx

Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/pptx`
- **Skill file**: `external/anthropic-skills/skills/pptx/SKILL.md`
- **Tags**: `afterward`, `both`, `combining`, `comments`, `content`, `created`, `creating`, `deck`, `decks`, `editing`, `elsewhere`, `email`, `even`, `existing`, `extracted`, `extracting`, `filename`, `includes`, `input`, `involved`, `layouts`, `like`, `mentions`, `modifying`, `needs`, `notes`, `opened`, `parsing`, `pitch`, `plan`, `pptx`, `presentation`, `presentations`, `reading`, `regardless`, `slide`, `slides`, `speaker`, `splitting`, `summary`, `text`, `they`, `time`, `touched`, `trigger`, `updating`, `used`, `way`, `whenever`, `will`, `working`

## process-optimization

Analyze and improve business processes. Trigger with "this process is slow", "how can we improve", "streamline this workflow", "too many steps", "bottleneck", or when the user describes an inefficient process they want to fix.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/operations/skills/process-optimization`
- **Skill file**: `external/anthropic-knowledge-work-plugins/operations/skills/process-optimization/SKILL.md`
- **Tags**: `analyze`, `bottleneck`, `business`, `can`, `describes`, `fix`, `improve`, `inefficient`, `many`, `operations`, `optimization`, `process`, `process-optimization`, `processes`, `slow`, `streamline`, `they`, `too`, `trigger`, `want`

## skill-improver

Iteratively reviews and fixes Claude Code skill quality issues until they meet standards. Runs automated fix-review cycles using the skill-reviewer agent. Use to fix skill quality issues, improve skill descriptions, run automated skill review loops, or iteratively refine a skill. Triggers on 'fix my skill', 'improve skill quality', 'skill improvement loop'. NOT for one-time reviews—use /skill-reviewer directly.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/skill-improver/skills/skill-improver`
- **Skill file**: `external/trailofbits-skills/plugins/skill-improver/skills/skill-improver/SKILL.md`
- **Tags**: `automated`, `code`, `cycles`, `descriptions`, `directly`, `fix`, `fix-review`, `fixes`, `improve`, `improvement`, `improver`, `issues`, `iteratively`, `loop`, `loops`, `meet`, `one`, `one-time`, `quality`, `refine`, `review`, `reviewer`, `reviews`, `runs`, `standards`, `they`, `time`, `triggers`, `until`
