# Tag: handles

Skills with tag `handles`:

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## figma-create-new-file

Create a new blank Figma file. Use when the user wants to create a new Figma design or FigJam file, or when you need a new file before calling use_figma. Handles plan resolution via whoami if needed. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard)

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-create-new-file`
- **Skill file**: `external/openai-skills/skills/.curated/figma-create-new-file/SKILL.md`
- **Tags**: `blank`, `calling`, `create`, `curated`, `design`, `editortype`, `figjam`, `figma`, `figma-create`, `filename`, `handles`, `needed`, `plan`, `resolution`, `whiteboard`, `whoami`

## knowledge-synthesis

Combines search results from multiple sources into coherent, deduplicated answers with source attribution. Handles confidence scoring based on freshness and authority, and summarizes large result sets effectively.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/knowledge-synthesis`
- **Skill file**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/knowledge-synthesis/SKILL.md`
- **Tags**: `answers`, `attribution`, `authority`, `coherent`, `combines`, `confidence`, `deduplicated`, `effectively`, `enterprise`, `enterprise-search`, `freshness`, `handles`, `knowledge`, `knowledge-synthesis`, `large`, `multiple`, `result`, `scoring`, `search`, `sets`, `sources`, `summarizes`, `synthesis`

## search-strategy

Query decomposition and multi-source search orchestration. Breaks natural language questions into targeted searches per source, translates queries into source-specific syntax, ranks results by relevance, and handles ambiguity and fallback strategies.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search-strategy`
- **Skill file**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search-strategy/SKILL.md`
- **Tags**: `ambiguity`, `breaks`, `decomposition`, `enterprise`, `enterprise-search`, `fallback`, `handles`, `language`, `multi`, `natural`, `orchestration`, `per`, `queries`, `query`, `questions`, `ranks`, `relevance`, `search`, `search-strategy`, `searches`, `strategies`, `strategy`, `syntax`, `targeted`, `translates`

## sequence-load

Find leads matching criteria and bulk-add them to an Apollo outreach sequence. Handles enrichment, contact creation, deduplication, and enrollment in one flow.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/sequence-load`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/sequence-load/SKILL.md`
- **Tags**: `apollo`, `bulk`, `contact`, `creation`, `criteria`, `deduplication`, `enrichment`, `enrollment`, `find`, `flow`, `handles`, `leads`, `load`, `matching`, `one`, `outreach`, `partner`, `sequence`, `sequence-load`, `them`

## source-management

Manages connected MCP sources for enterprise search. Detects available sources, guides users to connect new ones, handles source priority ordering, and manages rate limiting awareness.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/source-management`
- **Skill file**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/source-management/SKILL.md`
- **Tags**: `awareness`, `connect`, `connected`, `detects`, `enterprise`, `enterprise-search`, `guides`, `handles`, `limiting`, `management`, `manages`, `mcp`, `ones`, `ordering`, `priority`, `rate`, `search`, `sources`
