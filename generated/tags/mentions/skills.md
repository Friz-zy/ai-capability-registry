# Tag: mentions

Skills with tag `mentions`:

## build-mcp-app

This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`
- **Tags**: `already`, `app`, `apps`, `build`, `build-mcp-app`, `build-mcp-server`, `chat`, `components`, `confirmation`, `context`, `conversation`, `dashboard`, `deployment`, `dev`, `dialog`, `form`, `has`, `inline`, `interactive`, `knows`, `make`, `mcp`, `mcp-server-dev`, `mentions`, `model`, `picker`, `render`, `sdk`, `server`, `settled`, `shows`, `they`, `used`, `want`, `widgets`

## build-mcpb

This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb/SKILL.md`
- **Tags**: `apps`, `build`, `build-mcpb`, `bundle`, `bundling`, `desktop`, `dev`, `discusses`, `distribute`, `filesystem`, `having`, `installable`, `interacts`, `local`, `make`, `mcp`, `mcp-server-dev`, `mcpb`, `mentions`, `must`, `needs`, `node`, `package`, `python`, `runtime`, `server`, `set`, `ship`, `their`, `used`, `without`

## claude-automation-recommender

Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`
- **Tags**: `analyze`, `asks`, `automation`, `automation-recommender`, `automations`, `code`, `codebase`, `features`, `hooks`, `improving`, `know`, `mcp`, `mentions`, `optimize`, `project`, `recommend`, `recommendations`, `recommender`, `servers`, `set`, `subagents`, `their`, `they`

## claude-md-improver

Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization".

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver/SKILL.md`
- **Tags**: `against`, `asks`, `audit`, `evaluates`, `fix`, `improve`, `improver`, `maintenance`, `makes`, `management`, `md-improver`, `md-management`, `memory`, `mentions`, `optimization`, `outputs`, `project`, `quality`, `report`, `repositories`, `scans`, `targeted`, `then`, `updates`

## digest

Generate a daily or weekly digest of activity across all connected sources. Use when catching up after time away, starting the day and wanting a summary of mentions and action items, or reviewing a week's decisions and document updates grouped by project.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/digest`
- **Skill file**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/digest/SKILL.md`
- **Tags**: `activity`, `away`, `catching`, `connected`, `daily`, `day`, `decisions`, `digest`, `document`, `enterprise`, `enterprise-search`, `grouped`, `items`, `mentions`, `project`, `reviewing`, `search`, `sources`, `starting`, `summary`, `time`, `updates`, `wanting`, `week`, `weekly`

## doc-coauthoring

Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/doc-coauthoring`
- **Skill file**: `external/anthropic-skills/skills/doc-coauthoring/SKILL.md`
- **Tags**: `authoring`, `co-authoring`, `coauthoring`, `content`, `context`, `creating`, `decision`, `doc`, `doc-coauthoring`, `docs`, `documentation`, `drafting`, `efficiently`, `helps`, `iteration`, `mentions`, `proposals`, `readers`, `refine`, `similar`, `specs`, `structured`, `technical`, `transfer`, `trigger`, `verify`

## figma-implement-design

Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementing UI code from Figma files, when user mentions "implement design", "generate code", "implement component", provides Figma URLs, or asks to build components matching Figma specs. For Figma canvas writes via `use_figma`, use `figma-use`.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-implement-design`
- **Skill file**: `external/openai-skills/skills/.curated/figma-implement-design/SKILL.md`
- **Tags**: `application`, `asks`, `build`, `canvas`, `code`, `component`, `components`, `curated`, `design`, `designs`, `fidelity`, `figma`, `figma-implement-design`, `implement`, `implementing`, `matching`, `mentions`, `production`, `production-ready`, `provides`, `ready`, `specs`, `translates`, `urls`, `visual`, `writes`

## hook-development

This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development/SKILL.md`
- **Tags**: `advanced`, `api`, `asks`, `automation`, `block`, `code`, `commands`, `comprehensive`, `create`, `creating`, `dangerous`, `dev`, `development`, `driven`, `event`, `event-driven`, `events`, `focus`, `guidance`, `hook`, `hook-development`, `hooks`, `implement`, `implementing`, `mentions`, `notification`, `posttooluse`, `precompact`, `pretooluse`, `prompt`, `provides`, `root`, `sessionend`, `sessionstart`, `set`, `stop`, `subagentstop`, `used`, `userpromptsubmit`, `validate`

## mcp-integration

This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration/SKILL.md`
- **Tags**: `asks`, `code`, `comprehensive`, `configure`, `connect`, `context`, `dev`, `discusses`, `guidance`, `http`, `integrate`, `integrating`, `integration`, `mcp`, `mcp-integration`, `mentions`, `model`, `protocol`, `provides`, `root`, `server`, `servers`, `service`, `set`, `sse`, `stdio`, `types`, `used`, `websocket`

## mutation-testing

Configures mewt or muton mutation testing campaigns — scopes targets, tunes timeouts, and optimizes long-running runs. Use when the user mentions mewt, muton, mutation testing, or wants to configure or optimize a mutation testing campaign.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/mutation-testing/skills/mutation-testing`
- **Skill file**: `external/trailofbits-skills/plugins/mutation-testing/skills/mutation-testing/SKILL.md`
- **Tags**: `campaign`, `campaigns`, `configure`, `configures`, `long`, `long-running`, `mentions`, `mewt`, `mutation`, `mutation-testing`, `muton`, `optimize`, `optimizes`, `running`, `runs`, `scopes`, `targets`, `testing`, `timeouts`, `tunes`

## pdf

Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/pdf`
- **Skill file**: `external/anthropic-skills/skills/pdf/SKILL.md`
- **Tags**: `adding`, `anything`, `apart`, `asks`, `combining`, `creating`, `decrypting`, `encrypting`, `extracting`, `filling`, `forms`, `images`, `includes`, `make`, `mentions`, `merging`, `multiple`, `ocr`, `one`, `pages`, `pdf`, `pdfs`, `produce`, `reading`, `rotating`, `scanned`, `searchable`, `splitting`, `tables`, `text`, `them`, `watermarks`, `whenever`

## pptx

Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/pptx`
- **Skill file**: `external/anthropic-skills/skills/pptx/SKILL.md`
- **Tags**: `afterward`, `both`, `combining`, `comments`, `content`, `created`, `creating`, `deck`, `decks`, `editing`, `elsewhere`, `email`, `even`, `existing`, `extracted`, `extracting`, `filename`, `includes`, `input`, `involved`, `layouts`, `like`, `mentions`, `modifying`, `needs`, `notes`, `opened`, `parsing`, `pitch`, `plan`, `pptx`, `presentation`, `presentations`, `reading`, `regardless`, `slide`, `slides`, `speaker`, `splitting`, `summary`, `text`, `they`, `time`, `touched`, `trigger`, `updating`, `used`, `way`, `whenever`, `will`, `working`

## scvi-tools

Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need (1) data integration and batch correction with scVI/scANVI, (2) ATAC-seq analysis with PeakVI, (3) CITE-seq multi-modal analysis with totalVI, (4) multiome RNA+ATAC analysis with MultiVI, (5) spatial transcriptomics deconvolution with DestVI, (6) label transfer and reference mapping with scANVI/scArches, (7) RNA velocity with veloVI, or (8) any deep learning-based single-cell method. Triggers include mentions of scVI, scANVI, totalVI, PeakVI, MultiVI, DestVI, veloVI, sysVI, scArches, variational autoencoder, VAE, batch correction, data integration, multi-modal, CITE-seq, multiome, reference mapping, latent space.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/scvi-tools`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/scvi-tools/SKILL.md`
- **Tags**: `analysis`, `atac`, `atac-seq`, `autoencoder`, `batch`, `bio`, `bio-research`, `cell`, `cite`, `cite-seq`, `correction`, `data`, `deconvolution`, `deep`, `destvi`, `include`, `integration`, `label`, `latent`, `learning`, `mapping`, `mentions`, `method`, `modal`, `multi`, `multi-modal`, `multiome`, `multivi`, `peakvi`, `research`, `rna`, `scanvi`, `scarches`, `scvi`, `seq`, `single`, `single-cell`, `space`, `spatial`, `sysvi`, `totalvi`, `transcriptomics`, `transfer`, `triggers`, `used`, `vae`, `variational`, `velocity`, `velovi`

## second-opinion

Runs external LLM code reviews (OpenAI Codex or Google Gemini CLI) on uncommitted changes, branch diffs, or specific commits. Use when the user asks for a second opinion, external review, codex review, gemini review, or mentions /second-opinion.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion`
- **Skill file**: `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion/SKILL.md`
- **Tags**: `asks`, `branch`, `changes`, `cli`, `code`, `codex`, `commits`, `diffs`, `gemini`, `google`, `llm`, `mentions`, `opinion`, `review`, `reviews`, `runs`, `second`, `second-opinion`, `uncommitted`
