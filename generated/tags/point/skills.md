# point

## Skills
Load skill and **use it** when task matches.

### build-mcp-server
This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`

### debug-zoom
Debug a broken Zoom integration by isolating the failure point and routing into the right Zoom references. Use when auth, API, webhook, SDK, or MCP behavior is failing and you need a ranked hypothesis list plus verification steps.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom/SKILL.md`

### entry-point-analyzer
Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

File: `../external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`

### trailmark
Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

File: `../external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`

### trailmark-summary
Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview.

File: `../external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary/SKILL.md`
