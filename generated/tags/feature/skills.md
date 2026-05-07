# feature

## Navigation
Read skill files below to understand capabilities.
Load skill file when task matches.

## Skills

### claude-api
Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-skills/skills/claude-api/SKILL.md`

### competitive-brief
Create a competitive analysis brief for one or more competitors or a feature area. Use when informing product strategy or feature prioritization, building sales battle cards, prepping board or investor materials, or deciding where to differentiate vs. achieve parity.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/product-management/skills/competitive-brief/SKILL.md`

### compliance-check
Run a compliance check on a proposed action, product feature, or business initiative, surfacing applicable regulations, required approvals, and risk areas. Use when launching a feature that touches personal data, when marketing or product proposes something with regulatory implications, or when you need to know which approvals and jurisdictional requirements apply before proceeding.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/legal/skills/compliance-check/SKILL.md`

### deploy-checklist
Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI status and approvals before going to production, or documenting rollback triggers ahead of time.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/engineering/skills/deploy-checklist/SKILL.md`

### draft-response
Draft a professional customer-facing response tailored to the situation and relationship. Use when answering a product question, responding to an escalation or outage, delivering bad news like a delay or won't-fix, declining a feature request, or replying to a billing issue.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/customer-support/skills/draft-response/SKILL.md`

### notion-spec-to-implementation
Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.curated/notion-spec-to-implementation/SKILL.md`

### write-spec
Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user request into a structured document, scoping a feature with goals and non-goals, defining success metrics and acceptance criteria, or breaking a big ask into a phased spec.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/product-management/skills/write-spec/SKILL.md`
