# reports

## Skills
Load skill and **use it** when task matches.

### entry-point-analyzer
Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

File: `../external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`

### internal-comms
A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

File: `../external/anthropic-skills/skills/internal-comms/SKILL.md`

### notion-research-documentation
Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations.

File: `../external/openai-skills/skills/.curated/notion-research-documentation/SKILL.md`

### people-report
Generate headcount, attrition, diversity, or org health reports. Use when pulling a headcount snapshot for leadership, analyzing turnover trends by team, preparing diversity representation metrics, or assessing span of control and flight risk across the org.

File: `../external/anthropic-knowledge-work-plugins/human-resources/skills/people-report/SKILL.md`
