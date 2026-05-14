# development

## Skills
Select only the most relevant skills by description, then read only those `SKILL.md` files.

### agent-md-refactor
Refactor bloated AGENTS.md, CLAUDE.md, or similar agent instruction files to follow progressive disclosure principles. Splits monolithic files into organized, linked documentation.

File: `external/kilo-marketplace-skills/skills/agent-md-refactor/SKILL.md`

### angular-component
Create modern Angular standalone components following v20+ best practices. Use for building UI components with signal-based inputs/outputs, OnPush change detection, host bindings, content projection, and lifecycle hooks. Triggers on component creation, refactoring class-based inputs to signals, adding host bindings, or implementing accessible interactive components.

File: `external/kilo-marketplace-skills/skills/angular-component/SKILL.md`

### angular-di
Implement dependency injection in Angular v20+ using inject(), injection tokens, and provider configuration. Use for service architecture, providing dependencies at different levels, creating injectable tokens, and managing singleton vs scoped services. Triggers on service creation, configuring providers, using injection tokens, or understanding DI hierarchy.

File: `external/kilo-marketplace-skills/skills/angular-di/SKILL.md`

### angular-directives
Create custom directives in Angular v20+ for DOM manipulation and behavior extension. Use for attribute directives that modify element behavior/appearance, structural directives for portals/overlays, and host directives for composition. Triggers on creating reusable DOM behaviors, extending element functionality, or composing behaviors across components. Note - use native @if/@for/@switch for control flow, not custom structural directives.

File: `external/kilo-marketplace-skills/skills/angular-directives/SKILL.md`

### angular-forms
Build signal-based forms in Angular v21+ using the new Signal Forms API. Use for form creation with automatic two-way binding, schema-based validation, field state management, and dynamic forms. Triggers on form implementation, adding validation, creating multi-step forms, or building forms with conditional fields. Signal Forms are experimental but recommended for new Angular projects. Don't use for template-driven forms without signals or third-party form libraries like Formly or ngx-formly.

File: `external/kilo-marketplace-skills/skills/angular-forms/SKILL.md`

### angular-http
Implement HTTP data fetching in Angular v20+ using resource(), httpResource(), and HttpClient. Use for API calls, data loading with signals, request/response handling, and interceptors. Triggers on data fetching, API integration, loading states, error handling, or converting Observable-based HTTP to signal-based patterns.

File: `external/kilo-marketplace-skills/skills/angular-http/SKILL.md`

### angular-routing
Implement routing in Angular v20+ applications with lazy loading, functional guards, resolvers, and route parameters. Use for navigation setup, protected routes, route-based data loading, and nested routing. Triggers on route configuration, adding authentication guards, implementing lazy loading, or reading route parameters with signals.

File: `external/kilo-marketplace-skills/skills/angular-routing/SKILL.md`

### angular-signals
Implement signal-based reactive state management in Angular v20+. Use for creating reactive state with signal(), derived state with computed(), dependent state with linkedSignal(), and side effects with effect(). Triggers on state management questions, converting from BehaviorSubject/Observable patterns to signals, or implementing reactive data flows.

File: `external/kilo-marketplace-skills/skills/angular-signals/SKILL.md`

### angular-ssr
Implement server-side rendering and hydration in Angular v20+ using @angular/ssr. Use for SSR setup, hydration strategies, prerendering static pages, and handling browser-only APIs. Triggers on SSR configuration, fixing hydration mismatches, prerendering routes, or making code SSR-compatible.

File: `external/kilo-marketplace-skills/skills/angular-ssr/SKILL.md`

### angular-testing
Write unit and integration tests for Angular v20+ applications using Vitest or Jasmine with TestBed and modern testing patterns. Use for testing components with signals, OnPush change detection, services with inject(), and HTTP interactions. Triggers on test creation, testing signal-based components, mocking dependencies, or setting up test infrastructure. Don't use for E2E testing with Cypress or Playwright, or for testing non-Angular JavaScript/TypeScript code.

File: `external/kilo-marketplace-skills/skills/angular-testing/SKILL.md`

### angular-tooling
Use Angular CLI and development tools effectively in Angular v20+ projects. Use for project setup, code generation, building, testing, and configuration. Triggers on creating new projects, generating components/services/modules, configuring builds, running tests, or optimizing production builds. Don't use for Nx workspace commands, custom Webpack configurations, or non-Angular CLI build systems like Vite standalone or esbuild direct usage.

File: `external/kilo-marketplace-skills/skills/angular-tooling/SKILL.md`

### artifacts-builder
Suite of tools for creating elaborate, multi-component HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

File: `external/kilo-marketplace-skills/skills/artifacts-builder/SKILL.md`

### aspnet-core
Build, review, refactor, or architect ASP.NET Core web applications using current official guidance for .NET web development. Use when working on Blazor Web Apps, Razor Pages, MVC, Minimal APIs, controller-based Web APIs, SignalR, gRPC, middleware, dependency injection, configuration, authentication, authorization, testing, performance, deployment, or ASP.NET Core upgrades.

File: `external/openai-skills/skills/.curated/aspnet-core/SKILL.md`

### brainstorming
You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation.

File: `external/superpowers-skills/skills/brainstorming/SKILL.md`

### changelog-generator
Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical commits into clear, customer-friendly release notes. Turns hours of manual changelog writing into minutes of automated generation.

File: `external/kilo-marketplace-skills/skills/changelog-generator/SKILL.md`

### chatgpt-apps
Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold. Prefer a docs-first workflow by invoking the openai-docs skill or OpenAI developer docs MCP tools before generating code.

File: `external/openai-skills/skills/.curated/chatgpt-apps/SKILL.md`

### claude-api
Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

File: `external/anthropic-skills/skills/claude-api/SKILL.md`

### cli-creator
Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

File: `external/openai-skills/skills/.curated/cli-creator/SKILL.md`

### create-cowork-plugin
Guide users through creating a new plugin from scratch in a cowork session. Use when users want to create a plugin, build a plugin, make a new plugin, develop a plugin, scaffold a plugin, start a plugin from scratch, or design a plugin. This skill requires Cowork mode with access to the outputs directory for delivering the final .plugin file.

File: `external/anthropic-knowledge-work-plugins/cowork-plugin-management/skills/create-cowork-plugin/SKILL.md`

### dbt
Skills for analytics engineering with dbt - building models, writing tests, querying the semantic layer, troubleshooting jobs, and more. Use when doing any dbt analytics engineering work.

File: `external/kilo-marketplace-skills/skills/dbt/SKILL.md`

### dbt-migration
Skills for migrating dbt projects - moving from dbt Core to the Fusion engine or across data platforms. Use when migrating dbt projects between platforms or to dbt Fusion.

File: `external/kilo-marketplace-skills/skills/dbt-migration/SKILL.md`

### devcontainer-setup
Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configuring sandboxed Claude Code workspaces.

File: `external/trailofbits-skills/plugins/devcontainer-setup/skills/devcontainer-setup/SKILL.md`

### executing-plans
Use when you have a written implementation plan to execute in a separate session with review checkpoints

File: `external/superpowers-skills/skills/executing-plans/SKILL.md`

### finishing-a-development-branch
Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup

File: `external/superpowers-skills/skills/finishing-a-development-branch/SKILL.md`

### frontend-design
Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

File: `external/anthropic-skills/skills/frontend-design/SKILL.md`

### frontend-design
Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

File: `external/kilo-marketplace-skills/skills/frontend-design/SKILL.md`

### grill-me
Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".

File: `external/kilo-marketplace-skills/skills/grill-me/SKILL.md`

### jupyter-notebook
Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and run the helper script `new_notebook.py` to generate a clean starting notebook.

File: `external/openai-skills/skills/.curated/jupyter-notebook/SKILL.md`

### langsmith-fetch
Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio. Use when debugging agent behavior, investigating errors, analyzing tool calls, checking memory operations, or examining agent performance. Automatically fetches recent traces and analyzes execution patterns. Requires langsmith-fetch CLI installed.

File: `external/kilo-marketplace-skills/skills/langsmith-fetch/SKILL.md`

### mcp-builder
Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

File: `external/anthropic-skills/skills/mcp-builder/SKILL.md`

### modern-python
Configures Python projects with modern tooling (uv, ruff, ty). Use when creating projects, writing standalone scripts, or migrating from pip/Poetry/mypy/black.

File: `external/trailofbits-skills/plugins/modern-python/skills/modern-python/SKILL.md`

### openai-develop-web-game
'Use when the agent is building or iterating on a web game (HTML/JS) and needs a reliable

File: `external/trailofbits-skills-curated/plugins/openai-develop-web-game/skills/openai-develop-web-game/SKILL.md`

### openai-jupyter-notebook
Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments,

File: `external/trailofbits-skills-curated/plugins/openai-jupyter-notebook/skills/openai-jupyter-notebook/SKILL.md`

### openai-security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements.

File: `external/trailofbits-skills-curated/plugins/openai-security-best-practices/skills/openai-security-best-practices/SKILL.md`

### playwright-interactive
Persistent browser and Electron interaction through `js_repl` for fast iterative UI debugging.

File: `external/openai-skills/skills/.curated/playwright-interactive/SKILL.md`

### plugin-creator
Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders you can edit before publishing or testing. Use when Codex needs to create a new local plugin, add optional plugin structure, or generate or update repo-root `.agents/plugins/marketplace.json` entries for plugin ordering and availability metadata.

File: `external/openai-skills/skills/.system/plugin-creator/SKILL.md`

### receiving-code-review
Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation

File: `external/superpowers-skills/skills/receiving-code-review/SKILL.md`

### security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

File: `external/openai-skills/skills/.curated/security-best-practices/SKILL.md`

### skill-creator
Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

File: `external/anthropic-skills/skills/skill-creator/SKILL.md`

### skill-creator
Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Kilo's capabilities with specialized knowledge, workflows, or tool integrations.

File: `external/kilo-marketplace-skills/skills/skill-creator/SKILL.md`

### skill-creator
Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations.

File: `external/openai-skills/skills/.system/skill-creator/SKILL.md`

### skill-share
A skill that creates new agent skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery.

File: `external/kilo-marketplace-skills/skills/skill-share/SKILL.md`

### subagent-driven-development
Use when executing implementation plans with independent tasks in the current session

File: `external/superpowers-skills/skills/subagent-driven-development/SKILL.md`

### systematic-debugging
Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes

File: `external/superpowers-skills/skills/systematic-debugging/SKILL.md`

### test-driven-development
Use when implementing any feature or bugfix, before writing implementation code

File: `external/superpowers-skills/skills/test-driven-development/SKILL.md`

### using-git-worktrees
Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback

File: `external/superpowers-skills/skills/using-git-worktrees/SKILL.md`

### vercel-composition-patterns
React composition patterns that scale. Use when refactoring components with boolean prop proliferation, building flexible component libraries, or designing reusable APIs. Triggers on tasks involving compound components, render props, context providers, or component architecture. Includes React 19 API changes.

File: `external/kilo-marketplace-skills/skills/vercel-composition-patterns/SKILL.md`

### vercel-react-best-practices
React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.

File: `external/kilo-marketplace-skills/skills/vercel-react-best-practices/SKILL.md`

### verification-before-completion
Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always

File: `external/superpowers-skills/skills/verification-before-completion/SKILL.md`

### web-artifacts-builder
Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

File: `external/anthropic-skills/skills/web-artifacts-builder/SKILL.md`

### web-design-guidelines
Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".

File: `external/kilo-marketplace-skills/skills/web-design-guidelines/SKILL.md`

### webapp-testing
Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

File: `external/kilo-marketplace-skills/skills/webapp-testing/SKILL.md`

### winui-app
Bootstrap, develop, and design modern WinUI 3 desktop applications with C# and the Windows App SDK using official Microsoft guidance, WinUI Gallery patterns, Windows App SDK samples, and CommunityToolkit components. Use when creating a brand new app, preparing a machine for WinUI, reviewing, refactoring, planning, troubleshooting, environment-checking, or setting up WinUI 3 XAML, controls, navigation, windowing, theming, accessibility, responsiveness, performance, deployment, or related Windows app design and development work.

File: `external/openai-skills/skills/.curated/winui-app/SKILL.md`

### write-spec
Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user request into a structured document, scoping a feature with goals and non-goals, defining success metrics and acceptance criteria, or breaking a big ask into a phased spec.

File: `external/anthropic-knowledge-work-plugins/product-management/skills/write-spec/SKILL.md`

### writing-plans
Use when you have a spec or requirements for a multi-step task, before touching code

File: `external/superpowers-skills/skills/writing-plans/SKILL.md`
