# Tag: asks

Skills with tag `asks`:

## access

Manage Discord channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Discord channel.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/external_plugins/discord/skills/access`
- **Skill file**: `external/anthropic-claude-plugins-official/external_plugins/discord/skills/access/SKILL.md`
- **Tags**: `access`, `allowed`, `allowlists`, `approve`, `asks`, `change`, `channel`, `discord`, `edit`, `group`, `manage`, `pair`, `pairings`, `policy`, `set`, `someone`, `who`

## access

Manage iMessage channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the iMessage channel.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/external_plugins/imessage/skills/access`
- **Skill file**: `external/anthropic-claude-plugins-official/external_plugins/imessage/skills/access/SKILL.md`
- **Tags**: `access`, `allowed`, `allowlists`, `approve`, `asks`, `change`, `channel`, `edit`, `group`, `imessage`, `manage`, `pair`, `pairings`, `policy`, `set`, `someone`, `who`

## access

Manage Telegram channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Telegram channel.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/external_plugins/telegram/skills/access`
- **Skill file**: `external/anthropic-claude-plugins-official/external_plugins/telegram/skills/access/SKILL.md`
- **Tags**: `access`, `allowed`, `allowlists`, `approve`, `asks`, `change`, `channel`, `edit`, `group`, `manage`, `pair`, `pairings`, `policy`, `set`, `someone`, `telegram`, `who`

## agent-development

This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/agent-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/agent-development/SKILL.md`
- **Tags**: `asks`, `autonomous`, `code`, `colors`, `conditions`, `create`, `description`, `dev`, `development`, `frontmatter`, `guidance`, `needs`, `practices`, `prompts`, `structure`, `subagent`, `triggering`, `used`

## build-mcp-server

This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`
- **Tags**: `api`, `app`, `asks`, `build`, `build-mcp-server`, `building`, `case`, `context`, `create`, `deployment`, `design`, `determines`, `dev`, `development`, `discusses`, `entry`, `expose`, `hands`, `http`, `integration`, `interrogates`, `local`, `make`, `mcp`, `mcp-server-dev`, `mcpb`, `model`, `off`, `picks`, `point`, `protocol`, `remote`, `right`, `server`, `something`, `specialized`, `stdio`, `their`, `used`, `wrap`

## canvas-design

Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/canvas-design`
- **Skill file**: `external/anthropic-skills/skills/canvas-design/SKILL.md`
- **Tags**: `art`, `artists`, `asks`, `avoid`, `beautiful`, `canvas`, `canvas-design`, `copying`, `copyright`, `create`, `design`, `designs`, `documents`, `existing`, `never`, `original`, `other`, `pdf`, `philosophy`, `piece`, `png`, `poster`, `static`, `violations`, `visual`

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

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

## cloudflare-deploy

Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. Use when the user asks to deploy, host, publish, or set up a project on Cloudflare.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/cloudflare-deploy`
- **Skill file**: `external/openai-skills/skills/.curated/cloudflare-deploy/SKILL.md`
- **Tags**: `applications`, `asks`, `cloudflare`, `cloudflare-deploy`, `curated`, `deploy`, `host`, `infrastructure`, `pages`, `platform`, `project`, `publish`, `services`, `set`, `workers`

## command-development

This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in commands, user interaction patterns, or command development best practices for Claude Code.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/command-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/command-development/SKILL.md`
- **Tags**: `arguments`, `asks`, `askuserquestion`, `bash`, `code`, `command`, `command-development`, `commands`, `create`, `custom`, `define`, `dev`, `development`, `dynamic`, `execution`, `fields`, `frontmatter`, `guidance`, `interaction`, `interactive`, `needs`, `organize`, `practices`, `slash`, `structure`, `used`, `yaml`

## configure

Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord bot token, asks to configure Discord, asks "how do I set this up" or "who can reach me," or wants to check channel status.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/external_plugins/discord/skills/configure`
- **Skill file**: `external/anthropic-claude-plugins-official/external_plugins/discord/skills/configure/SKILL.md`
- **Tags**: `access`, `asks`, `bot`, `can`, `channel`, `configure`, `discord`, `pastes`, `policy`, `reach`, `review`, `save`, `set`, `status`, `token`, `who`

## configure

Check iMessage channel setup and review access policy. Use when the user asks to configure iMessage, asks "how do I set this up" or "who can reach me," or wants to know why texts aren't reaching the assistant.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/external_plugins/imessage/skills/configure`
- **Skill file**: `external/anthropic-claude-plugins-official/external_plugins/imessage/skills/configure/SKILL.md`
- **Tags**: `access`, `aren`, `asks`, `can`, `channel`, `configure`, `imessage`, `know`, `policy`, `reach`, `reaching`, `review`, `set`, `texts`, `who`, `why`

## configure

Set up the Telegram channel — save the bot token and review access policy. Use when the user pastes a Telegram bot token, asks to configure Telegram, asks "how do I set this up" or "who can reach me," or wants to check channel status.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/external_plugins/telegram/skills/configure`
- **Skill file**: `external/anthropic-claude-plugins-official/external_plugins/telegram/skills/configure/SKILL.md`
- **Tags**: `access`, `asks`, `bot`, `can`, `channel`, `configure`, `pastes`, `policy`, `reach`, `review`, `save`, `set`, `status`, `telegram`, `token`, `who`

## customer-research

Multi-source research on a customer question or topic with source attribution. Use when a customer asks something you need to look up, investigating whether a bug has been reported before, checking what was previously told to a specific account, or gathering background before drafting a response.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/customer-support/skills/customer-research`
- **Skill file**: `external/anthropic-knowledge-work-plugins/customer-support/skills/customer-research/SKILL.md`
- **Tags**: `account`, `asks`, `attribution`, `background`, `been`, `bug`, `checking`, `customer`, `customer-research`, `customer-support`, `drafting`, `gathering`, `has`, `investigating`, `look`, `multi`, `previously`, `question`, `reported`, `research`, `response`, `something`, `support`, `told`, `topic`, `was`, `whether`

## dimensional-analysis

Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol, offchain code, or other blockchain-related codebase with arithmetic. Prevents dimensional mismatches and catches formula bugs early.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis/SKILL.md`
- **Tags**: `analysis`, `annotate`, `annotates`, `arithmetic`, `asks`, `blockchain`, `bugs`, `catches`, `code`, `codebase`, `codebases`, `comments`, `decimal`, `defi`, `dimensional`, `dimensional-analysis`, `dimensions`, `documenting`, `early`, `find`, `formula`, `mismatches`, `offchain`, `other`, `perform`, `prevents`, `protocol`, `scaling`, `someone`, `units`, `vulnerabilities`

## docx

Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/docx`
- **Skill file**: `external/anthropic-skills/skills/docx/SKILL.md`
- **Tags**: `asks`, `changes`, `coding`, `comments`, `content`, `converting`, `create`, `deliverable`, `doc`, `docs`, `document`, `documents`, `docx`, `edit`, `extracting`, `find`, `find-replace`, `formatting`, `general`, `generation`, `google`, `headings`, `images`, `include`, `inserting`, `letter`, `letterheads`, `like`, `manipulate`, `memo`, `mention`, `numbers`, `page`, `pdfs`, `performing`, `polished`, `produce`, `professional`, `reorganizing`, `replace`, `replacing`, `report`, `requests`, `similar`, `spreadsheets`, `tables`, `tracked`, `triggers`, `unrelated`, `whenever`, `word`, `working`

## example-skill

This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or discusses skill development patterns. Provides a reference template for creating Claude Code plugin skills.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/example-plugin/skills/example-skill`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/example-plugin/skills/example-skill/SKILL.md`
- **Tags**: `asks`, `code`, `create`, `creating`, `demonstrate`, `development`, `discusses`, `format`, `provides`, `show`, `used`

## figma-implement-design

Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementing UI code from Figma files, when user mentions "implement design", "generate code", "implement component", provides Figma URLs, or asks to build components matching Figma specs. For Figma canvas writes via `use_figma`, use `figma-use`.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-implement-design`
- **Skill file**: `external/openai-skills/skills/.curated/figma-implement-design/SKILL.md`
- **Tags**: `application`, `asks`, `build`, `canvas`, `code`, `component`, `components`, `curated`, `design`, `designs`, `fidelity`, `figma`, `figma-implement-design`, `implement`, `implementing`, `matching`, `mentions`, `production`, `production-ready`, `provides`, `ready`, `specs`, `translates`, `urls`, `visual`, `writes`

## frontend-design

Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/frontend-design`
- **Skill file**: `external/anthropic-skills/skills/frontend-design/SKILL.md`
- **Tags**: `aesthetics`, `applications`, `artifacts`, `asks`, `avoids`, `beautifying`, `build`, `code`, `components`, `create`, `creative`, `css`, `dashboards`, `design`, `distinctive`, `frontend`, `frontend-design`, `generates`, `generic`, `grade`, `high`, `html`, `include`, `interfaces`, `landing`, `layouts`, `pages`, `polished`, `posters`, `production`, `production-grade`, `quality`, `react`, `styling`, `web`, `websites`

## frontend-design

Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/frontend-design/skills/frontend-design`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/frontend-design/skills/frontend-design/SKILL.md`
- **Tags**: `aesthetics`, `applications`, `asks`, `avoids`, `build`, `code`, `components`, `create`, `creative`, `design`, `distinctive`, `frontend`, `frontend-design`, `generates`, `generic`, `grade`, `high`, `interfaces`, `pages`, `polished`, `production`, `production-grade`, `quality`, `web`

## gh-fix-ci

Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/gh-fix-ci`
- **Skill file**: `external/openai-skills/skills/.curated/gh-fix-ci/SKILL.md`
- **Tags**: `actions`, `approval`, `asks`, `buildkite`, `checks`, `context`, `curated`, `debug`, `draft`, `explicit`, `failing`, `failure`, `fix`, `gh-fix-ci`, `github`, `implement`, `inspect`, `logs`, `out`, `plan`, `providers`, `report`, `scope`, `summarize`, `treat`, `url`

## hook-development

This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development/SKILL.md`
- **Tags**: `advanced`, `api`, `asks`, `automation`, `block`, `code`, `commands`, `comprehensive`, `create`, `creating`, `dangerous`, `dev`, `development`, `driven`, `event`, `event-driven`, `events`, `focus`, `guidance`, `hook`, `hook-development`, `hooks`, `implement`, `implementing`, `mentions`, `notification`, `posttooluse`, `precompact`, `pretooluse`, `prompt`, `provides`, `root`, `sessionend`, `sessionstart`, `set`, `stop`, `subagentstop`, `used`, `userpromptsubmit`, `validate`

## jupyter-notebook

Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and run the helper script `new_notebook.py` to generate a clean starting notebook.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/jupyter-notebook`
- **Skill file**: `external/openai-skills/skills/.curated/jupyter-notebook/SKILL.md`
- **Tags**: `asks`, `bundled`, `clean`, `create`, `curated`, `edit`, `experiments`, `explorations`, `helper`, `ipynb`, `jupyter`, `jupyter-notebook`, `notebook`, `notebooks`, `prefer`, `scaffold`, `script`, `starting`, `tutorials`

## mcp-integration

This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration/SKILL.md`
- **Tags**: `asks`, `code`, `comprehensive`, `configure`, `connect`, `context`, `dev`, `discusses`, `guidance`, `http`, `integrate`, `integrating`, `integration`, `mcp`, `mcp-integration`, `mentions`, `model`, `protocol`, `provides`, `root`, `server`, `servers`, `service`, `set`, `sse`, `stdio`, `types`, `used`, `websocket`

## netlify-deploy

Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/netlify-deploy`
- **Skill file**: `external/openai-skills/skills/.curated/netlify-deploy/SKILL.md`
- **Tags**: `asks`, `cli`, `curated`, `deploy`, `deploys`, `host`, `including`, `link`, `netlify`, `netlify-deploy`, `npx`, `preview`, `production`, `projects`, `publish`, `repo`, `site`, `web`

## openai-docs

Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/openai-docs`
- **Skill file**: `external/openai-skills/skills/.curated/openai-docs/SKILL.md`
- **Tags**: `apis`, `asks`, `browsing`, `build`, `bundled`, `case`, `choosing`, `citations`, `context`, `curated`, `date`, `docs`, `documentation`, `domains`, `fallback`, `guidance`, `helper`, `latest`, `mcp`, `model`, `needs`, `prioritize`, `products`, `prompt`, `prompt-upgrade`, `restrict`, `up-to-date`, `upgrade`

## openai-docs

Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.system/openai-docs`
- **Skill file**: `external/openai-skills/skills/.system/openai-docs/SKILL.md`
- **Tags**: `apis`, `asks`, `browsing`, `build`, `bundled`, `case`, `choosing`, `citations`, `context`, `date`, `docs`, `documentation`, `domains`, `fallback`, `guidance`, `helper`, `latest`, `mcp`, `model`, `needs`, `prioritize`, `products`, `prompt`, `prompt-upgrade`, `restrict`, `up-to-date`, `upgrade`

## openai-gh-fix-ci

Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions;

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-gh-fix-ci/skills/openai-gh-fix-ci`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-gh-fix-ci/skills/openai-gh-fix-ci/SKILL.md`
- **Tags**: `actions`, `asks`, `checks`, `debug`, `failing`, `fix`, `gh-fix-ci`, `github`

## openai-jupyter-notebook

Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments,

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-jupyter-notebook/skills/openai-jupyter-notebook`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-jupyter-notebook/skills/openai-jupyter-notebook/SKILL.md`
- **Tags**: `asks`, `create`, `edit`, `experiments`, `ipynb`, `jupyter`, `jupyter-notebook`, `notebook`, `notebooks`, `scaffold`

## openai-netlify-deploy

Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-netlify-deploy/skills/openai-netlify-deploy`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-netlify-deploy/skills/openai-netlify-deploy/SKILL.md`
- **Tags**: `asks`, `cli`, `deploy`, `netlify`, `netlify-deploy`, `npx`, `projects`, `web`

## openai-screenshot

Use when the user explicitly asks for a desktop or system screenshot (full screen, specific

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-screenshot/skills/openai-screenshot`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-screenshot/skills/openai-screenshot/SKILL.md`
- **Tags**: `asks`, `desktop`, `explicitly`, `full`, `screen`, `screenshot`

## openai-sentry

Use when the user asks to inspect Sentry issues or events, summarize recent production errors,

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-sentry/skills/openai-sentry`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-sentry/skills/openai-sentry/SKILL.md`
- **Tags**: `asks`, `errors`, `events`, `inspect`, `issues`, `production`, `recent`, `sentry`, `summarize`

## openai-yeet

Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-yeet/skills/openai-yeet`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-yeet/skills/openai-yeet/SKILL.md`
- **Tags**: `asks`, `commit`, `explicitly`, `github`, `open`, `pull`, `push`, `request`, `stage`, `yeet`

## pdf

Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/pdf`
- **Skill file**: `external/anthropic-skills/skills/pdf/SKILL.md`
- **Tags**: `adding`, `anything`, `apart`, `asks`, `combining`, `creating`, `decrypting`, `encrypting`, `extracting`, `filling`, `forms`, `images`, `includes`, `make`, `mentions`, `merging`, `multiple`, `ocr`, `one`, `pages`, `pdf`, `pdfs`, `produce`, `reading`, `rotating`, `scanned`, `searchable`, `splitting`, `tables`, `text`, `them`, `watermarks`, `whenever`

## playground

Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/playground/skills/playground`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/playground/skills/playground/SKILL.md`
- **Tags**: `asks`, `configure`, `contained`, `controls`, `copy`, `creates`, `explorer`, `explorers`, `html`, `interactive`, `let`, `live`, `make`, `out`, `playground`, `playgrounds`, `preview`, `prompt`, `self`, `self-contained`, `single`, `something`, `topic`, `visually`

## plugin-settings

This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-settings`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-settings/SKILL.md`
- **Tags**: `asks`, `behavior`, `configurable`, `configuration`, `content`, `dev`, `documents`, `frontmatter`, `local`, `make`, `markdown`, `per`, `per-project`, `project`, `settings`, `state`, `store`, `storing`, `used`, `yaml`

## plugin-structure

This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure/SKILL.md`
- **Tags**: `architecture`, `asks`, `auto`, `auto-discovery`, `code`, `commands`, `component`, `components`, `configuration`, `configure`, `conventions`, `create`, `dev`, `directory`, `discovery`, `guidance`, `hooks`, `layout`, `manifest`, `naming`, `needs`, `organization`, `organize`, `practices`, `root`, `scaffold`, `set`, `structure`, `understand`, `used`

## screenshot

Use when the user explicitly asks for a desktop or system screenshot (full screen, specific app or window, or a pixel region), or when tool-specific capture capabilities are unavailable and an OS-level capture is needed.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/screenshot`
- **Skill file**: `external/openai-skills/skills/.curated/screenshot/SKILL.md`
- **Tags**: `app`, `asks`, `capabilities`, `capture`, `curated`, `desktop`, `explicitly`, `full`, `level`, `needed`, `os-level`, `pixel`, `region`, `screen`, `screenshot`, `unavailable`, `window`

## second-opinion

Runs external LLM code reviews (OpenAI Codex or Google Gemini CLI) on uncommitted changes, branch diffs, or specific commits. Use when the user asks for a second opinion, external review, codex review, gemini review, or mentions /second-opinion.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion`
- **Skill file**: `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion/SKILL.md`
- **Tags**: `asks`, `branch`, `changes`, `cli`, `code`, `codex`, `commits`, `diffs`, `gemini`, `google`, `llm`, `mentions`, `opinion`, `review`, `reviews`, `runs`, `second`, `second-opinion`, `uncommitted`

## security-threat-model

Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-threat-model`
- **Skill file**: `external/openai-skills/skills/.curated/security-threat-model/SKILL.md`
- **Tags**: `abuse`, `appsec`, `architecture`, `asks`, `assets`, `attacker`, `boundaries`, `capabilities`, `code`, `codebase`, `concise`, `curated`, `design`, `enumerate`, `enumerates`, `explicitly`, `general`, `grounded`, `markdown`, `mitigations`, `model`, `modeling`, `non`, `non-security`, `path`, `paths`, `perform`, `repository`, `repository-grounded`, `review`, `security`, `security-threat-model`, `summaries`, `threat`, `threats`, `trigger`, `trust`, `writes`

## sentry

Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; perform read-only queries using the `sentry` command.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/sentry`
- **Skill file**: `external/openai-skills/skills/.curated/sentry/SKILL.md`
- **Tags**: `asks`, `basic`, `cli`, `command`, `curated`, `data`, `errors`, `events`, `health`, `inspect`, `issues`, `perform`, `production`, `pull`, `queries`, `recent`, `sentry`, `summarize`

## skill-installer

Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.system/skill-installer`
- **Skill file**: `external/openai-skills/skills/.system/skill-installer/SKILL.md`
- **Tags**: `another`, `asks`, `codex`, `codex-home`, `curated`, `github`, `home`, `including`, `install`, `installable`, `installer`, `path`, `private`, `repo`, `repos`

## speech

Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for live calls. Custom voice creation is out of scope.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/speech`
- **Skill file**: `external/openai-skills/skills/.curated/speech/SKILL.md`
- **Tags**: `accessibility`, `api`, `api-key`, `asks`, `audio`, `batch`, `bundled`, `calls`, `cli`, `creation`, `curated`, `custom`, `generation`, `key`, `live`, `narration`, `out`, `prompts`, `reads`, `require`, `scope`, `speech`, `text`, `text-to-speech`, `voice`, `voiceover`, `voices`

## task-management

Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, wants to add/complete tasks, or needs help tracking commitments.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/productivity/skills/task-management`
- **Skill file**: `external/anthropic-knowledge-work-plugins/productivity/skills/task-management/SKILL.md`
- **Tags**: `asks`, `commitments`, `complete`, `management`, `needs`, `productivity`, `shared`, `simple`, `their`, `tracking`

## tech-debt

Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or when the user asks about code quality, refactoring priorities, or maintenance backlog.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/tech-debt`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/tech-debt/SKILL.md`
- **Tags**: `asks`, `audit`, `backlog`, `categorize`, `code`, `debt`, `engineering`, `health`, `identify`, `maintenance`, `priorities`, `prioritize`, `quality`, `refactor`, `refactoring`, `tech`, `tech-debt`, `technical`, `trigger`

## transcribe

Transcribe audio files to text with optional diarization and known-speaker hints. Use when a user asks to transcribe speech from audio/video, extract text from recordings, or label speakers in interviews or meetings.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/transcribe`
- **Skill file**: `external/openai-skills/skills/.curated/transcribe/SKILL.md`
- **Tags**: `asks`, `audio`, `curated`, `diarization`, `extract`, `hints`, `interviews`, `label`, `meetings`, `optional`, `recordings`, `speaker`, `speakers`, `speech`, `text`, `transcribe`, `video`

## writing-hookify-rules

This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/hookify/skills/writing-rules`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/hookify/skills/writing-rules/SKILL.md`
- **Tags**: `asks`, `configure`, `create`, `guidance`, `hook`, `hookify`, `needs`, `rule`, `syntax`, `used`

## yeet

Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/yeet`
- **Skill file**: `external/openai-skills/skills/.curated/yeet/SKILL.md`
- **Tags**: `asks`, `cli`, `commit`, `curated`, `explicitly`, `flow`, `github`, `one`, `open`, `pull`, `push`, `request`, `stage`, `yeet`
