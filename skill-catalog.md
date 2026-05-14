# Skill Catalog

This is a generated human-readable view. Edit `enabled` and `keywords` in `skill-catalog.d/*.yaml`.

Total: 413 skills across 33 categories
Enabled: 308; Disabled: 105

## Ai

### agentic-actions-auditor
Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor`
**Keywords:** `ai`, `audit`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`

### algorithmic-art
Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/algorithmic-art`
**Keywords:** `ai`, `creative-media`, `imagegen`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/algorithmic-art/SKILL.md`

### artifacts-builder
Suite of tools for creating elaborate, multi-component HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/artifacts-builder`
**Keywords:** `ai`, `development`, `frontend`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/artifacts-builder/SKILL.md`

### canvas-design
Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/canvas-design`
**Keywords:** `ai`, `creative-media`, `design`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/canvas-design/SKILL.md`

### canvas-design
Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/canvas-design`
**Keywords:** `ai`, `creative`, `creative-media`, `design`, `frontend`, `media`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/canvas-design/SKILL.md`

### claude-api
Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/claude-api`
**Keywords:** `ai`, `claude-api`, `development`, `rest-api`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/claude-api/SKILL.md`

### docx
Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/docx`
**Keywords:** `ai`, `documents`, `docx`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/docx/SKILL.md`

### figma-generate-design
Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/figma-generate-design`
**Keywords:** `ai`, `design`, `figma`, `imagegen`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`

### grill-me
Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/grill-me`
**Keywords:** `ai`, `development`, `interviewing`, `research`, `testing`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/grill-me/SKILL.md`

### hatch-pet
Create, repair, validate, preview, and package Codex-compatible animated pets and pet spritesheets from character art, screenshots, generated images, or visual references. Use when a user wants to hatch a Codex pet, create a custom animated pet, or build a built-in pet asset with an 8x9 atlas, transparent unused cells, row-by-row animation prompts, QA contact sheets, preview videos, and pet.json packaging. This skill composes the installed $imagegen system skill for visual generation and uses bundled scripts for deterministic spritesheet assembly.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/hatch-pet`
**Keywords:** `ai`, `creative-media`, `imagegen`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/hatch-pet/SKILL.md`

### image-enhancer
Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clarity. Perfect for preparing images for presentations, documentation, or social media posts.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/image-enhancer`
**Keywords:** `ai`, `creative`, `creative-media`, `imagegen`, `media`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/image-enhancer/SKILL.md`

### imagegen
Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.system/imagegen`
**Keywords:** `ai`, `design`, `imagegen`
**Source:** openai-skills

File: `external/openai-skills/skills/.system/imagegen/SKILL.md`

### langsmith-fetch
Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio. Use when debugging agent behavior, investigating errors, analyzing tool calls, checking memory operations, or examining agent performance. Automatically fetches recent traces and analyzes execution patterns. Requires langsmith-fetch CLI installed.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/langsmith-fetch`
**Keywords:** `ai`, `development`, `langsmith`, `sentry`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/langsmith-fetch/SKILL.md`

### mcp-builder
Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/mcp-builder`
**Keywords:** `ai`, `development`, `mcp`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/mcp-builder/SKILL.md`

### notion-meeting-intelligence
Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/notion-meeting-intelligence`
**Keywords:** `ai`, `meeting`, `notion`, `productivity`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/notion-meeting-intelligence/SKILL.md`

### openai-doc
Use when the task involves reading, creating, or editing `.docx` documents, especially when

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-doc/skills/openai-doc`
**Keywords:** `ai`, `documents`, `docx`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-doc/skills/openai-doc/SKILL.md`

### openai-pdf
Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-pdf/skills/openai-pdf`
**Keywords:** `ai`, `documents`, `pdf`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-pdf/skills/openai-pdf/SKILL.md`

### pdf
Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/pdf`
**Keywords:** `ai`, `documents`, `pdf`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/pdf/SKILL.md`

### pdf
Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/pdf`
**Keywords:** `ai`, `documents`, `pdf`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/pdf/SKILL.md`

### plugin-creator
Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders you can edit before publishing or testing. Use when Codex needs to create a new local plugin, add optional plugin structure, or generate or update repo-root `.agents/plugins/marketplace.json` entries for plugin ordering and availability metadata.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.system/plugin-creator`
**Keywords:** `ai`, `development`, `plugin`
**Source:** openai-skills

File: `external/openai-skills/skills/.system/plugin-creator/SKILL.md`

### pptx
Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions "deck," "slides," "presentation," or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/pptx`
**Keywords:** `ai`, `documents`, `pptx`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/pptx/SKILL.md`

### skill-creator
Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.system/skill-creator`
**Keywords:** `ai`, `development`, `skill-creator`
**Source:** openai-skills

File: `external/openai-skills/skills/.system/skill-creator/SKILL.md`

### slack-gif-creator
Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack."

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/slack-gif-creator`
**Keywords:** `ai`, `creative-media`, `slack`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/slack-gif-creator/SKILL.md`

### slack-gif-creator
Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives. This skill applies when users request animated GIFs or emoji animations for Slack from descriptions like "make me a GIF for Slack of X doing Y".

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/slack-gif-creator`
**Keywords:** `ai`, `creative`, `creative-media`, `media`, `slack`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/slack-gif-creator/SKILL.md`

### speech
Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for live calls. Custom voice creation is out of scope.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/speech`
**Keywords:** `ai`, `speech`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/speech/SKILL.md`

### theme-factory
Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/theme-factory`
**Keywords:** `ai`, `design`, `theme`, `ui`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/theme-factory/SKILL.md`

### theme-factory
Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/theme-factory`
**Keywords:** `ai`, `creative`, `creative-media`, `design`, `media`, `theme`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/theme-factory/SKILL.md`

### transcribe
Transcribe audio files to text with optional diarization and known-speaker hints. Use when a user asks to transcribe speech from audio/video, extract text from recordings, or label speakers in interviews or meetings.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/transcribe`
**Keywords:** `ai`, `speech`, `transcribe`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/transcribe/SKILL.md`

### web-artifacts-builder
Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/web-artifacts-builder`
**Keywords:** `ai`, `development`, `frontend`, `react`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/web-artifacts-builder/SKILL.md`

### webapp-testing
Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/webapp-testing`
**Keywords:** `ai`, `playwright`, `testing`, `web`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/webapp-testing/SKILL.md`

### xlsx
Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like "the xlsx in my downloads") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/xlsx`
**Keywords:** `ai`, `data`, `xlsx`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/xlsx/SKILL.md`

## Core

### accessibility-review
Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "is this accessible?", or when reviewing a design for color contrast, keyboard navigation, touch target size, or screen reader behavior before handoff.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/design/skills/accessibility-review`
**Keywords:** `accessibility`, `audit`, `design`, `review`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/accessibility-review/SKILL.md`

### add-remote-skill
This skill should be used when the user wants to add one or more skills from GitHub repositories to the kilo-marketplace. It handles parsing GitHub URLs, cloning skill directories, and updating SKILL.md frontmatter with source metadata.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/.kilocode/skills/add-remote-skill`
**Keywords:** `integration`, `skill-creator`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/.kilocode/skills/add-remote-skill/SKILL.md`

### agent-md-refactor
Refactor bloated AGENTS.md, CLAUDE.md, or similar agent instruction files to follow progressive disclosure principles. Splits monolithic files into organized, linked documentation.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/agent-md-refactor`
**Keywords:** `agent`, `ai`, `development`, `documentation`, `refactor`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/agent-md-refactor/SKILL.md`

### analyze
Answer data questions -- from quick lookups to full analyses. Use when looking up a single metric, investigating what's driving a trend or drop, comparing segments over time, or preparing a formal data report for stakeholders.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/data/skills/analyze`
**Keywords:** `analysis`, `analytics`, `data`, `metrics`, `reporting`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/analyze/SKILL.md`

### architecture
Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decision with trade-offs and consequences, reviewing a system design proposal, or designing a new component from requirements and constraints.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/engineering/skills/architecture`
**Keywords:** `architecture`, `design`, `engineering`, `planning`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/architecture/SKILL.md`

### ask-questions-if-underspecified
Clarify requirements before implementing. Use when serious doubts arise.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/ask-questions-if-underspecified/skills/ask-questions-if-underspecified`
**Keywords:** `ai`, `research`, `workflow`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/ask-questions-if-underspecified/skills/ask-questions-if-underspecified/SKILL.md`

### audit-context-building
Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/audit-context-building/skills/audit-context-building`
**Keywords:** `analysis`, `audit`, `security`, `smart-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/audit-context-building/skills/audit-context-building/SKILL.md`

### audit-prep-assistant
Prepares codebases for security review using Trail of Bits' checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation (flowcharts, user stories, inline comments).

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant`
**Keywords:** `audit`, `planning`, `security`, `smart-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md`

### brainstorming
You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation.

**Enabled:** `true`
**ID:** `external/superpowers-skills/skills/brainstorming`
**Keywords:** `architecture`, `brainstorming`, `design`, `development`, `planning`, `requirements`, `spec`, `user-research`, `workflow`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/brainstorming/SKILL.md`

### brand-guidelines
Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/brand-guidelines`
**Keywords:** `ai`, `brand`, `design`, `documentation`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/brand-guidelines/SKILL.md`

### brand-review
Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixes. Use when checking a draft before it ships, when auditing copy for voice consistency and terminology, or when screening for unsubstantiated claims, missing disclaimers, and other legal flags.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/marketing/skills/brand-review`
**Keywords:** `brand`, `content`, `marketing`, `review`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/brand-review/SKILL.md`

### brief
Generate contextual briefings for legal work — daily summary, topic research, or incident response. Use when starting your day and need a scan of legal-relevant items across email, calendar, and contracts, when researching a specific legal question across internal sources, or when a developing situation (data breach, litigation threat, regulatory inquiry) needs rapid context.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/legal/skills/brief`
**Keywords:** `documents`, `legal`, `research`, `summarization`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/brief/SKILL.md`

### build-zoom-bot
Build a Zoom meeting bot, recorder, or real-time media workflow. Use when joining meetings programmatically, processing live media or transcripts, or combining Meeting SDK, RTMS, and backend services.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-bot`
**Keywords:** `bot`, `development`, `integration`, `media`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-bot/SKILL.md`

### build-zoom-contact-center-app
Reference skill for Zoom Contact Center. Use after routing to a contact-center workflow when implementing app, web, or native integrations; engagement context and state handling; campaigns; callbacks; or version-drift troubleshooting.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center`
**Keywords:** `contact-center`, `development`, `integration`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/SKILL.md`

### build-zoom-meeting-app
Build or embed a Zoom meeting flow. Use when implementing Meeting SDK joins, web or mobile meeting embeds, meeting lifecycle flows, or when deciding between Meeting SDK and Video SDK.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-meeting-app`
**Keywords:** `development`, `integration`, `meeting`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-meeting-app/SKILL.md`

### build-zoom-phone-integration
Reference skill for Zoom Phone. Use after routing to a phone workflow when implementing OAuth, Phone APIs, webhooks, Smart Embed events, URI schemes, CRM or CTI dialers, or call handling automation.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/phone`
**Keywords:** `development`, `integration`, `phone`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/phone/SKILL.md`

### build-zoom-rest-api-app
Reference skill for Zoom REST API. Use after choosing an API-based workflow when you need endpoint selection, resource-management patterns, OAuth requirements, rate-limit awareness, or API error debugging.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rest-api`
**Keywords:** `development`, `integration`, `rest-api`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rest-api/SKILL.md`

### build-zoom-team-chat-app
Reference skill for Zoom Team Chat. Use after routing to a chat workflow when building user-scoped messaging integrations, chatbot experiences, rich cards, buttons, slash commands, or chat webhooks.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/team-chat`
**Keywords:** `communication`, `development`, `integration`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/team-chat/SKILL.md`

### build-zoom-virtual-agent
Reference skill for Zoom Virtual Agent. Use after routing to a virtual-agent workflow when implementing web embeds, Android or iOS wrapper integrations, knowledge-base sync, lifecycle handling, or troubleshooting.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent`
**Keywords:** `ai`, `integration`, `virtual-agent`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/SKILL.md`

### c-review
Performs comprehensive C/C++ security review for memory corruption, integer overflows, race conditions, and platform-specific vulnerabilities. Use when auditing native C/C++ applications, reviewing daemons or services for memory safety, or hunting integer overflow / use-after-free / race conditions in userspace code.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/c-review/skills/c-review`
**Keywords:** `cpp`, `review`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/c-review/skills/c-review/SKILL.md`

### call-prep
Prepare for a customer or prospect call using Common Room signals. Triggers on 'prep me for my call with [company]', 'prepare for a meeting with [company]', 'what should I know before talking to [company]', or any call preparation request.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/call-prep`
**Keywords:** `common-room`, `crm`, `planning`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/call-prep/SKILL.md`

### call-prep
Prepare for a sales call with account context, attendee research, and suggested agenda. Works standalone with user input and web research, supercharged when you connect your CRM, email, chat, or transcripts. Trigger with "prep me for my call with [company]", "I'm meeting with [company] prep me", "call prep [company]", or "get me ready for [meeting]".

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/sales/skills/call-prep`
**Keywords:** `call-prep`, `crm`, `planning`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/call-prep/SKILL.md`

### campaign-plan
Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics. Use when planning a product launch, lead-gen push, or awareness campaign, when you need a week-by-week content calendar with dependencies, or when translating a marketing goal into a structured, executable plan.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/marketing/skills/campaign-plan`
**Keywords:** `campaign`, `marketing`, `planning`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/campaign-plan/SKILL.md`

### capacity-plan
Plan resource capacity — workload analysis and utilization forecasting. Use when heading into quarterly planning, the team feels overallocated and you need the numbers, deciding whether to hire or deprioritize, or stress-testing whether upcoming projects fit the people you have.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/operations/skills/capacity-plan`
**Keywords:** `capacity`, `operations`, `planning`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/capacity-plan/SKILL.md`

### chatgpt-apps
Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold. Prefer a docs-first workflow by invoking the openai-docs skill or OpenAI developer docs MCP tools before generating code.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/chatgpt-apps`
**Keywords:** `ai`, `chatgpt`, `development`, `integration`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/chatgpt-apps/SKILL.md`

### choose-zoom-approach
Choose the right Zoom architecture for a use case. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zoom MCP, Phone, Contact Center, or a hybrid approach.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/choose-zoom-approach`
**Keywords:** `architecture`, `planning`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/choose-zoom-approach/SKILL.md`

### claude-in-chrome-troubleshooting
Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratically.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/claude-in-chrome-troubleshooting/skills/claude-in-chrome-troubleshooting`
**Keywords:** `ai`, `debugging`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/claude-in-chrome-troubleshooting/skills/claude-in-chrome-troubleshooting/SKILL.md`

### cli-creator
Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/cli-creator`
**Keywords:** `command`, `development`, `integration`, `rest-api`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/cli-creator/SKILL.md`

### close-management
Manage the month-end close process with task sequencing, dependencies, and status tracking. Use when planning the close calendar, tracking close progress, identifying blockers, or sequencing close activities by day.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/finance/skills/close-management`
**Keywords:** `finance`, `management`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/close-management/SKILL.md`

### code-maturity-assessor
Systematic code maturity assessment using Trail of Bits' 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level code, and testing. Produces professional scorecard with evidence-based ratings and actionable recommendations.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/building-secure-contracts/skills/code-maturity-assessor`
**Keywords:** `analysis`, `audit`, `security`, `smart-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/code-maturity-assessor/SKILL.md`

### comp-analysis
Analyze compensation — benchmarking, band placement, and equity modeling. Trigger with "what should we pay a [role]", "is this offer competitive", "model this equity grant", or when uploading comp data to find outliers and retention risks.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/human-resources/skills/comp-analysis`
**Keywords:** `analysis`, `compensation`, `hr`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/comp-analysis/SKILL.md`

### competitive-brief
Research competitors and generate a positioning and messaging comparison with content gaps, opportunities, and threats. Use when building sales battlecards, when finding positioning gaps and messaging angles competitors haven't claimed, or when a competitor makes a move and you need to assess the impact.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/marketing/skills/competitive-brief`
**Keywords:** `analysis`, `competitive-intelligence`, `marketing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/competitive-brief/SKILL.md`

### competitive-brief
Create a competitive analysis brief for one or more competitors or a feature area. Use when informing product strategy or feature prioritization, building sales battle cards, prepping board or investor materials, or deciding where to differentiate vs. achieve parity.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/product-management/skills/competitive-brief`
**Keywords:** `analysis`, `competitive-intelligence`, `planning`, `product`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/competitive-brief/SKILL.md`

### compliance-tracking
Track compliance requirements and audit readiness. Trigger with "compliance", "audit prep", "SOC 2", "ISO 27001", "GDPR", "regulatory requirement", or when the user needs help tracking, preparing for, or documenting compliance activities.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/operations/skills/compliance-tracking`
**Keywords:** `audit`, `compliance`, `management`, `operations`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/compliance-tracking/SKILL.md`

### configuring-dbt-mcp-server
Generates MCP server configuration JSON, resolves authentication setup, and validates server connectivity for dbt. Use when setting up, configuring, or troubleshooting the dbt MCP server for AI tools like Kilo, Cursor, VS Code, or Claude Desktop.

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/dbt/skills/configuring-dbt-mcp-server`
**Keywords:** `configuration`, `dbt`, `mcp`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/configuring-dbt-mcp-server/SKILL.md`

### constant-time-analysis
Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or Ruby.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis`
**Keywords:** `analysis`, `cryptography`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md`

### content-creation
Draft marketing content across channels — blog posts, social media, email newsletters, landing pages, press releases, and case studies. Use when writing any marketing content, when you need channel-specific formatting, SEO-optimized copy, headline options, or calls to action.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/marketing/skills/content-creation`
**Keywords:** `brand`, `content`, `marketing`, `writing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/content-creation/SKILL.md`

### content-research-writer
Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section. Transforms your writing process from solo effort to collaborative partnership.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/content-research-writer`
**Keywords:** `communication`, `communication-writing`, `content`, `marketing`, `research`, `writing`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/content-research-writer/SKILL.md`

### cowork-plugin-customizer
Customize a Claude Code plugin for a specific organization's tools and workflows. Use when: customize plugin, set up plugin, configure plugin, tailor plugin, adjust plugin settings, customize plugin connectors, customize plugin skill, tweak plugin, modify plugin configuration.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/cowork-plugin-management/skills/cowork-plugin-customizer`
**Keywords:** `configuration`, `integration`, `management`, `plugin`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/cowork-plugin-management/skills/cowork-plugin-customizer/SKILL.md`

### create-cowork-plugin
Guide users through creating a new plugin from scratch in a cowork session. Use when users want to create a plugin, build a plugin, make a new plugin, develop a plugin, scaffold a plugin, start a plugin from scratch, or design a plugin. This skill requires Cowork mode with access to the outputs directory for delivering the final .plugin file.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/cowork-plugin-management/skills/create-cowork-plugin`
**Keywords:** `development`, `integration`, `management`, `plugin`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/cowork-plugin-management/skills/create-cowork-plugin/SKILL.md`

### create-pull-request
Create a GitHub pull request following project conventions. Use when the user asks to create a PR, submit changes for review, or open a pull request. Handles commit analysis, branch management, and PR creation using the gh CLI tool.

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/create-pull-request`
**Keywords:** `development`, `git`, `github`, `workflow`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/create-pull-request/SKILL.md`

### customer-escalation
Package an escalation for engineering, product, or leadership with full context. Use when a bug needs engineering attention beyond normal support, multiple customers report the same issue, a customer is threatening to churn, or an issue has sat unresolved past its SLA.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/customer-support/skills/customer-escalation`
**Keywords:** `customer-support`, `ticket-triage`, `workflow`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/customer-support/skills/customer-escalation/SKILL.md`

### daily-briefing
Start your day with a prioritized sales briefing. Works standalone when you tell me your meetings and priorities, supercharged when you connect your calendar, CRM, and email. Trigger with "morning briefing", "daily brief", "what's on my plate today", "prep my day", or "start my day".

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/sales/skills/daily-briefing`
**Keywords:** `crm`, `reporting`, `sales`, `summarization`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/daily-briefing/SKILL.md`

### dbt-migration
Skills for migrating dbt projects - moving from dbt Core to the Fusion engine or across data platforms. Use when migrating dbt projects between platforms or to dbt Fusion.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/dbt-migration`
**Keywords:** `data`, `dbt`, `development`, `migration`, `sql`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt-migration/SKILL.md`

### debug
Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected and the cause isn't obvious.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/engineering/skills/debug`
**Keywords:** `debugging`, `engineering`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/debug/SKILL.md`

### debug-zoom
Debug a broken Zoom integration by isolating the failure point and routing into the right Zoom references. Use when auth, API, webhook, SDK, or MCP behavior is failing and you need a ranked hypothesis list plus verification steps.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom`
**Keywords:** `debugging`, `integration`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom/SKILL.md`

### debug-zoom-integration
Debug broken Zoom implementations quickly. Use when auth, webhooks, SDK joins, MCP transport, or real-time media workflows are failing and you need to isolate the layer before proposing a fix.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom-integration`
**Keywords:** `debugging`, `integration`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom-integration/SKILL.md`

### deploy-checklist
Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI status and approvals before going to production, or documenting rollback triggers ahead of time.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/engineering/skills/deploy-checklist`
**Keywords:** `deployment`, `documentation`, `engineering`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/deploy-checklist/SKILL.md`

### design-critique
Get structured design feedback on usability, hierarchy, and consistency. Trigger with "review this design", "critique this mockup", "what do you think of this screen?", or when sharing a Figma link or screenshot for feedback at any stage from exploration to final polish.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/design/skills/design-critique`
**Keywords:** `design`, `review`, `ux`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/design-critique/SKILL.md`

### design-mcp-workflow
Design a Zoom MCP workflow for Claude. Use when deciding whether Zoom MCP fits a task, when planning tool-based AI workflows, or when separating MCP responsibilities from REST API responsibilities.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/design-mcp-workflow`
**Keywords:** `design`, `mcp`, `workflow`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/design-mcp-workflow/SKILL.md`

### design-system
Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded values across components, writing documentation for a component's variants, states, and accessibility notes, or designing a new pattern that fits the existing system.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/design/skills/design-system`
**Keywords:** `design`, `design-system`, `documentation`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/design-system/SKILL.md`

### devcontainer-setup
Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configuring sandboxed Claude Code workspaces.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/devcontainer-setup/skills/devcontainer-setup`
**Keywords:** `configuration`, `devcontainer`, `development`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/devcontainer-setup/skills/devcontainer-setup/SKILL.md`

### digest
Generate a daily or weekly digest of activity across all connected sources. Use when catching up after time away, starting the day and wanting a summary of mentions and action items, or reviewing a week's decisions and document updates grouped by project.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/enterprise-search/skills/digest`
**Keywords:** `enterprise-search`, `knowledge`, `search`, `summarization`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/digest/SKILL.md`

### dimensional-analysis
Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol, offchain code, or other blockchain-related codebase with arithmetic. Prevents dimensional mismatches and catches formula bugs early.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis`
**Keywords:** `analysis`, `blockchain`, `security`, `smart-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis/SKILL.md`

### dispatching-parallel-agents
Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies

**Enabled:** `true`
**ID:** `external/superpowers-skills/skills/dispatching-parallel-agents`
**Keywords:** `agent`, `automation`, `management`, `parallel-task`, `planning`, `task-management`, `workflow`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/dispatching-parallel-agents/SKILL.md`

### doc-coauthoring
Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/doc-coauthoring`
**Keywords:** `ai`, `communication`, `documents`, `writing`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/doc-coauthoring/SKILL.md`

### documentation
Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README", "write a runbook", "onboarding guide", or when the user needs help with any form of technical writing — API docs, architecture docs, or operational runbooks.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/engineering/skills/documentation`
**Keywords:** `documentation`, `engineering`, `runbook`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/documentation/SKILL.md`

### domain-name-brainstormer
Generates creative domain name ideas for your project and checks availability across multiple TLDs (.com, .io, .dev, .ai, etc.). Saves hours of brainstorming and manual checking.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/domain-name-brainstormer`
**Keywords:** `brainstorming`, `business`, `business-marketing`, `marketing`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/domain-name-brainstormer/SKILL.md`

### draft-content
Draft blog posts, social media, email newsletters, landing pages, press releases, and case studies with channel-specific formatting and SEO recommendations. Use when writing any marketing content, when you need headline or subject line options, or when adapting a message for a specific platform, audience, and brand voice.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/marketing/skills/draft-content`
**Keywords:** `brand`, `content`, `marketing`, `writing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/draft-content/SKILL.md`

### draft-response
Draft a professional customer-facing response tailored to the situation and relationship. Use when answering a product question, responding to an escalation or outage, delivering bad news like a delay or won't-fix, declining a feature request, or replying to a billing issue.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/customer-support/skills/draft-response`
**Keywords:** `communication`, `customer-support`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/customer-support/skills/draft-response/SKILL.md`

### dwarf-expert
Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). Triggers when understanding DWARF information, interacting with DWARF files, answering DWARF-related questions, or working with code that parses DWARF data.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/dwarf-expert/skills/dwarf-expert`
**Keywords:** `binary`, `debugging`, `dwarf`, `ghidra`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/dwarf-expert/skills/dwarf-expert/SKILL.md`

### email-sequence
Design and draft multi-email sequences with full copy, timing, branching logic, exit conditions, and performance benchmarks. Use when building onboarding, lead nurture, re-engagement, win-back, or product launch flows, when you need a complete drip campaign with A/B test suggestions, or when mapping a sequence end-to-end with a flow diagram.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/marketing/skills/email-sequence`
**Keywords:** `automation`, `campaign`, `email`, `marketing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/email-sequence/SKILL.md`

### entry-point-analyzer
Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer`
**Keywords:** `analysis`, `security`, `smart-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`

### executing-plans
Use when you have a written implementation plan to execute in a separate session with review checkpoints

**Enabled:** `true`
**ID:** `external/superpowers-skills/skills/executing-plans`
**Keywords:** `development`, `execute`, `planning`, `review`, `task-management`, `validation`, `workflow`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/executing-plans/SKILL.md`

### fetching-dbt-docs
Retrieves and searches dbt documentation pages in LLM-friendly markdown format. Use when fetching dbt documentation, looking up dbt features, or answering questions about dbt Cloud, dbt Core, or the dbt Semantic Layer.

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/dbt/skills/fetching-dbt-docs`
**Keywords:** `analytics`, `dbt`, `documentation`, `sql`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/fetching-dbt-docs/SKILL.md`

### figma
Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma nodes into production code. Trigger when a task involves Figma URLs, node IDs, design-to-code implementation, or Figma MCP setup and troubleshooting.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/figma`
**Keywords:** `design`, `figma`, `integration`, `rest-api`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma/SKILL.md`

### figma-create-design-system-rules
Generates custom design system rules for the user's codebase. Use when user says "create design system rules", "generate rules for my project", "set up design rules", "customize design system guidelines", or wants to establish project-specific conventions for Figma-to-code workflows. Requires Figma MCP server connection.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/figma-create-design-system-rules`
**Keywords:** `automation`, `design-system`, `documentation`, `figma`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-create-design-system-rules/SKILL.md`

### figma-use
**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/figma-use`
**Keywords:** `design`, `figma`, `integration`, `mcp`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-use/SKILL.md`

### file-organizer
Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks. Reduces cognitive load and keeps your digital workspace tidy without manual effort.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/file-organizer`
**Keywords:** `organization`, `productivity`, `productivity-organization`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/file-organizer/SKILL.md`

### financial-statements
Generate financial statements (income statement, balance sheet, cash flow) with period-over-period comparison and variance analysis. Use when preparing a monthly or quarterly P&L, closing the books and need to flag material variances, comparing actuals to budget, building a financial summary for leadership review, or looking up GAAP presentation requirements and period-end adjustments.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/finance/skills/financial-statements`
**Keywords:** `finance`, `reporting`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/financial-statements/SKILL.md`

### finishing-a-development-branch
Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup

**Enabled:** `true`
**ID:** `external/superpowers-skills/skills/finishing-a-development-branch`
**Keywords:** `changelog`, `ci`, `code-review`, `deployment`, `development`, `git`, `pull-requests`, `testing`, `validation`, `workflow`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/finishing-a-development-branch/SKILL.md`

### fp-check
Systematically verifies suspected security bugs to eliminate false positives. Produces TRUE POSITIVE or FALSE POSITIVE verdicts with documented evidence for each bug.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/fp-check/skills/fp-check`
**Keywords:** `security`, `validation`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/fp-check/skills/fp-check/SKILL.md`

### gh-address-comments
Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/gh-address-comments`
**Keywords:** `git`, `github`, `review`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/gh-address-comments/SKILL.md`

### gh-cli
Enforces authenticated gh CLI workflows over unauthenticated curl/WebFetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/.codex/skills/gh-cli`
**Keywords:** `command`, `git`, `github`, `workflow`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/.codex/skills/gh-cli/SKILL.md`

### gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/gh-fix-ci`
**Keywords:** `debugging`, `git`, `github`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/gh-fix-ci/SKILL.md`

### git-cleanup
Safely analyzes and cleans up local git branches and worktrees by categorizing them as merged, squash-merged, superseded, or active work.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/git-cleanup/skills/git-cleanup`
**Keywords:** `git`, `tech-debt`, `workflow`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/git-cleanup/skills/git-cleanup/SKILL.md`

### graph-evolution
Compares Trailmark code graphs at two source code snapshots (git commits, tags, or directories) to surface security-relevant structural changes. Detects new attack paths, complexity shifts, blast radius growth, taint propagation changes, and privilege boundary modifications that text diffs miss. Use when comparing code between commits or tags, analyzing structural evolution, detecting attack surface growth, reviewing what changed between audit snapshots, or finding security-relevant changes that text diffs miss.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/trailmark/skills/graph-evolution`
**Keywords:** `analysis`, `binary`, `security`, `trailmark`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/graph-evolution/SKILL.md`

### guideline-generation
This skill generates, creates, or builds brand voice guidelines from source materials. It should be used when the user asks to "generate brand guidelines", "create a style guide", "extract brand voice", "create guidelines from calls", "consolidate brand materials", "analyze my sales calls for brand voice", "build a brand playbook from documents", "synthesize a voice and tone guide", or uploads brand documents, transcripts, or meeting recordings for brand analysis. Also triggers when the user has a discovery report and wants to convert it into actionable guidelines.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/brand-voice/skills/guideline-generation`
**Keywords:** `brand`, `content`, `documentation`, `marketing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/brand-voice/skills/guideline-generation/SKILL.md`

### guidelines-advisor
Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Provides actionable recommendations.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor`
**Keywords:** `documentation`, `review`, `security`, `smart-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor/SKILL.md`

### insecure-defaults
Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults`
**Keywords:** `configuration`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults/SKILL.md`

### internal-comms
A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/internal-comms`
**Keywords:** `ai`, `communication`, `content`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/internal-comms/SKILL.md`

### internal-comms
A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. The agent should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/internal-comms`
**Keywords:** `business`, `business-marketing`, `communication`, `content`, `marketing`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/internal-comms/SKILL.md`

### interpreting-culture-index
Interprets Culture Index (CI) surveys, behavioral profiles, and personality assessment data. Supports individual profile interpretation, team composition analysis (gas/brake/glue), burnout detection, profile comparison, hiring profiles, manager coaching, interview transcript analysis for trait prediction, candidate debrief, onboarding planning, and conflict mediation. Accepts extracted JSON or PDF input via OpenCV extraction script.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/culture-index/skills/interpreting-culture-index`
**Keywords:** `analysis`, `hr`, `people`, `recruiting`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/culture-index/skills/interpreting-culture-index/SKILL.md`

### kb-article
Draft a knowledge base article from a resolved issue or common question. Use when a ticket resolution is worth documenting for self-service, the same question keeps coming up, a workaround needs to be published, or a known issue should be communicated to customers.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/customer-support/skills/kb-article`
**Keywords:** `customer-support`, `documentation`, `knowledge`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/customer-support/skills/kb-article/SKILL.md`

### knowledge-synthesis
Combines search results from multiple sources into coherent, deduplicated answers with source attribution. Handles confidence scoring based on freshness and authority, and summarizes large result sets effectively.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/enterprise-search/skills/knowledge-synthesis`
**Keywords:** `enterprise-search`, `knowledge`, `search`, `summarization`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/knowledge-synthesis/SKILL.md`

### legal-response
Generate a response to a common legal inquiry using configured templates, with built-in escalation checks for situations that shouldn't use a templated reply. Use when responding to data subject requests, litigation hold notices, vendor legal questions, NDA requests from business teams, or subpoenas.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/legal/skills/legal-response`
**Keywords:** `communication`, `legal`, `risk`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/legal-response/SKILL.md`

### legal-risk-assessment
Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria. Use when evaluating contract risk, assessing deal exposure, classifying issues by severity, or determining whether a matter needs senior counsel or outside legal review.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/legal/skills/legal-risk-assessment`
**Keywords:** `analysis`, `compliance`, `legal`, `risk`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/legal-risk-assessment/SKILL.md`

### let-fate-decide
Draws 4 Tarot cards to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the user says 'let fate decide', 'YOLO', 'whatever', 'idk', or other nonchalant phrases, makes Yu-Gi-Oh references, or when you are about to arbitrarily pick between multiple reasonable approaches. Prefer over ask-questions-if-underspecified when the user's tone is casual or playful rather than precision-seeking.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/let-fate-decide/skills/let-fate-decide`
**Keywords:** `automation`, `planning`, `productivity`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/let-fate-decide/skills/let-fate-decide/SKILL.md`

### linear
Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets in Linear.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/linear`
**Keywords:** `development`, `linear`, `planning`, `ticket-triage`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/linear/SKILL.md`

### mcp-builder
Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/mcp-builder`
**Keywords:** `ai`, `development`, `integration`, `mcp`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/mcp-builder/SKILL.md`

### meeting-briefing
Prepare structured briefings for meetings with legal relevance and track resulting action items. Use when preparing for contract negotiations, board meetings, compliance reviews, or any meeting where legal context, background research, or action tracking is needed.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/legal/skills/meeting-briefing`
**Keywords:** `legal`, `meeting`, `planning`, `summarization`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/meeting-briefing/SKILL.md`

### meeting-insights-analyzer
Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. Identifies when you avoid conflict, use filler words, dominate conversations, or miss opportunities to listen. Perfect for professionals seeking to improve their communication and leadership skills.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/meeting-insights-analyzer`
**Keywords:** `ai`, `analytics`, `communication`, `communication-writing`, `meeting`, `transcribe`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/meeting-insights-analyzer/SKILL.md`

### metrics-review
Review and analyze product metrics with trend analysis and actionable insights. Use when running a weekly, monthly, or quarterly metrics review, investigating a sudden spike or drop, comparing performance against targets, or turning raw numbers into a scorecard with recommended actions.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/product-management/skills/metrics-review`
**Keywords:** `analytics`, `metrics`, `product`, `review`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/metrics-review/SKILL.md`

### migrate-to-codex
Migrate supported instruction files, skills, agents, and MCP config into Codex project and global files.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/migrate-to-codex`
**Keywords:** `ai`, `configuration`, `migration`, `openai`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/migrate-to-codex/SKILL.md`

### migrating-dbt-core-to-fusion
Classifies dbt-core to Fusion migration errors into actionable categories (auto-fixable, guided fixes, needs input, blocked). Use when a user needs help triaging migration errors to understand what they can fix vs what requires Fusion engine updates.

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/dbt-migration/skills/migrating-dbt-core-to-fusion`
**Keywords:** `analytics`, `dbt`, `migration`, `sql`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt-migration/skills/migrating-dbt-core-to-fusion/SKILL.md`

### migrating-dbt-project-across-platforms
Use when migrating a dbt project from one data platform or data warehouse to another (e.g., Snowflake to Databricks, Databricks to Snowflake) using dbt Fusion's real-time compilation to identify and fix SQL dialect differences.

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/dbt-migration/skills/migrating-dbt-project-across-platforms`
**Keywords:** `analytics`, `dbt`, `migration`, `sql`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt-migration/skills/migrating-dbt-project-across-platforms/SKILL.md`

### notion-research-documentation
Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/notion-research-documentation`
**Keywords:** `documentation`, `notion`, `research`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/notion-research-documentation/SKILL.md`

### openai-docs
Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/openai-docs`
**Keywords:** `ai`, `documentation`, `openai`, `rest-api`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/openai-docs/SKILL.md`

### openai-gh-address-comments
Help address review/issue comments on the open GitHub PR for the current branch using gh

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-gh-address-comments/skills/openai-gh-address-comments`
**Keywords:** `git`, `github`, `review`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-gh-address-comments/skills/openai-gh-address-comments/SKILL.md`

### openai-gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions;

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-gh-fix-ci/skills/openai-gh-fix-ci`
**Keywords:** `debugging`, `git`, `github`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-gh-fix-ci/skills/openai-gh-fix-ci/SKILL.md`

### openai-playwright
Use when the task requires automating a real browser from the terminal (navigation, form

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-playwright/skills/openai-playwright`
**Keywords:** `automation`, `playwright`, `testing`, `web`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-playwright/skills/openai-playwright/SKILL.md`

### openai-screenshot
Use when the user explicitly asks for a desktop or system screenshot (full screen, specific

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-screenshot/skills/openai-screenshot`
**Keywords:** `automation`, `screenshot`, `windows`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-screenshot/skills/openai-screenshot/SKILL.md`

### openai-security-ownership-map
'Analyze git repositories to build a security ownership topology (people-to-file), compute

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-security-ownership-map/skills/openai-security-ownership-map`
**Keywords:** `analysis`, `code-review`, `git`, `security`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-security-ownership-map/skills/openai-security-ownership-map/SKILL.md`

### openai-security-threat-model
Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities,

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-security-threat-model/skills/openai-security-threat-model`
**Keywords:** `analysis`, `security`, `threat-model`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-security-threat-model/skills/openai-security-threat-model/SKILL.md`

### openai-sentry
Use when the user asks to inspect Sentry issues or events, summarize recent production errors,

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-sentry/skills/openai-sentry`
**Keywords:** `debugging`, `sentry`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-sentry/skills/openai-sentry/SKILL.md`

### openai-yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-yeet/skills/openai-yeet`
**Keywords:** `automation`, `git`, `workflow`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-yeet/skills/openai-yeet/SKILL.md`

### org-planning
Headcount planning, org design, and team structure optimization. Trigger with "org planning", "headcount plan", "team structure", "reorg", "who should we hire next", or when the user is thinking about team size, reporting structure, or organizational design.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/human-resources/skills/org-planning`
**Keywords:** `hr`, `org-planning`, `planning`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/org-planning/SKILL.md`

### ossfuzz
OSS-Fuzz provides free continuous fuzzing for open source projects. Use when setting up continuous fuzzing infrastructure or enrolling projects.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/ossfuzz`
**Keywords:** `fuzzing`, `integration`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/ossfuzz/SKILL.md`

### people-report
Generate headcount, attrition, diversity, or org health reports. Use when pulling a headcount snapshot for leadership, analyzing turnover trends by team, preparing diversity representation metrics, or assessing span of control and flight risk across the org.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/human-resources/skills/people-report`
**Keywords:** `analytics`, `hr`, `people`, `reporting`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/people-report/SKILL.md`

### performance-report
Build a marketing performance report with key metrics, trend analysis, wins and misses, and prioritized optimization recommendations. Use when wrapping a campaign, when preparing weekly, monthly, or quarterly channel summaries for stakeholders, or when you need data translated into an executive summary with next-period priorities.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/marketing/skills/performance-report`
**Keywords:** `analytics`, `campaign`, `marketing`, `reporting`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/performance-report/SKILL.md`

### performance-review
Structure a performance review with self-assessment, manager template, and calibration prep. Use when review season kicks off and you need a self-assessment template, writing a manager review for a direct report, prepping rating distributions and promotion cases for calibration, or turning vague feedback into specific behavioral examples.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/human-resources/skills/performance-review`
**Keywords:** `hr`, `performance-review`, `review`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/performance-review/SKILL.md`

### pipeline-review
Analyze pipeline health — prioritize deals, flag risks, get a weekly action plan. Use when running a weekly pipeline review, deciding which deals to focus on this week, spotting stale or stuck opportunities, auditing for hygiene issues like bad close dates, or identifying single-threaded deals.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/sales/skills/pipeline-review`
**Keywords:** `crm`, `management`, `pipeline`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/pipeline-review/SKILL.md`

### plan-zoom-integration
Turn a Zoom integration idea into an implementation plan with architecture, auth, and delivery milestones. Use when you need a practical build plan, phased delivery sequence, risk list, and next-step recommendation.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-integration`
**Keywords:** `architecture`, `integration`, `planning`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-integration/SKILL.md`

### plan-zoom-product
Choose the right Zoom building surface for a use case and explain the tradeoffs clearly. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Phone, Contact Center, or MCP for a specific product idea or integration goal.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product`
**Keywords:** `architecture`, `planning`, `product`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product/SKILL.md`

### playwright
Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/playwright`
**Keywords:** `automation`, `playwright`, `testing`, `web`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/playwright/SKILL.md`

### probe-sdk
Reference skill for Zoom Probe SDK. Use after routing to a preflight workflow when testing browser compatibility, media permissions, audio or video diagnostics, and network readiness before users join.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/probe-sdk`
**Keywords:** `debugging`, `media`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/probe-sdk/SKILL.md`

### process-doc
Document a business process — flowcharts, RACI, and SOPs. Use when formalizing a process that lives in someone's head, building a RACI to clarify who owns what, writing an SOP for a handoff or audit, or capturing the exceptions and edge cases of how work actually gets done.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/operations/skills/process-doc`
**Keywords:** `documentation`, `operations`, `process`, `workflow`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/process-doc/SKILL.md`

### process-optimization
Analyze and improve business processes. Trigger with "this process is slow", "how can we improve", "streamline this workflow", "too many steps", "bottleneck", or when the user describes an inefficient process they want to fix.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/operations/skills/process-optimization`
**Keywords:** `operations`, `optimization`, `process`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/process-optimization/SKILL.md`

### product-brainstorming
Brainstorm product ideas, explore problem spaces, and challenge assumptions as a thinking partner. Use when exploring a new opportunity, generating solutions to a product problem, stress-testing an idea, or when a PM needs to think out loud with a sharp sparring partner before converging on a direction.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/product-management/skills/product-brainstorming`
**Keywords:** `brainstorming`, `planning`, `product`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/product-brainstorming/SKILL.md`

### receiving-code-review
Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation

**Enabled:** `true`
**ID:** `external/superpowers-skills/skills/receiving-code-review`
**Keywords:** `code-review`, `development`, `review`, `testing`, `validation`, `workflow`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/receiving-code-review/SKILL.md`

### requesting-code-review
Use when completing tasks, implementing major features, or before merging to verify work meets requirements

**Enabled:** `true`
**ID:** `external/superpowers-skills/skills/requesting-code-review`
**Keywords:** `code-review`, `pull-requests`, `requirements`, `review`, `testing`, `validation`, `workflow`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/requesting-code-review/SKILL.md`

### research-synthesis
Synthesize user research into themes, insights, and recommendations. Use when you have interview transcripts, survey results, usability test notes, support tickets, or NPS responses that need to be distilled into patterns, user segments, and prioritized next steps.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/design/skills/research-synthesis`
**Keywords:** `analysis`, `design`, `research`, `summarization`, `ux`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/research-synthesis/SKILL.md`

### review-contract
Review a contract against your organization's negotiation playbook — flag deviations, generate redlines, provide business impact analysis. Use when reviewing vendor or customer agreements, when you need clause-by-clause analysis against standard positions, or when preparing a negotiation strategy with prioritized redlines and fallback positions.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/legal/skills/review-contract`
**Keywords:** `compliance`, `contract`, `legal`, `review`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/review-contract/SKILL.md`

### risk-assessment
Identify, assess, and mitigate operational risks. Trigger with "what are the risks", "risk assessment", "risk register", "what could go wrong", or when the user is evaluating risks associated with a project, vendor, process, or decision.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/operations/skills/risk-assessment`
**Keywords:** `analysis`, `compliance`, `operations`, `risk`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/risk-assessment/SKILL.md`

### rivet-sdk
Reference skill for Zoom Rivet SDK. Use after routing to a Rivet-based server workflow when implementing auth handling, webhook consumers, API wrappers, multi-module composition, or Lambda receiver patterns.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rivet-sdk`
**Keywords:** `development`, `integration`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rivet-sdk/SKILL.md`

### roadmap-update
Update, create, or reprioritize your product roadmap. Use when adding a new initiative and deciding what moves to make room, shifting priorities after new information comes in, moving timelines due to a dependency slip, or building a Now/Next/Later view from scratch.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/product-management/skills/roadmap-update`
**Keywords:** `management`, `planning`, `product`, `roadmap`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/roadmap-update/SKILL.md`

### runbook
Create or update an operational runbook for a recurring task or procedure. Use when documenting a task that on-call or ops needs to run repeatably, turning tribal knowledge into exact step-by-step commands, adding troubleshooting and rollback steps to an existing procedure, or writing escalation paths for when things go wrong.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/operations/skills/runbook`
**Keywords:** `documentation`, `operations`, `runbook`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/runbook/SKILL.md`

### scientific-problem-selection
This skill should be used when scientists need help with research problem selection, project ideation, troubleshooting stuck projects, or strategic scientific decisions. Use this skill when users ask to pitch a new research idea, work through a project problem, evaluate project risks, plan research strategy, navigate decision trees, or get help choosing what scientific problem to work on. Typical requests include "I have an idea for a project", "I'm stuck on my research", "help me evaluate this project", "what should I work on", or "I need strategic advice about my research".

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/bio-research/skills/scientific-problem-selection`
**Keywords:** `bio-research`, `brainstorming`, `planning`, `research`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/scientific-problem-selection/SKILL.md`

### screenshot
Use when the user explicitly asks for a desktop or system screenshot (full screen, specific app or window, or a pixel region), or when tool-specific capture capabilities are unavailable and an OS-level capture is needed.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/screenshot`
**Keywords:** `automation`, `screenshot`, `windows`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/screenshot/SKILL.md`

### scvi-tools
Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need (1) data integration and batch correction with scVI/scANVI, (2) ATAC-seq analysis with PeakVI, (3) CITE-seq multi-modal analysis with totalVI, (4) multiome RNA+ATAC analysis with MultiVI, (5) spatial transcriptomics deconvolution with DestVI, (6) label transfer and reference mapping with scANVI/scArches, (7) RNA velocity with veloVI, or (8) any deep learning-based single-cell method. Triggers include mentions of scVI, scANVI, totalVI, PeakVI, MultiVI, DestVI, veloVI, sysVI, scArches, variational autoencoder, VAE, batch correction, data integration, multi-modal, CITE-seq, multiome, reference mapping, latent space.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/bio-research/skills/scvi-tools`
**Keywords:** `analysis`, `bio-research`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/scvi-tools/SKILL.md`

### search-strategy
Query decomposition and multi-source search orchestration. Breaks natural language questions into targeted searches per source, translates queries into source-specific syntax, ranks results by relevance, and handles ambiguity and fallback strategies.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search-strategy`
**Keywords:** `enterprise-search`, `planning`, `search`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search-strategy/SKILL.md`

### second-opinion
Runs external LLM code reviews (OpenAI Codex or Google Gemini CLI) on uncommitted changes, branch diffs, or specific commits. Use when the user asks for a second opinion, external review, codex review, gemini review, or mentions /second-opinion.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion`
**Keywords:** `ai`, `analysis`, `code-review`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion/SKILL.md`

### secure-workflow-guide
Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide`
**Keywords:** `review`, `security`, `smart-contracts`, `workflow`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide/SKILL.md`

### security-ownership-map
Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/security-ownership-map`
**Keywords:** `analysis`, `code-review`, `git`, `security`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/security-ownership-map/SKILL.md`

### security-threat-model
Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/security-threat-model`
**Keywords:** `analysis`, `security`, `threat-model`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/security-threat-model/SKILL.md`

### semgrep-rule-creator
Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/semgrep-rule-creator/skills/semgrep-rule-creator`
**Keywords:** `automation`, `security`, `semgrep`, `static-analysis`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md`

### semgrep-rule-variant-creator
Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for each language.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator`
**Keywords:** `automation`, `security`, `semgrep`, `static-analysis`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md`

### sentry
Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; perform read-only queries using the `sentry` command.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/sentry`
**Keywords:** `debugging`, `sentry`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/sentry/SKILL.md`

### sequence-load
Find leads matching criteria and bulk-add them to an Apollo outreach sequence. Handles enrichment, contact creation, deduplication, and enrollment in one flow.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/sequence-load`
**Keywords:** `apollo`, `automation`, `outreach`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/sequence-load/SKILL.md`

### setup-zoom-mcp
Decide when Zoom MCP is the right fit and produce a safe setup plan for Claude. Use when planning AI workflows over Zoom data, deciding between MCP and REST, or defining a hybrid MCP architecture.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-mcp`
**Keywords:** `configuration`, `integration`, `mcp`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-mcp/SKILL.md`

### setup-zoom-oauth
Implement Zoom authentication correctly. Use when setting up app credentials, choosing an OAuth grant, requesting scopes, handling token refresh, or debugging auth failures.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-oauth`
**Keywords:** `configuration`, `oauth`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-oauth/SKILL.md`

### setup-zoom-webhooks
Reference skill for Zoom webhooks. Use after routing to an event-driven workflow when implementing subscriptions, signature verification, delivery handling, retries, or event-type selection.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/webhooks`
**Keywords:** `integration`, `webhooks`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/webhooks/SKILL.md`

### setup-zoom-websockets
Reference skill for Zoom WebSockets. Use after routing to a low-latency event workflow when persistent connections, faster event delivery, or security constraints make WebSockets preferable to webhooks.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/websockets`
**Keywords:** `integration`, `websockets`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/websockets/SKILL.md`

### sharp-edges
Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges`
**Keywords:** `rest-api`, `review`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges/SKILL.md`

### signature-request
Prepare and route a document for e-signature — run a pre-signature checklist, configure signing order, and send for execution. Use when a contract is finalized and ready to sign, when verifying entity names, exhibits, and signature blocks before sending, or when setting up an envelope with sequential or parallel signers.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/legal/skills/signature-request`
**Keywords:** `contract`, `legal`, `signature-request`, `workflow`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/signature-request/SKILL.md`

### skill-creator
Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/skill-creator`
**Keywords:** `ai`, `development`, `optimization`, `skill-creator`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/skill-creator/SKILL.md`

### skill-improver
Iteratively reviews and fixes Claude Code skill quality issues until they meet standards. Runs automated fix-review cycles using the skill-reviewer agent. Use to fix skill quality issues, improve skill descriptions, run automated skill review loops, or iteratively refine a skill. Triggers on 'fix my skill', 'improve skill quality', 'skill improvement loop'. NOT for one-time reviews—use /skill-reviewer directly.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/skill-improver/skills/skill-improver`
**Keywords:** `ai`, `optimization`, `skill-creator`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/skill-improver/skills/skill-improver/SKILL.md`

### skill-installer
Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.system/skill-installer`
**Keywords:** `ai`, `configuration`, `skill-creator`
**Source:** openai-skills

File: `external/openai-skills/skills/.system/skill-installer/SKILL.md`

### skill-share
A skill that creates new agent skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/skill-share`
**Keywords:** `development`, `integration`, `skill-creator`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/skill-share/SKILL.md`

### slack-messaging
Guidance for composing well-formatted, effective Slack messages using mrkdwn syntax

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/slack/skills/slack-messaging`
**Keywords:** `communication`, `integration`, `slack`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/slack/skills/slack-messaging/SKILL.md`

### slack-search
Guidance for effectively searching Slack to find messages, files, channels, and people

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/slack/skills/slack-search`
**Keywords:** `communication`, `search`, `slack`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/slack/skills/slack-search/SKILL.md`

### source-management
Manages connected MCP sources for enterprise search. Detects available sources, guides users to connect new ones, handles source priority ordering, and manages rate limiting awareness.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/enterprise-search/skills/source-management`
**Keywords:** `enterprise-search`, `management`, `search`, `source-management`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/source-management/SKILL.md`

### spec-to-code-compliance
Verifies code implements exactly what documentation specifies for blockchain audits. Use when comparing code against whitepapers, finding gaps between specs and implementation, or performing compliance checks for protocol implementations.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/spec-to-code-compliance/skills/spec-to-code-compliance`
**Keywords:** `compliance`, `security`, `spec`, `validation`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md`

### sprint-planning
Plan a sprint — scope work, estimate capacity, set goals, and draft a sprint plan. Use when kicking off a new sprint, sizing a backlog against team availability (accounting for PTO and meetings), deciding what's P0 vs. stretch, or handling carryover from the last sprint.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/product-management/skills/sprint-planning`
**Keywords:** `planning`, `product`, `sprint`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/sprint-planning/SKILL.md`

### stakeholder-update
Generate a stakeholder update tailored to audience and cadence. Use when writing a weekly or monthly status for leadership, announcing a launch, escalating a risk or blocker, or translating the same progress into exec-brief, engineering-detail, or customer-facing versions.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/product-management/skills/stakeholder-update`
**Keywords:** `communication`, `product`, `reporting`, `stakeholder`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/stakeholder-update/SKILL.md`

### standup
Generate a standup update from recent activity. Use when preparing for daily standup, summarizing yesterday's commits and PRs and ticket moves, formatting work into yesterday/today/blockers, or structuring a few rough notes into a shareable update.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/engineering/skills/standup`
**Keywords:** `engineering`, `reporting`, `sprint`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/standup/SKILL.md`

### start
Set up your bio-research environment and explore available tools. Use when first getting oriented with the plugin, checking which literature, drug-discovery, or visualization MCP servers are connected, or surveying available analysis skills before starting a new project.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/bio-research/skills/start`
**Keywords:** `bio-research`, `configuration`, `onboarding`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/start/SKILL.md`

### start
Start here for any Zoom integration or app idea. Use when you need to choose the right Zoom surface, shape the architecture, or route into the correct implementation skill without reading the whole Zoom doc set first.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/start`
**Keywords:** `architecture`, `configuration`, `onboarding`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/start/SKILL.md`

### start
Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your existing task list, or decoding the shorthand (nicknames, acronyms, project codenames) you use in your todos.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/productivity/skills/start`
**Keywords:** `configuration`, `onboarding`, `productivity`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/productivity/skills/start/SKILL.md`

### statistical-analysis
Apply statistical methods including descriptive stats, trend analysis, outlier detection, and hypothesis testing. Use when analyzing distributions, testing for significance, detecting anomalies, computing correlations, or interpreting statistical results.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/data/skills/statistical-analysis`
**Keywords:** `analysis`, `analytics`, `data`, `statistics`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/statistical-analysis/SKILL.md`

### status-report
Generate a status report with KPIs, risks, and action items. Use when writing a weekly or monthly update for leadership, summarizing project health with green/yellow/red status, surfacing risks and decisions that need stakeholder attention, or turning a pile of project tracker activity into a readable narrative.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/operations/skills/status-report`
**Keywords:** `management`, `operations`, `reporting`, `status-report`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/status-report/SKILL.md`

### subagent-driven-development
Use when executing implementation plans with independent tasks in the current session

**Enabled:** `true`
**ID:** `external/superpowers-skills/skills/subagent-driven-development`
**Keywords:** `agent`, `automation`, `development`, `execute`, `planning`, `task-management`, `testing`, `workflow`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/subagent-driven-development/SKILL.md`

### synthesize-research
Synthesize user research from interviews, surveys, and feedback into structured insights. Use when you have a pile of interview notes, survey responses, or support tickets to make sense of, need to extract themes and rank findings by frequency and impact, or want to turn raw feedback into roadmap recommendations.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/product-management/skills/synthesize-research`
**Keywords:** `analysis`, `product`, `research`, `summarization`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/synthesize-research/SKILL.md`

### systematic-debugging
Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes

**Enabled:** `true`
**ID:** `external/superpowers-skills/skills/systematic-debugging`
**Keywords:** `debug`, `debugging`, `development`, `error-analysis`, `incident`, `runbook`, `testing`, `validation`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/systematic-debugging/SKILL.md`

### task-management
Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, wants to add/complete tasks, or needs help tracking commitments.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/productivity/skills/task-management`
**Keywords:** `management`, `productivity`, `task-management`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/productivity/skills/task-management/SKILL.md`

### test-driven-development
Use when implementing any feature or bugfix, before writing implementation code

**Enabled:** `true`
**ID:** `external/superpowers-skills/skills/test-driven-development`
**Keywords:** `development`, `quality`, `refactor`, `testing`, `testing-strategy`, `validation`, `workflow`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/test-driven-development/SKILL.md`

### testing-handbook-generator
Meta-skill that analyzes the Trail of Bits Testing Handbook (appsec.guide) and generates Claude Code skills for security testing tools and techniques. Use when creating new skills based on handbook content.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/testing-handbook-generator`
**Keywords:** `documentation`, `security`, `testing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/testing-handbook-generator/SKILL.md`

### ticket-triage
Triage and prioritize a support ticket or customer issue. Use when a new ticket comes in and needs categorization, assigning P1-P4 priority, deciding which team should handle it, or checking whether it's a duplicate or known issue before routing.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/customer-support/skills/ticket-triage`
**Keywords:** `customer-support`, `ticket-triage`, `workflow`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/customer-support/skills/ticket-triage/SKILL.md`

### trailmark
Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/trailmark/skills/trailmark`
**Keywords:** `analysis`, `binary`, `security`, `trailmark`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`

### trailmark-structural
Runs full Trailmark structural analysis on Trailmark 0.2.x by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, and attack surface. Use when vivisect needs detailed structural data for a target. Triggers: structural analysis, blast radius, taint analysis, complexity hotspots.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/trailmark/skills/trailmark-structural`
**Keywords:** `analysis`, `binary`, `security`, `trailmark`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-structural/SKILL.md`

### trailmark-summary
Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary`
**Keywords:** `analysis`, `binary`, `security`, `summarization`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary/SKILL.md`

### troubleshooting-dbt-job-errors
Diagnoses dbt Cloud/platform job failures by analyzing run logs, querying the Admin API, reviewing git history, and investigating data issues. Use when a dbt Cloud/platform job fails and you need to diagnose the root cause, especially when error messages are unclear or when intermittent failures occur. Do not use for local dbt development errors.

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/dbt/skills/troubleshooting-dbt-job-errors`
**Keywords:** `analytics`, `dbt`, `debugging`, `sql`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/troubleshooting-dbt-job-errors/SKILL.md`

### ui-toolkit/web
Reference skill for Zoom Video SDK UI Toolkit. Use after routing to a web video workflow when you want prebuilt React UI instead of building a fully custom Video SDK interface.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/ui-toolkit`
**Keywords:** `integration`, `react`, `ui`, `web`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/ui-toolkit/SKILL.md`

### update
Sync tasks and refresh memory from your current activity. Use when pulling new assignments from your project tracker into TASKS.md, triaging stale or overdue tasks, filling memory gaps for unknown people or projects, or running a comprehensive scan to catch todos buried in chat and email.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/productivity/skills/update`
**Keywords:** `memory`, `productivity`, `reporting`, `status-report`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/productivity/skills/update/SKILL.md`

### using-git-worktrees
Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback

**Enabled:** `true`
**ID:** `external/superpowers-skills/skills/using-git-worktrees`
**Keywords:** `development`, `execute`, `git`, `planning`, `source-management`, `task-management`, `workflow`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/using-git-worktrees/SKILL.md`

### using-superpowers
Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions

**Enabled:** `false`
**ID:** `external/superpowers-skills/skills/using-superpowers`
**Keywords:** `agent`, `automation`, `claude-code`, `codex`, `plugin`, `skill-creator`, `workflow`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/using-superpowers/SKILL.md`

### ux-copy
Write or review UX copy — microcopy, error messages, empty states, CTAs. Trigger with "write copy for", "what should this button say?", "review this error message", or when naming a CTA, wording a confirmation dialog, filling an empty state, or writing onboarding text.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/design/skills/ux-copy`
**Keywords:** `content`, `design`, `ux`, `writing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/ux-copy/SKILL.md`

### validate-data
QA an analysis before sharing -- methodology, accuracy, and bias checks. Use when reviewing an analysis before a stakeholder presentation, spot-checking calculations and aggregation logic, verifying a SQL query's results look right, or assessing whether conclusions are actually supported by the data.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/data/skills/validate-data`
**Keywords:** `analytics`, `data`, `testing`, `validation`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/validate-data/SKILL.md`

### variance-analysis
Decompose financial variances into drivers with narrative explanations and waterfall analysis. Use when analyzing budget vs. actual, period-over-period changes, revenue or expense variances, or preparing variance commentary for leadership.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/finance/skills/variance-analysis`
**Keywords:** `analysis`, `finance`, `reporting`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/variance-analysis/SKILL.md`

### vendor-review
Evaluate a vendor — cost analysis, risk assessment, and recommendation. Use when reviewing a new vendor proposal, deciding whether to renew or replace a contract, comparing two vendors side-by-side, or building a TCO breakdown and negotiation points before procurement sign-off.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/operations/skills/vendor-review`
**Keywords:** `analysis`, `management`, `operations`, `vendor`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/vendor-review/SKILL.md`

### vercel-cli-with-tokens
Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using access tokens rather than interactive login — e.g. "deploy to vercel", "set up vercel", "add environment variables to vercel".

**Enabled:** `true`
**ID:** `external/vercel-agent-skills/skills/vercel-cli-with-tokens`
**Keywords:** `access`, `authentication`, `cli`, `configuration`, `deploy`, `deployment`, `management`, `vercel`
**Source:** vercel-agent-skills

File: `external/vercel-agent-skills/skills/vercel-cli-with-tokens/SKILL.md`

### vercel-react-best-practices
React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.

**Enabled:** `true`
**ID:** `external/vercel-agent-skills/skills/react-best-practices`
**Keywords:** `code`, `data`, `development`, `frontend`, `next`, `optimization`, `pages`, `react`, `refactoring`, `review`
**Source:** vercel-agent-skills

File: `external/vercel-agent-skills/skills/react-best-practices/SKILL.md`

### vercel-react-native-skills
No description.

**Enabled:** `true`
**ID:** `external/vercel-agent-skills/skills/react-native-skills`
**Keywords:** `android`, `configuration`, `development`, `ios`, `optimization`, `react-native`, `ui`, `vercel`
**Source:** vercel-agent-skills

File: `external/vercel-agent-skills/skills/react-native-skills/SKILL.md`

### vercel-react-view-transitions
Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component, `addTransitionType`, and CSS view transition pseudo-elements). Use this skill whenever the user wants to add page transitions, animate route changes, create shared element animations, animate enter/exit of components, animate list reorder, implement directional (forward/back) navigation animations, or integrate view transitions in Next.js. Also use when the user mentions view transitions, `startViewTransition`, `ViewTransition`, transition types, or asks about animating between UI states in React without third-party animation libraries.

**Enabled:** `true`
**ID:** `external/vercel-agent-skills/skills/react-view-transitions`
**Keywords:** `design`, `development`, `frontend`, `integration`, `next`, `react`, `ui`, `vercel`, `web`
**Source:** vercel-agent-skills

File: `external/vercel-agent-skills/skills/react-view-transitions/SKILL.md`

### verification-before-completion
Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always

**Enabled:** `true`
**ID:** `external/superpowers-skills/skills/verification-before-completion`
**Keywords:** `ci`, `code-review`, `development`, `quality`, `review`, `testing`, `validation`, `workflow`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/verification-before-completion/SKILL.md`

### web-design-guidelines
Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".

**Enabled:** `true`
**ID:** `external/vercel-agent-skills/skills/web-design-guidelines`
**Keywords:** `accessibility`, `audit`, `code`, `compliance`, `design`, `review`, `ui`, `ux`, `web`
**Source:** vercel-agent-skills

File: `external/vercel-agent-skills/skills/web-design-guidelines/SKILL.md`

### webapp-testing
Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/webapp-testing`
**Keywords:** `automation`, `development`, `playwright`, `testing`, `web`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/webapp-testing/SKILL.md`

### weekly-prep-brief
Generate a comprehensive weekly briefing for all external calls in the next 7 days. Triggers on 'weekly prep brief', 'prepare my week', 'what calls do I have this week', 'Monday prep', or any weekly planning request.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/weekly-prep-brief`
**Keywords:** `common-room`, `planning`, `sales`, `summarization`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/weekly-prep-brief/SKILL.md`

### write-spec
Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user request into a structured document, scoping a feature with goals and non-goals, defining success metrics and acceptance criteria, or breaking a big ask into a phased spec.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/product-management/skills/write-spec`
**Keywords:** `development`, `product`, `requirements`, `spec`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/product-management/skills/write-spec/SKILL.md`

### writing-plans
Use when you have a spec or requirements for a multi-step task, before touching code

**Enabled:** `true`
**ID:** `external/superpowers-skills/skills/writing-plans`
**Keywords:** `architecture`, `development`, `planning`, `requirements`, `spec`, `task-management`, `workflow`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/writing-plans/SKILL.md`

### writing-skills
Use when creating new skills, editing existing skills, or verifying skills work before deployment

**Enabled:** `true`
**ID:** `external/superpowers-skills/skills/writing-skills`
**Keywords:** `agent`, `automation`, `documentation`, `plugin`, `skill-creator`, `testing`, `validation`
**Source:** superpowers-skills

File: `external/superpowers-skills/skills/writing-skills/SKILL.md`

### yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/yeet`
**Keywords:** `automation`, `git`, `workflow`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/yeet/SKILL.md`

### zoom-apps-sdk
Reference skill for Zoom Apps SDK. Use after routing to an in-client app workflow when building web apps that run inside Zoom meetings, webinars, the main client, or Zoom Phone.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-apps-sdk`
**Keywords:** `integration`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-apps-sdk/SKILL.md`

### zoom-general
Cross-product Zoom reference skill. Use after the workflow is clear when you need shared platform guidance, app-model comparisons, authentication context, scopes, marketplace considerations, or API-vs-MCP routing.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general`
**Keywords:** `architecture`, `integration`, `rest-api`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general/SKILL.md`

### zoom-mcp
Guidance for the bundled Zoom MCP connectors. Use after routing to an MCP workflow when planning or troubleshooting tool-based access to meetings, recordings, meeting assets, or transcripts. Route Zoom Docs requests to the dedicated Docs MCP server and Whiteboard-specific requests to `zoom-mcp/whiteboard`.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-mcp`
**Keywords:** `ai`, `integration`, `mcp`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-mcp/SKILL.md`

### zoom-mcp/whiteboard
Guidance for the bundled Zoom Whiteboard MCP connector. Use for Whiteboard MCP auth,
endpoints, ID mapping, and tool workflows such as list_whiteboards and get_a_whiteboard.
Prefer this skill when the request is specifically about Whiteboard MCP rather than general Zoom MCP.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-mcp/whiteboard`
**Keywords:** `integration`, `mcp`, `whiteboard`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-mcp/whiteboard/SKILL.md`

### zoom-oauth
Reference skill for Zoom authentication. Use after routing to an auth workflow when choosing app credentials, grant types, scopes, token refresh behavior, or debugging Zoom OAuth failures.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/oauth`
**Keywords:** `configuration`, `oauth`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/oauth/SKILL.md`

## Customer Success

### triage-nda
Rapidly triage an incoming NDA and classify it as GREEN (standard approval), YELLOW (counsel review), or RED (full legal review). Use when a new NDA arrives from sales or business development, when screening for embedded non-solicits, non-competes, or missing carveouts, or when deciding whether an NDA can be signed under standard delegation.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/legal/skills/triage-nda`
**Keywords:** `contract`, `legal`, `nda`, `ticket-triage`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/triage-nda/SKILL.md`

## Data

### explore-data
Profile and explore a dataset to understand its shape, quality, and patterns. Use when encountering a new table or file, checking null rates and column distributions, spotting data quality issues like duplicates or suspicious values, or deciding which dimensions and metrics to analyze.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/data/skills/explore-data`
**Keywords:** `analytics`, `data`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/explore-data/SKILL.md`

### forecast
Generate a weighted sales forecast with best/likely/worst scenarios, commit vs. upside breakdown, and gap analysis. Use when preparing a quarterly forecast call, assessing gap-to-quota from a pipeline CSV, deciding which deals to commit vs. call upside, or checking pipeline coverage against your number.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/sales/skills/forecast`
**Keywords:** `crm`, `forecast`, `pipeline`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/forecast/SKILL.md`

### instrument-data-to-allotrope
Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope`
**Keywords:** `bio-research`, `data`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md`

### openai-spreadsheet
Use when tasks involve creating, editing, analyzing, or formatting spreadsheets (`.xlsx`,

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-spreadsheet/skills/openai-spreadsheet`
**Keywords:** `data`, `xlsx`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-spreadsheet/skills/openai-spreadsheet/SKILL.md`

### sql-queries
Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, PostgreSQL, etc.). Use when writing queries, optimizing slow SQL, translating between dialects, or building complex analytical queries with CTEs, window functions, or aggregations.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/data/skills/sql-queries`
**Keywords:** `analytics`, `data`, `sql`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/sql-queries/SKILL.md`

### write-query
Write optimized SQL for your dialect with best practices. Use when translating a natural-language data need into SQL, building a multi-CTE query with joins and aggregations, optimizing a query against a large partitioned table, or getting dialect-specific syntax for Snowflake, BigQuery, Postgres, etc.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/data/skills/write-query`
**Keywords:** `analytics`, `data`, `sql`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/write-query/SKILL.md`

## Design

### brand-voice-enforcement
This skill applies brand guidelines to content creation. It should be used when the user asks to "write an email", "draft a proposal", "create a pitch deck", "write a LinkedIn post", "draft a presentation", "write a Slack message", "draft sales content", or any content creation request where brand voice should be applied. Also triggers on "on-brand", "brand voice", "enforce voice", "apply brand guidelines", "brand-aligned content", "write in our voice", "use our brand tone", "make this sound like us", "rewrite this in our tone", or "this doesn't sound on-brand". Not for generating guidelines from scratch (use guideline-generation) or discovering brand materials (use discover-brand).

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/brand-voice/skills/brand-voice-enforcement`
**Keywords:** `brand`, `content`, `marketing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/brand-voice/skills/brand-voice-enforcement/SKILL.md`

### create-an-asset
Generate tailored sales assets (landing pages, decks, one-pagers, workflow demos) from your deal context. Describe your prospect, audience, and goal — get a polished, branded asset ready to share with customers.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/sales/skills/create-an-asset`
**Keywords:** `creative-media`, `design`, `pptx`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/create-an-asset/SKILL.md`

### figma-create-new-file
Create a new blank Figma file. Use when the user wants to create a new Figma design or FigJam file, or when you need a new file before calling use_figma. Handles plan resolution via whoami if needed. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard)

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/figma-create-new-file`
**Keywords:** `creative-media`, `design`, `figma`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-create-new-file/SKILL.md`

### figma-generate-library
Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/figma-generate-library`
**Keywords:** `design-system`, `figma`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-generate-library/SKILL.md`

### youtube-downloader
Download YouTube videos with customizable quality and format options. Use this skill when the user asks to download, save, or grab YouTube videos. Supports various quality settings (best, 1080p, 720p, 480p, 360p), multiple formats (mp4, webm, mkv), and audio-only downloads as MP3.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/youtube-downloader`
**Keywords:** `creative`, `creative-media`, `media`, `youtube`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/youtube-downloader/SKILL.md`

## Desktop

### seatbelt-sandboxer
Generates minimal macOS Seatbelt sandbox configurations. Use when sandboxing, isolating, or restricting macOS applications with allowlist-based profiles.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/seatbelt-sandboxer/skills/seatbelt-sandboxer`
**Keywords:** `macos`, `seatbelt`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/seatbelt-sandboxer/skills/seatbelt-sandboxer/SKILL.md`

## Developer Tools

### adding-dbt-unit-test
Creates unit test YAML definitions that mock upstream model inputs and validate expected outputs. Use when adding unit tests for a dbt model or practicing test-driven development (TDD) in dbt.

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/dbt/skills/adding-dbt-unit-test`
**Keywords:** `analytics`, `dbt`, `sql`, `testing`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/adding-dbt-unit-test/SKILL.md`

### angular-component
Create modern Angular standalone components following v20+ best practices. Use for building UI components with signal-based inputs/outputs, OnPush change detection, host bindings, content projection, and lifecycle hooks. Triggers on component creation, refactoring class-based inputs to signals, adding host bindings, or implementing accessible interactive components.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/angular-component`
**Keywords:** `angular`, `development`, `frontend`, `ui`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/angular-component/SKILL.md`

### angular-di
Implement dependency injection in Angular v20+ using inject(), injection tokens, and provider configuration. Use for service architecture, providing dependencies at different levels, creating injectable tokens, and managing singleton vs scoped services. Triggers on service creation, configuring providers, using injection tokens, or understanding DI hierarchy.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/angular-di`
**Keywords:** `angular`, `development`, `frontend`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/angular-di/SKILL.md`

### angular-directives
Create custom directives in Angular v20+ for DOM manipulation and behavior extension. Use for attribute directives that modify element behavior/appearance, structural directives for portals/overlays, and host directives for composition. Triggers on creating reusable DOM behaviors, extending element functionality, or composing behaviors across components. Note - use native @if/@for/@switch for control flow, not custom structural directives.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/angular-directives`
**Keywords:** `angular`, `development`, `frontend`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/angular-directives/SKILL.md`

### angular-forms
Build signal-based forms in Angular v21+ using the new Signal Forms API. Use for form creation with automatic two-way binding, schema-based validation, field state management, and dynamic forms. Triggers on form implementation, adding validation, creating multi-step forms, or building forms with conditional fields. Signal Forms are experimental but recommended for new Angular projects. Don't use for template-driven forms without signals or third-party form libraries like Formly or ngx-formly.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/angular-forms`
**Keywords:** `angular`, `development`, `frontend`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/angular-forms/SKILL.md`

### angular-http
Implement HTTP data fetching in Angular v20+ using resource(), httpResource(), and HttpClient. Use for API calls, data loading with signals, request/response handling, and interceptors. Triggers on data fetching, API integration, loading states, error handling, or converting Observable-based HTTP to signal-based patterns.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/angular-http`
**Keywords:** `angular`, `development`, `frontend`, `rest-api`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/angular-http/SKILL.md`

### angular-routing
Implement routing in Angular v20+ applications with lazy loading, functional guards, resolvers, and route parameters. Use for navigation setup, protected routes, route-based data loading, and nested routing. Triggers on route configuration, adding authentication guards, implementing lazy loading, or reading route parameters with signals.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/angular-routing`
**Keywords:** `angular`, `development`, `frontend`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/angular-routing/SKILL.md`

### angular-signals
Implement signal-based reactive state management in Angular v20+. Use for creating reactive state with signal(), derived state with computed(), dependent state with linkedSignal(), and side effects with effect(). Triggers on state management questions, converting from BehaviorSubject/Observable patterns to signals, or implementing reactive data flows.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/angular-signals`
**Keywords:** `angular`, `development`, `frontend`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/angular-signals/SKILL.md`

### angular-ssr
Implement server-side rendering and hydration in Angular v20+ using @angular/ssr. Use for SSR setup, hydration strategies, prerendering static pages, and handling browser-only APIs. Triggers on SSR configuration, fixing hydration mismatches, prerendering routes, or making code SSR-compatible.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/angular-ssr`
**Keywords:** `angular`, `development`, `frontend`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/angular-ssr/SKILL.md`

### angular-testing
Write unit and integration tests for Angular v20+ applications using Vitest or Jasmine with TestBed and modern testing patterns. Use for testing components with signals, OnPush change detection, services with inject(), and HTTP interactions. Triggers on test creation, testing signal-based components, mocking dependencies, or setting up test infrastructure. Don't use for E2E testing with Cypress or Playwright, or for testing non-Angular JavaScript/TypeScript code.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/angular-testing`
**Keywords:** `angular`, `development`, `testing`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/angular-testing/SKILL.md`

### angular-tooling
Use Angular CLI and development tools effectively in Angular v20+ projects. Use for project setup, code generation, building, testing, and configuration. Triggers on creating new projects, generating components/services/modules, configuring builds, running tests, or optimizing production builds. Don't use for Nx workspace commands, custom Webpack configurations, or non-Angular CLI build systems like Vite standalone or esbuild direct usage.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/angular-tooling`
**Keywords:** `angular`, `devcontainer`, `development`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/angular-tooling/SKILL.md`

### answering-natural-language-questions-with-dbt
Writes and executes SQL queries against the data warehouse using dbt's Semantic Layer or ad-hoc SQL to answer business questions. Use when a user asks about analytics, metrics, KPIs, or data (e.g., "What were total sales last quarter?", "Show me top customers by revenue"). NOT for validating, testing, or building dbt models during development.

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/dbt/skills/answering-natural-language-questions-with-dbt`
**Keywords:** `analytics`, `data`, `dbt`, `sql`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/answering-natural-language-questions-with-dbt/SKILL.md`

### aspnet-core
Build, review, refactor, or architect ASP.NET Core web applications using current official guidance for .NET web development. Use when working on Blazor Web Apps, Razor Pages, MVC, Minimal APIs, controller-based Web APIs, SignalR, gRPC, middleware, dependency injection, configuration, authentication, authorization, testing, performance, deployment, or ASP.NET Core upgrades.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/aspnet-core`
**Keywords:** `aspnet`, `development`, `dotnet`, `engineering`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/aspnet-core/SKILL.md`

### build-zoom-meeting-sdk-app
Reference skill for Zoom Meeting SDK. Use after routing to a meeting-embed workflow when implementing real Zoom meeting joins, platform-specific SDK behavior, auth and join flows, waiting room issues, or meeting bot patterns.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk`
**Keywords:** `development`, `meeting`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/SKILL.md`

### build-zoom-video-sdk-app
Reference skill for Zoom Video SDK. Use after routing to a custom-session workflow when the user needs full control over the video experience rather than an actual Zoom meeting.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk`
**Keywords:** `development`, `sdk`, `video`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/SKILL.md`

### building-dbt-semantic-layer
Use when creating or modifying dbt Semantic Layer components — semantic models, metrics, dimensions, entities, measures, or time spines. Covers MetricFlow configuration, metric types (simple, derived, cumulative, ratio, conversion), and validation for both latest and legacy YAML specs.

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/dbt/skills/building-dbt-semantic-layer`
**Keywords:** `analytics`, `data`, `dbt`, `sql`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/building-dbt-semantic-layer/SKILL.md`

### changelog-generator
Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical commits into clear, customer-friendly release notes. Turns hours of manual changelog writing into minutes of automated generation.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/changelog-generator`
**Keywords:** `development`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/changelog-generator/SKILL.md`

### code-review
Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/engineering/skills/code-review`
**Keywords:** `code-review`, `engineering`, `security`, `testing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/code-review/SKILL.md`

### contact-center/android
Zoom Contact Center SDK for Android. Use for native Android chat/video/ZVA/scheduled callback integrations, campaign mode, service lifecycle, and rejoin handling.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/android`
**Keywords:** `android`, `contact-center`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/android/SKILL.md`

### contact-center/ios
Zoom Contact Center SDK for iOS. Use for native iOS chat/video/ZVA/scheduled callback integrations, app lifecycle bridging, rejoin flow, and callback handling.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/ios`
**Keywords:** `contact-center`, `ios`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/ios/SKILL.md`

### contact-center/web
Zoom Contact Center SDK for Web. Use for web chat/video/campaign embeds, engagement event handling, app-context integrations, and Smart Embed postMessage workflows.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/web`
**Keywords:** `contact-center`, `sdk`, `web`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/web/SKILL.md`

### dbt
Skills for analytics engineering with dbt - building models, writing tests, querying the semantic layer, troubleshooting jobs, and more. Use when doing any dbt analytics engineering work.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/dbt`
**Keywords:** `analytics`, `data`, `dbt`, `development`, `sql`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/SKILL.md`

### deploy-to-vercel
Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

**Enabled:** `true`
**ID:** `external/vercel-agent-skills/skills/deploy-to-vercel`
**Keywords:** `actions`, `deploy`, `deployment`, `hosting`, `link`, `vercel`, `web`
**Source:** vercel-agent-skills

File: `external/vercel-agent-skills/skills/deploy-to-vercel/SKILL.md`

### figma-code-connect-components
Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code connect", "connect this component to code", "map this component", "link component to code", "create code connect mapping", or wants to establish mappings between Figma designs and code implementations. For canvas writes via `use_figma`, use `figma-use`.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/figma-code-connect-components`
**Keywords:** `design`, `design-system`, `development`, `figma`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-code-connect-components/SKILL.md`

### figma-implement-design
Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementing UI code from Figma files, when user mentions "implement design", "generate code", "implement component", provides Figma URLs, or asks to build components matching Figma specs. For Figma canvas writes via `use_figma`, use `figma-use`.

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/figma-implement-design`
**Keywords:** `design`, `development`, `figma`, `frontend`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/figma-implement-design/SKILL.md`

### frontend-design
Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

**Enabled:** `true`
**ID:** `external/anthropic-skills/skills/frontend-design`
**Keywords:** `design`, `development`, `frontend`, `ui`
**Source:** anthropic-skills

File: `external/anthropic-skills/skills/frontend-design/SKILL.md`

### frontend-design
Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/frontend-design`
**Keywords:** `design`, `development`, `frontend`, `ui`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/frontend-design/SKILL.md`

### jupyter-notebook
Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and run the helper script `new_notebook.py` to generate a clean starting notebook.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/jupyter-notebook`
**Keywords:** `data`, `development`, `jupyter`, `python`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/jupyter-notebook/SKILL.md`

### meeting-sdk/linux
Zoom Meeting SDK for Linux - C++ headless meeting bots with raw audio/video access, transcription, recording, and AI integration for server-side automation

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/linux`
**Keywords:** `linux`, `meeting`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/linux/SKILL.md`

### modern-python
Configures Python projects with modern tooling (uv, ruff, ty). Use when creating projects, writing standalone scripts, or migrating from pip/Poetry/mypy/black.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/modern-python/skills/modern-python`
**Keywords:** `devcontainer`, `development`, `engineering`, `python`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/modern-python/skills/modern-python/SKILL.md`

### notion-spec-to-implementation
Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/notion-spec-to-implementation`
**Keywords:** `development`, `notion`, `product`, `spec`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/notion-spec-to-implementation/SKILL.md`

### openai-develop-web-game
'Use when the agent is building or iterating on a web game (HTML/JS) and needs a reliable

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-develop-web-game/skills/openai-develop-web-game`
**Keywords:** `development`, `frontend`, `web`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-develop-web-game/skills/openai-develop-web-game/SKILL.md`

### openai-jupyter-notebook
Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments,

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-jupyter-notebook/skills/openai-jupyter-notebook`
**Keywords:** `data`, `development`, `jupyter`, `python`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-jupyter-notebook/skills/openai-jupyter-notebook/SKILL.md`

### openai-security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements.

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-security-best-practices/skills/openai-security-best-practices`
**Keywords:** `code-review`, `development`, `security`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-security-best-practices/skills/openai-security-best-practices/SKILL.md`

### playwright-interactive
Persistent browser and Electron interaction through `js_repl` for fast iterative UI debugging.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/playwright-interactive`
**Keywords:** `development`, `playwright`, `testing`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/playwright-interactive/SKILL.md`

### running-dbt-commands
Formats and executes dbt CLI commands, selects the correct dbt executable, and structures command parameters. Use when running models, tests, builds, compiles, or show queries via dbt CLI. Use when unsure which dbt executable to use or how to format command parameters.

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/dbt/skills/running-dbt-commands`
**Keywords:** `analytics`, `command`, `dbt`, `sql`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/running-dbt-commands/SKILL.md`

### security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/security-best-practices`
**Keywords:** `code-review`, `development`, `security`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/security-best-practices/SKILL.md`

### skill-creator
Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Kilo's capabilities with specialized knowledge, workflows, or tool integrations.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/skill-creator`
**Keywords:** `development`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/skill-creator/SKILL.md`

### using-dbt-for-analytics-engineering
Builds and modifies dbt models, writes SQL transformations using ref() and source(), creates tests, and validates results with dbt show. Use when doing any dbt work - building or modifying models, debugging errors, exploring unfamiliar data sources, writing tests, or evaluating impact of changes.

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/dbt/skills/using-dbt-for-analytics-engineering`
**Keywords:** `analytics`, `data`, `dbt`, `sql`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/dbt/skills/using-dbt-for-analytics-engineering/SKILL.md`

### vercel-composition-patterns
React composition patterns that scale. Use when refactoring components with boolean prop proliferation, building flexible component libraries, or designing reusable APIs. Triggers on tasks involving compound components, render props, context providers, or component architecture. Includes React 19 API changes.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/vercel-composition-patterns`
**Keywords:** `deployment`, `development`, `frontend`, `vercel`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/vercel-composition-patterns/SKILL.md`

### vercel-composition-patterns
No description.

**Enabled:** `true`
**ID:** `external/vercel-agent-skills/skills/composition-patterns`
**Keywords:** `architecture`, `development`, `frontend`, `react`, `refactor`, `refactoring`, `ui`, `vercel`
**Source:** vercel-agent-skills

File: `external/vercel-agent-skills/skills/composition-patterns/SKILL.md`

### vercel-deploy
Deploy applications and websites to Vercel. Use this skill when the user requests deployment actions such as "Deploy my app", "Deploy this to production", "Create a preview deployment", "Deploy and give me the link", or "Push this live". No authentication required - returns preview URL and claimable deployment link.

**Enabled:** `false`
**ID:** `external/kilo-marketplace-skills/skills/vercel-deploy`
**Keywords:** `deployment`, `development`, `frontend`, `vercel`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/vercel-deploy/SKILL.md`

### vercel-react-best-practices
React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/vercel-react-best-practices`
**Keywords:** `development`, `frontend`, `react`, `vercel`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/vercel-react-best-practices/SKILL.md`

### video-sdk/linux
Zoom Video SDK for Linux - C++ headless bots, raw audio/video capture/injection, Qt/GTK integration, Docker support

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/linux`
**Keywords:** `linux`, `sdk`, `video`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/linux/SKILL.md`

### video-sdk/web
Zoom Video SDK for Web - JavaScript/TypeScript integration for browser-based video sessions, real-time communication, screen sharing, recording, and live transcription

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/web`
**Keywords:** `sdk`, `video`, `web`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/web/SKILL.md`

### video-sdk/windows
Zoom Video SDK for Windows - C++ integration for video sessions, raw audio/video capture, screen sharing, recording, and real-time communication

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/windows`
**Keywords:** `sdk`, `video`, `windows`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/windows/SKILL.md`

### virtual-agent/android
Zoom Virtual Agent Android integration via WebView. Use for Java/Kotlin bridge callbacks, native URL handling, support_handoff relay, and lifecycle-safe embedding.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/android`
**Keywords:** `android`, `sdk`, `virtual-agent`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/android/SKILL.md`

### virtual-agent/ios
Zoom Virtual Agent iOS integration via WKWebView. Use for Swift/Objective-C script injection, message handlers, support_handoff relay, and URL routing policies.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/ios`
**Keywords:** `ios`, `sdk`, `virtual-agent`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/ios/SKILL.md`

### virtual-agent/web
Zoom Virtual Agent SDK for web embeds. Use for campaign or entry ID chat launch, event-driven controls, user context updates, and CSP-safe deployment.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/web`
**Keywords:** `sdk`, `virtual-agent`, `web`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/web/SKILL.md`

### web-design-guidelines
Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/web-design-guidelines`
**Keywords:** `development`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/web-design-guidelines/SKILL.md`

### winui-app
Bootstrap, develop, and design modern WinUI 3 desktop applications with C# and the Windows App SDK using official Microsoft guidance, WinUI Gallery patterns, Windows App SDK samples, and CommunityToolkit components. Use when creating a brand new app, preparing a machine for WinUI, reviewing, refactoring, planning, troubleshooting, environment-checking, or setting up WinUI 3 XAML, controls, navigation, windowing, theming, accessibility, responsiveness, performance, deployment, or related Windows app design and development work.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/winui-app`
**Keywords:** `development`, `ui`, `windows`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/winui-app/SKILL.md`

### zoom-cobrowse-sdk
Reference skill for Zoom Cobrowse SDK. Use after routing to a collaborative-support workflow when implementing browser co-browsing, annotation tools, privacy masking, remote assist, or PIN-based session sharing.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/cobrowse-sdk`
**Keywords:** `cobrowse`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/cobrowse-sdk/SKILL.md`

### zoom-meeting-sdk-android
Zoom Meeting SDK for Android native apps. Use when embedding Zoom meetings in Android with
default/custom UI, PKCE + SDK auth, join/start flows, and Meeting SDK API integration.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/android`
**Keywords:** `android`, `meeting`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/android/SKILL.md`

### zoom-meeting-sdk-electron
Zoom Meeting SDK for Electron desktop applications. Use when embedding Zoom meetings in an Electron app
with the Node addon wrapper, JWT auth, join/start flows, settings controllers, and raw data integration.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/electron`
**Keywords:** `electron`, `meeting`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/electron/SKILL.md`

### zoom-meeting-sdk-ios
Zoom Meeting SDK for iOS native apps. Use when embedding Zoom meetings in iOS with
default/custom UI, PKCE + SDK auth, host start with ZAK, and mobile lifecycle handling.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/ios`
**Keywords:** `ios`, `meeting`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/ios/SKILL.md`

### zoom-meeting-sdk-macos
Zoom Meeting SDK for macOS native apps. Use when embedding Zoom meetings in macOS with
default/custom UI, PKCE + SDK auth, host start/join flows, and desktop meeting feature controllers.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/macos`
**Keywords:** `macos`, `meeting`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/macos/SKILL.md`

### zoom-meeting-sdk-react-native
Zoom Meeting SDK for React Native. Use when embedding Zoom meetings in React Native iOS/Android apps with @zoom/meetingsdk-react-native, JWT auth, join/start flows, platform setup, and native bridge troubleshooting.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/react-native`
**Keywords:** `meeting`, `react-native`, `sdk`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/react-native/SKILL.md`

### zoom-meeting-sdk-unreal
Zoom Meeting SDK for Unreal Engine wrapper integrations. Use when building Unreal projects that
embed Zoom meetings with C++ and Blueprint wrappers, including wrapper-to-SDK mapping concerns.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/unreal`
**Keywords:** `meeting`, `sdk`, `unreal`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/unreal/SKILL.md`

### zoom-meeting-sdk-web
Zoom Meeting SDK for Web - Embed Zoom meeting capabilities into web applications. Two integration
options: Client View (full-page, familiar Zoom UI) and Component View (embeddable, Promise-based API).
Includes SharedArrayBuffer setup for HD video, gallery view, and virtual backgrounds.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web`
**Keywords:** `meeting`, `sdk`, `web`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/SKILL.md`

### zoom-meeting-sdk-web-client-view
Zoom Meeting SDK Web - Client View. Full-page Zoom meeting experience with the familiar Zoom interface.
Uses ZoomMtg global singleton with callback-based API. Ideal for quick integration with minimal
customization. Provides the same UI as Zoom Web Client.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/client-view`
**Keywords:** `meeting`, `meeting-sdk`, `sdk`, `web`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/client-view/SKILL.md`

### zoom-meeting-sdk-web-component-view
Zoom Meeting SDK Web - Component View. Embeddable Zoom meeting components with Promise-based API
for flexible integration. Ideal for React/Vue/Angular apps and custom layouts. Uses ZoomMtgEmbedded
with async/await patterns and embeddable UI containers.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/component-view`
**Keywords:** `meeting`, `meeting-sdk`, `sdk`, `web`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/component-view/SKILL.md`

### zoom-meeting-sdk-windows
Zoom Meeting SDK for Windows - Native C++ SDK for embedding Zoom meetings into Windows desktop
applications. Supports custom UI architecture with raw video/audio data, headless bots, and deep
integration with meeting features. Includes SDK architecture patterns and Windows message loop handling.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/windows`
**Keywords:** `meeting`, `sdk`, `windows`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/windows/SKILL.md`

### zoom-video-sdk-android
Zoom Video SDK for Android native apps. Use when building custom Android video experiences
with full UI control, session tokens, raw media options, and event-driven participant state.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/android`
**Keywords:** `android`, `sdk`, `video`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/android/SKILL.md`

### zoom-video-sdk-flutter
Zoom Video SDK for Flutter. Use when building custom video session apps in Flutter with
flutter_zoom_videosdk, event-driven architecture, session lifecycle handling, and mobile
platform integration patterns.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/flutter`
**Keywords:** `flutter`, `sdk`, `video`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/flutter/SKILL.md`

### zoom-video-sdk-ios
Zoom Video SDK for iOS native apps. Use when building custom iOS video sessions with
full UI control, token-based session auth, and event-driven media/participant flows.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/ios`
**Keywords:** `ios`, `sdk`, `video`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/ios/SKILL.md`

### zoom-video-sdk-macos
Zoom Video SDK for macOS native desktop apps. Use when building custom macOS video sessions
with native UI control, tokenized join, and desktop-oriented media/device workflows.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/macos`
**Keywords:** `macos`, `sdk`, `video`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/macos/SKILL.md`

### zoom-video-sdk-react-native
Zoom Video SDK for React Native. Use when building custom mobile video session experiences
with @zoom/react-native-videosdk, event listeners, helper-based APIs, and backend JWT token flows.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/react-native`
**Keywords:** `react-native`, `sdk`, `video`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/react-native/SKILL.md`

### zoom-video-sdk-unity
Zoom Video SDK for Unity wrapper integrations. Use when building custom Unity-based
video session experiences and mapping Unity scene/UI state to Video SDK events.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/unity`
**Keywords:** `sdk`, `unity`, `video`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/unity/SKILL.md`

## Devops

### cloudflare-deploy
Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. Use when the user asks to deploy, host, publish, or set up a project on Cloudflare.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/cloudflare-deploy`
**Keywords:** `cloudflare`, `deployment`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/cloudflare-deploy/SKILL.md`

### netlify-deploy
Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/netlify-deploy`
**Keywords:** `deployment`, `netlify`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/netlify-deploy/SKILL.md`

### openai-cloudflare-deploy
Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-cloudflare-deploy/skills/openai-cloudflare-deploy`
**Keywords:** `cloudflare`, `deployment`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-cloudflare-deploy/skills/openai-cloudflare-deploy/SKILL.md`

### openai-netlify-deploy
Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/openai-netlify-deploy/skills/openai-netlify-deploy`
**Keywords:** `deployment`, `netlify`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/openai-netlify-deploy/skills/openai-netlify-deploy/SKILL.md`

### render-deploy
Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deeplinks. Use when the user wants to deploy, host, publish, or set up their application on Render's cloud platform.

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/render-deploy`
**Keywords:** `deployment`, `render`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/render-deploy/SKILL.md`

### vercel-deploy
Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

**Enabled:** `true`
**ID:** `external/openai-skills/skills/.curated/vercel-deploy`
**Keywords:** `deployment`, `vercel`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/vercel-deploy/SKILL.md`

## Documents

### view-pdf
Interactive PDF viewer. Use when the user wants to open, show, or view a PDF and collaborate on it visually — annotate, highlight, stamp, fill form fields, place signature/initials, or review markup together. Not for summarization or text extraction (use native Read instead).

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/pdf-viewer/skills/view-pdf`
**Keywords:** `documents`, `pdf`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/pdf-viewer/skills/view-pdf/SKILL.md`

## Engineering

### address-sanitizer
AddressSanitizer detects memory errors during fuzzing. Use when fuzzing C/C++ code to find buffer overflows and use-after-free bugs.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/address-sanitizer`
**Keywords:** `cpp`, `fuzzing`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/address-sanitizer/SKILL.md`

### atheris
Atheris is a coverage-guided Python fuzzer based on libFuzzer. Use for fuzzing pure Python code and Python C extensions.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/atheris`
**Keywords:** `fuzzing`, `python`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/atheris/SKILL.md`

### cargo-fuzz
cargo-fuzz is the de facto fuzzing tool for Rust projects using Cargo. Use for fuzzing Rust code with libFuzzer backend.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/cargo-fuzz`
**Keywords:** `fuzzing`, `rust`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/cargo-fuzz/SKILL.md`

### codeql
Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. Triggers on "run codeql", "codeql scan", "codeql analysis", "build codeql database", or "find vulnerabilities with codeql". Supports "run all" (security-and-quality + security-experimental suites) and "important only" (high-precision security findings) scan modes. Also handles creating data extension models and processing CodeQL SARIF output.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/static-analysis/skills/codeql`
**Keywords:** `codeql`, `security`, `static-analysis`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/static-analysis/skills/codeql/SKILL.md`

### create-viz
Create publication-quality visualizations with Python. Use when turning query results or a DataFrame into a chart, selecting the right chart type for a trend or comparison, generating a plot for a report or presentation, or needing an interactive chart with hover and zoom.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/data/skills/create-viz`
**Keywords:** `data`, `python`, `visualization`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/create-viz/SKILL.md`

### crypto-protocol-diagram
Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow, extracting message flow from a spec or RFC, diagramming a ProVerif or Tamarin model, or drawing sequence diagrams for TLS, Noise, Signal, X3DH, Double Ratchet, FROST, DH, or ECDH protocols.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram`
**Keywords:** `architecture`, `cryptography`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram/SKILL.md`

### data-visualization
Create effective data visualizations with Python (matplotlib, seaborn, plotly). Use when building charts, choosing the right chart type for a dataset, creating publication-quality figures, or applying design principles like accessibility and color theory.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/data/skills/data-visualization`
**Keywords:** `data`, `python`, `visualization`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/data-visualization/SKILL.md`

### incident-response
Run an incident response workflow — triage, communicate, and write postmortem. Trigger with "we have an incident", "production is down", an alert that needs severity assessment, a status update mid-incident, or when writing a blameless postmortem after resolution.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/engineering/skills/incident-response`
**Keywords:** `engineering`, `incident`, `operations`, `ticket-triage`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/incident-response/SKILL.md`

### libafl
LibAFL is a modular fuzzing library for building custom fuzzers. Use for advanced fuzzing needs, custom mutators, or non-standard fuzzing targets.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/libafl`
**Keywords:** `fuzzing`, `rust`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/libafl/SKILL.md`

### ruzzy
Ruzzy is a coverage-guided Ruby fuzzer by Trail of Bits. Use for fuzzing pure Ruby code and Ruby C extensions.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/ruzzy`
**Keywords:** `fuzzing`, `rust`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/ruzzy/SKILL.md`

### sarif-parsing
Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on "parse sarif", "read scan results", "aggregate findings", "deduplicate alerts", or "process sarif output". Handles filtering, deduplication, format conversion, and CI/CD integration of SARIF data. Does NOT run scans — use the Semgrep or CodeQL skills for that.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/static-analysis/skills/sarif-parsing`
**Keywords:** `sarif`, `security`, `static-analysis`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/static-analysis/skills/sarif-parsing/SKILL.md`

### semgrep
Run Semgrep static analysis scan on a codebase using parallel subagents. Supports two scan modes — "run all" (full ruleset coverage) and "important only" (high-confidence security vulnerabilities). Automatically detects and uses Semgrep Pro for cross-file taint analysis when available. Use when asked to scan code for vulnerabilities, run a security audit with Semgrep, find bugs, or perform static analysis. Spawns parallel workers for multi-language codebases.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/static-analysis/skills/semgrep`
**Keywords:** `security`, `semgrep`, `static-analysis`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/static-analysis/skills/semgrep/SKILL.md`

### system-design
Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "system design for", "what's the right architecture for", or when the user needs help with API design, data modeling, or service boundaries.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/engineering/skills/system-design`
**Keywords:** `architecture`, `design`, `engineering`, `system-design`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/system-design/SKILL.md`

### tech-debt
Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or when the user asks about code quality, refactoring priorities, or maintenance backlog.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/engineering/skills/tech-debt`
**Keywords:** `engineering`, `refactor`, `tech-debt`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/tech-debt/SKILL.md`

### testing-strategy
Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests for", "test plan", "what tests do we need", or when the user needs help with testing approaches, coverage, or test architecture.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/engineering/skills/testing-strategy`
**Keywords:** `engineering`, `testing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/engineering/skills/testing-strategy/SKILL.md`

### variant-analysis
Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audits after finding an initial issue.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis`
**Keywords:** `security`, `static-analysis`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis/SKILL.md`

### zeroize-audit
Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling secrets, keys, passwords, or other sensitive data.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/zeroize-audit/skills/zeroize-audit`
**Keywords:** `cryptography`, `rust`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/zeroize-audit/skills/zeroize-audit/SKILL.md`

## Finance

### journal-entry
Prepare journal entries with proper debits, credits, and supporting detail. Use when booking month-end accruals (AP, payroll, prepaid), recording depreciation or amortization, posting revenue recognition or deferred revenue adjustments, or documenting an entry for audit review.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/finance/skills/journal-entry`
**Keywords:** `finance`, `journal-entry`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/journal-entry/SKILL.md`

### journal-entry-prep
Prepare journal entries with proper debits, credits, and supporting documentation for month-end close. Use when booking accruals, prepaid amortization, fixed asset depreciation, payroll entries, revenue recognition, or any manual journal entry.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/finance/skills/journal-entry-prep`
**Keywords:** `finance`, `journal-entry`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/journal-entry-prep/SKILL.md`

## Frontend

### build-dashboard
Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results into a shareable self-contained report, building a team monitoring snapshot, or needing multiple charts with filters in one browser-openable file.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/data/skills/build-dashboard`
**Keywords:** `analytics`, `dashboard`, `data`, `frontend`, `visualization`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/data/skills/build-dashboard/SKILL.md`

### burpsuite-project-parser
Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or analyzing HTTP traffic captured in a Burp project.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/burpsuite-project-parser/skills/burpsuite-project-parser`
**Keywords:** `burp`, `security`, `web`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md`

### design-handoff
Generate developer handoff specs from a design. Use when a design is ready for engineering and needs a spec sheet covering layout, design tokens, component props, interaction states, responsive breakpoints, edge cases, and animation details.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/design/skills/design-handoff`
**Keywords:** `design`, `frontend`, `spec`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/design-handoff/SKILL.md`

### ffuf-web-fuzzing
Expert guidance for ffuf web fuzzing during authorized penetration testing. Covers directory discovery, subdomain enumeration, parameter fuzzing, authenticated fuzzing with raw requests, auto-calibration, and result analysis. Use when running ffuf scans, analyzing ffuf output, or building fuzzing strategies for web targets.

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/ffuf-web-fuzzing/skills/ffuf-web-fuzzing`
**Keywords:** `fuzzing`, `security`, `web`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/ffuf-web-fuzzing/skills/ffuf-web-fuzzing/SKILL.md`

### figma-implement-design
Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementing UI code from Figma files, when user mentions "implement design", "generate code", "implement component", provides Figma URLs, or asks to build components matching Figma specs. For Figma canvas writes via `use_figma`, use `figma-use`.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/figma-implement-design`
**Keywords:** `design`, `figma`, `frontend`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/figma-implement-design/SKILL.md`

### react-pdf
No description.

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/react-pdf/skills/react-pdf`
**Keywords:** `frontend`, `pdf`, `react`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/react-pdf/skills/react-pdf/SKILL.md`

## Ml

### nextflow-development
Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing RNA-seq, WGS/WES, or ATAC-seq data—either local FASTQs or public datasets from GEO/SRA. Triggers on nf-core, Nextflow, FASTQ analysis, variant calling, gene expression, differential expression, GEO reanalysis, GSE/GSM/SRR accessions, or samplesheet creation.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/bio-research/skills/nextflow-development`
**Keywords:** `bio-research`, `nextflow`, `pipeline`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/nextflow-development/SKILL.md`

## Mobile

### firebase-apk-scanner
Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase vulnerabilities, performing mobile app security audits, or testing Firebase endpoint security. For authorized security research only.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/firebase-apk-scanner/skills/firebase-apk-scanner`
**Keywords:** `android`, `firebase`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md`

## Operations

### change-request
Create a change management request with impact analysis and rollback plan. Use when proposing a system or process change that needs approval, preparing a change record for CAB review, documenting risk and rollback steps before a deployment, or planning stakeholder communications for a rollout.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/operations/skills/change-request`
**Keywords:** `change-management`, `operations`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/operations/skills/change-request/SKILL.md`

## People

### draft-offer
Draft an offer letter with comp details and terms. Use when a candidate is ready for an offer, assembling a total comp package (base, equity, signing bonus), writing the offer letter text itself, or prepping negotiation guidance for the hiring manager.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/human-resources/skills/draft-offer`
**Keywords:** `compensation`, `hr`, `offer`, `recruiting`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/draft-offer/SKILL.md`

### interview-prep
Create structured interview plans with competency-based questions and scorecards. Trigger with "interview plan for", "interview questions for", "how should we interview", "scorecard for", or when the user is preparing to interview candidates.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/human-resources/skills/interview-prep`
**Keywords:** `hr`, `interviewing`, `recruiting`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/interview-prep/SKILL.md`

### onboarding
Generate an onboarding checklist and first-week plan for a new hire. Use when someone has a start date coming up, building the pre-start task list (accounts, equipment, buddy), scheduling Day 1 and Week 1, or setting 30/60/90-day goals for a new team member.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/human-resources/skills/onboarding`
**Keywords:** `hr`, `onboarding`, `recruiting`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/onboarding/SKILL.md`

## Product

### competitive-ads-extractor
Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging, problems, and creative approaches are working. Helps inspire and improve your own ad campaigns.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/competitive-ads-extractor`
**Keywords:** `ads`, `business`, `business-marketing`, `competitive-intelligence`, `marketing`, `research`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/competitive-ads-extractor/SKILL.md`

### competitive-intelligence
Research your competitors and build an interactive battlecard. Outputs an HTML artifact with clickable competitor cards and a comparison matrix. Trigger with "competitive intel", "research competitors", "how do we compare to [competitor]", "battlecard for [competitor]", or "what's new with [competitor]".

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/sales/skills/competitive-intelligence`
**Keywords:** `competitive-intelligence`, `research`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/competitive-intelligence/SKILL.md`

### discover-brand
This skill orchestrates autonomous discovery of brand materials across enterprise platforms (Notion, Confluence, Google Drive, Box, SharePoint, Figma, Gong, Granola, Slack). It should be used when the user asks to "discover brand materials", "find brand documents", "search for brand guidelines", "audit brand content", "what brand materials do we have", "find our style guide", "where are our brand docs", "do we have a style guide", "discover brand voice", "brand content audit", or "find brand assets".

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/brand-voice/skills/discover-brand`
**Keywords:** `brand`, `marketing`, `user-research`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/brand-voice/skills/discover-brand/SKILL.md`

### user-research
Plan, conduct, and synthesize user research. Trigger with "user research plan", "interview guide", "usability test", "survey design", "research questions", or when the user needs help with any aspect of understanding their users through research.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/design/skills/user-research`
**Keywords:** `design`, `research`, `user-research`, `ux`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/design/skills/user-research/SKILL.md`

## Qa

### aflpp
AFL++ is a fork of AFL with better fuzzing performance and advanced features. Use for multi-core fuzzing of C/C++ projects.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/aflpp`
**Keywords:** `afl`, `fuzzing`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/aflpp/SKILL.md`

### audit-support
Support SOX 404 compliance with control testing methodology, sample selection, and documentation standards. Use when generating testing workpapers, selecting audit samples, classifying control deficiencies, or preparing for internal or external audits.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/finance/skills/audit-support`
**Keywords:** `audit`, `compliance`, `finance`, `sox`, `testing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/audit-support/SKILL.md`

### constant-time-testing
Constant-time testing detects timing side channels in cryptographic code. Use when auditing crypto implementations for timing vulnerabilities.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/constant-time-testing`
**Keywords:** `cryptography`, `security`, `testing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/constant-time-testing/SKILL.md`

### coverage-analysis
Coverage analysis measures code exercised during fuzzing. Use when assessing harness effectiveness or identifying fuzzing blockers.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/coverage-analysis`
**Keywords:** `security`, `testing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/coverage-analysis/SKILL.md`

### fuzzing-dictionary
Fuzzing dictionaries guide fuzzers with domain-specific tokens. Use when fuzzing parsers, protocols, or format-specific code.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-dictionary`
**Keywords:** `fuzzing`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-dictionary/SKILL.md`

### fuzzing-obstacles
Techniques for patching code to overcome fuzzing obstacles. Use when checksums, global state, or other barriers block fuzzer progress.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-obstacles`
**Keywords:** `fuzzing`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-obstacles/SKILL.md`

### genotoxic
Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circomvent and cairo-mutants), or using necessist.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/trailmark/skills/genotoxic`
**Keywords:** `fuzzing`, `security`, `smart-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/genotoxic/SKILL.md`

### harness-writing
Techniques for writing effective fuzzing harnesses across languages. Use when creating new fuzz targets or improving existing harness code.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/harness-writing`
**Keywords:** `fuzzing`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/harness-writing/SKILL.md`

### mutation-testing
Configures mewt or muton mutation testing campaigns — scopes targets, tunes timeouts, and optimizes long-running runs. Use when the user mentions mewt, muton, mutation testing, or wants to configure or optimize a mutation testing campaign.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/mutation-testing/skills/mutation-testing`
**Keywords:** `fuzzing`, `security`, `testing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/mutation-testing/skills/mutation-testing/SKILL.md`

### property-based-testing
Provides guidance for property-based testing across multiple languages and smart contracts. Use when writing tests, reviewing code with serialization/validation/parsing patterns, designing features, or when property-based testing would provide stronger coverage than example-based tests.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/property-based-testing/skills/property-based-testing`
**Keywords:** `security`, `testing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/property-based-testing/skills/property-based-testing/SKILL.md`

### single-cell-rna-qc
Performs quality control on single-cell RNA-seq data (.h5ad or .h5 files) using scverse best practices with MAD-based filtering and comprehensive visualizations. Use when users request QC analysis, filtering low-quality cells, assessing data quality, or following scverse/scanpy best practices for single-cell analysis.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/bio-research/skills/single-cell-rna-qc`
**Keywords:** `bio-research`, `testing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/single-cell-rna-qc/SKILL.md`

### sox-testing
Generate SOX sample selections, testing workpapers, and control assessments. Use when planning quarterly or annual SOX 404 testing, pulling a sample for a control (revenue, P2P, ITGC, close), building a testing workpaper template, or evaluating and classifying a control deficiency.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/finance/skills/sox-testing`
**Keywords:** `audit`, `compliance`, `finance`, `sox`, `testing`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/sox-testing/SKILL.md`

### vector-forge
Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/trailmark/skills/vector-forge`
**Keywords:** `cryptography`, `fuzzing`, `security`, `testing`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`

## Research

### account-research
Research a company using Common Room data. Triggers on 'research [company]', 'tell me about [domain]', 'pull up signals for [account]', 'what's going on with [company]', or any account-level question.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/account-research`
**Keywords:** `account-research`, `common-room`, `research`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/account-research/SKILL.md`

### account-research
Research a company or person and get actionable sales intel. Works standalone with web search, supercharged when you connect enrichment tools or your CRM. Trigger with "research [company]", "look up [person]", "intel on [prospect]", "who is [name] at [company]", or "tell me about [company]".

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/sales/skills/account-research`
**Keywords:** `account-research`, `crm`, `research`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/account-research/SKILL.md`

### contact-research
Research a specific person using Common Room data. Triggers on 'who is [name]', 'look up [email]', 'research [contact]', 'is [name] a warm lead', or any contact-level question.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/contact-research`
**Keywords:** `common-room`, `research`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/contact-research/SKILL.md`

### customer-research
Multi-source research on a customer question or topic with source attribution. Use when a customer asks something you need to look up, investigating whether a bug has been reported before, checking what was previously told to a specific account, or gathering background before drafting a response.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/customer-support/skills/customer-research`
**Keywords:** `customer-support`, `knowledge`, `research`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/customer-support/skills/customer-research/SKILL.md`

### lead-research-assistant
Identifies high-quality leads for your product or service by analyzing your business, searching for target companies, and providing actionable contact strategies. Perfect for sales, business development, and marketing professionals.

**Enabled:** `true`
**ID:** `external/kilo-marketplace-skills/skills/lead-research-assistant`
**Keywords:** `business`, `business-marketing`, `crm`, `lead-generation`, `marketing`, `research`, `sales`
**Source:** kilo-marketplace-skills

File: `external/kilo-marketplace-skills/skills/lead-research-assistant/SKILL.md`

### memory-management
Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames, and internal language so Claude understands requests like a colleague would. CLAUDE.md for working memory, memory/ directory for the full knowledge base.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/productivity/skills/memory-management`
**Keywords:** `knowledge`, `memory`, `productivity`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/productivity/skills/memory-management/SKILL.md`

### notion-knowledge-capture
Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking.

**Enabled:** `false`
**ID:** `external/openai-skills/skills/.curated/notion-knowledge-capture`
**Keywords:** `knowledge`, `notion`, `productivity`
**Source:** openai-skills

File: `external/openai-skills/skills/.curated/notion-knowledge-capture/SKILL.md`

### search
Search across all connected sources in one query. Trigger with "find that doc about...", "what did we decide on...", "where was the conversation about...", or when looking for a decision, document, or discussion that could live in chat, email, cloud storage, or a project tracker.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search`
**Keywords:** `enterprise-search`, `knowledge`, `search`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search/SKILL.md`

### x-research
Searches X/Twitter for real-time perspectives, dev discussions, product feedback, breaking news, and expert opinions using the X API v2. Provides search with engagement sorting, user profiles, thread fetching, watchlists, and result caching. Use when: (1) user says "x research", "search x for", "search twitter for", "what are people saying about", "what's twitter saying", "check x for", "x search", (2) user needs recent X discourse on a topic (library releases, API changes, product launches, industry events), (3) user wants to find what devs/experts/community thinks about a topic. NOT for: posting tweets or account management.

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/x-research/skills/x-research`
**Keywords:** `marketing`, `research`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/x-research/skills/x-research/SKILL.md`

## Sales

### call-summary
Process call notes or a transcript — extract action items, draft follow-up email, generate internal summary. Use when pasting rough notes or a transcript after a discovery, demo, or negotiation call, drafting a customer follow-up, logging the activity for your CRM, or capturing objections and next steps for your team.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/sales/skills/call-summary`
**Keywords:** `crm`, `email`, `sales`, `transcribe`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/call-summary/SKILL.md`

### compose-outreach
Generate personalized outreach messages using Common Room signals. Triggers on 'draft outreach to [person]', 'write an email to [name]', 'compose a message for [contact]', or any outreach drafting request.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/compose-outreach`
**Keywords:** `common-room`, `email`, `outreach`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/compose-outreach/SKILL.md`

### draft-outreach
Research a prospect then draft personalized outreach. Uses web research by default, supercharged with enrichment and CRM. Trigger with "draft outreach to [person/company]", "write cold email to [prospect]", "reach out to [name]".

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/sales/skills/draft-outreach`
**Keywords:** `crm`, `email`, `outreach`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/sales/skills/draft-outreach/SKILL.md`

### enrich-lead
Instant lead enrichment. Drop a name, company, LinkedIn URL, or email and get the full contact card with email, phone, title, company intel, and next actions.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/enrich-lead`
**Keywords:** `apollo`, `crm`, `lead-generation`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/enrich-lead/SKILL.md`

### prospect
Full ICP-to-leads pipeline. Describe your ideal customer in plain English and get a ranked table of enriched decision-maker leads with emails and phone numbers.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/prospect`
**Keywords:** `apollo`, `crm`, `lead-generation`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/prospect/SKILL.md`

### prospect
Build targeted account or contact lists using Common Room's Prospector. Triggers on 'find companies that match [criteria]', 'build a prospect list', 'find contacts at [type of company]', 'show me companies hiring [role]', or any list-building request.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/prospect`
**Keywords:** `common-room`, `crm`, `lead-generation`, `sales`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/prospect/SKILL.md`

### recruiting-pipeline
Track and manage recruiting pipeline stages. Trigger with "recruiting update", "candidate pipeline", "how many candidates", "hiring status", or when the user discusses sourcing, screening, interviewing, or extending offers.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/human-resources/skills/recruiting-pipeline`
**Keywords:** `hr`, `pipeline`, `recruiting`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/recruiting-pipeline/SKILL.md`

## Security

### algorand-vulnerability-scanner
Scans Algorand smart contracts for 11 common vulnerabilities including rekeying attacks, unchecked transaction fees, missing field validations, and access control issues. Use when auditing Algorand projects (TEAL/PyTeal).

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/building-secure-contracts/skills/algorand-vulnerability-scanner`
**Keywords:** `algorand`, `blockchain`, `security`, `smart-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md`

### cairo-vulnerability-scanner
Scans Cairo/StarkNet smart contracts for 6 critical vulnerabilities including felt252 arithmetic overflow, L1-L2 messaging issues, address conversion problems, and signature replay. Use when auditing StarkNet projects.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/building-secure-contracts/skills/cairo-vulnerability-scanner`
**Keywords:** `blockchain`, `cairo`, `security`, `smart-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md`

### compliance-check
Run a compliance check on a proposed action, product feature, or business initiative, surfacing applicable regulations, required approvals, and risk areas. Use when launching a feature that touches personal data, when marketing or product proposes something with regulatory implications, or when you need to know which approvals and jurisdictional requirements apply before proceeding.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/legal/skills/compliance-check`
**Keywords:** `compliance`, `legal`, `risk`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/compliance-check/SKILL.md`

### cosmos-vulnerability-scanner
Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner`
**Keywords:** `blockchain`, `cosmos`, `security`, `smart-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md`

### ghidra-headless
Reverse engineers binaries using Ghidra's headless analyzer. Use when decompiling executables, extracting functions, strings, symbols, or analyzing call graphs from compiled binaries without the Ghidra GUI.

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/ghidra-headless/skills/ghidra-headless`
**Keywords:** `binary`, `ghidra`, `security`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/ghidra-headless/skills/ghidra-headless/SKILL.md`

### last30days
Researches a topic from the last 30 days on Reddit, X, and the web. Surfaces real community discussions with engagement metrics and synthesizes findings into actionable insights. Use when the user wants to know what people are saying about a topic right now.

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/last30days/skills/last30days`
**Keywords:** `research`, `security`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/last30days/skills/last30days/SKILL.md`

### mermaid-to-proverif
Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, forward secrecy), checking for replay attacks, or producing a .pv file from a sequence diagram.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif`
**Keywords:** `cryptography`, `security`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif/SKILL.md`

### policy-lookup
Find and explain company policies in plain language. Trigger with "what's our PTO policy", "can I work remotely from another country", "how do expenses work", or any plain-language question about benefits, travel, leave, or handbook rules.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/human-resources/skills/policy-lookup`
**Keywords:** `hr`, `knowledge`, `policy`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/human-resources/skills/policy-lookup/SKILL.md`

### reconciliation
Reconcile accounts by comparing GL balances to subledgers, bank statements, or third-party data. Use when performing bank reconciliations, GL-to-subledger recs, intercompany reconciliations, or identifying and categorizing reconciling items.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/finance/skills/reconciliation`
**Keywords:** `audit`, `finance`, `reconciliation`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/finance/skills/reconciliation/SKILL.md`

### scv-scan
Audits Solidity codebases for smart contract vulnerabilities using a four-phase workflow (cheatsheet loading, codebase sweep, deep validation, reporting) covering 36 vulnerability classes. Use when auditing Solidity contracts for security issues, performing smart contract vulnerability scans, or reviewing Solidity code for common exploit patterns.

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/scv-scan/skills/scv-scan`
**Keywords:** `audit`, `security`, `smart-contracts`, `solidity`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/scv-scan/skills/scv-scan/SKILL.md`

### seo-audit
Run a comprehensive SEO audit — keyword research, on-page analysis, content gaps, technical checks, and competitor comparison. Use when assessing a site's SEO health, when finding keyword opportunities and content gaps competitors own, or when you need a prioritized action plan split into quick wins and strategic investments.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/marketing/skills/seo-audit`
**Keywords:** `audit`, `content`, `marketing`, `seo`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/marketing/skills/seo-audit/SKILL.md`

### solana-vulnerability-scanner
Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use when auditing Solana/Anchor programs.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/building-secure-contracts/skills/solana-vulnerability-scanner`
**Keywords:** `blockchain`, `security`, `smart-contracts`, `solana`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md`

### substrate-vulnerability-scanner
Scans Substrate/Polkadot pallets for 7 critical vulnerabilities including arithmetic overflow, panic DoS, incorrect weights, and bad origin checks. Use when auditing Substrate runtimes or FRAME pallets.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/building-secure-contracts/skills/substrate-vulnerability-scanner`
**Keywords:** `blockchain`, `security`, `smart-contracts`, `substrate`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md`

### supply-chain-risk-auditor
Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagements.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor`
**Keywords:** `audit`, `risk`, `security`, `supply-chain`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md`

### token-integration-analyzer
Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Context-aware for both token implementations and token integrations.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer`
**Keywords:** `blockchain`, `security`, `smart-contracts`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer/SKILL.md`

### ton-vulnerability-scanner
Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without gas checks. Use when auditing FunC contracts.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/building-secure-contracts/skills/ton-vulnerability-scanner`
**Keywords:** `blockchain`, `security`, `smart-contracts`, `ton`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md`

### vendor-check
Check the status of existing agreements with a vendor across all connected systems — CLM, CRM, email, and document storage — with gap analysis and upcoming deadlines. Use when onboarding or renewing a vendor, when you need a consolidated view of what's signed and what's missing (MSA, DPA, SOW), or when checking for approaching expirations and surviving obligations.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/legal/skills/vendor-check`
**Keywords:** `compliance`, `contract`, `legal`, `vendor`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/legal/skills/vendor-check/SKILL.md`

### wooyun-legacy
Provides web vulnerability testing methodology distilled from 88,636 real-world cases from the WooYun vulnerability database (2010-2016). Use when performing penetration testing, security audits, code reviews for security flaws, or vulnerability research. Covers SQL injection, XSS, command execution, file upload, path traversal, unauthorized access, information disclosure, and business logic flaws.

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/wooyun-legacy/skills/wooyun-legacy`
**Keywords:** `security`
**Source:** trailofbits-skills-curated

File: `external/trailofbits-skills-curated/plugins/wooyun-legacy/skills/wooyun-legacy/SKILL.md`

### yara-rule-authoring
Guides authoring of high-quality YARA-X detection rules for malware identification. Use when writing, reviewing, or optimizing YARA rules. Covers naming conventions, string selection, performance optimization, migration from legacy YARA, and false positive reduction. Triggers on: YARA, YARA-X, malware detection, threat hunting, IOC, signature, crx module, dex module.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/yara-authoring/skills/yara-rule-authoring`
**Keywords:** `malware`, `security`, `yara`
**Source:** trailofbits-skills

File: `external/trailofbits-skills/plugins/yara-authoring/skills/yara-rule-authoring/SKILL.md`

## Zoom

### scribe
Reference skill for Zoom AI Services Scribe. Use after routing to a transcription workflow when handling uploaded or stored media, Build-platform JWT auth, fast mode transcription, batch jobs, or transcript pipeline design.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/scribe`
**Keywords:** `media`, `transcribe`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/scribe/SKILL.md`

### zoom-rtms
Reference skill for Zoom RTMS. Use after routing to a live-media workflow when processing real-time audio, video, chat, transcripts, screen share, or contact-center voice streams.

**Enabled:** `false`
**ID:** `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rtms`
**Keywords:** `media`, `rtms`, `zoom`
**Source:** anthropic-knowledge-work-plugins

File: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rtms/SKILL.md`

## Other

### audit-augmentation
Augments Trailmark code graphs with external audit findings from SARIF static analysis results and weAudit annotation files. Maps findings to graph nodes by file and line overlap, creates severity-based subgraphs, and enables cross-referencing findings with pre-analysis data (blast radius, taint, etc.). Use when projecting SARIF results onto a code graph, overlaying weAudit annotations, cross-referencing Semgrep or CodeQL findings with call graph data, or visualizing audit findings in the context of code structure.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/trailmark/skills/audit-augmentation`
**Keywords:** uncategorized
**Source:** trailofbits-skills

### data-context-extractor
Generate or improve a company-specific data analysis skill by extracting tribal knowledge from analysts.

BOOTSTRAP MODE - Triggers: "Create a data context skill", "Set up data analysis for our warehouse", "Help me create a skill for our database", "Generate a data skill for [company]" → Discovers schemas, asks key questions, generates initial skill with reference files

ITERATION MODE - Triggers: "Add context about [domain]", "The skill needs more info about [topic]", "Update the data skill with [metrics/tables/terminology]", "Improve the [domain] reference" → Loads existing skill, asks targeted questions, appends/updates reference files

Use when data analysts want Claude to understand their company's specific data warehouse, terminology, metrics definitions, and common query patterns.

**Enabled:** `true`
**ID:** `external/anthropic-knowledge-work-plugins/data/skills/data-context-extractor`
**Keywords:** uncategorized
**Source:** anthropic-knowledge-work-plugins

### debug-buttercup
Debugs the Buttercup CRS (Cyber Reasoning System) running on Kubernetes. Use when diagnosing pod crashes, restart loops, Redis failures, resource pressure, disk saturation, DinD issues, or any service misbehavior in the crs namespace. Covers triage, log analysis, queue inspection, and common failure patterns for: redis, fuzzer-bot, coverage-bot, seed-gen, patcher, build-bot, scheduler, task-server, task-downloader, program-model, litellm, dind, tracer-bot, merger-bot, competition-api, pov-reproducer, scratch-cleaner, registry-cache, image-preloader, ui.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/debug-buttercup/skills/debug-buttercup`
**Keywords:** uncategorized
**Source:** trailofbits-skills

### designing-workflow-skills
Guides the design and structuring of workflow-based Claude Code skills with multi-step phases, decision trees, subagent delegation, and progressive disclosure. Use when creating skills that involve sequential pipelines, routing patterns, safety gates, task tracking, phased execution, or any multi-step workflow. Also applies when reviewing or refactoring existing workflow skills for quality.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/workflow-skill-design/skills/designing-workflow-skills`
**Keywords:** uncategorized
**Source:** trailofbits-skills

### diagramming-code
Generates Mermaid diagrams from Trailmark code graphs. Produces call graphs, class hierarchies, module dependency maps, containment diagrams, complexity heatmaps, and attack surface data flow visualizations. Use when visualizing code architecture, drawing call graphs, generating class diagrams, creating dependency maps, producing complexity heatmaps, or visualizing data flow and attack surface paths as Mermaid diagrams.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/trailmark/skills/diagramming-code`
**Keywords:** uncategorized
**Source:** trailofbits-skills

### differential-review
Performs security-focused differential review of code changes (PRs, commits, diffs). Adapts analysis depth to codebase size, uses git history for context, calculates blast radius, checks test coverage, and generates comprehensive markdown reports. Automatically detects and prevents security regressions.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/differential-review/skills/differential-review`
**Keywords:** uncategorized
**Source:** trailofbits-skills

### humanizer
Remove signs of AI-generated writing from text. Use when editing or reviewing
text to make it sound more natural and human-written. Based on Wikipedia's
comprehensive "Signs of AI writing" guide. Detects and fixes patterns including:
inflated symbolism, promotional language, superficial -ing analyses, vague
attributions, em dash overuse, rule of three, AI vocabulary words, negative
parallelisms, and excessive conjunctive phrases. 30c5c8d (Update humanizer plugin to upstream v2.2.0)

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/humanizer/skills/humanizer`
**Keywords:** uncategorized
**Source:** trailofbits-skills-curated

### libfuzzer
Coverage-guided fuzzer built into LLVM for C/C++ projects. Use for fuzzing C/C++ code that can be compiled with Clang.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/libfuzzer`
**Keywords:** uncategorized
**Source:** trailofbits-skills

### planning-with-files
Implements file-based planning for complex multi-step tasks. Creates task_plan.md, findings.md, and progress.md as persistent working memory. Use when starting tasks requiring >5 tool calls, multi-phase projects, research, or any work where losing track of goals and progress would be costly.

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/planning-with-files/skills/planning-with-files`
**Keywords:** uncategorized
**Source:** trailofbits-skills-curated

### security-awareness
Teaches agents to recognize and avoid security threats during normal activity. Covers phishing detection, credential protection, domain verification, and social engineering defense. Use when building or operating agents that access email, credential vaults, web browsers, or sensitive data.

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/security-awareness/skills/security-awareness`
**Keywords:** uncategorized
**Source:** trailofbits-skills-curated

### skill-extractor
Extracts reusable skills from work sessions. Use when: (1) a non-obvious problem was solved worth preserving, (2) a pattern was discovered that would help future sessions, (3) a workaround or debugging technique needs documentation. Manual invocation only via /skill-extractor command - no automatic triggers or hooks.

**Enabled:** `true`
**ID:** `external/trailofbits-skills-curated/plugins/skill-extractor/skills/skill-extractor`
**Keywords:** uncategorized
**Source:** trailofbits-skills-curated

### wycheproof
Wycheproof provides test vectors for validating cryptographic implementations. Use when testing crypto code for known attacks and edge cases.

**Enabled:** `true`
**ID:** `external/trailofbits-skills/plugins/testing-handbook-skills/skills/wycheproof`
**Keywords:** uncategorized
**Source:** trailofbits-skills
