# Tag: between

Skills with tag `between`:

## architecture

Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decision with trade-offs and consequences, reviewing a system design proposal, or designing a new component from requirements and constraints.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/architecture`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/architecture/SKILL.md`
- **Tags**: `adr`, `architecture`, `between`, `choosing`, `component`, `consequences`, `constraints`, `create`, `decision`, `design`, `designing`, `documenting`, `engineering`, `evaluate`, `kafka`, `offs`, `proposal`, `record`, `requirements`, `reviewing`, `sqs`, `technologies`, `trade`, `trade-offs`

## build-zoom-meeting-app

Build or embed a Zoom meeting flow. Use when implementing Meeting SDK joins, web or mobile meeting embeds, meeting lifecycle flows, or when deciding between Meeting SDK and Video SDK.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-meeting-app`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-meeting-app/SKILL.md`
- **Tags**: `app`, `between`, `build`, `build-zoom-meeting-app`, `deciding`, `embed`, `embeds`, `flow`, `flows`, `implementing`, `joins`, `lifecycle`, `meeting`, `mobile`, `partner`, `sdk`, `video`, `web`, `zoom`

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

## figma-code-connect-components

Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code connect", "connect this component to code", "map this component", "link component to code", "create code connect mapping", or wants to establish mappings between Figma designs and code implementations. For canvas writes via `use_figma`, use `figma-use`.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-code-connect-components`
- **Skill file**: `external/openai-skills/skills/.curated/figma-code-connect-components/SKILL.md`
- **Tags**: `between`, `canvas`, `code`, `component`, `components`, `connect`, `connects`, `create`, `curated`, `design`, `designs`, `establish`, `figma`, `figma-code-connect-components`, `implementations`, `link`, `map`, `mapping`, `mappings`, `says`, `writes`

## figma-generate-library

Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-generate-library`
- **Skill file**: `external/openai-skills/skills/.curated/figma-generate-library/SKILL.md`
- **Tags**: `api`, `between`, `both`, `build`, `call`, `code`, `codebase`, `complements`, `component`, `create`, `curated`, `dark`, `design`, `document`, `figma`, `figma-library`, `foundations`, `gaps`, `grade`, `libraries`, `library`, `light`, `loaded`, `modes`, `order`, `professional`, `professional-grade`, `reconcile`, `set`, `teaches`, `theming`, `together`, `tokens`, `variables`, `which`

## let-fate-decide

Draws 4 Tarot cards to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the user says 'let fate decide', 'YOLO', 'whatever', 'idk', or other nonchalant phrases, makes Yu-Gi-Oh references, or when you are about to arbitrarily pick between multiple reasonable approaches. Prefer over ask-questions-if-underspecified when the user's tone is casual or playful rather than precision-seeking.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/let-fate-decide/skills/let-fate-decide`
- **Skill file**: `external/trailofbits-skills/plugins/let-fate-decide/skills/let-fate-decide/SKILL.md`
- **Tags**: `ambiguous`, `approaches`, `arbitrarily`, `ask`, `ask-questions-if-underspecified`, `between`, `cards`, `casual`, `casually`, `decide`, `delegated`, `draws`, `entropy`, `fate`, `idk`, `inject`, `interprets`, `let`, `let-fate-decide`, `makes`, `multiple`, `next`, `nonchalant`, `other`, `over`, `phrases`, `pick`, `planning`, `playful`, `precision`, `precision-seeking`, `prefer`, `prompts`, `questions`, `rather`, `reasonable`, `says`, `seeking`, `spread`, `tarot`, `than`, `tone`, `underspecified`, `vague`, `whatever`, `yolo`, `yu-gi-oh`

## plan-zoom-product

Choose the right Zoom building surface for a use case and explain the tradeoffs clearly. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Phone, Contact Center, or MCP for a specific product idea or integration goal.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product/SKILL.md`
- **Tags**: `api`, `apps`, `between`, `building`, `case`, `center`, `choose`, `clearly`, `contact`, `deciding`, `explain`, `goal`, `idea`, `integration`, `mcp`, `meeting`, `partner`, `phone`, `plan`, `plan-zoom-product`, `product`, `rest`, `right`, `sdk`, `surface`, `tradeoffs`, `video`, `webhooks`, `websockets`, `zoom`

## setup-zoom-mcp

Decide when Zoom MCP is the right fit and produce a safe setup plan for Claude. Use when planning AI workflows over Zoom data, deciding between MCP and REST, or defining a hybrid MCP architecture.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-mcp`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-mcp/SKILL.md`
- **Tags**: `architecture`, `between`, `data`, `decide`, `deciding`, `defining`, `fit`, `hybrid`, `mcp`, `over`, `partner`, `plan`, `planning`, `produce`, `rest`, `right`, `safe`, `zoom`, `zoom-mcp`

## spec-to-code-compliance

Verifies code implements exactly what documentation specifies for blockchain audits. Use when comparing code against whitepapers, finding gaps between specs and implementation, or performing compliance checks for protocol implementations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/spec-to-code-compliance/skills/spec-to-code-compliance`
- **Skill file**: `external/trailofbits-skills/plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md`
- **Tags**: `against`, `audits`, `between`, `blockchain`, `checks`, `code`, `comparing`, `compliance`, `documentation`, `exactly`, `finding`, `gaps`, `implementation`, `implementations`, `implements`, `performing`, `protocol`, `spec`, `spec-to-code-compliance`, `specifies`, `specs`, `verifies`, `whitepapers`

## sql-queries

Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, PostgreSQL, etc.). Use when writing queries, optimizing slow SQL, translating between dialects, or building complex analytical queries with CTEs, window functions, or aggregations.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/data/skills/sql-queries`
- **Skill file**: `external/anthropic-knowledge-work-plugins/data/skills/sql-queries/SKILL.md`
- **Tags**: `aggregations`, `analytical`, `between`, `bigquery`, `building`, `complex`, `correct`, `ctes`, `data`, `databricks`, `dialects`, `etc`, `functions`, `major`, `optimizing`, `performant`, `postgresql`, `queries`, `slow`, `snowflake`, `sql`, `sql-queries`, `translating`, `warehouse`, `window`

## xlsx

Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/xlsx`
- **Skill file**: `external/anthropic-skills/skills/xlsx/SKILL.md`
- **Tags**: `adding`, `api`, `between`, `casually`, `charting`, `cleaning`, `columns`, `computing`, `convert`, `create`, `csv`, `data`, `database`, `deliverable`, `document`, `done`, `downloads`, `edit`, `especially`, `even`, `existing`, `fix`, `formats`, `formatting`, `formulas`, `google`, `headers`, `html`, `input`, `integration`, `involved`, `junk`, `like`, `malformed`, `means`, `messy`, `misplaced`, `must`, `open`, `other`, `path`, `pipeline`, `primary`, `produced`, `proper`, `python`, `report`, `restructuring`, `rows`, `scratch`, `script`, `sheets`, `something`, `sources`, `spreadsheet`, `spreadsheets`, `standalone`, `tabular`, `time`, `trigger`, `tsv`, `where`, `word`, `xlsm`, `xlsx`
