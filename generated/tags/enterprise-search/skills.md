# enterprise-search

## Skills
Load skill file when task matches.

### digest
Generate a daily or weekly digest of activity across all connected sources. Use when catching up after time away, starting the day and wanting a summary of mentions and action items, or reviewing a week's decisions and document updates grouped by project.

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/digest/SKILL.md`

### knowledge-synthesis
Combines search results from multiple sources into coherent, deduplicated answers with source attribution. Handles confidence scoring based on freshness and authority, and summarizes large result sets effectively.

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/knowledge-synthesis/SKILL.md`

### search
Search across all connected sources in one query. Trigger with "find that doc about...", "what did we decide on...", "where was the conversation about...", or when looking for a decision, document, or discussion that could live in chat, email, cloud storage, or a project tracker.

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search/SKILL.md`

### search-strategy
Query decomposition and multi-source search orchestration. Breaks natural language questions into targeted searches per source, translates queries into source-specific syntax, ranks results by relevance, and handles ambiguity and fallback strategies.

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search-strategy/SKILL.md`

### source-management
Manages connected MCP sources for enterprise search. Detects available sources, guides users to connect new ones, handles source priority ordering, and manages rate limiting awareness.

File: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/source-management/SKILL.md`
