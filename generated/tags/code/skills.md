# Tag: code

Skills with tag `code`:

## agent-development

This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/agent-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/agent-development/SKILL.md`
- **Tags**: `asks`, `autonomous`, `code`, `colors`, `conditions`, `create`, `description`, `dev`, `development`, `frontmatter`, `guidance`, `needs`, `practices`, `prompts`, `structure`, `subagent`, `triggering`, `used`

## agentic-actions-auditor

Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor`
- **Skill file**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`
- **Tags**: `actions`, `agentic`, `agentic-actions-auditor`, `allowlists`, `attack`, `attacker`, `attacker-controlled`, `auditing`, `auditor`, `audits`, `cli`, `code`, `codex`, `coding`, `configurations`, `controlled`, `dangerous`, `detects`, `direct`, `env`, `evaluating`, `expression`, `gemini`, `github`, `including`, `inference`, `injection`, `input`, `integrations`, `intermediary`, `invoke`, `pipeline`, `pipelines`, `prompt`, `reaches`, `reviewing`, `risks`, `running`, `sandbox`, `security`, `var`, `vectors`, `vulnerabilities`, `where`, `wildcard`

## algorithmic-art

Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/algorithmic-art`
- **Skill file**: `external/anthropic-skills/skills/algorithmic-art/SKILL.md`
- **Tags**: `algorithmic`, `algorithmic-art`, `art`, `artists`, `avoid`, `code`, `copying`, `copyright`, `create`, `creating`, `existing`, `exploration`, `fields`, `flow`, `generative`, `interactive`, `original`, `parameter`, `particle`, `randomness`, `rather`, `request`, `seeded`, `systems`, `than`, `violations`

## audit-context-building

Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/audit-context-building/skills/audit-context-building`
- **Skill file**: `external/trailofbits-skills/plugins/audit-context-building/skills/audit-context-building/SKILL.md`
- **Tags**: `analysis`, `architectural`, `audit`, `audit-context-building`, `bug`, `build`, `building`, `code`, `context`, `deep`, `enables`, `finding`, `granular`, `line`, `line-by-line`, `ultra`, `ultra-granular`, `vulnerability`

## audit-prep-assistant

Prepares codebases for security review using Trail of Bits' checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation (flowcharts, user stories, inline comments).

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md`
- **Tags**: `accessibility`, `analysis`, `audit`, `audit-prep`, `building`, `building-secure-contracts`, `checklist`, `code`, `codebases`, `comments`, `contracts`, `coverage`, `dead`, `documentation`, `ensures`, `flowcharts`, `generates`, `goals`, `helps`, `increases`, `inline`, `prep`, `prepares`, `removes`, `review`, `runs`, `secure`, `security`, `set`, `static`, `stories`, `test`

## c-review

Performs comprehensive C/C++ security review for memory corruption, integer overflows, race conditions, and platform-specific vulnerabilities. Use when auditing native C/C++ applications, reviewing daemons or services for memory safety, or hunting integer overflow / use-after-free / race conditions in userspace code.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/c-review/skills/c-review`
- **Skill file**: `external/trailofbits-skills/plugins/c-review/skills/c-review/SKILL.md`
- **Tags**: `applications`, `auditing`, `c-review`, `code`, `comprehensive`, `conditions`, `corruption`, `daemons`, `free`, `hunting`, `integer`, `memory`, `native`, `overflow`, `overflows`, `performs`, `platform`, `race`, `review`, `reviewing`, `safety`, `security`, `services`, `userspace`, `vulnerabilities`

## chatgpt-apps

Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold. Prefer a docs-first workflow by invoking the openai-docs skill or OpenAI developer docs MCP tools before generating code.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/chatgpt-apps`
- **Skill file**: `external/openai-skills/skills/.curated/chatgpt-apps/SKILL.md`
- **Tags**: `aligned`, `apis`, `applications`, `apply`, `apps`, `bridge`, `build`, `chatgpt`, `chatgpt-apps`, `code`, `codex`, `combine`, `compatibility`, `csp`, `curated`, `design`, `developer`, `docs`, `docs-aligned`, `domain`, `generating`, `invoking`, `mcp`, `metadata`, `needs`, `prefer`, `produce`, `project`, `refactor`, `register`, `scaffold`, `sdk`, `server`, `settings`, `troubleshoot`, `widget`, `wire`

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

## code-maturity-assessor

Systematic code maturity assessment using Trail of Bits' 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level code, and testing. Produces professional scorecard with evidence-based ratings and actionable recommendations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/code-maturity-assessor`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/code-maturity-assessor/SKILL.md`
- **Tags**: `access`, `actionable`, `analyzes`, `arithmetic`, `assessment`, `assessor`, `auditing`, `building`, `building-secure-contracts`, `category`, `code`, `code-maturity-assessor`, `codebase`, `complexity`, `contracts`, `controls`, `decentralization`, `documentation`, `evidence`, `framework`, `level`, `low`, `low-level`, `maturity`, `mev`, `practices`, `produces`, `professional`, `ratings`, `recommendations`, `risks`, `safety`, `scorecard`, `secure`, `systematic`, `testing`

## code-review

Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/code-review`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/code-review/SKILL.md`
- **Tags**: `cases`, `change`, `changes`, `checking`, `code`, `code-review`, `correctness`, `diff`, `edge`, `engineering`, `error`, `gaps`, `handling`, `injection`, `merge`, `missing`, `performance`, `queries`, `review`, `risks`, `safe`, `security`, `trigger`, `url`

## command-development

This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in commands, user interaction patterns, or command development best practices for Claude Code.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/command-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/command-development/SKILL.md`
- **Tags**: `arguments`, `asks`, `askuserquestion`, `bash`, `code`, `command`, `command-development`, `commands`, `create`, `custom`, `define`, `dev`, `development`, `dynamic`, `execution`, `fields`, `frontmatter`, `guidance`, `interaction`, `interactive`, `needs`, `organize`, `practices`, `slash`, `structure`, `used`, `yaml`

## constant-time-analysis

Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or Ruby.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md`
- **Tags**: `analysis`, `branches`, `channel`, `code`, `constant`, `constant-time`, `constant-time-analysis`, `crypto`, `cryptographic`, `dependent`, `detects`, `division`, `encountering`, `implementing`, `java`, `javascript`, `kotlin`, `php`, `programming`, `python`, `questions`, `reviewing`, `ruby`, `rust`, `secret`, `secret-dependent`, `secrets`, `side`, `side-channel`, `swift`, `time`, `timing`, `typescript`, `vulnerabilities`

## crypto-protocol-diagram

Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow, extracting message flow from a spec or RFC, diagramming a ProVerif or Tamarin model, or drawing sequence diagrams for TLS, Noise, Signal, X3DH, Double Ratchet, FROST, DH, or ECDH protocols.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram/SKILL.md`
- **Tags**: `academic`, `annotations`, `code`, `crypto`, `crypto-protocol-diagram`, `cryptographic`, `diagram`, `diagramming`, `diagrams`, `double`, `drawing`, `ecdh`, `exchange`, `extracting`, `extracts`, `flow`, `frost`, `generates`, `handshake`, `informal`, `key`, `mermaid`, `message`, `model`, `models`, `noise`, `papers`, `prose`, `protocol`, `protocols`, `proverif`, `pseudocode`, `ratchet`, `rfc`, `rfcs`, `sequence`, `sequencediagrams`, `signal`, `spec`, `spthy`, `tamarin`, `tls`, `trailmark`, `visualizing`, `x3dh`

## devcontainer-setup

Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configuring sandboxed Claude Code workspaces.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/devcontainer-setup/skills/devcontainer-setup`
- **Skill file**: `external/trailofbits-skills/plugins/devcontainer-setup/skills/devcontainer-setup/SKILL.md`
- **Tags**: `adding`, `code`, `configuring`, `creates`, `devcontainer`, `devcontainers`, `development`, `environments`, `isolated`, `language`, `node`, `persistent`, `project`, `python`, `rust`, `sandboxed`, `setting`, `support`, `tooling`, `volumes`, `workspaces`

## diagramming-code

>

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/diagramming-code`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/diagramming-code/SKILL.md`
- **Tags**: `code`, `diagramming`, `diagramming-code`, `trailmark`

## dimensional-analysis

Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol, offchain code, or other blockchain-related codebase with arithmetic. Prevents dimensional mismatches and catches formula bugs early.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis/SKILL.md`
- **Tags**: `analysis`, `annotate`, `annotates`, `arithmetic`, `asks`, `blockchain`, `bugs`, `catches`, `code`, `codebase`, `codebases`, `comments`, `decimal`, `defi`, `dimensional`, `dimensional-analysis`, `dimensions`, `documenting`, `early`, `find`, `formula`, `mismatches`, `offchain`, `other`, `perform`, `prevents`, `protocol`, `scaling`, `someone`, `units`, `vulnerabilities`

## dwarf-expert

Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). Triggers when understanding DWARF information, interacting with DWARF files, answering DWARF-related questions, or working with code that parses DWARF data.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/dwarf-expert/skills/dwarf-expert`
- **Skill file**: `external/trailofbits-skills/plugins/dwarf-expert/skills/dwarf-expert/SKILL.md`
- **Tags**: `analyzing`, `answering`, `code`, `data`, `debug`, `dwarf`, `dwarf-expert`, `expert`, `expertise`, `format`, `information`, `interacting`, `parses`, `provides`, `questions`, `standard`, `triggers`, `understanding`, `v3-v5`, `working`

## example-skill

This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or discusses skill development patterns. Provides a reference template for creating Claude Code plugin skills.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/example-plugin/skills/example-skill`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/example-plugin/skills/example-skill/SKILL.md`
- **Tags**: `asks`, `code`, `create`, `creating`, `demonstrate`, `development`, `discusses`, `format`, `provides`, `show`, `used`

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

## hook-development

This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development/SKILL.md`
- **Tags**: `advanced`, `api`, `asks`, `automation`, `block`, `code`, `commands`, `comprehensive`, `create`, `creating`, `dangerous`, `dev`, `development`, `driven`, `event`, `event-driven`, `events`, `focus`, `guidance`, `hook`, `hook-development`, `hooks`, `implement`, `implementing`, `mentions`, `notification`, `posttooluse`, `precompact`, `pretooluse`, `prompt`, `provides`, `root`, `sessionend`, `sessionstart`, `set`, `stop`, `subagentstop`, `used`, `userpromptsubmit`, `validate`

## imagegen

Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.system/imagegen`
- **Skill file**: `external/openai-skills/skills/.system/imagegen/SKILL.md`
- **Tags**: `ai-created`, `asset`, `assets`, `background`, `benefits`, `better`, `bitmap`, `brand`, `building`, `canvas`, `code`, `code-native`, `codex`, `create`, `created`, `css`, `cutouts`, `derive`, `directly`, `edit`, `editing`, `established`, `existing`, `extending`, `handled`, `html`, `icon`, `illustrations`, `image`, `imagegen`, `images`, `logo`, `mockups`, `native`, `photos`, `raster`, `rather`, `repo`, `repo-native`, `sprites`, `such`, `svg`, `textures`, `than`, `transform`, `transparent`, `transparent-background`, `variants`, `vector`, `visual`, `visuals`

## instrument-data-to-allotrope

Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md`
- **Tags**: `allotrope`, `analysis`, `asm`, `auto`, `auto-detection`, `bio`, `bio-research`, `code`, `convert`, `converting`, `csv`, `data`, `detection`, `downstream`, `easy`, `eln`, `engineers`, `excel`, `exportable`, `flattened`, `format`, `full`, `generating`, `import`, `include`, `instrument`, `instrument-data-to-allotrope`, `lab`, `laboratory`, `lakes`, `lims`, `model`, `outputs`, `parser`, `pdf`, `pipelines`, `preparing`, `production`, `python`, `research`, `scientists`, `simple`, `standardize`, `standardizing`, `supports`, `systems`, `triggers`, `txt`, `types`, `upload`

## mcp-integration

This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration/SKILL.md`
- **Tags**: `asks`, `code`, `comprehensive`, `configure`, `connect`, `context`, `dev`, `discusses`, `guidance`, `http`, `integrate`, `integrating`, `integration`, `mcp`, `mcp-integration`, `mentions`, `model`, `protocol`, `provides`, `root`, `server`, `servers`, `service`, `set`, `sse`, `stdio`, `types`, `used`, `websocket`

## plugin-structure

This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure/SKILL.md`
- **Tags**: `architecture`, `asks`, `auto`, `auto-discovery`, `code`, `commands`, `component`, `components`, `configuration`, `configure`, `conventions`, `create`, `dev`, `directory`, `discovery`, `guidance`, `hooks`, `layout`, `manifest`, `naming`, `needs`, `organization`, `organize`, `practices`, `root`, `scaffold`, `set`, `structure`, `understand`, `used`

## property-based-testing

Provides guidance for property-based testing across multiple languages and smart contracts. Use when writing tests, reviewing code with serialization/validation/parsing patterns, designing features, or when property-based testing would provide stronger coverage than example-based tests.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/property-based-testing/skills/property-based-testing`
- **Skill file**: `external/trailofbits-skills/plugins/property-based-testing/skills/property-based-testing/SKILL.md`
- **Tags**: `code`, `contracts`, `coverage`, `designing`, `features`, `guidance`, `languages`, `multiple`, `parsing`, `property`, `property-testing`, `provide`, `provides`, `reviewing`, `serialization`, `smart`, `stronger`, `testing`, `tests`, `than`, `validation`, `would`

## scv-scan

Audits Solidity codebases for smart contract vulnerabilities using a four-phase workflow (cheatsheet loading, codebase sweep, deep validation, reporting) covering 36 vulnerability classes. Use when auditing Solidity contracts for security issues, performing smart contract vulnerability scans, or reviewing Solidity code for common exploit patterns.

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/scv-scan/skills/scv-scan`
- **Skill file**: `external/trailofbits-skills-curated/plugins/scv-scan/skills/scv-scan/SKILL.md`
- **Tags**: `auditing`, `audits`, `cheatsheet`, `classes`, `code`, `codebase`, `codebases`, `contract`, `contracts`, `covering`, `deep`, `exploit`, `four`, `four-phase`, `issues`, `loading`, `performing`, `phase`, `reporting`, `reviewing`, `scan`, `scans`, `scv`, `scv-scan`, `security`, `smart`, `solidity`, `sweep`, `validation`, `vulnerabilities`, `vulnerability`

## second-opinion

Runs external LLM code reviews (OpenAI Codex or Google Gemini CLI) on uncommitted changes, branch diffs, or specific commits. Use when the user asks for a second opinion, external review, codex review, gemini review, or mentions /second-opinion.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion`
- **Skill file**: `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion/SKILL.md`
- **Tags**: `asks`, `branch`, `changes`, `cli`, `code`, `codex`, `commits`, `diffs`, `gemini`, `google`, `llm`, `mentions`, `opinion`, `review`, `reviews`, `runs`, `second`, `second-opinion`, `uncommitted`

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

## semgrep-rule-creator

Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/semgrep-rule-creator/skills/semgrep-rule-creator`
- **Skill file**: `external/trailofbits-skills/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md`
- **Tags**: `analysis`, `bug`, `building`, `code`, `creates`, `creator`, `custom`, `detecting`, `detections`, `rule`, `security`, `semgrep`, `semgrep-rule-creator`, `static`, `vulnerabilities`

## session-report

Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/session-report/skills/session-report`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/session-report/skills/session-report/SKILL.md`
- **Tags**: `cache`, `code`, `expensive`, `explorable`, `html`, `projects`, `prompts`, `report`, `session`, `session-report`, `subagents`, `tokens`, `transcripts`

## sharp-edges

Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges`
- **Skill file**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges/SKILL.md`
- **Tags**: `api`, `apis`, `code`, `configuration`, `configurations`, `cryptographic`, `dangerous`, `default`, `defaults`, `designs`, `edges`, `enable`, `ergonomics`, `error`, `error-prone`, `evaluating`, `follows`, `footgun`, `identifies`, `library`, `mistakes`, `misuse`, `misuse-resistant`, `pit`, `principles`, `prone`, `resistant`, `reviewing`, `schemas`, `secure`, `security`, `sharp`, `sharp-edges`, `success`, `triggers`, `usability`, `whether`

## skill-development

This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/skill-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/skill-development/SKILL.md`
- **Tags**: `code`, `content`, `create`, `description`, `dev`, `development`, `disclosure`, `guidance`, `improve`, `needs`, `organize`, `practices`, `progressive`, `structure`, `used`

## skill-improver

Iteratively reviews and fixes Claude Code skill quality issues until they meet standards. Runs automated fix-review cycles using the skill-reviewer agent. Use to fix skill quality issues, improve skill descriptions, run automated skill review loops, or iteratively refine a skill. Triggers on 'fix my skill', 'improve skill quality', 'skill improvement loop'. NOT for one-time reviews—use /skill-reviewer directly.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/skill-improver/skills/skill-improver`
- **Skill file**: `external/trailofbits-skills/plugins/skill-improver/skills/skill-improver/SKILL.md`
- **Tags**: `automated`, `code`, `cycles`, `descriptions`, `directly`, `fix`, `fix-review`, `fixes`, `improve`, `improvement`, `improver`, `issues`, `iteratively`, `loop`, `loops`, `meet`, `one`, `one-time`, `quality`, `refine`, `review`, `reviewer`, `reviews`, `runs`, `standards`, `they`, `time`, `triggers`, `until`

## spec-to-code-compliance

Verifies code implements exactly what documentation specifies for blockchain audits. Use when comparing code against whitepapers, finding gaps between specs and implementation, or performing compliance checks for protocol implementations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/spec-to-code-compliance/skills/spec-to-code-compliance`
- **Skill file**: `external/trailofbits-skills/plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md`
- **Tags**: `against`, `audits`, `between`, `blockchain`, `checks`, `code`, `comparing`, `compliance`, `documentation`, `exactly`, `finding`, `gaps`, `implementation`, `implementations`, `implements`, `performing`, `protocol`, `spec`, `spec-to-code-compliance`, `specifies`, `specs`, `verifies`, `whitepapers`

## tech-debt

Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or when the user asks about code quality, refactoring priorities, or maintenance backlog.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/tech-debt`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/tech-debt/SKILL.md`
- **Tags**: `asks`, `audit`, `backlog`, `categorize`, `code`, `debt`, `engineering`, `health`, `identify`, `maintenance`, `priorities`, `prioritize`, `quality`, `refactor`, `refactoring`, `tech`, `tech-debt`, `technical`, `trigger`

## trailmark

Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`
- **Tags**: `analysis`, `analyzing`, `attack`, `audit`, `auto`, `blast`, `boundaries`, `building`, `builds`, `call`, `code`, `complexity`, `detect`, `detect-languages`, `entry`, `enumerating`, `enumeration`, `finding`, `graph`, `graphs`, `hotspots`, `includes`, `language`, `languages`, `mapping`, `measuring`, `multi`, `multi-language`, `parse`, `passes`, `paths`, `point`, `points`, `polyglot`, `pre`, `pre-analysis`, `prefer`, `prioritization`, `privilege`, `propagation`, `queries`, `radius`, `security`, `surface`, `taint`, `target`, `tracing`, `trailmark`, `unknown`

## trailmark-summary

Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary/SKILL.md`
- **Tags**: `analysis`, `auto`, `auto-detected`, `code`, `codebase`, `count`, `dependency`, `detected`, `entry`, `galvanize`, `languages`, `needs`, `point`, `returns`, `runs`, `structural`, `summary`, `trailmark`, `trailmark-summary`, `triggers`, `vivisect`

## variant-analysis

Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audits after finding an initial issue.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis/SKILL.md`
- **Tags**: `analysis`, `analyzing`, `audits`, `bug`, `bugs`, `building`, `code`, `codebases`, `codeql`, `find`, `finding`, `hunting`, `initial`, `issue`, `performing`, `queries`, `security`, `semgrep`, `similar`, `systematic`, `variant`, `variant-analysis`, `variants`, `vulnerabilities`

## vector-forge

Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`
- **Tags**: `algorithm`, `code`, `compares`, `coverage`, `creating`, `cross`, `cross-implementation`, `crypto`, `cryptographic`, `deliberately`, `driven`, `effectiveness`, `escaped`, `exercise`, `finding`, `finds`, `forge`, `gaps`, `generates`, `generating`, `generation`, `identify`, `implementation`, `implementations`, `improving`, `kill`, `measuring`, `mutants`, `mutation`, `mutation-driven`, `paths`, `primitives`, `protocol`, `prove`, `rates`, `runs`, `suites`, `test`, `testing`, `then`, `trailmark`, `uncovered`, `vector`, `vector-forge`, `vectors`, `wycheproof`

## zeroize-audit

Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling secrets, keys, passwords, or other sensitive data.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/zeroize-audit/skills/zeroize-audit`
- **Skill file**: `external/trailofbits-skills/plugins/zeroize-audit/skills/zeroize-audit/SKILL.md`
- **Tags**: `analysis`, `assembly`, `assembly-level`, `audit`, `auditing`, `code`, `compiler`, `control`, `control-flow`, `data`, `detects`, `flow`, `handling`, `identifies`, `keys`, `level`, `missing`, `optimizations`, `other`, `passwords`, `removed`, `rust`, `secrets`, `sensitive`, `verification`, `zeroization`, `zeroize`, `zeroize-audit`
