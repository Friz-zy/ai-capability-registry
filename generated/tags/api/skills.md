# Tag: api

Skills with tag `api`:

## build-mcp-server

This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`
- **Tags**: `api`, `app`, `asks`, `build`, `build-mcp-server`, `building`, `case`, `context`, `create`, `deployment`, `design`, `determines`, `dev`, `development`, `discusses`, `entry`, `expose`, `hands`, `http`, `integration`, `interrogates`, `local`, `make`, `mcp`, `mcp-server-dev`, `mcpb`, `model`, `off`, `picks`, `point`, `protocol`, `remote`, `right`, `server`, `something`, `specialized`, `stdio`, `their`, `used`, `wrap`

## build-zoom-rest-api-app

Reference skill for Zoom REST API. Use after choosing an API-based workflow when you need endpoint selection, resource-management patterns, OAuth requirements, rate-limit awareness, or API error debugging.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rest-api`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rest-api/SKILL.md`
- **Tags**: `api`, `app`, `awareness`, `build`, `build-zoom-rest-api-app`, `choosing`, `debugging`, `endpoint`, `error`, `limit`, `management`, `oauth`, `partner`, `rate`, `rate-limit`, `requirements`, `resource`, `resource-management`, `rest`, `rest-api`, `selection`, `zoom`

## choose-zoom-approach

Choose the right Zoom architecture for a use case. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zoom MCP, Phone, Contact Center, or a hybrid approach.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/choose-zoom-approach`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/choose-zoom-approach/SKILL.md`
- **Tags**: `api`, `approach`, `apps`, `architecture`, `between`, `case`, `center`, `choose`, `choose-zoom-approach`, `contact`, `deciding`, `hybrid`, `mcp`, `meeting`, `partner`, `phone`, `rest`, `right`, `sdk`, `video`, `webhooks`, `websockets`, `zoom`

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## cli-creator

Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/cli-creator`
- **Skill file**: `external/openai-skills/skills/.curated/cli-creator/SKILL.md`
- **Tags**: `admin`, `api`, `app`, `auth`, `build`, `can`, `cli`, `cli-creator`, `codex`, `command`, `command-line`, `commands`, `companion`, `composable`, `create`, `creator`, `curated`, `curl`, `docs`, `existing`, `expose`, `line`, `local`, `manage`, `openapi`, `pair`, `repo`, `return`, `script`, `sdk`, `spec`, `stable`, `web`

## debug-zoom

Debug a broken Zoom integration by isolating the failure point and routing into the right Zoom references. Use when auth, API, webhook, SDK, or MCP behavior is failing and you need a ranked hypothesis list plus verification steps.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom/SKILL.md`
- **Tags**: `api`, `auth`, `behavior`, `broken`, `debug`, `debug-zoom`, `failing`, `failure`, `hypothesis`, `integration`, `isolating`, `mcp`, `partner`, `plus`, `point`, `ranked`, `right`, `routing`, `sdk`, `verification`, `webhook`, `zoom`

## design-mcp-workflow

Design a Zoom MCP workflow for Claude. Use when deciding whether Zoom MCP fits a task, when planning tool-based AI workflows, or when separating MCP responsibilities from REST API responsibilities.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/design-mcp-workflow`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/design-mcp-workflow/SKILL.md`
- **Tags**: `api`, `deciding`, `design`, `design-mcp`, `fits`, `mcp`, `partner`, `planning`, `responsibilities`, `rest`, `separating`, `whether`, `zoom`

## documentation

Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README", "write a runbook", "onboarding guide", or when the user needs help with any form of technical writing — API docs, architecture docs, or operational runbooks.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/documentation`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/documentation/SKILL.md`
- **Tags**: `api`, `architecture`, `create`, `docs`, `document`, `documentation`, `engineering`, `form`, `maintain`, `needs`, `onboarding`, `operational`, `readme`, `runbook`, `runbooks`, `technical`, `trigger`

## figma-generate-library

Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-generate-library`
- **Skill file**: `external/openai-skills/skills/.curated/figma-generate-library/SKILL.md`
- **Tags**: `api`, `between`, `both`, `build`, `call`, `code`, `codebase`, `complements`, `component`, `create`, `curated`, `dark`, `design`, `document`, `figma`, `figma-library`, `foundations`, `gaps`, `grade`, `libraries`, `library`, `light`, `loaded`, `modes`, `order`, `professional`, `professional-grade`, `reconcile`, `set`, `teaches`, `theming`, `together`, `tokens`, `variables`, `which`

## gh-cli

Enforces authenticated gh CLI workflows over unauthenticated curl/WebFetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/.codex/skills/gh-cli`
- **Skill file**: `external/trailofbits-skills/.codex/skills/gh-cli/SKILL.md`
- **Tags**: `access`, `api`, `authenticated`, `cli`, `codex`, `curl`, `enforces`, `gh-cli`, `github`, `issues`, `over`, `pull`, `requests`, `unauthenticated`, `urls`, `webfetch`, `working`

## hook-development

This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development/SKILL.md`
- **Tags**: `advanced`, `api`, `asks`, `automation`, `block`, `code`, `commands`, `comprehensive`, `create`, `creating`, `dangerous`, `dev`, `development`, `driven`, `event`, `event-driven`, `events`, `focus`, `guidance`, `hook`, `hook-development`, `hooks`, `implement`, `implementing`, `mentions`, `notification`, `posttooluse`, `precompact`, `pretooluse`, `prompt`, `provides`, `root`, `sessionend`, `sessionstart`, `set`, `stop`, `subagentstop`, `used`, `userpromptsubmit`, `validate`

## plan-zoom-product

Choose the right Zoom building surface for a use case and explain the tradeoffs clearly. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Phone, Contact Center, or MCP for a specific product idea or integration goal.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product/SKILL.md`
- **Tags**: `api`, `apps`, `between`, `building`, `case`, `center`, `choose`, `clearly`, `contact`, `deciding`, `explain`, `goal`, `idea`, `integration`, `mcp`, `meeting`, `partner`, `phone`, `plan`, `plan-zoom-product`, `product`, `rest`, `right`, `sdk`, `surface`, `tradeoffs`, `video`, `webhooks`, `websockets`, `zoom`

## rivet-sdk

Reference skill for Zoom Rivet SDK. Use after routing to a Rivet-based server workflow when implementing auth handling, webhook consumers, API wrappers, multi-module composition, or Lambda receiver patterns.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rivet-sdk`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rivet-sdk/SKILL.md`
- **Tags**: `api`, `auth`, `composition`, `consumers`, `handling`, `implementing`, `lambda`, `module`, `multi`, `multi-module`, `partner`, `receiver`, `rivet`, `rivet-sdk`, `routing`, `sdk`, `server`, `webhook`, `wrappers`, `zoom`

## sharp-edges

Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges`
- **Skill file**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges/SKILL.md`
- **Tags**: `api`, `apis`, `code`, `configuration`, `configurations`, `cryptographic`, `dangerous`, `default`, `defaults`, `designs`, `edges`, `enable`, `ergonomics`, `error`, `error-prone`, `evaluating`, `follows`, `footgun`, `identifies`, `library`, `mistakes`, `misuse`, `misuse-resistant`, `pit`, `principles`, `prone`, `resistant`, `reviewing`, `schemas`, `secure`, `security`, `sharp`, `sharp-edges`, `success`, `triggers`, `usability`, `whether`

## speech

Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for live calls. Custom voice creation is out of scope.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/speech`
- **Skill file**: `external/openai-skills/skills/.curated/speech/SKILL.md`
- **Tags**: `accessibility`, `api`, `api-key`, `asks`, `audio`, `batch`, `bundled`, `calls`, `cli`, `creation`, `curated`, `custom`, `generation`, `key`, `live`, `narration`, `out`, `prompts`, `reads`, `require`, `scope`, `speech`, `text`, `text-to-speech`, `voice`, `voiceover`, `voices`

## system-design

Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "system design for", "what's the right architecture for", or when the user needs help with API design, data modeling, or service boundaries.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/system-design`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/system-design/SKILL.md`
- **Tags**: `api`, `architect`, `architecture`, `architectures`, `boundaries`, `data`, `design`, `engineering`, `modeling`, `needs`, `right`, `service`, `services`, `systems`, `trigger`

## xlsx

Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/xlsx`
- **Skill file**: `external/anthropic-skills/skills/xlsx/SKILL.md`
- **Tags**: `adding`, `api`, `between`, `casually`, `charting`, `cleaning`, `columns`, `computing`, `convert`, `create`, `csv`, `data`, `database`, `deliverable`, `document`, `done`, `downloads`, `edit`, `especially`, `even`, `existing`, `fix`, `formats`, `formatting`, `formulas`, `google`, `headers`, `html`, `input`, `integration`, `involved`, `junk`, `like`, `malformed`, `means`, `messy`, `misplaced`, `must`, `open`, `other`, `path`, `pipeline`, `primary`, `produced`, `proper`, `python`, `report`, `restructuring`, `rows`, `scratch`, `script`, `sheets`, `something`, `sources`, `spreadsheet`, `spreadsheets`, `standalone`, `tabular`, `time`, `trigger`, `tsv`, `where`, `word`, `xlsm`, `xlsx`

## zoom-general

Cross-product Zoom reference skill. Use after the workflow is clear when you need shared platform guidance, app-model comparisons, authentication context, scopes, marketplace considerations, or API-vs-MCP routing.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general/SKILL.md`
- **Tags**: `api`, `api-vs-mcp`, `app`, `app-model`, `authentication`, `clear`, `comparisons`, `considerations`, `context`, `cross`, `cross-product`, `general`, `guidance`, `marketplace`, `mcp`, `model`, `partner`, `platform`, `product`, `routing`, `scopes`, `shared`, `zoom`, `zoom-general`
