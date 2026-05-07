# handles

## Skills
Load skill file when task matches.

### claude-api
Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

File: `external/anthropic-skills/skills/claude-api/SKILL.md`

### figma-create-new-file
Create a new blank Figma file. Use when the user wants to create a new Figma design or FigJam file, or when you need a new file before calling use_figma. Handles plan resolution via whoami if needed. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard)

File: `external/openai-skills/skills/.curated/figma-create-new-file/SKILL.md`

### knowledge-synthesis
Combines search results from multiple sources into coherent, deduplicated answers with source attribution. Handles confidence scoring based on freshness and authority, and summarizes large result sets effectively.

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/knowledge-synthesis/SKILL.md`

### search-strategy
Query decomposition and multi-source search orchestration. Breaks natural language questions into targeted searches per source, translates queries into source-specific syntax, ranks results by relevance, and handles ambiguity and fallback strategies.

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search-strategy/SKILL.md`

### sequence-load
Find leads matching criteria and bulk-add them to an Apollo outreach sequence. Handles enrichment, contact creation, deduplication, and enrollment in one flow.

File: `external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/sequence-load/SKILL.md`

### source-management
Manages connected MCP sources for enterprise search. Detects available sources, guides users to connect new ones, handles source priority ordering, and manages rate limiting awareness.

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/source-management/SKILL.md`
