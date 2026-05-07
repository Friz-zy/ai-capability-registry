# Tag: curated

Skills with tag `curated`:

## aspnet-core

Build, review, refactor, or architect ASP.NET Core web applications using current official guidance for .NET web development. Use when working on Blazor Web Apps, Razor Pages, MVC, Minimal APIs, controller-based Web APIs, SignalR, gRPC, middleware, dependency injection, configuration, authentication, authorization, testing, performance, deployment, or ASP.NET Core upgrades.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/aspnet-core`
- **Skill file**: `external/openai-skills/skills/.curated/aspnet-core/SKILL.md`
- **Tags**: `apis`, `applications`, `apps`, `architect`, `asp`, `aspnet`, `aspnet-core`, `authentication`, `authorization`, `blazor`, `build`, `configuration`, `controller`, `core`, `curated`, `dependency`, `deployment`, `development`, `grpc`, `guidance`, `injection`, `middleware`, `minimal`, `mvc`, `net`, `pages`, `performance`, `razor`, `refactor`, `review`, `signalr`, `testing`, `upgrades`, `web`, `working`

## chatgpt-apps

Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold. Prefer a docs-first workflow by invoking the openai-docs skill or OpenAI developer docs MCP tools before generating code.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/chatgpt-apps`
- **Skill file**: `external/openai-skills/skills/.curated/chatgpt-apps/SKILL.md`
- **Tags**: `aligned`, `apis`, `applications`, `apply`, `apps`, `bridge`, `build`, `chatgpt`, `chatgpt-apps`, `code`, `codex`, `combine`, `compatibility`, `csp`, `curated`, `design`, `developer`, `docs`, `docs-aligned`, `domain`, `generating`, `invoking`, `mcp`, `metadata`, `needs`, `prefer`, `produce`, `project`, `refactor`, `register`, `scaffold`, `sdk`, `server`, `settings`, `troubleshoot`, `widget`, `wire`

## cli-creator

Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/cli-creator`
- **Skill file**: `external/openai-skills/skills/.curated/cli-creator/SKILL.md`
- **Tags**: `admin`, `api`, `app`, `auth`, `build`, `can`, `cli`, `cli-creator`, `codex`, `command`, `command-line`, `commands`, `companion`, `composable`, `create`, `creator`, `curated`, `curl`, `docs`, `existing`, `expose`, `line`, `local`, `manage`, `openapi`, `pair`, `repo`, `return`, `script`, `sdk`, `spec`, `stable`, `web`

## cloudflare-deploy

Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. Use when the user asks to deploy, host, publish, or set up a project on Cloudflare.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/cloudflare-deploy`
- **Skill file**: `external/openai-skills/skills/.curated/cloudflare-deploy/SKILL.md`
- **Tags**: `applications`, `asks`, `cloudflare`, `cloudflare-deploy`, `curated`, `deploy`, `host`, `infrastructure`, `pages`, `platform`, `project`, `publish`, `services`, `set`, `workers`

## figma

Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma nodes into production code. Trigger when a task involves Figma URLs, node IDs, design-to-code implementation, or Figma MCP setup and troubleshooting.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma`
- **Skill file**: `external/openai-skills/skills/.curated/figma/SKILL.md`
- **Tags**: `assets`, `code`, `context`, `curated`, `design`, `design-to-code`, `fetch`, `figma`, `ids`, `implementation`, `involves`, `mcp`, `node`, `nodes`, `production`, `screenshots`, `server`, `translate`, `trigger`, `troubleshooting`, `urls`, `variables`

## figma-code-connect-components

Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code connect", "connect this component to code", "map this component", "link component to code", "create code connect mapping", or wants to establish mappings between Figma designs and code implementations. For canvas writes via `use_figma`, use `figma-use`.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-code-connect-components`
- **Skill file**: `external/openai-skills/skills/.curated/figma-code-connect-components/SKILL.md`
- **Tags**: `between`, `canvas`, `code`, `component`, `components`, `connect`, `connects`, `create`, `curated`, `design`, `designs`, `establish`, `figma`, `figma-code-connect-components`, `implementations`, `link`, `map`, `mapping`, `mappings`, `says`, `writes`

## figma-create-design-system-rules

Generates custom design system rules for the user's codebase. Use when user says "create design system rules", "generate rules for my project", "set up design rules", "customize design system guidelines", or wants to establish project-specific conventions for Figma-to-code workflows. Requires Figma MCP server connection.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-create-design-system-rules`
- **Skill file**: `external/openai-skills/skills/.curated/figma-create-design-system-rules/SKILL.md`
- **Tags**: `code`, `codebase`, `connection`, `conventions`, `create`, `curated`, `custom`, `customize`, `design`, `establish`, `figma`, `figma-create-design`, `figma-to-code`, `generates`, `guidelines`, `mcp`, `project`, `requires`, `says`, `server`, `set`

## figma-create-new-file

Create a new blank Figma file. Use when the user wants to create a new Figma design or FigJam file, or when you need a new file before calling use_figma. Handles plan resolution via whoami if needed. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard)

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-create-new-file`
- **Skill file**: `external/openai-skills/skills/.curated/figma-create-new-file/SKILL.md`
- **Tags**: `blank`, `calling`, `create`, `curated`, `design`, `editortype`, `figjam`, `figma`, `figma-create`, `filename`, `handles`, `needed`, `plan`, `resolution`, `whiteboard`, `whoami`

## figma-generate-design

Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-generate-design`
- **Skill file**: `external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`
- **Tags**: `alongside`, `app`, `application`, `assembles`, `build`, `code`, `components`, `create`, `curated`, `description`, `design`, `discovers`, `figma`, `figma-design`, `full`, `hardcoded`, `imports`, `incrementally`, `instead`, `involves`, `landing`, `layout`, `match`, `multi`, `multi-section`, `page`, `preferred`, `push`, `screen`, `screens`, `search`, `search-design`, `section`, `section-by-section`, `styles`, `take`, `them`, `tokens`, `translating`, `triggers`, `values`, `variables`, `view`, `whenever`

## figma-generate-library

Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-generate-library`
- **Skill file**: `external/openai-skills/skills/.curated/figma-generate-library/SKILL.md`
- **Tags**: `api`, `between`, `both`, `build`, `call`, `code`, `codebase`, `complements`, `component`, `create`, `curated`, `dark`, `design`, `document`, `figma`, `figma-library`, `foundations`, `gaps`, `grade`, `libraries`, `library`, `light`, `loaded`, `modes`, `order`, `professional`, `professional-grade`, `reconcile`, `set`, `teaches`, `theming`, `together`, `tokens`, `variables`, `which`

## figma-implement-design

Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementing UI code from Figma files, when user mentions "implement design", "generate code", "implement component", provides Figma URLs, or asks to build components matching Figma specs. For Figma canvas writes via `use_figma`, use `figma-use`.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-implement-design`
- **Skill file**: `external/openai-skills/skills/.curated/figma-implement-design/SKILL.md`
- **Tags**: `application`, `asks`, `build`, `canvas`, `code`, `component`, `components`, `curated`, `design`, `designs`, `fidelity`, `figma`, `figma-implement-design`, `implement`, `implementing`, `matching`, `mentions`, `production`, `production-ready`, `provides`, `ready`, `specs`, `translates`, `urls`, `visual`, `writes`

## figma-use

**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-use`
- **Skill file**: `external/openai-skills/skills/.curated/figma-use/SKILL.md`
- **Tags**: `auto`, `auto-layout`, `bind`, `build`, `call`, `causes`, `components`, `context`, `create`, `curated`, `debug`, `delete`, `directly`, `edit`, `every`, `execution`, `failures`, `figma`, `fills`, `hard`, `hard-to-debug`, `inspect`, `invoke`, `javascript`, `layout`, `loading`, `mandatory`, `modify`, `must`, `never`, `nodes`, `perform`, `prerequisite`, `programmatically`, `properties`, `requires`, `set`, `skipping`, `structure`, `tokens`, `trigger`, `unique`, `variables`, `variants`, `whenever`, `without`

## gh-address-comments

Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/gh-address-comments`
- **Skill file**: `external/openai-skills/skills/.curated/gh-address-comments/SKILL.md`
- **Tags**: `address`, `auth`, `authenticate`, `branch`, `cli`, `comments`, `curated`, `gh-address-comments`, `github`, `issue`, `logged`, `open`, `prompt`, `review`, `verify`

## gh-fix-ci

Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/gh-fix-ci`
- **Skill file**: `external/openai-skills/skills/.curated/gh-fix-ci/SKILL.md`
- **Tags**: `actions`, `approval`, `asks`, `buildkite`, `checks`, `context`, `curated`, `debug`, `draft`, `explicit`, `failing`, `failure`, `fix`, `gh-fix-ci`, `github`, `implement`, `inspect`, `logs`, `out`, `plan`, `providers`, `report`, `scope`, `summarize`, `treat`, `url`

## hatch-pet

Create, repair, validate, preview, and package Codex-compatible animated pets and pet spritesheets from character art, screenshots, generated images, or visual references. Use when a user wants to hatch a Codex pet, create a custom animated pet, or build a built-in pet asset with an 8x9 atlas, transparent unused cells, row-by-row animation prompts, QA contact sheets, preview videos, and pet.json packaging. This skill composes the installed $imagegen system skill for visual generation and uses bundled scripts for deterministic spritesheet assembly.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/hatch-pet`
- **Skill file**: `external/openai-skills/skills/.curated/hatch-pet/SKILL.md`
- **Tags**: `8x9`, `animated`, `animation`, `art`, `assembly`, `asset`, `atlas`, `build`, `bundled`, `cells`, `character`, `codex`, `codex-compatible`, `compatible`, `composes`, `contact`, `create`, `curated`, `custom`, `deterministic`, `generation`, `hatch`, `hatch-pet`, `imagegen`, `images`, `installed`, `package`, `packaging`, `pet`, `pets`, `preview`, `prompts`, `repair`, `row`, `row-by-row`, `screenshots`, `sheets`, `spritesheet`, `spritesheets`, `transparent`, `unused`, `validate`, `videos`, `visual`

## jupyter-notebook

Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and run the helper script `new_notebook.py` to generate a clean starting notebook.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/jupyter-notebook`
- **Skill file**: `external/openai-skills/skills/.curated/jupyter-notebook/SKILL.md`
- **Tags**: `asks`, `bundled`, `clean`, `create`, `curated`, `edit`, `experiments`, `explorations`, `helper`, `ipynb`, `jupyter`, `jupyter-notebook`, `notebook`, `notebooks`, `prefer`, `scaffold`, `script`, `starting`, `tutorials`

## linear

Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets in Linear.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/linear`
- **Skill file**: `external/openai-skills/skills/.curated/linear/SKILL.md`
- **Tags**: `create`, `curated`, `issues`, `linear`, `manage`, `projects`, `team`, `tickets`, `updates`

## migrate-to-codex

Migrate supported instruction files, skills, agents, and MCP config into Codex project and global files.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/migrate-to-codex`
- **Skill file**: `external/openai-skills/skills/.curated/migrate-to-codex/SKILL.md`
- **Tags**: `codex`, `config`, `curated`, `global`, `instruction`, `mcp`, `migrate`, `migrate-to-codex`, `project`, `supported`

## netlify-deploy

Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/netlify-deploy`
- **Skill file**: `external/openai-skills/skills/.curated/netlify-deploy/SKILL.md`
- **Tags**: `asks`, `cli`, `curated`, `deploy`, `deploys`, `host`, `including`, `link`, `netlify`, `netlify-deploy`, `npx`, `preview`, `production`, `projects`, `publish`, `repo`, `site`, `web`

## notion-knowledge-capture

Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/notion-knowledge-capture`
- **Skill file**: `external/openai-skills/skills/.curated/notion-knowledge-capture/SKILL.md`
- **Tags**: `capture`, `chats`, `conversations`, `curated`, `decisions`, `entries`, `faqs`, `knowledge`, `linking`, `notes`, `notion`, `notion-knowledge-capture`, `pages`, `proper`, `structured`, `tos`, `turning`, `wiki`

## notion-meeting-intelligence

Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/notion-meeting-intelligence`
- **Skill file**: `external/openai-skills/skills/.curated/notion-meeting-intelligence/SKILL.md`
- **Tags**: `agendas`, `attendees`, `codex`, `context`, `curated`, `drafting`, `gathering`, `intelligence`, `materials`, `meeting`, `notion`, `notion-meeting-intelligence`, `pre`, `pre-reads`, `prepare`, `reads`, `research`, `tailoring`

## notion-research-documentation

Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/notion-research-documentation`
- **Skill file**: `external/openai-skills/skills/.curated/notion-research-documentation/SKILL.md`
- **Tags**: `briefs`, `citations`, `comparisons`, `curated`, `documentation`, `gathering`, `info`, `multiple`, `notion`, `notion-research-documentation`, `produce`, `reports`, `research`, `sources`, `structured`, `synthesize`

## notion-spec-to-implementation

Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/notion-spec-to-implementation`
- **Skill file**: `external/openai-skills/skills/.curated/notion-spec-to-implementation/SKILL.md`
- **Tags**: `creating`, `curated`, `feature`, `implementation`, `implementing`, `notion`, `notion-spec-to-implementation`, `plans`, `prds`, `progress`, `spec`, `specs`, `them`, `tracking`, `turn`

## openai-docs

Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/openai-docs`
- **Skill file**: `external/openai-skills/skills/.curated/openai-docs/SKILL.md`
- **Tags**: `apis`, `asks`, `browsing`, `build`, `bundled`, `case`, `choosing`, `citations`, `context`, `curated`, `date`, `docs`, `documentation`, `domains`, `fallback`, `guidance`, `helper`, `latest`, `mcp`, `model`, `needs`, `prioritize`, `products`, `prompt`, `prompt-upgrade`, `restrict`, `up-to-date`, `upgrade`

## pdf

Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/pdf`
- **Skill file**: `external/openai-skills/skills/.curated/pdf/SKILL.md`
- **Tags**: `checks`, `creating`, `curated`, `extraction`, `generation`, `involve`, `layout`, `matter`, `pages`, `pdf`, `pdfplumber`, `poppler`, `prefer`, `pypdf`, `python`, `reading`, `rendering`, `reportlab`, `reviewing`, `such`, `visual`, `where`

## playwright

Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/playwright`
- **Skill file**: `external/openai-skills/skills/.curated/playwright/SKILL.md`
- **Tags**: `automating`, `browser`, `bundled`, `cli`, `curated`, `data`, `debugging`, `extraction`, `filling`, `flow`, `form`, `navigation`, `playwright`, `playwright-cli`, `real`, `requires`, `screenshots`, `script`, `snapshots`, `terminal`, `ui-flow`, `wrapper`

## playwright-interactive

Persistent browser and Electron interaction through `js_repl` for fast iterative UI debugging.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/playwright-interactive`
- **Skill file**: `external/openai-skills/skills/.curated/playwright-interactive/SKILL.md`
- **Tags**: `browser`, `curated`, `debugging`, `electron`, `fast`, `interaction`, `interactive`, `iterative`, `js-repl`, `persistent`, `playwright`, `playwright-interactive`, `repl`

## render-deploy

Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deeplinks. Use when the user wants to deploy, host, publish, or set up their application on Render's cloud platform.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/render-deploy`
- **Skill file**: `external/openai-skills/skills/.curated/render-deploy/SKILL.md`
- **Tags**: `analyzing`, `application`, `applications`, `blueprints`, `cloud`, `codebases`, `curated`, `dashboard`, `deeplinks`, `deploy`, `generating`, `host`, `platform`, `providing`, `publish`, `render`, `render-deploy`, `set`, `their`, `yaml`

## screenshot

Use when the user explicitly asks for a desktop or system screenshot (full screen, specific app or window, or a pixel region), or when tool-specific capture capabilities are unavailable and an OS-level capture is needed.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/screenshot`
- **Skill file**: `external/openai-skills/skills/.curated/screenshot/SKILL.md`
- **Tags**: `app`, `asks`, `capabilities`, `capture`, `curated`, `desktop`, `explicitly`, `full`, `level`, `needed`, `os-level`, `pixel`, `region`, `screen`, `screenshot`, `unavailable`, `window`

## security-best-practices

Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-best-practices`
- **Skill file**: `external/openai-skills/skills/.curated/security-best-practices/SKILL.md`
- **Tags**: `code`, `coding`, `curated`, `debugging`, `default`, `explicitly`, `framework`, `general`, `guidance`, `improvements`, `javascript`, `language`, `languages`, `non`, `non-security`, `perform`, `practice`, `practices`, `python`, `report`, `requests`, `review`, `reviews`, `secure`, `secure-by-default`, `security`, `security-practices`, `suggest`, `supported`, `trigger`, `typescript`

## security-ownership-map

Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-ownership-map`
- **Skill file**: `external/openai-skills/skills/.curated/security-ownership-map/SKILL.md`
- **Tags**: `analysis`, `analyze`, `build`, `bus`, `bus-factor`, `checks`, `clusters`, `code`, `codeowners`, `compute`, `csv`, `curated`, `databases`, `explicitly`, `export`, `factor`, `general`, `git`, `graph`, `grounded`, `history`, `hotspots`, `lists`, `maintainer`, `maintainers`, `map`, `non`, `non-security`, `oriented`, `orphaned`, `ownership`, `people`, `people-to`, `questions`, `reality`, `repositories`, `risk`, `security`, `security-oriented`, `security-ownership-map`, `sensitive`, `sensitive-code`, `topology`, `trigger`, `visualization`

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

## transcribe

Transcribe audio files to text with optional diarization and known-speaker hints. Use when a user asks to transcribe speech from audio/video, extract text from recordings, or label speakers in interviews or meetings.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/transcribe`
- **Skill file**: `external/openai-skills/skills/.curated/transcribe/SKILL.md`
- **Tags**: `asks`, `audio`, `curated`, `diarization`, `extract`, `hints`, `interviews`, `label`, `meetings`, `optional`, `recordings`, `speaker`, `speakers`, `speech`, `text`, `transcribe`, `video`

## vercel-deploy

Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/vercel-deploy`
- **Skill file**: `external/openai-skills/skills/.curated/vercel-deploy/SKILL.md`
- **Tags**: `actions`, `app`, `applications`, `create`, `curated`, `deploy`, `deployment`, `give`, `like`, `link`, `live`, `preview`, `push`, `requests`, `vercel`, `vercel-deploy`, `websites`

## winui-app

Bootstrap, develop, and design modern WinUI 3 desktop applications with C# and the Windows App SDK using official Microsoft guidance, WinUI Gallery patterns, Windows App SDK samples, and CommunityToolkit components. Use when creating a brand new app, preparing a machine for WinUI, reviewing, refactoring, planning, troubleshooting, environment-checking, or setting up WinUI 3 XAML, controls, navigation, windowing, theming, accessibility, responsiveness, performance, deployment, or related Windows app design and development work.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/winui-app`
- **Skill file**: `external/openai-skills/skills/.curated/winui-app/SKILL.md`
- **Tags**: `accessibility`, `app`, `applications`, `bootstrap`, `brand`, `checking`, `communitytoolkit`, `components`, `controls`, `creating`, `curated`, `deployment`, `design`, `desktop`, `develop`, `development`, `environment`, `environment-checking`, `gallery`, `guidance`, `machine`, `microsoft`, `modern`, `navigation`, `performance`, `planning`, `preparing`, `refactoring`, `responsiveness`, `reviewing`, `samples`, `sdk`, `setting`, `theming`, `troubleshooting`, `windowing`, `windows`, `winui`, `winui-app`, `xaml`

## yeet

Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/yeet`
- **Skill file**: `external/openai-skills/skills/.curated/yeet/SKILL.md`
- **Tags**: `asks`, `cli`, `commit`, `curated`, `explicitly`, `flow`, `github`, `one`, `open`, `pull`, `push`, `request`, `stage`, `yeet`
