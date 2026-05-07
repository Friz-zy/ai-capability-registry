# Skill Catalog

Total: 421 skills across 23 categories

## Ai Ml

### claude-in-chrome-troubleshooting
Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratically.

**Tags:** `behave`, `browser`, `chrome`, `connected`, `connectivity`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/claude-in-chrome-troubleshooting/skills/claude-in-chrome-troubleshooting/SKILL.md`

### hatch-pet
Create, repair, validate, preview, and package Codex-compatible animated pets and pet spritesheets from character art, screenshots, generated images, or visual references. Use when a user wants to hatch a Codex pet, create a custom animated pet, or build a built-in pet asset with an 8x9 atlas, transparent unused cells, row-by-row animation prompts, QA contact sheets, preview videos, and pet.json packaging. This skill composes the installed $imagegen system skill for visual generation and uses bundled scripts for deterministic spritesheet assembly.

**Tags:** `8x9`, `animated`, `animation`, `art`, `assembly`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/hatch-pet/SKILL.md`

### mcp-builder
>-

**Tags:** `builder`, `mcp`, `mcp-builder`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/mcp-builder/SKILL.md`

### migrate-to-codex
Migrate supported instruction files, skills, agents, and MCP config into Codex project and global files.

**Tags:** `codex`, `config`, `curated`, `global`, `instruction`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/migrate-to-codex/SKILL.md`

### source-management
Manages connected MCP sources for enterprise search. Detects available sources, guides users to connect new ones, handles source priority ordering, and manages rate limiting awareness.

**Tags:** `awareness`, `connect`, `connected`, `detects`, `enterprise`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/source-management/SKILL.md`

### transcribe
Transcribe audio files to text with optional diarization and known-speaker hints. Use when a user asks to transcribe speech from audio/video, extract text from recordings, or label speakers in interviews or meetings.

**Tags:** `asks`, `audio`, `curated`, `diarization`, `extract`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/transcribe/SKILL.md`

### zoom-mcp/whiteboard
|

**Tags:** `mcp`, `partner`, `whiteboard`, `zoom`, `zoom-mcp`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-mcp/whiteboard/SKILL.md`

## Backend

### build-mcp-app
This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

**Tags:** `already`, `app`, `apps`, `build`, `build-mcp-app`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`

### build-mcpb
This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up.

**Tags:** `apps`, `build`, `build-mcpb`, `bundle`, `bundling`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb/SKILL.md`

### build-zoom-bot
Build a Zoom meeting bot, recorder, or real-time media workflow. Use when joining meetings programmatically, processing live media or transcripts, or combining Meeting SDK, RTMS, and backend services.

**Tags:** `backend`, `bot`, `build`, `build-zoom-bot`, `combining`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-bot/SKILL.md`

### contact-center/android
Zoom Contact Center SDK for Android. Use for native Android chat/video/ZVA/scheduled callback integrations, campaign mode, service lifecycle, and rejoin handling.

**Tags:** `android`, `callback`, `campaign`, `center`, `chat`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/android/SKILL.md`

### create-viz
Create publication-quality visualizations with Python. Use when turning query results or a DataFrame into a chart, selecting the right chart type for a trend or comparison, generating a plot for a report or presentation, or needing an interactive chart with hover and zoom.

**Tags:** `chart`, `comparison`, `create`, `create-viz`, `data`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/create-viz/SKILL.md`

### data-visualization
Create effective data visualizations with Python (matplotlib, seaborn, plotly). Use when building charts, choosing the right chart type for a dataset, creating publication-quality figures, or applying design principles like accessibility and color theory.

**Tags:** `accessibility`, `applying`, `building`, `chart`, `charts`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/data-visualization/SKILL.md`

### kb-article
Draft a knowledge base article from a resolved issue or common question. Use when a ticket resolution is worth documenting for self-service, the same question keeps coming up, a workaround needs to be published, or a known issue should be communicated to customers.

**Tags:** `article`, `base`, `coming`, `communicated`, `customer`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/customer-support/skills/kb-article/SKILL.md`

### mcp-builder
Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

**Tags:** `apis`, `builder`, `building`, `context`, `creating`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/mcp-builder/SKILL.md`

### meeting-sdk/linux
Zoom Meeting SDK for Linux - C++ headless meeting bots with raw audio/video access, transcription, recording, and AI integration for server-side automation

**Tags:** `access`, `audio`, `automation`, `bots`, `headless`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/linux/SKILL.md`

### migrating-dbt-project-across-platforms
Use when migrating a dbt project from one data platform or data warehouse to another (e.g., Snowflake to Databricks, Databricks to Snowflake) using dbt Fusion's real-time compilation to identify and fix SQL dialect differences.

**Tags:** `another`, `compilation`, `data`, `databricks`, `dbt`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt-migration/skills/migrating-dbt-project-across-platforms/SKILL.md`

### modern-python
Configures Python projects with modern tooling (uv, ruff, ty). Use when creating projects, writing standalone scripts, or migrating from pip/Poetry/mypy/black.

**Tags:** `black`, `configures`, `creating`, `migrating`, `modern`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/modern-python/skills/modern-python/SKILL.md`

### pdf
Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction.

**Tags:** `checks`, `creating`, `curated`, `extraction`, `generation`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/pdf/SKILL.md`

### sql-queries
Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, PostgreSQL, etc.). Use when writing queries, optimizing slow SQL, translating between dialects, or building complex analytical queries with CTEs, window functions, or aggregations.

**Tags:** `aggregations`, `analytical`, `between`, `bigquery`, `building`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/sql-queries/SKILL.md`

### validate-data
QA an analysis before sharing -- methodology, accuracy, and bias checks. Use when reviewing an analysis before a stakeholder presentation, spot-checking calculations and aggregation logic, verifying a SQL query's results look right, or assessing whether conclusions are actually supported by the data.

**Tags:** `accuracy`, `actually`, `aggregation`, `analysis`, `assessing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/validate-data/SKILL.md`

### video-sdk/web
Zoom Video SDK for Web - JavaScript/TypeScript integration for browser-based video sessions, real-time communication, screen sharing, recording, and live transcription

**Tags:** `browser`, `communication`, `integration`, `javascript`, `live`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/web/SKILL.md`

### virtual-agent/android
Zoom Virtual Agent Android integration via WebView. Use for Java/Kotlin bridge callbacks, native URL handling, support_handoff relay, and lifecycle-safe embedding.

**Tags:** `android`, `bridge`, `callbacks`, `embedding`, `handling`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/android/SKILL.md`

### write-query
Write optimized SQL for your dialect with best practices. Use when translating a natural-language data need into SQL, building a multi-CTE query with joins and aggregations, optimizing a query against a large partitioned table, or getting dialect-specific syntax for Snowflake, BigQuery, Postgres, etc.

**Tags:** `against`, `aggregations`, `bigquery`, `building`, `cte`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/write-query/SKILL.md`

## Core

### accessibility-review
Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "is this accessible?", or when reviewing a design for color contrast, keyboard navigation, touch target size, or screen reader behavior before handoff.

**Tags:** `a11y`, `accessibility`, `accessibility-review`, `accessible`, `audit`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/accessibility-review/SKILL.md`

### adding-dbt-unit-test
Creates unit test YAML definitions that mock upstream model inputs and validate expected outputs. Use when adding unit tests for a dbt model or practicing test-driven development (TDD) in dbt.

**Tags:** `adding`, `adding-dbt-unit-test`, `creates`, `dbt`, `definitions`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/adding-dbt-unit-test/SKILL.md`

### address-sanitizer
>

**Tags:** `address`, `address-sanitizer`, `handbook`, `sanitizer`, `testing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/address-sanitizer/SKILL.md`

### aflpp
>

**Tags:** `aflpp`, `handbook`, `testing`, `testing-handbook`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/aflpp/SKILL.md`

### agent-development
This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins.

**Tags:** `asks`, `autonomous`, `code`, `colors`, `conditions`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/agent-development/SKILL.md`

### agent-md-refactor
>-

**Tags:** `md-refactor`, `refactor`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/agent-md-refactor/SKILL.md`

### agentic-actions-auditor
Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

**Tags:** `actions`, `agentic`, `agentic-actions-auditor`, `allowlists`, `attack`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`

### algorithmic-art
Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.

**Tags:** `algorithmic`, `algorithmic-art`, `art`, `artists`, `avoid`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/algorithmic-art/SKILL.md`

### angular-testing
>-

**Tags:** `angular`, `angular-testing`, `testing`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/angular-testing/SKILL.md`

### answering-natural-language-questions-with-dbt
Writes and executes SQL queries against the data warehouse using dbt's Semantic Layer or ad-hoc SQL to answer business questions. Use when a user asks about analytics, metrics, KPIs, or data (e.g., "What were total sales last quarter?", "Show me top customers by revenue"). NOT for validating, testing, or building dbt models during development.

**Tags:** `ad-hoc`, `against`, `analytics`, `answer`, `answering`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/answering-natural-language-questions-with-dbt/SKILL.md`

### architecture
Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decision with trade-offs and consequences, reviewing a system design proposal, or designing a new component from requirements and constraints.

**Tags:** `adr`, `architecture`, `between`, `choosing`, `component`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/architecture/SKILL.md`

### aspnet-core
Build, review, refactor, or architect ASP.NET Core web applications using current official guidance for .NET web development. Use when working on Blazor Web Apps, Razor Pages, MVC, Minimal APIs, controller-based Web APIs, SignalR, gRPC, middleware, dependency injection, configuration, authentication, authorization, testing, performance, deployment, or ASP.NET Core upgrades.

**Tags:** `apis`, `applications`, `apps`, `architect`, `asp`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/aspnet-core/SKILL.md`

### atheris
>

**Tags:** `atheris`, `handbook`, `testing`, `testing-handbook`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/atheris/SKILL.md`

### audit-context-building
Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding.

**Tags:** `analysis`, `architectural`, `audit`, `audit-context-building`, `bug`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/audit-context-building/skills/audit-context-building/SKILL.md`

### audit-prep-assistant
Prepares codebases for security review using Trail of Bits' checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation (flowcharts, user stories, inline comments).

**Tags:** `accessibility`, `analysis`, `audit`, `audit-prep`, `building`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md`

### audit-support
Support SOX 404 compliance with control testing methodology, sample selection, and documentation standards. Use when generating testing workpapers, selecting audit samples, classifying control deficiencies, or preparing for internal or external audits.

**Tags:** `audit`, `audit-support`, `audits`, `classifying`, `compliance`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/audit-support/SKILL.md`

### brand-review
Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixes. Use when checking a draft before it ships, when auditing copy for voice consistency and terminology, or when screening for unsubstantiated claims, missing disclaimers, and other legal flags.

**Tags:** `against`, `auditing`, `brand`, `brand-review`, `checking`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/brand-review/SKILL.md`

### build-zoom-rest-api-app
Reference skill for Zoom REST API. Use after choosing an API-based workflow when you need endpoint selection, resource-management patterns, OAuth requirements, rate-limit awareness, or API error debugging.

**Tags:** `api`, `app`, `awareness`, `build`, `build-zoom-rest-api-app`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rest-api/SKILL.md`

### c-review
Performs comprehensive C/C++ security review for memory corruption, integer overflows, race conditions, and platform-specific vulnerabilities. Use when auditing native C/C++ applications, reviewing daemons or services for memory safety, or hunting integer overflow / use-after-free / race conditions in userspace code.

**Tags:** `applications`, `auditing`, `c-review`, `code`, `comprehensive`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/c-review/skills/c-review/SKILL.md`

### campaign-plan
Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics. Use when planning a product launch, lead-gen push, or awareness campaign, when you need a week-by-week content calendar with dependencies, or when translating a marketing goal into a structured, executable plan.

**Tags:** `audience`, `awareness`, `brief`, `calendar`, `campaign`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/campaign-plan/SKILL.md`

### capacity-plan
Plan resource capacity — workload analysis and utilization forecasting. Use when heading into quarterly planning, the team feels overallocated and you need the numbers, deciding whether to hire or deprioritize, or stress-testing whether upcoming projects fit the people you have.

**Tags:** `analysis`, `capacity`, `capacity-plan`, `deciding`, `deprioritize`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/capacity-plan/SKILL.md`

### cargo-fuzz
>

**Tags:** `cargo`, `cargo-fuzz`, `fuzz`, `handbook`, `testing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/cargo-fuzz/SKILL.md`

### change-request
Create a change management request with impact analysis and rollback plan. Use when proposing a system or process change that needs approval, preparing a change record for CAB review, documenting risk and rollback steps before a deployment, or planning stakeholder communications for a rollout.

**Tags:** `analysis`, `approval`, `cab`, `change`, `change-request`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/change-request/SKILL.md`

### chatgpt-apps
Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold. Prefer a docs-first workflow by invoking the openai-docs skill or OpenAI developer docs MCP tools before generating code.

**Tags:** `aligned`, `apis`, `applications`, `apply`, `apps`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/chatgpt-apps/SKILL.md`

### choose-zoom-approach
Choose the right Zoom architecture for a use case. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zoom MCP, Phone, Contact Center, or a hybrid approach.

**Tags:** `api`, `approach`, `apps`, `architecture`, `between`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/choose-zoom-approach/SKILL.md`

### claude-api
Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

**Tags:** `adds`, `api`, `apps`, `asks`, `batch`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/claude-api/SKILL.md`

### claude-automation-recommender
Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.

**Tags:** `analyze`, `asks`, `automation`, `automation-recommender`, `automations`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`

### close-management
Manage the month-end close process with task sequencing, dependencies, and status tracking. Use when planning the close calendar, tracking close progress, identifying blockers, or sequencing close activities by day.

**Tags:** `activities`, `blockers`, `calendar`, `close`, `close-management`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/close-management/SKILL.md`

### code-maturity-assessor
Systematic code maturity assessment using Trail of Bits' 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level code, and testing. Produces professional scorecard with evidence-based ratings and actionable recommendations.

**Tags:** `access`, `actionable`, `analyzes`, `arithmetic`, `assessment`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/code-maturity-assessor/SKILL.md`

### code-review
Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.

**Tags:** `cases`, `change`, `changes`, `checking`, `code`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/code-review/SKILL.md`

### command-development
This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in commands, user interaction patterns, or command development best practices for Claude Code.

**Tags:** `arguments`, `asks`, `askuserquestion`, `bash`, `code`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/command-development/SKILL.md`

### competitive-brief
Create a competitive analysis brief for one or more competitors or a feature area. Use when informing product strategy or feature prioritization, building sales battle cards, prepping board or investor materials, or deciding where to differentiate vs. achieve parity.

**Tags:** `achieve`, `analysis`, `area`, `battle`, `board`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/competitive-brief/SKILL.md`

### configure
Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord bot token, asks to configure Discord, asks "how do I set this up" or "who can reach me," or wants to check channel status.

**Tags:** `access`, `asks`, `bot`, `can`, `channel`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/external_plugins/discord/skills/configure/SKILL.md`

### configure
Check iMessage channel setup and review access policy. Use when the user asks to configure iMessage, asks "how do I set this up" or "who can reach me," or wants to know why texts aren't reaching the assistant.

**Tags:** `access`, `aren`, `asks`, `can`, `channel`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/external_plugins/imessage/skills/configure/SKILL.md`

### configure
Set up the Telegram channel — save the bot token and review access policy. Use when the user pastes a Telegram bot token, asks to configure Telegram, asks "how do I set this up" or "who can reach me," or wants to check channel status.

**Tags:** `access`, `asks`, `bot`, `can`, `channel`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/external_plugins/telegram/skills/configure/SKILL.md`

### configuring-dbt-mcp-server
Generates MCP server configuration JSON, resolves authentication setup, and validates server connectivity for dbt. Use when setting up, configuring, or troubleshooting the dbt MCP server for AI tools like Kilo, Cursor, VS Code, or Claude Desktop.

**Tags:** `authentication`, `code`, `configuration`, `configuring`, `configuring-dbt-mcp-server`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/configuring-dbt-mcp-server/SKILL.md`

### constant-time-analysis
Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or Ruby.

**Tags:** `analysis`, `branches`, `channel`, `code`, `constant`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md`

### constant-time-testing
>

**Tags:** `constant`, `constant-time-testing`, `handbook`, `testing`, `testing-handbook`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/constant-time-testing/SKILL.md`

### coverage-analysis
>

**Tags:** `analysis`, `coverage`, `coverage-analysis`, `handbook`, `testing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/coverage-analysis/SKILL.md`

### crypto-protocol-diagram
Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow, extracting message flow from a spec or RFC, diagramming a ProVerif or Tamarin model, or drawing sequence diagrams for TLS, Noise, Signal, X3DH, Double Ratchet, FROST, DH, or ECDH protocols.

**Tags:** `academic`, `annotations`, `code`, `crypto`, `crypto-protocol-diagram`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram/SKILL.md`

### debug
Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected and the cause isn't obvious.

**Tags:** `behavior`, `broke`, `but`, `cause`, `debug`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/debug/SKILL.md`

### debug-buttercup
>

**Tags:** `buttercup`, `debug`, `debug-buttercup`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/debug-buttercup/skills/debug-buttercup/SKILL.md`

### debug-zoom
Debug a broken Zoom integration by isolating the failure point and routing into the right Zoom references. Use when auth, API, webhook, SDK, or MCP behavior is failing and you need a ranked hypothesis list plus verification steps.

**Tags:** `api`, `auth`, `behavior`, `broken`, `debug`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom/SKILL.md`

### debug-zoom-integration
Debug broken Zoom implementations quickly. Use when auth, webhooks, SDK joins, MCP transport, or real-time media workflows are failing and you need to isolate the layer before proposing a fix.

**Tags:** `auth`, `broken`, `debug`, `debug-zoom-integration`, `failing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom-integration/SKILL.md`

### design-critique
Get structured design feedback on usability, hierarchy, and consistency. Trigger with "review this design", "critique this mockup", "what do you think of this screen?", or when sharing a Figma link or screenshot for feedback at any stage from exploration to final polish.

**Tags:** `consistency`, `critique`, `design`, `design-critique`, `exploration`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/design-critique/SKILL.md`

### design-mcp-workflow
Design a Zoom MCP workflow for Claude. Use when deciding whether Zoom MCP fits a task, when planning tool-based AI workflows, or when separating MCP responsibilities from REST API responsibilities.

**Tags:** `api`, `deciding`, `design`, `design-mcp`, `fits`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/design-mcp-workflow/SKILL.md`

### design-system
Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded values across components, writing documentation for a component's variants, states, and accessibility notes, or designing a new pattern that fits the existing system.

**Tags:** `accessibility`, `audit`, `checking`, `component`, `components`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/design-system/SKILL.md`

### devcontainer-setup
Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configuring sandboxed Claude Code workspaces.

**Tags:** `adding`, `code`, `configuring`, `creates`, `devcontainer`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/devcontainer-setup/skills/devcontainer-setup/SKILL.md`

### diagramming-code
>

**Tags:** `code`, `diagramming`, `diagramming-code`, `trailmark`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/diagramming-code/SKILL.md`

### differential-review
>

**Tags:** `differential`, `differential-review`, `review`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/differential-review/skills/differential-review/SKILL.md`

### dimensional-analysis
Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol, offchain code, or other blockchain-related codebase with arithmetic. Prevents dimensional mismatches and catches formula bugs early.

**Tags:** `analysis`, `annotate`, `annotates`, `arithmetic`, `asks`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis/SKILL.md`

### doc-coauthoring
Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

**Tags:** `authoring`, `co-authoring`, `coauthoring`, `content`, `context`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/doc-coauthoring/SKILL.md`

### documentation
Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README", "write a runbook", "onboarding guide", or when the user needs help with any form of technical writing — API docs, architecture docs, or operational runbooks.

**Tags:** `api`, `architecture`, `create`, `docs`, `document`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/documentation/SKILL.md`

### dwarf-expert
Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). Triggers when understanding DWARF information, interacting with DWARF files, answering DWARF-related questions, or working with code that parses DWARF data.

**Tags:** `analyzing`, `answering`, `code`, `data`, `debug`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/dwarf-expert/skills/dwarf-expert/SKILL.md`

### example-skill
This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or discusses skill development patterns. Provides a reference template for creating Claude Code plugin skills.

**Tags:** `asks`, `code`, `create`, `creating`, `demonstrate`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/example-plugin/skills/example-skill/SKILL.md`

### fetching-dbt-docs
Retrieves and searches dbt documentation pages in LLM-friendly markdown format. Use when fetching dbt documentation, looking up dbt features, or answering questions about dbt Cloud, dbt Core, or the dbt Semantic Layer.

**Tags:** `answering`, `cloud`, `core`, `dbt`, `docs`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/fetching-dbt-docs/SKILL.md`

### figma
Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma nodes into production code. Trigger when a task involves Figma URLs, node IDs, design-to-code implementation, or Figma MCP setup and troubleshooting.

**Tags:** `assets`, `code`, `context`, `curated`, `design`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma/SKILL.md`

### figma-code-connect-components
Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code connect", "connect this component to code", "map this component", "link component to code", "create code connect mapping", or wants to establish mappings between Figma designs and code implementations. For canvas writes via `use_figma`, use `figma-use`.

**Tags:** `between`, `canvas`, `code`, `component`, `components`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-code-connect-components/SKILL.md`

### figma-create-design-system-rules
Generates custom design system rules for the user's codebase. Use when user says "create design system rules", "generate rules for my project", "set up design rules", "customize design system guidelines", or wants to establish project-specific conventions for Figma-to-code workflows. Requires Figma MCP server connection.

**Tags:** `code`, `codebase`, `connection`, `conventions`, `create`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-create-design-system-rules/SKILL.md`

### figma-generate-design
Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

**Tags:** `alongside`, `app`, `application`, `assembles`, `build`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`

### figma-generate-library
Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.

**Tags:** `api`, `between`, `both`, `build`, `call`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-generate-library/SKILL.md`

### figma-implement-design
Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementing UI code from Figma files, when user mentions "implement design", "generate code", "implement component", provides Figma URLs, or asks to build components matching Figma specs. For Figma canvas writes via `use_figma`, use `figma-use`.

**Tags:** `application`, `asks`, `build`, `canvas`, `code`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-implement-design/SKILL.md`

### figma-use
**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

**Tags:** `auto`, `auto-layout`, `bind`, `build`, `call`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-use/SKILL.md`

### financial-statements
Generate financial statements (income statement, balance sheet, cash flow) with period-over-period comparison and variance analysis. Use when preparing a monthly or quarterly P&L, closing the books and need to flag material variances, comparing actuals to budget, building a financial summary for leadership review, or looking up GAAP presentation requirements and period-end adjustments.

**Tags:** `actuals`, `adjustments`, `analysis`, `balance`, `books`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/financial-statements/SKILL.md`

### firebase-apk-scanner
Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase vulnerabilities, performing mobile app security audits, or testing Firebase endpoint security. For authorized security research only.

**Tags:** `analyzing`, `android`, `apk`, `apks`, `app`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md`

### frontend-design
Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

**Tags:** `aesthetics`, `applications`, `artifacts`, `asks`, `avoids`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/frontend-design/SKILL.md`

### frontend-design
Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.

**Tags:** `aesthetics`, `applications`, `asks`, `avoids`, `build`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/frontend-design/skills/frontend-design/SKILL.md`

### fuzzing-dictionary
>

**Tags:** `dictionary`, `fuzzing`, `fuzzing-dictionary`, `handbook`, `testing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-dictionary/SKILL.md`

### fuzzing-obstacles
>

**Tags:** `fuzzing`, `fuzzing-obstacles`, `handbook`, `obstacles`, `testing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-obstacles/SKILL.md`

### genotoxic
Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circomvent and cairo-mutants), or using necessist.

**Tags:** `analyzing`, `cairo`, `cairo-mutants`, `call`, `circomvent`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/genotoxic/SKILL.md`

### gh-address-comments
Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.

**Tags:** `address`, `auth`, `authenticate`, `branch`, `cli`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/gh-address-comments/SKILL.md`

### gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

**Tags:** `actions`, `approval`, `asks`, `buildkite`, `checks`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/gh-fix-ci/SKILL.md`

### guidelines-advisor
Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Provides actionable recommendations.

**Tags:** `actionable`, `advisor`, `analyzes`, `architecture`, `assess`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor/SKILL.md`

### harness-writing
>

**Tags:** `handbook`, `harness`, `testing`, `testing-handbook`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/harness-writing/SKILL.md`

### hook-development
This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API.

**Tags:** `advanced`, `api`, `asks`, `automation`, `block`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development/SKILL.md`

### imagegen
Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.

**Tags:** `ai-created`, `asset`, `assets`, `background`, `benefits`
**Source:** openai-skills

File: `external/openai-skills/skills/.system/imagegen/SKILL.md`

### instrument-data-to-allotrope
Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.

**Tags:** `allotrope`, `analysis`, `asm`, `auto`, `auto-detection`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md`

### interpreting-culture-index
Interprets Culture Index (CI) surveys, behavioral profiles, and personality assessment data. Supports individual profile interpretation, team composition analysis (gas/brake/glue), burnout detection, profile comparison, hiring profiles, manager coaching, interview transcript analysis for trait prediction, candidate debrief, onboarding planning, and conflict mediation. Accepts extracted JSON or PDF input via OpenCV extraction script.

**Tags:** `accepts`, `analysis`, `assessment`, `behavioral`, `brake`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/culture-index/skills/interpreting-culture-index/SKILL.md`

### journal-entry
Prepare journal entries with proper debits, credits, and supporting detail. Use when booking month-end accruals (AP, payroll, prepaid), recording depreciation or amortization, posting revenue recognition or deferred revenue adjustments, or documenting an entry for audit review.

**Tags:** `accruals`, `adjustments`, `amortization`, `audit`, `booking`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/journal-entry/SKILL.md`

### journal-entry-prep
Prepare journal entries with proper debits, credits, and supporting documentation for month-end close. Use when booking accruals, prepaid amortization, fixed asset depreciation, payroll entries, revenue recognition, or any manual journal entry.

**Tags:** `accruals`, `amortization`, `asset`, `booking`, `close`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/journal-entry-prep/SKILL.md`

### legal-risk-assessment
Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria. Use when evaluating contract risk, assessing deal exposure, classifying issues by severity, or determining whether a matter needs senior counsel or outside legal review.

**Tags:** `assess`, `assessing`, `assessment`, `classify`, `classifying`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/legal-risk-assessment/SKILL.md`

### let-fate-decide
Draws 4 Tarot cards to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the user says 'let fate decide', 'YOLO', 'whatever', 'idk', or other nonchalant phrases, makes Yu-Gi-Oh references, or when you are about to arbitrarily pick between multiple reasonable approaches. Prefer over ask-questions-if-underspecified when the user's tone is casual or playful rather than precision-seeking.

**Tags:** `ambiguous`, `approaches`, `arbitrarily`, `ask`, `ask-questions-if-underspecified`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/let-fate-decide/skills/let-fate-decide/SKILL.md`

### libafl
>

**Tags:** `handbook`, `libafl`, `testing`, `testing-handbook`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/libafl/SKILL.md`

### libfuzzer
>

**Tags:** `handbook`, `libfuzzer`, `testing`, `testing-handbook`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/libfuzzer/SKILL.md`

### mcp-integration
This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.

**Tags:** `asks`, `code`, `comprehensive`, `configure`, `connect`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration/SKILL.md`

### metrics-review
Review and analyze product metrics with trend analysis and actionable insights. Use when running a weekly, monthly, or quarterly metrics review, investigating a sudden spike or drop, comparing performance against targets, or turning raw numbers into a scorecard with recommended actions.

**Tags:** `actionable`, `actions`, `against`, `analysis`, `analyze`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/metrics-review/SKILL.md`

### mutation-testing
Configures mewt or muton mutation testing campaigns — scopes targets, tunes timeouts, and optimizes long-running runs. Use when the user mentions mewt, muton, mutation testing, or wants to configure or optimize a mutation testing campaign.

**Tags:** `campaign`, `campaigns`, `configure`, `configures`, `long`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/mutation-testing/skills/mutation-testing/SKILL.md`

### notion-research-documentation
Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations.

**Tags:** `briefs`, `citations`, `comparisons`, `curated`, `documentation`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/notion-research-documentation/SKILL.md`

### openai-docs
Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.

**Tags:** `apis`, `asks`, `browsing`, `build`, `bundled`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/openai-docs/SKILL.md`

### openai-docs
Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.

**Tags:** `apis`, `asks`, `browsing`, `build`, `bundled`
**Source:** openai-skills

File: `external/openai-skills/skills/.system/openai-docs/SKILL.md`

### openai-gh-address-comments
Help address review/issue comments on the open GitHub PR for the current branch using gh

**Tags:** `address`, `branch`, `comments`, `gh-address-comments`, `github`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-gh-address-comments/skills/openai-gh-address-comments/SKILL.md`

### openai-gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions;

**Tags:** `actions`, `asks`, `checks`, `debug`, `failing`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-gh-fix-ci/skills/openai-gh-fix-ci/SKILL.md`

### org-planning
Headcount planning, org design, and team structure optimization. Trigger with "org planning", "headcount plan", "team structure", "reorg", "who should we hire next", or when the user is thinking about team size, reporting structure, or organizational design.

**Tags:** `design`, `headcount`, `hire`, `human`, `next`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/org-planning/SKILL.md`

### ossfuzz
>

**Tags:** `handbook`, `ossfuzz`, `testing`, `testing-handbook`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/ossfuzz/SKILL.md`

### performance-review
Structure a performance review with self-assessment, manager template, and calibration prep. Use when review season kicks off and you need a self-assessment template, writing a manager review for a direct report, prepping rating distributions and promotion cases for calibration, or turning vague feedback into specific behavioral examples.

**Tags:** `assessment`, `behavioral`, `calibration`, `cases`, `direct`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/performance-review/SKILL.md`

### pipeline-review
Analyze pipeline health — prioritize deals, flag risks, get a weekly action plan. Use when running a weekly pipeline review, deciding which deals to focus on this week, spotting stale or stuck opportunities, auditing for hygiene issues like bad close dates, or identifying single-threaded deals.

**Tags:** `analyze`, `auditing`, `bad`, `close`, `dates`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/pipeline-review/SKILL.md`

### plan-zoom-integration
Turn a Zoom integration idea into an implementation plan with architecture, auth, and delivery milestones. Use when you need a practical build plan, phased delivery sequence, risk list, and next-step recommendation.

**Tags:** `architecture`, `auth`, `build`, `delivery`, `idea`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-integration/SKILL.md`

### planning-with-files
>-

**Tags:** `planning`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/planning-with-files/skills/planning-with-files/SKILL.md`

### playwright
Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script.

**Tags:** `automating`, `browser`, `bundled`, `cli`, `curated`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/playwright/SKILL.md`

### playwright-interactive
Persistent browser and Electron interaction through `js_repl` for fast iterative UI debugging.

**Tags:** `browser`, `curated`, `debugging`, `electron`, `fast`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/playwright-interactive/SKILL.md`

### plugin-creator
Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders you can edit before publishing or testing. Use when Codex needs to create a new local plugin, add optional plugin structure, or generate or update repo-root `.agents/plugins/marketplace.json` entries for plugin ordering and availability metadata.

**Tags:** `availability`, `baseline`, `can`, `codex`, `create`
**Source:** openai-skills

File: `external/openai-skills/skills/.system/plugin-creator/SKILL.md`

### plugin-structure
This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices.

**Tags:** `architecture`, `asks`, `auto`, `auto-discovery`, `code`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure/SKILL.md`

### probe-sdk
Reference skill for Zoom Probe SDK. Use after routing to a preflight workflow when testing browser compatibility, media permissions, audio or video diagnostics, and network readiness before users join.

**Tags:** `audio`, `browser`, `compatibility`, `diagnostics`, `join`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/probe-sdk/SKILL.md`

### product-brainstorming
Brainstorm product ideas, explore problem spaces, and challenge assumptions as a thinking partner. Use when exploring a new opportunity, generating solutions to a product problem, stress-testing an idea, or when a PM needs to think out loud with a sharp sparring partner before converging on a direction.

**Tags:** `assumptions`, `brainstorm`, `brainstorming`, `challenge`, `converging`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/product-brainstorming/SKILL.md`

### property-based-testing
Provides guidance for property-based testing across multiple languages and smart contracts. Use when writing tests, reviewing code with serialization/validation/parsing patterns, designing features, or when property-based testing would provide stronger coverage than example-based tests.

**Tags:** `code`, `contracts`, `coverage`, `designing`, `features`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/property-based-testing/skills/property-based-testing/SKILL.md`

### review-contract
Review a contract against your organization's negotiation playbook — flag deviations, generate redlines, provide business impact analysis. Use when reviewing vendor or customer agreements, when you need clause-by-clause analysis against standard positions, or when preparing a negotiation strategy with prioritized redlines and fallback positions.

**Tags:** `against`, `agreements`, `analysis`, `business`, `clause`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/review-contract/SKILL.md`

### ruzzy
>

**Tags:** `handbook`, `ruzzy`, `testing`, `testing-handbook`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/ruzzy/SKILL.md`

### scientific-problem-selection
This skill should be used when scientists need help with research problem selection, project ideation, troubleshooting stuck projects, or strategic scientific decisions. Use this skill when users ask to pitch a new research idea, work through a project problem, evaluate project risks, plan research strategy, navigate decision trees, or get help choosing what scientific problem to work on. Typical requests include "I have an idea for a project", "I'm stuck on my research", "help me evaluate this project", "what should I work on", or "I need strategic advice about my research".

**Tags:** `advice`, `ask`, `bio`, `bio-research`, `choosing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/scientific-problem-selection/SKILL.md`

### scv-scan
Audits Solidity codebases for smart contract vulnerabilities using a four-phase workflow (cheatsheet loading, codebase sweep, deep validation, reporting) covering 36 vulnerability classes. Use when auditing Solidity contracts for security issues, performing smart contract vulnerability scans, or reviewing Solidity code for common exploit patterns.

**Tags:** `auditing`, `audits`, `cheatsheet`, `classes`, `code`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/scv-scan/skills/scv-scan/SKILL.md`

### search-strategy
Query decomposition and multi-source search orchestration. Breaks natural language questions into targeted searches per source, translates queries into source-specific syntax, ranks results by relevance, and handles ambiguity and fallback strategies.

**Tags:** `ambiguity`, `breaks`, `decomposition`, `enterprise`, `enterprise-search`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search-strategy/SKILL.md`

### second-opinion
Runs external LLM code reviews (OpenAI Codex or Google Gemini CLI) on uncommitted changes, branch diffs, or specific commits. Use when the user asks for a second opinion, external review, codex review, gemini review, or mentions /second-opinion.

**Tags:** `asks`, `branch`, `changes`, `cli`, `code`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion/SKILL.md`

### security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

**Tags:** `code`, `coding`, `curated`, `debugging`, `default`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/security-best-practices/SKILL.md`

### security-ownership-map
Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

**Tags:** `analysis`, `analyze`, `build`, `bus`, `bus-factor`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/security-ownership-map/SKILL.md`

### security-threat-model
Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work.

**Tags:** `abuse`, `appsec`, `architecture`, `asks`, `assets`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/security-threat-model/SKILL.md`

### semgrep-rule-creator
Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections.

**Tags:** `analysis`, `bug`, `building`, `code`, `creates`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md`

### session-report
Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts.

**Tags:** `cache`, `code`, `expensive`, `explorable`, `html`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/session-report/skills/session-report/SKILL.md`

### setup-zoom-mcp
Decide when Zoom MCP is the right fit and produce a safe setup plan for Claude. Use when planning AI workflows over Zoom data, deciding between MCP and REST, or defining a hybrid MCP architecture.

**Tags:** `architecture`, `between`, `data`, `decide`, `deciding`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-mcp/SKILL.md`

### setup-zoom-oauth
Implement Zoom authentication correctly. Use when setting up app credentials, choosing an OAuth grant, requesting scopes, handling token refresh, or debugging auth failures.

**Tags:** `app`, `auth`, `authentication`, `choosing`, `correctly`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-oauth/SKILL.md`

### sharp-edges
Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

**Tags:** `api`, `apis`, `code`, `configuration`, `configurations`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges/SKILL.md`

### skill-development
This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins.

**Tags:** `code`, `content`, `create`, `description`, `dev`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/skill-development/SKILL.md`

### skill-improver
Iteratively reviews and fixes Claude Code skill quality issues until they meet standards. Runs automated fix-review cycles using the skill-reviewer agent. Use to fix skill quality issues, improve skill descriptions, run automated skill review loops, or iteratively refine a skill. Triggers on 'fix my skill', 'improve skill quality', 'skill improvement loop'. NOT for one-time reviews—use /skill-reviewer directly.

**Tags:** `automated`, `code`, `cycles`, `descriptions`, `directly`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/skill-improver/skills/skill-improver/SKILL.md`

### sox-testing
Generate SOX sample selections, testing workpapers, and control assessments. Use when planning quarterly or annual SOX 404 testing, pulling a sample for a control (revenue, P2P, ITGC, close), building a testing workpaper template, or evaluating and classifying a control deficiency.

**Tags:** `annual`, `assessments`, `building`, `classifying`, `close`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/sox-testing/SKILL.md`

### spec-to-code-compliance
Verifies code implements exactly what documentation specifies for blockchain audits. Use when comparing code against whitepapers, finding gaps between specs and implementation, or performing compliance checks for protocol implementations.

**Tags:** `against`, `audits`, `between`, `blockchain`, `checks`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md`

### sprint-planning
Plan a sprint — scope work, estimate capacity, set goals, and draft a sprint plan. Use when kicking off a new sprint, sizing a backlog against team availability (accounting for PTO and meetings), deciding what's P0 vs. stretch, or handling carryover from the last sprint.

**Tags:** `accounting`, `against`, `availability`, `backlog`, `capacity`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/sprint-planning/SKILL.md`

### start
Start here for any Zoom integration or app idea. Use when you need to choose the right Zoom surface, shape the architecture, or route into the correct implementation skill without reading the whole Zoom doc set first.

**Tags:** `app`, `architecture`, `choose`, `correct`, `doc`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/start/SKILL.md`

### statistical-analysis
Apply statistical methods including descriptive stats, trend analysis, outlier detection, and hypothesis testing. Use when analyzing distributions, testing for significance, detecting anomalies, computing correlations, or interpreting statistical results.

**Tags:** `analysis`, `analyzing`, `anomalies`, `apply`, `computing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/statistical-analysis/SKILL.md`

### system-design
Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "system design for", "what's the right architecture for", or when the user needs help with API design, data modeling, or service boundaries.

**Tags:** `api`, `architect`, `architecture`, `architectures`, `boundaries`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/system-design/SKILL.md`

### tech-debt
Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or when the user asks about code quality, refactoring priorities, or maintenance backlog.

**Tags:** `asks`, `audit`, `backlog`, `categorize`, `code`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/tech-debt/SKILL.md`

### testing-handbook-generator
>

**Tags:** `generator`, `handbook`, `testing`, `testing-handbook`, `testing-handbook-generator`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/testing-handbook-generator/SKILL.md`

### testing-strategy
Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests for", "test plan", "what tests do we need", or when the user needs help with testing approaches, coverage, or test architecture.

**Tags:** `approaches`, `architecture`, `coverage`, `design`, `engineering`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/testing-strategy/SKILL.md`

### trailmark
Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

**Tags:** `analysis`, `analyzing`, `attack`, `audit`, `auto`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`

### trailmark-summary
Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview.

**Tags:** `analysis`, `auto`, `auto-detected`, `code`, `codebase`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary/SKILL.md`

### triage-nda
Rapidly triage an incoming NDA and classify it as GREEN (standard approval), YELLOW (counsel review), or RED (full legal review). Use when a new NDA arrives from sales or business development, when screening for embedded non-solicits, non-competes, or missing carveouts, or when deciding whether an NDA can be signed under standard delegation.

**Tags:** `approval`, `arrives`, `business`, `can`, `carveouts`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/triage-nda/SKILL.md`

### using-dbt-for-analytics-engineering
Builds and modifies dbt models, writes SQL transformations using ref() and source(), creates tests, and validates results with dbt show. Use when doing any dbt work - building or modifying models, debugging errors, exploring unfamiliar data sources, writing tests, or evaluating impact of changes.

**Tags:** `analytics`, `building`, `builds`, `changes`, `creates`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/using-dbt-for-analytics-engineering/SKILL.md`

### ux-copy
Write or review UX copy — microcopy, error messages, empty states, CTAs. Trigger with "write copy for", "what should this button say?", "review this error message", or when naming a CTA, wording a confirmation dialog, filling an empty state, or writing onboarding text.

**Tags:** `button`, `confirmation`, `copy`, `cta`, `ctas`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/ux-copy/SKILL.md`

### variant-analysis
Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audits after finding an initial issue.

**Tags:** `analysis`, `analyzing`, `audits`, `bug`, `bugs`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis/SKILL.md`

### vector-forge
Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

**Tags:** `algorithm`, `code`, `compares`, `coverage`, `creating`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`

### vendor-review
Evaluate a vendor — cost analysis, risk assessment, and recommendation. Use when reviewing a new vendor proposal, deciding whether to renew or replace a contract, comparing two vendors side-by-side, or building a TCO breakdown and negotiation points before procurement sign-off.

**Tags:** `analysis`, `assessment`, `breakdown`, `building`, `comparing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/vendor-review/SKILL.md`

### view-pdf
Interactive PDF viewer. Use when the user wants to open, show, or view a PDF and collaborate on it visually — annotate, highlight, stamp, fill form fields, place signature/initials, or review markup together. Not for summarization or text extraction (use native Read instead).

**Tags:** `annotate`, `collaborate`, `extraction`, `fields`, `fill`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/pdf-viewer/skills/view-pdf/SKILL.md`

### webapp-testing
>-

**Tags:** `testing`, `webapp`, `webapp-testing`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/webapp-testing/SKILL.md`

### webapp-testing
Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

**Tags:** `applications`, `behavior`, `browser`, `capturing`, `debugging`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/webapp-testing/SKILL.md`

### weekly-prep-brief
Generate a comprehensive weekly briefing for all external calls in the next 7 days. Triggers on 'weekly prep brief', 'prepare my week', 'what calls do I have this week', 'Monday prep', or any weekly planning request.

**Tags:** `brief`, `briefing`, `calls`, `comprehensive`, `days`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/weekly-prep-brief/SKILL.md`

### winui-app
Bootstrap, develop, and design modern WinUI 3 desktop applications with C# and the Windows App SDK using official Microsoft guidance, WinUI Gallery patterns, Windows App SDK samples, and CommunityToolkit components. Use when creating a brand new app, preparing a machine for WinUI, reviewing, refactoring, planning, troubleshooting, environment-checking, or setting up WinUI 3 XAML, controls, navigation, windowing, theming, accessibility, responsiveness, performance, deployment, or related Windows app design and development work.

**Tags:** `accessibility`, `app`, `applications`, `bootstrap`, `brand`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/winui-app/SKILL.md`

### wycheproof
>

**Tags:** `handbook`, `testing`, `testing-handbook`, `wycheproof`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/wycheproof/SKILL.md`

### zeroize-audit
Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling secrets, keys, passwords, or other sensitive data.

**Tags:** `analysis`, `assembly`, `assembly-level`, `audit`, `auditing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/zeroize-audit/skills/zeroize-audit/SKILL.md`

### zoom-mcp
Guidance for the bundled Zoom MCP connectors. Use after routing to an MCP workflow when planning or troubleshooting tool-based access to meetings, recordings, meeting assets, or transcripts. Route Zoom Docs requests to the dedicated Docs MCP server and Whiteboard-specific requests to `zoom-mcp/whiteboard`.

**Tags:** `access`, `assets`, `bundled`, `connectors`, `dedicated`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-mcp/SKILL.md`

### zoom-oauth
Reference skill for Zoom authentication. Use after routing to an auth workflow when choosing app credentials, grant types, scopes, token refresh behavior, or debugging Zoom OAuth failures.

**Tags:** `app`, `auth`, `authentication`, `behavior`, `choosing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/oauth/SKILL.md`

## Customer Success

### ticket-triage
Triage and prioritize a support ticket or customer issue. Use when a new ticket comes in and needs categorization, assigning P1-P4 priority, deciding which team should handle it, or checking whether it's a duplicate or known issue before routing.

**Tags:** `assigning`, `categorization`, `checking`, `comes`, `customer`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/customer-support/skills/ticket-triage/SKILL.md`

### zoom-cobrowse-sdk
Reference skill for Zoom Cobrowse SDK. Use after routing to a collaborative-support workflow when implementing browser co-browsing, annotation tools, privacy masking, remote assist, or PIN-based session sharing.

**Tags:** `annotation`, `assist`, `browser`, `browsing`, `co-browsing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/cobrowse-sdk/SKILL.md`

## Data

### account-research
Research a company using Common Room data. Triggers on 'research [company]', 'tell me about [domain]', 'pull up signals for [account]', 'what's going on with [company]', or any account-level question.

**Tags:** `account`, `account-level`, `account-research`, `company`, `data`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/account-research/SKILL.md`

### analyze
Answer data questions -- from quick lookups to full analyses. Use when looking up a single metric, investigating what's driving a trend or drop, comparing segments over time, or preparing a formal data report for stakeholders.

**Tags:** `analyses`, `analyze`, `answer`, `comparing`, `data`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/analyze/SKILL.md`

### building-dbt-semantic-layer
Use when creating or modifying dbt Semantic Layer components — semantic models, metrics, dimensions, entities, measures, or time spines. Covers MetricFlow configuration, metric types (simple, derived, cumulative, ratio, conversion), and validation for both latest and legacy YAML specs.

**Tags:** `both`, `building`, `building-dbt-semantic-layer`, `components`, `configuration`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/building-dbt-semantic-layer/SKILL.md`

### comp-analysis
Analyze compensation — benchmarking, band placement, and equity modeling. Trigger with "what should we pay a [role]", "is this offer competitive", "model this equity grant", or when uploading comp data to find outliers and retention risks.

**Tags:** `analysis`, `analyze`, `band`, `benchmarking`, `comp`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/comp-analysis/SKILL.md`

### compliance-check
Run a compliance check on a proposed action, product feature, or business initiative, surfacing applicable regulations, required approvals, and risk areas. Use when launching a feature that touches personal data, when marketing or product proposes something with regulatory implications, or when you need to know which approvals and jurisdictional requirements apply before proceeding.

**Tags:** `applicable`, `apply`, `approvals`, `areas`, `business`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/compliance-check/SKILL.md`

### contact-research
Research a specific person using Common Room data. Triggers on 'who is [name]', 'look up [email]', 'research [contact]', 'is [name] a warm lead', or any contact-level question.

**Tags:** `contact`, `contact-level`, `contact-research`, `data`, `email`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/contact-research/SKILL.md`

### data-context-extractor
>

**Tags:** `context`, `data`, `data-context-extractor`, `extractor`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/data-context-extractor/SKILL.md`

### dbt-migration
Skills for migrating dbt projects - moving from dbt Core to the Fusion engine or across data platforms. Use when migrating dbt projects between platforms or to dbt Fusion.

**Tags:** `between`, `core`, `data`, `dbt`, `dbt-migration`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt-migration/SKILL.md`

### legal-response
Generate a response to a common legal inquiry using configured templates, with built-in escalation checks for situations that shouldn't use a templated reply. Use when responding to data subject requests, litigation hold notices, vendor legal questions, NDA requests from business teams, or subpoenas.

**Tags:** `business`, `checks`, `configured`, `data`, `escalation`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/legal-response/SKILL.md`

### nextflow-development
Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing RNA-seq, WGS/WES, or ATAC-seq data—either local FASTQs or public datasets from GEO/SRA. Triggers on nf-core, Nextflow, FASTQ analysis, variant calling, gene expression, differential expression, GEO reanalysis, GSE/GSM/SRR accessions, or samplesheet creation.

**Tags:** `accessions`, `analysis`, `analyzing`, `atac`, `atac-seq`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/nextflow-development/SKILL.md`

### people-report
Generate headcount, attrition, diversity, or org health reports. Use when pulling a headcount snapshot for leadership, analyzing turnover trends by team, preparing diversity representation metrics, or assessing span of control and flight risk across the org.

**Tags:** `analyzing`, `assessing`, `attrition`, `control`, `diversity`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/people-report/SKILL.md`

### performance-report
Build a marketing performance report with key metrics, trend analysis, wins and misses, and prioritized optimization recommendations. Use when wrapping a campaign, when preparing weekly, monthly, or quarterly channel summaries for stakeholders, or when you need data translated into an executive summary with next-period priorities.

**Tags:** `analysis`, `build`, `campaign`, `channel`, `data`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/performance-report/SKILL.md`

### reconciliation
Reconcile accounts by comparing GL balances to subledgers, bank statements, or third-party data. Use when performing bank reconciliations, GL-to-subledger recs, intercompany reconciliations, or identifying and categorizing reconciling items.

**Tags:** `accounts`, `balances`, `bank`, `categorizing`, `comparing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/reconciliation/SKILL.md`

### scvi-tools
Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need (1) data integration and batch correction with scVI/scANVI, (2) ATAC-seq analysis with PeakVI, (3) CITE-seq multi-modal analysis with totalVI, (4) multiome RNA+ATAC analysis with MultiVI, (5) spatial transcriptomics deconvolution with DestVI, (6) label transfer and reference mapping with scANVI/scArches, (7) RNA velocity with veloVI, or (8) any deep learning-based single-cell method. Triggers include mentions of scVI, scANVI, totalVI, PeakVI, MultiVI, DestVI, veloVI, sysVI, scArches, variational autoencoder, VAE, batch correction, data integration, multi-modal, CITE-seq, multiome, reference mapping, latent space.

**Tags:** `analysis`, `atac`, `atac-seq`, `autoencoder`, `batch`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/scvi-tools/SKILL.md`

### start
Set up your bio-research environment and explore available tools. Use when first getting oriented with the plugin, checking which literature, drug-discovery, or visualization MCP servers are connected, or surveying available analysis skills before starting a new project.

**Tags:** `analysis`, `bio`, `bio-research`, `checking`, `connected`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/start/SKILL.md`

### start
Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your existing task list, or decoding the shorthand (nicknames, acronyms, project codenames) you use in your todos.

**Tags:** `acronyms`, `bootstrapping`, `codenames`, `dashboard`, `decoding`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/productivity/skills/start/SKILL.md`

### trailmark-structural
Runs full Trailmark structural analysis on Trailmark 0.2.x by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, and attack surface. Use when vivisect needs detailed structural data for a target. Triggers: structural analysis, blast radius, taint analysis, complexity hotspots.

**Tags:** `analysis`, `attack`, `blast`, `boundaries`, `building`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-structural/SKILL.md`

### write-spec
Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user request into a structured document, scoping a feature with goals and non-goals, defining success metrics and acceptance criteria, or breaking a big ask into a phased spec.

**Tags:** `acceptance`, `ask`, `big`, `breaking`, `criteria`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/write-spec/SKILL.md`

## Design

### brand-voice-enforcement
>

**Tags:** `brand`, `brand-voice`, `brand-voice-enforcement`, `enforcement`, `partner`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/brand-voice/skills/brand-voice-enforcement/SKILL.md`

### discover-brand
>

**Tags:** `brand`, `brand-voice`, `discover`, `discover-brand`, `partner`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/brand-voice/skills/discover-brand/SKILL.md`

### draft-content
Draft blog posts, social media, email newsletters, landing pages, press releases, and case studies with channel-specific formatting and SEO recommendations. Use when writing any marketing content, when you need headline or subject line options, or when adapting a message for a specific platform, audience, and brand voice.

**Tags:** `adapting`, `audience`, `blog`, `brand`, `case`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/draft-content/SKILL.md`

### guideline-generation
>

**Tags:** `brand`, `brand-voice`, `generation`, `guideline`, `guideline-generation`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/brand-voice/skills/guideline-generation/SKILL.md`

## Devops

### cloudflare-deploy
Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. Use when the user asks to deploy, host, publish, or set up a project on Cloudflare.

**Tags:** `applications`, `asks`, `cloudflare`, `cloudflare-deploy`, `curated`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/cloudflare-deploy/SKILL.md`

### enrich-lead
Instant lead enrichment. Drop a name, company, LinkedIn URL, or email and get the full contact card with email, phone, title, company intel, and next actions.

**Tags:** `actions`, `apollo`, `card`, `company`, `contact`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/enrich-lead/SKILL.md`

### openai-cloudflare-deploy
Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform

**Tags:** `applications`, `cloudflare`, `cloudflare-deploy`, `deploy`, `infrastructure`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-cloudflare-deploy/skills/openai-cloudflare-deploy/SKILL.md`

### render-deploy
Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deeplinks. Use when the user wants to deploy, host, publish, or set up their application on Render's cloud platform.

**Tags:** `analyzing`, `application`, `applications`, `blueprints`, `cloud`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/render-deploy/SKILL.md`

### search
Search across all connected sources in one query. Trigger with "find that doc about...", "what did we decide on...", "where was the conversation about...", or when looking for a decision, document, or discussion that could live in chat, email, cloud storage, or a project tracker.

**Tags:** `chat`, `cloud`, `connected`, `conversation`, `could`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search/SKILL.md`

### vercel-composition-patterns
>-

**Tags:** `composition`, `vercel`, `vercel-composition`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/vercel-composition-patterns/SKILL.md`

### vercel-deploy
>-

**Tags:** `deploy`, `vercel`, `vercel-deploy`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/vercel-deploy/SKILL.md`

### vercel-deploy
Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

**Tags:** `actions`, `app`, `applications`, `create`, `curated`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/vercel-deploy/SKILL.md`

### video-sdk/linux
Zoom Video SDK for Linux - C++ headless bots, raw audio/video capture/injection, Qt/GTK integration, Docker support

**Tags:** `audio`, `bots`, `capture`, `docker`, `gtk`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/linux/SKILL.md`

## Engineering

### build-mcp-server
This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

**Tags:** `api`, `app`, `asks`, `build`, `build-mcp-server`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`

### cli-creator
Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

**Tags:** `admin`, `api`, `app`, `auth`, `build`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/cli-creator/SKILL.md`

### customer-escalation
Package an escalation for engineering, product, or leadership with full context. Use when a bug needs engineering attention beyond normal support, multiple customers report the same issue, a customer is threatening to churn, or an issue has sat unresolved past its SLA.

**Tags:** `attention`, `beyond`, `bug`, `churn`, `context`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/customer-support/skills/customer-escalation/SKILL.md`

### dbt
Skills for analytics engineering with dbt - building models, writing tests, querying the semantic layer, troubleshooting jobs, and more. Use when doing any dbt analytics engineering work.

**Tags:** `analytics`, `building`, `dbt`, `doing`, `engineering`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/SKILL.md`

### deploy-checklist
Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI status and approvals before going to production, or documenting rollback triggers ahead of time.

**Tags:** `ahead`, `approvals`, `change`, `checklist`, `database`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/deploy-checklist/SKILL.md`

### design-handoff
Generate developer handoff specs from a design. Use when a design is ready for engineering and needs a spec sheet covering layout, design tokens, component props, interaction states, responsive breakpoints, edge cases, and animation details.

**Tags:** `animation`, `breakpoints`, `cases`, `component`, `covering`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/design-handoff/SKILL.md`

### gh-cli
Enforces authenticated gh CLI workflows over unauthenticated curl/WebFetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues.

**Tags:** `access`, `api`, `authenticated`, `cli`, `codex`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/.codex/skills/gh-cli/SKILL.md`

### incident-response
Run an incident response workflow — triage, communicate, and write postmortem. Trigger with "we have an incident", "production is down", an alert that needs severity assessment, a status update mid-incident, or when writing a blameless postmortem after resolution.

**Tags:** `alert`, `assessment`, `blameless`, `communicate`, `down`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/incident-response/SKILL.md`

### notion-spec-to-implementation
Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them.

**Tags:** `creating`, `curated`, `feature`, `implementation`, `implementing`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/notion-spec-to-implementation/SKILL.md`

### plan-zoom-product
Choose the right Zoom building surface for a use case and explain the tradeoffs clearly. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Phone, Contact Center, or MCP for a specific product idea or integration goal.

**Tags:** `api`, `apps`, `between`, `building`, `case`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product/SKILL.md`

### rivet-sdk
Reference skill for Zoom Rivet SDK. Use after routing to a Rivet-based server workflow when implementing auth handling, webhook consumers, API wrappers, multi-module composition, or Lambda receiver patterns.

**Tags:** `api`, `auth`, `composition`, `consumers`, `handling`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rivet-sdk/SKILL.md`

### speech
Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for live calls. Custom voice creation is out of scope.

**Tags:** `accessibility`, `api`, `api-key`, `asks`, `audio`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/speech/SKILL.md`

### stakeholder-update
Generate a stakeholder update tailored to audience and cadence. Use when writing a weekly or monthly status for leadership, announcing a launch, escalating a risk or blocker, or translating the same progress into exec-brief, engineering-detail, or customer-facing versions.

**Tags:** `announcing`, `audience`, `blocker`, `brief`, `cadence`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/stakeholder-update/SKILL.md`

### standup
Generate a standup update from recent activity. Use when preparing for daily standup, summarizing yesterday's commits and PRs and ticket moves, formatting work into yesterday/today/blockers, or structuring a few rough notes into a shareable update.

**Tags:** `activity`, `blockers`, `commits`, `daily`, `engineering`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/standup/SKILL.md`

### token-integration-analyzer
Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Context-aware for both token implementations and token integrations.

**Tags:** `analysis`, `analyzer`, `analyzes`, `assesses`, `aware`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer/SKILL.md`

### troubleshooting-dbt-job-errors
Diagnoses dbt Cloud/platform job failures by analyzing run logs, querying the Admin API, reviewing git history, and investigating data issues. Use when a dbt Cloud/platform job fails and you need to diagnose the root cause, especially when error messages are unclear or when intermittent failures occur. Do not use for local dbt development errors.

**Tags:** `admin`, `analyzing`, `api`, `cause`, `cloud`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/troubleshooting-dbt-job-errors/SKILL.md`

### xlsx
Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

**Tags:** `adding`, `api`, `between`, `casually`, `charting`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/xlsx/SKILL.md`

### zoom-general
Cross-product Zoom reference skill. Use after the workflow is clear when you need shared platform guidance, app-model comparisons, authentication context, scopes, marketplace considerations, or API-vs-MCP routing.

**Tags:** `api`, `api-vs-mcp`, `app`, `app-model`, `authentication`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general/SKILL.md`

## Frontend

### account-research
Research a company or person and get actionable sales intel. Works standalone with web search, supercharged when you connect enrichment tools or your CRM. Trigger with "research [company]", "look up [person]", "intel on [prospect]", "who is [name] at [company]", or "tell me about [company]".

**Tags:** `account`, `account-research`, `actionable`, `company`, `connect`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/account-research/SKILL.md`

### brand-guidelines
Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.

**Tags:** `applies`, `apply`, `artifact`, `benefit`, `brand`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/brand-guidelines/SKILL.md`

### build-dashboard
Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results into a shareable self-contained report, building a team monitoring snapshot, or needing multiple charts with filters in one browser-openable file.

**Tags:** `browser`, `browser-openable`, `build`, `build-dashboard`, `building`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/build-dashboard/SKILL.md`

### build-zoom-contact-center-app
Reference skill for Zoom Contact Center. Use after routing to a contact-center workflow when implementing app, web, or native integrations; engagement context and state handling; campaigns; callbacks; or version-drift troubleshooting.

**Tags:** `app`, `build`, `build-zoom-contact-center-app`, `callbacks`, `campaigns`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/SKILL.md`

### build-zoom-meeting-app
Build or embed a Zoom meeting flow. Use when implementing Meeting SDK joins, web or mobile meeting embeds, meeting lifecycle flows, or when deciding between Meeting SDK and Video SDK.

**Tags:** `app`, `between`, `build`, `build-zoom-meeting-app`, `deciding`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-meeting-app/SKILL.md`

### build-zoom-virtual-agent
Reference skill for Zoom Virtual Agent. Use after routing to a virtual-agent workflow when implementing web embeds, Android or iOS wrapper integrations, knowledge-base sync, lifecycle handling, or troubleshooting.

**Tags:** `android`, `base`, `build`, `build-zoom-virtual`, `embeds`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/SKILL.md`

### call-prep
Prepare for a sales call with account context, attendee research, and suggested agenda. Works standalone with user input and web research, supercharged when you connect your CRM, email, chat, or transcripts. Trigger with "prep me for my call with [company]", "I'm meeting with [company] prep me", "call prep [company]", or "get me ready for [meeting]".

**Tags:** `account`, `agenda`, `attendee`, `call`, `call-prep`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/call-prep/SKILL.md`

### canvas-design
>-

**Tags:** `canvas`, `canvas-design`, `design`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/canvas-design/SKILL.md`

### canvas-design
Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

**Tags:** `art`, `artists`, `asks`, `avoid`, `beautiful`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/canvas-design/SKILL.md`

### competitive-intelligence
Research your competitors and build an interactive battlecard. Outputs an HTML artifact with clickable competitor cards and a comparison matrix. Trigger with "competitive intel", "research competitors", "how do we compare to [competitor]", "battlecard for [competitor]", or "what's new with [competitor]".

**Tags:** `artifact`, `battlecard`, `build`, `cards`, `clickable`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/competitive-intelligence/SKILL.md`

### contact-center/web
Zoom Contact Center SDK for Web. Use for web chat/video/campaign embeds, engagement event handling, app-context integrations, and Smart Embed postMessage workflows.

**Tags:** `app`, `app-context`, `campaign`, `center`, `chat`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/web/SKILL.md`

### designing-workflow-skills
>-

**Tags:** `design`, `designing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/workflow-skill-design/skills/designing-workflow-skills/SKILL.md`

### draft-outreach
Research a prospect then draft personalized outreach. Uses web research by default, supercharged with enrichment and CRM. Trigger with "draft outreach to [person/company]", "write cold email to [prospect]", "reach out to [name]".

**Tags:** `cold`, `company`, `crm`, `default`, `draft`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/draft-outreach/SKILL.md`

### email-sequence
Design and draft multi-email sequences with full copy, timing, branching logic, exit conditions, and performance benchmarks. Use when building onboarding, lead nurture, re-engagement, win-back, or product launch flows, when you need a complete drip campaign with A/B test suggestions, or when mapping a sequence end-to-end with a flow diagram.

**Tags:** `back`, `benchmarks`, `branching`, `building`, `campaign`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/email-sequence/SKILL.md`

### ffuf-web-fuzzing
>-

**Tags:** `ffuf`, `ffuf-web-fuzzing`, `fuzzing`, `web`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/ffuf-web-fuzzing/skills/ffuf-web-fuzzing/SKILL.md`

### figma-create-new-file
Create a new blank Figma file. Use when the user wants to create a new Figma design or FigJam file, or when you need a new file before calling use_figma. Handles plan resolution via whoami if needed. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard)

**Tags:** `blank`, `calling`, `create`, `curated`, `design`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-create-new-file/SKILL.md`

### figma-implement-design
>-

**Tags:** `design`, `figma`, `figma-implement-design`, `implement`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/figma-implement-design/SKILL.md`

### frontend-design
>-

**Tags:** `design`, `frontend`, `frontend-design`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/frontend-design/SKILL.md`

### last30days
Researches a topic from the last 30 days on Reddit, X, and the web. Surfaces real community discussions with engagement metrics and synthesizes findings into actionable insights. Use when the user wants to know what people are saying about a topic right now.

**Tags:** `actionable`, `community`, `days`, `discussions`, `engagement`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/last30days/skills/last30days/SKILL.md`

### netlify-deploy
Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys.

**Tags:** `asks`, `cli`, `curated`, `deploy`, `deploys`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/netlify-deploy/SKILL.md`

### openai-develop-web-game
Use when the agent is building or iterating on a web game (HTML/JS) and needs a reliable

**Tags:** `building`, `develop`, `develop-web-game`, `game`, `html`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-develop-web-game/skills/openai-develop-web-game/SKILL.md`

### openai-netlify-deploy
Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks

**Tags:** `asks`, `cli`, `deploy`, `netlify`, `netlify-deploy`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-netlify-deploy/skills/openai-netlify-deploy/SKILL.md`

### playground
Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic.

**Tags:** `asks`, `configure`, `contained`, `controls`, `copy`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/playground/skills/playground/SKILL.md`

### react-pdf
No description.

**Tags:** `pdf`, `react`, `react-pdf`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/react-pdf/skills/react-pdf/SKILL.md`

### research-synthesis
Synthesize user research into themes, insights, and recommendations. Use when you have interview transcripts, survey results, usability test notes, support tickets, or NPS responses that need to be distilled into patterns, user segments, and prioritized next steps.

**Tags:** `design`, `distilled`, `have`, `insights`, `interview`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/research-synthesis/SKILL.md`

### scribe
Reference skill for Zoom AI Services Scribe. Use after routing to a transcription workflow when handling uploaded or stored media, Build-platform JWT auth, fast mode transcription, batch jobs, or transcript pipeline design.

**Tags:** `auth`, `batch`, `build`, `build-platform`, `design`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/scribe/SKILL.md`

### theme-factory
Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.

**Tags:** `apply`, `artifact`, `artifacts`, `been`, `can`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/theme-factory/SKILL.md`

### ui-toolkit/web
Reference skill for Zoom Video SDK UI Toolkit. Use after routing to a web video workflow when you want prebuilt React UI instead of building a fully custom Video SDK interface.

**Tags:** `building`, `custom`, `fully`, `instead`, `interface`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/ui-toolkit/SKILL.md`

### user-research
Plan, conduct, and synthesize user research. Trigger with "user research plan", "interview guide", "usability test", "survey design", "research questions", or when the user needs help with any aspect of understanding their users through research.

**Tags:** `aspect`, `conduct`, `design`, `interview`, `needs`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/user-research/SKILL.md`

### vercel-react-best-practices
>-

**Tags:** `practices`, `react`, `vercel`, `vercel-react-practices`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/vercel-react-best-practices/SKILL.md`

### virtual-agent/web
Zoom Virtual Agent SDK for web embeds. Use for campaign or entry ID chat launch, event-driven controls, user context updates, and CSP-safe deployment.

**Tags:** `campaign`, `chat`, `context`, `controls`, `csp`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/web/SKILL.md`

### web-artifacts-builder
Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

**Tags:** `artifacts`, `builder`, `complex`, `component`, `components`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/web-artifacts-builder/SKILL.md`

### web-design-guidelines
>-

**Tags:** `design`, `guidelines`, `web`, `web-design-guidelines`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/web-design-guidelines/SKILL.md`

### zoom-apps-sdk
Reference skill for Zoom Apps SDK. Use after routing to an in-client app workflow when building web apps that run inside Zoom meetings, webinars, the main client, or Zoom Phone.

**Tags:** `app`, `apps`, `building`, `client`, `in-client`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-apps-sdk/SKILL.md`

### zoom-meeting-sdk-react-native
Zoom Meeting SDK for React Native. Use when embedding Zoom meetings in React Native iOS/Android apps with @zoom/meetingsdk-react-native, JWT auth, join/start flows, platform setup, and native bridge troubleshooting.

**Tags:** `android`, `apps`, `auth`, `bridge`, `embedding`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/react-native/SKILL.md`

### zoom-meeting-sdk-web
|

**Tags:** `meeting`, `meeting-sdk`, `partner`, `sdk`, `web`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/SKILL.md`

### zoom-meeting-sdk-web-client-view
|

**Tags:** `client`, `client-view`, `meeting`, `meeting-sdk`, `partner`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/client-view/SKILL.md`

### zoom-meeting-sdk-web-component-view
|

**Tags:** `component`, `component-view`, `meeting`, `meeting-sdk`, `partner`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/component-view/SKILL.md`

### zoom-video-sdk-react-native
|

**Tags:** `native`, `partner`, `react`, `react-native`, `sdk`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/react-native/SKILL.md`

## Legal

### signature-request
Prepare and route a document for e-signature — run a pre-signature checklist, configure signing order, and send for execution. Use when a contract is finalized and ready to sign, when verifying entity names, exhibits, and signature blocks before sending, or when setting up an envelope with sequential or parallel signers.

**Tags:** `blocks`, `checklist`, `configure`, `contract`, `document`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/signature-request/SKILL.md`

## Marketing

### competitive-ads-extractor
>-

**Tags:** `ads`, `competitive`, `competitive-ads-extractor`, `extractor`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/competitive-ads-extractor/SKILL.md`

### content-creation
Draft marketing content across channels — blog posts, social media, email newsletters, landing pages, press releases, and case studies. Use when writing any marketing content, when you need channel-specific formatting, SEO-optimized copy, headline options, or calls to action.

**Tags:** `blog`, `calls`, `case`, `channel`, `channels`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/content-creation/SKILL.md`

## Mobile

### contact-center/ios
Zoom Contact Center SDK for iOS. Use for native iOS chat/video/ZVA/scheduled callback integrations, app lifecycle bridging, rejoin flow, and callback handling.

**Tags:** `app`, `bridging`, `callback`, `center`, `chat`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/ios/SKILL.md`

### virtual-agent/ios
Zoom Virtual Agent iOS integration via WKWebView. Use for Swift/Objective-C script injection, message handlers, support_handoff relay, and URL routing policies.

**Tags:** `handlers`, `handoff`, `injection`, `integration`, `ios`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/ios/SKILL.md`

### zoom-meeting-sdk-android
|

**Tags:** `android`, `meeting`, `meeting-sdk`, `partner`, `sdk`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/android/SKILL.md`

### zoom-meeting-sdk-ios
|

**Tags:** `ios`, `meeting`, `meeting-sdk`, `partner`, `sdk`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/ios/SKILL.md`

### zoom-video-sdk-android
|

**Tags:** `android`, `partner`, `sdk`, `video`, `video-sdk`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/android/SKILL.md`

### zoom-video-sdk-ios
|

**Tags:** `ios`, `partner`, `sdk`, `video`, `video-sdk`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/ios/SKILL.md`

## Personal Assistant

### pptx
Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.

**Tags:** `afterward`, `both`, `combining`, `comments`, `content`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/pptx/SKILL.md`

### task-management
Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, wants to add/complete tasks, or needs help tracking commitments.

**Tags:** `asks`, `commitments`, `complete`, `management`, `needs`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/productivity/skills/task-management/SKILL.md`

### update
Sync tasks and refresh memory from your current activity. Use when pulling new assignments from your project tracker into TASKS.md, triaging stale or overdue tasks, filling memory gaps for unknown people or projects, or running a comprehensive scan to catch todos buried in chat and email.

**Tags:** `activity`, `assignments`, `buried`, `catch`, `chat`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/productivity/skills/update/SKILL.md`

## Product

### draft-response
Draft a professional customer-facing response tailored to the situation and relationship. Use when answering a product question, responding to an escalation or outage, delivering bad news like a delay or won't-fix, declining a feature request, or replying to a billing issue.

**Tags:** `answering`, `bad`, `billing`, `customer`, `customer-facing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/customer-support/skills/draft-response/SKILL.md`

### roadmap-update
Update, create, or reprioritize your product roadmap. Use when adding a new initiative and deciding what moves to make room, shifting priorities after new information comes in, moving timelines due to a dependency slip, or building a Now/Next/Later view from scratch.

**Tags:** `adding`, `building`, `comes`, `create`, `deciding`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/roadmap-update/SKILL.md`

### synthesize-research
Synthesize user research from interviews, surveys, and feedback into structured insights. Use when you have a pile of interview notes, survey responses, or support tickets to make sense of, need to extract themes and rank findings by frequency and impact, or want to turn raw feedback into roadmap recommendations.

**Tags:** `extract`, `feedback`, `findings`, `frequency`, `have`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/synthesize-research/SKILL.md`

## Qa

### claude-md-improver
Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization".

**Tags:** `against`, `asks`, `audit`, `evaluates`, `fix`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver/SKILL.md`

### explore-data
Profile and explore a dataset to understand its shape, quality, and patterns. Use when encountering a new table or file, checking null rates and column distributions, spotting data quality issues like duplicates or suspicious values, or deciding which dimensions and metrics to analyze.

**Tags:** `analyze`, `checking`, `column`, `data`, `dataset`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/explore-data/SKILL.md`

### openai-playwright
Use when the task requires automating a real browser from the terminal (navigation, form

**Tags:** `automating`, `browser`, `form`, `navigation`, `playwright`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-playwright/skills/openai-playwright/SKILL.md`

### semgrep-rule-variant-creator
Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for each language.

**Tags:** `creates`, `creator`, `directories`, `existing`, `independent`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md`

### single-cell-rna-qc
Performs quality control on single-cell RNA-seq data (.h5ad or .h5 files) using scverse best practices with MAD-based filtering and comprehensive visualizations. Use when users request QC analysis, filtering low-quality cells, assessing data quality, or following scverse/scanpy best practices for single-cell analysis.

**Tags:** `analysis`, `assessing`, `bio`, `bio-research`, `cell`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/single-cell-rna-qc/SKILL.md`

### skill-creator
Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

**Tags:** `accuracy`, `analysis`, `benchmark`, `better`, `create`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/skill-creator/SKILL.md`

### skill-creator
Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

**Tags:** `accuracy`, `analysis`, `benchmark`, `better`, `create`
**Source:** anthropic-claude-plugins-official

File: `external/anthropic-claude-plugins-official/plugins/skill-creator/skills/skill-creator/SKILL.md`

## Research

### call-summary
Process call notes or a transcript — extract action items, draft follow-up email, generate internal summary. Use when pasting rough notes or a transcript after a discovery, demo, or negotiation call, drafting a customer follow-up, logging the activity for your CRM, or capturing objections and next steps for your team.

**Tags:** `activity`, `call`, `call-summary`, `capturing`, `crm`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/call-summary/SKILL.md`

### competitive-brief
Research competitors and generate a positioning and messaging comparison with content gaps, opportunities, and threats. Use when building sales battlecards, when finding positioning gaps and messaging angles competitors haven't claimed, or when a competitor makes a move and you need to assess the impact.

**Tags:** `angles`, `assess`, `battlecards`, `brief`, `building`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/competitive-brief/SKILL.md`

### content-research-writer
>-

**Tags:** `content`, `content-research-writer`, `research`, `writer`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/content-research-writer/SKILL.md`

### customer-research
Multi-source research on a customer question or topic with source attribution. Use when a customer asks something you need to look up, investigating whether a bug has been reported before, checking what was previously told to a specific account, or gathering background before drafting a response.

**Tags:** `account`, `asks`, `attribution`, `background`, `been`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/customer-support/skills/customer-research/SKILL.md`

### digest
Generate a daily or weekly digest of activity across all connected sources. Use when catching up after time away, starting the day and wanting a summary of mentions and action items, or reviewing a week's decisions and document updates grouped by project.

**Tags:** `activity`, `away`, `catching`, `connected`, `daily`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/digest/SKILL.md`

### forecast
Generate a weighted sales forecast with best/likely/worst scenarios, commit vs. upside breakdown, and gap analysis. Use when preparing a quarterly forecast call, assessing gap-to-quota from a pipeline CSV, deciding which deals to commit vs. call upside, or checking pipeline coverage against your number.

**Tags:** `against`, `analysis`, `assessing`, `breakdown`, `call`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/forecast/SKILL.md`

### knowledge-synthesis
Combines search results from multiple sources into coherent, deduplicated answers with source attribution. Handles confidence scoring based on freshness and authority, and summarizes large result sets effectively.

**Tags:** `answers`, `attribution`, `authority`, `coherent`, `combines`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/knowledge-synthesis/SKILL.md`

### lead-research-assistant
>-

**Tags:** `lead`, `lead-research`, `research`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/lead-research-assistant/SKILL.md`

### meeting-briefing
Prepare structured briefings for meetings with legal relevance and track resulting action items. Use when preparing for contract negotiations, board meetings, compliance reviews, or any meeting where legal context, background research, or action tracking is needed.

**Tags:** `background`, `board`, `briefing`, `briefings`, `compliance`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/meeting-briefing/SKILL.md`

### memory-management
Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames, and internal language so Claude understands requests like a colleague would. CLAUDE.md for working memory, memory/ directory for the full knowledge base.

**Tags:** `acronyms`, `base`, `collaborator`, `colleague`, `decodes`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/productivity/skills/memory-management/SKILL.md`

### notion-knowledge-capture
Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking.

**Tags:** `capture`, `chats`, `conversations`, `curated`, `decisions`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/notion-knowledge-capture/SKILL.md`

### notion-meeting-intelligence
Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees.

**Tags:** `agendas`, `attendees`, `codex`, `context`, `curated`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/notion-meeting-intelligence/SKILL.md`

### openai-pdf
Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout

**Tags:** `creating`, `involve`, `layout`, `pdf`, `reading`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-pdf/skills/openai-pdf/SKILL.md`

### openai-spreadsheet
Use when tasks involve creating, editing, analyzing, or formatting spreadsheets (`.xlsx`,

**Tags:** `analyzing`, `creating`, `editing`, `formatting`, `involve`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-spreadsheet/skills/openai-spreadsheet/SKILL.md`

### pdf
Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

**Tags:** `adding`, `anything`, `apart`, `asks`, `combining`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/pdf/SKILL.md`

### skill-creator
Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations.

**Tags:** `capabilities`, `codex`, `create`, `creating`, `creator`
**Source:** openai-skills

File: `external/openai-skills/skills/.system/skill-creator/SKILL.md`

### slack-gif-creator
Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack.

**Tags:** `animated`, `animation`, `concepts`, `constraints`, `creating`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/slack-gif-creator/SKILL.md`

### slack-search
Guidance for effectively searching Slack to find messages, files, channels, and people

**Tags:** `channels`, `effectively`, `find`, `guidance`, `messages`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/slack/skills/slack-search/SKILL.md`

### variance-analysis
Decompose financial variances into drivers with narrative explanations and waterfall analysis. Use when analyzing budget vs. actual, period-over-period changes, revenue or expense variances, or preparing variance commentary for leadership.

**Tags:** `actual`, `analysis`, `analyzing`, `budget`, `changes`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/variance-analysis/SKILL.md`

### vendor-check
Check the status of existing agreements with a vendor across all connected systems — CLM, CRM, email, and document storage — with gap analysis and upcoming deadlines. Use when onboarding or renewing a vendor, when you need a consolidated view of what's signed and what's missing (MSA, DPA, SOW), or when checking for approaching expirations and surviving obligations.

**Tags:** `agreements`, `analysis`, `approaching`, `checking`, `clm`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/vendor-check/SKILL.md`

### x-research
>

**Tags:** `research`, `x-research`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/x-research/skills/x-research/SKILL.md`

## Sales

### call-prep
Prepare for a customer or prospect call using Common Room signals. Triggers on 'prep me for my call with [company]', 'prepare for a meeting with [company]', 'what should I know before talking to [company]', or any call preparation request.

**Tags:** `call`, `call-prep`, `company`, `customer`, `know`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/call-prep/SKILL.md`

### compose-outreach
Generate personalized outreach messages using Common Room signals. Triggers on 'draft outreach to [person]', 'write an email to [name]', 'compose a message for [contact]', or any outreach drafting request.

**Tags:** `compose`, `compose-outreach`, `contact`, `draft`, `drafting`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/compose-outreach/SKILL.md`

### create-an-asset
Generate tailored sales assets (landing pages, decks, one-pagers, workflow demos) from your deal context. Describe your prospect, audience, and goal — get a polished, branded asset ready to share with customers.

**Tags:** `asset`, `assets`, `audience`, `branded`, `context`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/create-an-asset/SKILL.md`

### daily-briefing
Start your day with a prioritized sales briefing. Works standalone when you tell me your meetings and priorities, supercharged when you connect your calendar, CRM, and email. Trigger with "morning briefing", "daily brief", "what's on my plate today", "prep my day", or "start my day".

**Tags:** `brief`, `briefing`, `calendar`, `connect`, `crm`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/daily-briefing/SKILL.md`

### prospect
Full ICP-to-leads pipeline. Describe your ideal customer in plain English and get a ranked table of enriched decision-maker leads with emails and phone numbers.

**Tags:** `apollo`, `customer`, `decision`, `decision-maker`, `describe`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/prospect/SKILL.md`

### prospect
Build targeted account or contact lists using Common Room's Prospector. Triggers on 'find companies that match [criteria]', 'build a prospect list', 'find contacts at [type of company]', 'show me companies hiring [role]', or any list-building request.

**Tags:** `account`, `build`, `building`, `companies`, `company`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/prospect/SKILL.md`

### recruiting-pipeline
Track and manage recruiting pipeline stages. Trigger with "recruiting update", "candidate pipeline", "how many candidates", "hiring status", or when the user discusses sourcing, screening, interviewing, or extending offers.

**Tags:** `candidate`, `candidates`, `discusses`, `extending`, `hiring`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/recruiting-pipeline/SKILL.md`

### sequence-load
Find leads matching criteria and bulk-add them to an Apollo outreach sequence. Handles enrichment, contact creation, deduplication, and enrollment in one flow.

**Tags:** `apollo`, `bulk`, `contact`, `creation`, `criteria`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/sequence-load/SKILL.md`

## Security

### algorand-vulnerability-scanner
Scans Algorand smart contracts for 11 common vulnerabilities including rekeying attacks, unchecked transaction fees, missing field validations, and access control issues. Use when auditing Algorand projects (TEAL/PyTeal).

**Tags:** `access`, `algorand`, `algorand-vulnerability-scanner`, `attacks`, `auditing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md`

### audit-augmentation
>

**Tags:** `audit`, `audit-augmentation`, `augmentation`, `trailmark`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/audit-augmentation/SKILL.md`

### burpsuite-project-parser
Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or analyzing HTTP traffic captured in a Burp project.

**Tags:** `analyzing`, `audit`, `bodies`, `burp`, `burpsuite`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md`

### cairo-vulnerability-scanner
Scans Cairo/StarkNet smart contracts for 6 critical vulnerabilities including felt252 arithmetic overflow, L1-L2 messaging issues, address conversion problems, and signature replay. Use when auditing StarkNet projects.

**Tags:** `address`, `arithmetic`, `auditing`, `building`, `building-secure-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md`

### codeql
>-

**Tags:** `analysis`, `codeql`, `static`, `static-analysis`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/static-analysis/skills/codeql/SKILL.md`

### compliance-tracking
Track compliance requirements and audit readiness. Trigger with "compliance", "audit prep", "SOC 2", "ISO 27001", "GDPR", "regulatory requirement", or when the user needs help tracking, preparing for, or documenting compliance activities.

**Tags:** `activities`, `audit`, `compliance`, `compliance-tracking`, `documenting`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/compliance-tracking/SKILL.md`

### cosmos-vulnerability-scanner
Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x.

**Tags:** `assessing`, `auditing`, `blockchain`, `building`, `building-secure-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md`

### entry-point-analyzer
Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

**Tags:** `access`, `admin`, `analyzer`, `analyzes`, `asked`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`

### fp-check
Systematically verifies suspected security bugs to eliminate false positives. Produces TRUE POSITIVE or FALSE POSITIVE verdicts with documented evidence for each bug.

**Tags:** `bug`, `bugs`, `documented`, `eliminate`, `evidence`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/fp-check/skills/fp-check/SKILL.md`

### ghidra-headless
>-

**Tags:** `ghidra`, `ghidra-headless`, `headless`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/ghidra-headless/skills/ghidra-headless/SKILL.md`

### insecure-defaults
Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling.

**Tags:** `allow`, `analyzing`, `apps`, `auditing`, `auth`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults/SKILL.md`

### mermaid-to-proverif
Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, forward secrecy), checking for replay attacks, or producing a .pv file from a sequence diagram.

**Tags:** `attacks`, `authentication`, `checking`, `converting`, `cryptographic`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif/SKILL.md`

### openai-security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements.

**Tags:** `framework`, `improvements`, `language`, `perform`, `practice`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-security-best-practices/skills/openai-security-best-practices/SKILL.md`

### openai-security-ownership-map
Analyze git repositories to build a security ownership topology (people-to-file), compute

**Tags:** `analyze`, `build`, `compute`, `git`, `map`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-security-ownership-map/skills/openai-security-ownership-map/SKILL.md`

### openai-security-threat-model
Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities,

**Tags:** `assets`, `attacker`, `boundaries`, `capabilities`, `enumerates`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-security-threat-model/skills/openai-security-threat-model/SKILL.md`

### process-doc
Document a business process — flowcharts, RACI, and SOPs. Use when formalizing a process that lives in someone's head, building a RACI to clarify who owns what, writing an SOP for a handoff or audit, or capturing the exceptions and edge cases of how work actually gets done.

**Tags:** `actually`, `audit`, `building`, `business`, `capturing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/process-doc/SKILL.md`

### sarif-parsing
>-

**Tags:** `analysis`, `parsing`, `sarif`, `sarif-parsing`, `static`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/static-analysis/skills/sarif-parsing/SKILL.md`

### secure-workflow-guide
Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas.

**Tags:** `areas`, `building`, `building-secure-contracts`, `checks`, `conformance`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide/SKILL.md`

### security-awareness
>

**Tags:** `awareness`, `security`, `security-awareness`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/security-awareness/skills/security-awareness/SKILL.md`

### semgrep
>-

**Tags:** `analysis`, `semgrep`, `static`, `static-analysis`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/static-analysis/skills/semgrep/SKILL.md`

### seo-audit
Run a comprehensive SEO audit — keyword research, on-page analysis, content gaps, technical checks, and competitor comparison. Use when assessing a site's SEO health, when finding keyword opportunities and content gaps competitors own, or when you need a prioritized action plan split into quick wins and strategic investments.

**Tags:** `analysis`, `assessing`, `audit`, `checks`, `comparison`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/seo-audit/SKILL.md`

### setup-zoom-websockets
Reference skill for Zoom WebSockets. Use after routing to a low-latency event workflow when persistent connections, faster event delivery, or security constraints make WebSockets preferable to webhooks.

**Tags:** `connections`, `constraints`, `delivery`, `event`, `faster`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/websockets/SKILL.md`

### solana-vulnerability-scanner
Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use when auditing Solana/Anchor programs.

**Tags:** `anchor`, `arbitrary`, `auditing`, `building`, `building-secure-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md`

### substrate-vulnerability-scanner
Scans Substrate/Polkadot pallets for 7 critical vulnerabilities including arithmetic overflow, panic DoS, incorrect weights, and bad origin checks. Use when auditing Substrate runtimes or FRAME pallets.

**Tags:** `arithmetic`, `auditing`, `bad`, `building`, `building-secure-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md`

### supply-chain-risk-auditor
Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagements.

**Tags:** `assessing`, `attack`, `auditor`, `chain`, `dependencies`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md`

### ton-vulnerability-scanner
Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without gas checks. Use when auditing FunC contracts.

**Tags:** `auditing`, `boolean`, `building`, `building-secure-contracts`, `checks`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md`

### yara-rule-authoring
>

**Tags:** `authoring`, `rule`, `yara`, `yara-authoring`, `yara-rule-authoring`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/yara-authoring/skills/yara-rule-authoring/SKILL.md`

## Sre

### brief
Generate contextual briefings for legal work — daily summary, topic research, or incident response. Use when starting your day and need a scan of legal-relevant items across email, calendar, and contracts, when researching a specific legal question across internal sources, or when a developing situation (data breach, litigation threat, regulatory inquiry) needs rapid context.

**Tags:** `breach`, `brief`, `briefings`, `calendar`, `context`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/brief/SKILL.md`

### internal-comms
A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

**Tags:** `asked`, `comms`, `communications`, `company`, `etc`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/internal-comms/SKILL.md`

### openai-sentry
Use when the user asks to inspect Sentry issues or events, summarize recent production errors,

**Tags:** `asks`, `errors`, `events`, `inspect`, `issues`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-sentry/skills/openai-sentry/SKILL.md`

### process-optimization
Analyze and improve business processes. Trigger with "this process is slow", "how can we improve", "streamline this workflow", "too many steps", "bottleneck", or when the user describes an inefficient process they want to fix.

**Tags:** `analyze`, `bottleneck`, `business`, `can`, `describes`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/process-optimization/SKILL.md`

### risk-assessment
Identify, assess, and mitigate operational risks. Trigger with "what are the risks", "risk assessment", "risk register", "what could go wrong", or when the user is evaluating risks associated with a project, vendor, process, or decision.

**Tags:** `assess`, `assessment`, `associated`, `could`, `decision`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/risk-assessment/SKILL.md`

### runbook
Create or update an operational runbook for a recurring task or procedure. Use when documenting a task that on-call or ops needs to run repeatably, turning tribal knowledge into exact step-by-step commands, adding troubleshooting and rollback steps to an existing procedure, or writing escalation paths for when things go wrong.

**Tags:** `adding`, `call`, `commands`, `create`, `documenting`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/runbook/SKILL.md`

### sentry
Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; perform read-only queries using the `sentry` command.

**Tags:** `asks`, `basic`, `cli`, `command`, `curated`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/sentry/SKILL.md`

### status-report
Generate a status report with KPIs, risks, and action items. Use when writing a weekly or monthly update for leadership, summarizing project health with green/yellow/red status, surfacing risks and decisions that need stakeholder attention, or turning a pile of project tracker activity into a readable narrative.

**Tags:** `activity`, `attention`, `decisions`, `green`, `health`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/status-report/SKILL.md`

## Other

### access
Manage Discord channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Discord channel.

**Tags:** access, allowed, allowlists, approve, asks
**Source:** anthropic-claude-plugins-official

### access
Manage iMessage channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the iMessage channel.

**Tags:** access, allowed, allowlists, approve, asks
**Source:** anthropic-claude-plugins-official

### access
Manage Telegram channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Telegram channel.

**Tags:** access, allowed, allowlists, approve, asks
**Source:** anthropic-claude-plugins-official

### add-remote-skill
This skill should be used when the user wants to add one or more skills from GitHub repositories to the kilo-marketplace. It handles parsing GitHub URLs, cloning skill directories, and updating SKILL.md frontmatter with source metadata.

**Tags:** cloning, directories, frontmatter, github, handles
**Source:** kilo-marketplace-skills

### angular-component
>-

**Tags:** angular, angular-component, component
**Source:** kilo-marketplace-skills

### angular-di
>-

**Tags:** angular, angular-di
**Source:** kilo-marketplace-skills

### angular-directives
>-

**Tags:** angular, angular-directives, directives
**Source:** kilo-marketplace-skills

### angular-forms
>-

**Tags:** angular, angular-forms, forms
**Source:** kilo-marketplace-skills

### angular-http
>-

**Tags:** angular, angular-http, http
**Source:** kilo-marketplace-skills

### angular-routing
>-

**Tags:** angular, angular-routing, routing
**Source:** kilo-marketplace-skills

### angular-signals
>-

**Tags:** angular, angular-signals, signals
**Source:** kilo-marketplace-skills

### angular-ssr
>-

**Tags:** angular, angular-ssr, ssr
**Source:** kilo-marketplace-skills

### angular-tooling
>-

**Tags:** angular, angular-tooling, tooling
**Source:** kilo-marketplace-skills

### artifacts-builder
>-

**Tags:** artifacts, artifacts-builder, builder
**Source:** kilo-marketplace-skills

### ask-questions-if-underspecified
Clarify requirements before implementing. Use when serious doubts arise.

**Tags:** arise, ask, ask-questions-if-underspecified, clarify, doubts
**Source:** trailofbits-skills

### build-zoom-meeting-sdk-app
Reference skill for Zoom Meeting SDK. Use after routing to a meeting-embed workflow when implementing real Zoom meeting joins, platform-specific SDK behavior, auth and join flows, waiting room issues, or meeting bot patterns.

**Tags:** app, auth, behavior, bot, build
**Source:** anthropic-knowledge-work-plugins

### build-zoom-phone-integration
Reference skill for Zoom Phone. Use after routing to a phone workflow when implementing OAuth, Phone APIs, webhooks, Smart Embed events, URI schemes, CRM or CTI dialers, or call handling automation.

**Tags:** apis, automation, build, build-zoom-phone-integration, call
**Source:** anthropic-knowledge-work-plugins

### build-zoom-team-chat-app
Reference skill for Zoom Team Chat. Use after routing to a chat workflow when building user-scoped messaging integrations, chatbot experiences, rich cards, buttons, slash commands, or chat webhooks.

**Tags:** app, build, build-zoom-team-chat-app, building, buttons
**Source:** anthropic-knowledge-work-plugins

### build-zoom-video-sdk-app
Reference skill for Zoom Video SDK. Use after routing to a custom-session workflow when the user needs full control over the video experience rather than an actual Zoom meeting.

**Tags:** actual, app, build, build-zoom-video-sdk-app, control
**Source:** anthropic-knowledge-work-plugins

### cardputer-buddy
Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already provisioned via m5-onboard. Use when the user wants to add a new app, push a single changed .py without re-flashing, watch device serial logs, or run a one-shot REPL command. Trigger on "add an app", "push to the cardputer", "tail the device", "run on the device", or follow-up work after /maker-setup.

**Tags:** adv, already, app, buddy, bundle
**Source:** anthropic-claude-plugins-official

### changelog-generator
>-

**Tags:** changelog, changelog-generator, generator
**Source:** kilo-marketplace-skills

### cowork-plugin-customizer
>

**Tags:** cowork, cowork-customizer, cowork-management, customizer, management
**Source:** anthropic-knowledge-work-plugins

### create-cowork-plugin
>

**Tags:** cowork, cowork-management, create, create-cowork, management
**Source:** anthropic-knowledge-work-plugins

### create-pull-request
>-

**Tags:** create, create-pull-request, pull, request
**Source:** kilo-marketplace-skills

### docx
Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

**Tags:** asks, changes, coding, comments, content
**Source:** anthropic-skills

### domain-name-brainstormer
>-

**Tags:** brainstormer, domain, domain-brainstormer
**Source:** kilo-marketplace-skills

### draft-offer
Draft an offer letter with comp details and terms. Use when a candidate is ready for an offer, assembling a total comp package (base, equity, signing bonus), writing the offer letter text itself, or prepping negotiation guidance for the hiring manager.

**Tags:** assembling, base, bonus, candidate, comp
**Source:** anthropic-knowledge-work-plugins

### example-command
An example user-invoked skill that demonstrates frontmatter options and the skills/<name>/SKILL.md layout

**Tags:** command, demonstrates, frontmatter, invoked, layout
**Source:** anthropic-claude-plugins-official

### file-organizer
>-

**Tags:** organizer
**Source:** kilo-marketplace-skills

### git-cleanup
Safely analyzes and cleans up local git branches and worktrees by categorizing them as merged, squash-merged, superseded, or active work.

**Tags:** active, analyzes, branches, categorizing, cleans
**Source:** trailofbits-skills

### graph-evolution
>

**Tags:** evolution, graph, graph-evolution, trailmark
**Source:** trailofbits-skills

### grill-me
>-

**Tags:** grill, grill-me
**Source:** kilo-marketplace-skills

### humanizer
|

**Tags:** humanizer
**Source:** trailofbits-skills-curated

### image-enhancer
>-

**Tags:** enhancer, image, image-enhancer
**Source:** kilo-marketplace-skills

### internal-comms
>-

**Tags:** comms, internal, internal-comms
**Source:** kilo-marketplace-skills

### interview-prep
Create structured interview plans with competency-based questions and scorecards. Trigger with "interview plan for", "interview questions for", "how should we interview", "scorecard for", or when the user is preparing to interview candidates.

**Tags:** candidates, competency, create, human, interview
**Source:** anthropic-knowledge-work-plugins

### jupyter-notebook
Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and run the helper script `new_notebook.py` to generate a clean starting notebook.

**Tags:** asks, bundled, clean, create, curated
**Source:** openai-skills

### langsmith-fetch
>-

**Tags:** fetch, langsmith, langsmith-fetch
**Source:** kilo-marketplace-skills

### linear
Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets in Linear.

**Tags:** create, curated, issues, linear, manage
**Source:** openai-skills

### m5-onboard
End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer, Cardputer-Adv, Core, CoreS3, Stick) — detect on USB, flash UIFlow 2.0 firmware, and install the Claude Buddy MicroPython app bundle. Use whenever the user plugs in or wants to flash/provision/reset an M5Stack or ESP32 board, or says "m5-onboard go".

**Tags:** adv, app, board, buddy, bundle
**Source:** anthropic-claude-plugins-official

### math-olympiad
No description.

**Tags:** math, math-olympiad, olympiad
**Source:** anthropic-claude-plugins-official

### meeting-insights-analyzer
>-

**Tags:** analyzer, insights, meeting, meeting-insights-analyzer
**Source:** kilo-marketplace-skills

### migrating-dbt-core-to-fusion
Classifies dbt-core to Fusion migration errors into actionable categories (auto-fixable, guided fixes, needs input, blocked). Use when a user needs help triaging migration errors to understand what they can fix vs what requires Fusion engine updates.

**Tags:** actionable, auto, auto-fixable, blocked, can
**Source:** kilo-marketplace-skills

### onboarding
Generate an onboarding checklist and first-week plan for a new hire. Use when someone has a start date coming up, building the pre-start task list (accounts, equipment, buddy), scheduling Day 1 and Week 1, or setting 30/60/90-day goals for a new team member.

**Tags:** accounts, buddy, building, checklist, coming
**Source:** anthropic-knowledge-work-plugins

### openai-doc
Use when the task involves reading, creating, or editing `.docx` documents, especially when

**Tags:** creating, doc, documents, docx, editing
**Source:** trailofbits-skills-curated

### openai-jupyter-notebook
Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments,

**Tags:** asks, create, edit, experiments, ipynb
**Source:** trailofbits-skills-curated

### openai-screenshot
Use when the user explicitly asks for a desktop or system screenshot (full screen, specific

**Tags:** asks, desktop, explicitly, full, screen
**Source:** trailofbits-skills-curated

### openai-yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request

**Tags:** asks, commit, explicitly, github, open
**Source:** trailofbits-skills-curated

### plugin-settings
This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content.

**Tags:** asks, behavior, configurable, configuration, content
**Source:** anthropic-claude-plugins-official

### policy-lookup
Find and explain company policies in plain language. Trigger with "what's our PTO policy", "can I work remotely from another country", "how do expenses work", or any plain-language question about benefits, travel, leave, or handbook rules.

**Tags:** another, benefits, can, company, country
**Source:** anthropic-knowledge-work-plugins

### running-dbt-commands
Formats and executes dbt CLI commands, selects the correct dbt executable, and structures command parameters. Use when running models, tests, builds, compiles, or show queries via dbt CLI. Use when unsure which dbt executable to use or how to format command parameters.

**Tags:** builds, cli, command, commands, compiles
**Source:** kilo-marketplace-skills

### screenshot
Use when the user explicitly asks for a desktop or system screenshot (full screen, specific app or window, or a pixel region), or when tool-specific capture capabilities are unavailable and an OS-level capture is needed.

**Tags:** app, asks, capabilities, capture, curated
**Source:** openai-skills

### seatbelt-sandboxer
Generates minimal macOS Seatbelt sandbox configurations. Use when sandboxing, isolating, or restricting macOS applications with allowlist-based profiles.

**Tags:** allowlist, applications, configurations, generates, isolating
**Source:** trailofbits-skills

### setup-zoom-webhooks
Reference skill for Zoom webhooks. Use after routing to an event-driven workflow when implementing subscriptions, signature verification, delivery handling, retries, or event-type selection.

**Tags:** delivery, driven, event, event-driven, handling
**Source:** anthropic-knowledge-work-plugins

### skill-creator
>-

**Tags:** creator
**Source:** kilo-marketplace-skills

### skill-extractor
>-

**Tags:** extractor
**Source:** trailofbits-skills-curated

### skill-installer
Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).

**Tags:** another, asks, codex, codex-home, curated
**Source:** openai-skills

### skill-share
>-

**Tags:** share
**Source:** kilo-marketplace-skills

### slack-gif-creator
>-

**Tags:** creator, gif, slack, slack-gif-creator
**Source:** kilo-marketplace-skills

### slack-messaging
Guidance for composing well-formatted, effective Slack messages using mrkdwn syntax

**Tags:** composing, effective, formatted, guidance, messages
**Source:** anthropic-knowledge-work-plugins

### theme-factory
>-

**Tags:** factory, theme, theme-factory
**Source:** kilo-marketplace-skills

### video-sdk/windows
Zoom Video SDK for Windows - C++ integration for video sessions, raw audio/video capture, screen sharing, recording, and real-time communication

**Tags:** audio, capture, communication, integration, partner
**Source:** anthropic-knowledge-work-plugins

### wooyun-legacy
>-

**Tags:** legacy, wooyun, wooyun-legacy
**Source:** trailofbits-skills-curated

### writing-hookify-rules
This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns.

**Tags:** asks, configure, create, guidance, hook
**Source:** anthropic-claude-plugins-official

### yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).

**Tags:** asks, cli, commit, curated, explicitly
**Source:** openai-skills

### youtube-downloader
>-

**Tags:** downloader, youtube, youtube-downloader
**Source:** kilo-marketplace-skills

### zoom-meeting-sdk-electron
|

**Tags:** electron, meeting, meeting-sdk, partner, sdk
**Source:** anthropic-knowledge-work-plugins

### zoom-meeting-sdk-macos
|

**Tags:** macos, meeting, meeting-sdk, partner, sdk
**Source:** anthropic-knowledge-work-plugins

### zoom-meeting-sdk-unreal
|

**Tags:** meeting, meeting-sdk, partner, sdk, unreal
**Source:** anthropic-knowledge-work-plugins

### zoom-meeting-sdk-windows
|

**Tags:** meeting, meeting-sdk, partner, sdk, windows
**Source:** anthropic-knowledge-work-plugins

### zoom-rtms
Reference skill for Zoom RTMS. Use after routing to a live-media workflow when processing real-time audio, video, chat, transcripts, screen share, or contact-center voice streams.

**Tags:** audio, center, chat, contact, contact-center
**Source:** anthropic-knowledge-work-plugins

### zoom-video-sdk-flutter
|

**Tags:** flutter, partner, sdk, video, video-sdk
**Source:** anthropic-knowledge-work-plugins

### zoom-video-sdk-macos
|

**Tags:** macos, partner, sdk, video, video-sdk
**Source:** anthropic-knowledge-work-plugins

### zoom-video-sdk-unity
|

**Tags:** partner, sdk, unity, video, video-sdk
**Source:** anthropic-knowledge-work-plugins
