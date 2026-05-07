# building

## Skills
Load skill file when task matches.

### algorand-vulnerability-scanner
Scans Algorand smart contracts for 11 common vulnerabilities including rekeying attacks, unchecked transaction fees, missing field validations, and access control issues. Use when auditing Algorand projects (TEAL/PyTeal).

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md`

### audit-context-building
Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding.

File: `../external/trailofbits-skills/plugins/audit-context-building/skills/audit-context-building/SKILL.md`

### audit-prep-assistant
Prepares codebases for security review using Trail of Bits' checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation (flowcharts, user stories, inline comments).

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md`

### build-dashboard
Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results into a shareable self-contained report, building a team monitoring snapshot, or needing multiple charts with filters in one browser-openable file.

File: `../external/anthropic-knowledge-work-plugins/data/skills/build-dashboard/SKILL.md`

### build-mcp-server
This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`

### build-zoom-team-chat-app
Reference skill for Zoom Team Chat. Use after routing to a chat workflow when building user-scoped messaging integrations, chatbot experiences, rich cards, buttons, slash commands, or chat webhooks.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/team-chat/SKILL.md`

### cairo-vulnerability-scanner
Scans Cairo/StarkNet smart contracts for 6 critical vulnerabilities including felt252 arithmetic overflow, L1-L2 messaging issues, address conversion problems, and signature replay. Use when auditing StarkNet projects.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md`

### code-maturity-assessor
Systematic code maturity assessment using Trail of Bits' 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level code, and testing. Produces professional scorecard with evidence-based ratings and actionable recommendations.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/code-maturity-assessor/SKILL.md`

### competitive-brief
Research competitors and generate a positioning and messaging comparison with content gaps, opportunities, and threats. Use when building sales battlecards, when finding positioning gaps and messaging angles competitors haven't claimed, or when a competitor makes a move and you need to assess the impact.

File: `../external/anthropic-knowledge-work-plugins/marketing/skills/competitive-brief/SKILL.md`

### competitive-brief
Create a competitive analysis brief for one or more competitors or a feature area. Use when informing product strategy or feature prioritization, building sales battle cards, prepping board or investor materials, or deciding where to differentiate vs. achieve parity.

File: `../external/anthropic-knowledge-work-plugins/product-management/skills/competitive-brief/SKILL.md`

### cosmos-vulnerability-scanner
Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md`

### data-visualization
Create effective data visualizations with Python (matplotlib, seaborn, plotly). Use when building charts, choosing the right chart type for a dataset, creating publication-quality figures, or applying design principles like accessibility and color theory.

File: `../external/anthropic-knowledge-work-plugins/data/skills/data-visualization/SKILL.md`

### email-sequence
Design and draft multi-email sequences with full copy, timing, branching logic, exit conditions, and performance benchmarks. Use when building onboarding, lead nurture, re-engagement, win-back, or product launch flows, when you need a complete drip campaign with A/B test suggestions, or when mapping a sequence end-to-end with a flow diagram.

File: `../external/anthropic-knowledge-work-plugins/marketing/skills/email-sequence/SKILL.md`

### financial-statements
Generate financial statements (income statement, balance sheet, cash flow) with period-over-period comparison and variance analysis. Use when preparing a monthly or quarterly P&L, closing the books and need to flag material variances, comparing actuals to budget, building a financial summary for leadership review, or looking up GAAP presentation requirements and period-end adjustments.

File: `../external/anthropic-knowledge-work-plugins/finance/skills/financial-statements/SKILL.md`

### guidelines-advisor
Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Provides actionable recommendations.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor/SKILL.md`

### imagegen
Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.

File: `../external/openai-skills/skills/.system/imagegen/SKILL.md`

### mcp-builder
Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

File: `../external/anthropic-skills/skills/mcp-builder/SKILL.md`

### onboarding
Generate an onboarding checklist and first-week plan for a new hire. Use when someone has a start date coming up, building the pre-start task list (accounts, equipment, buddy), scheduling Day 1 and Week 1, or setting 30/60/90-day goals for a new team member.

File: `../external/anthropic-knowledge-work-plugins/human-resources/skills/onboarding/SKILL.md`

### openai-develop-web-game
Use when the agent is building or iterating on a web game (HTML/JS) and needs a reliable

File: `../external/trailofbits-skills-curated/plugins/openai-develop-web-game/skills/openai-develop-web-game/SKILL.md`

### plan-zoom-product
Choose the right Zoom building surface for a use case and explain the tradeoffs clearly. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Phone, Contact Center, or MCP for a specific product idea or integration goal.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product/SKILL.md`

### process-doc
Document a business process — flowcharts, RACI, and SOPs. Use when formalizing a process that lives in someone's head, building a RACI to clarify who owns what, writing an SOP for a handoff or audit, or capturing the exceptions and edge cases of how work actually gets done.

File: `../external/anthropic-knowledge-work-plugins/operations/skills/process-doc/SKILL.md`

### prospect
Build targeted account or contact lists using Common Room's Prospector. Triggers on 'find companies that match [criteria]', 'build a prospect list', 'find contacts at [type of company]', 'show me companies hiring [role]', or any list-building request.

File: `../external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/prospect/SKILL.md`

### roadmap-update
Update, create, or reprioritize your product roadmap. Use when adding a new initiative and deciding what moves to make room, shifting priorities after new information comes in, moving timelines due to a dependency slip, or building a Now/Next/Later view from scratch.

File: `../external/anthropic-knowledge-work-plugins/product-management/skills/roadmap-update/SKILL.md`

### secure-workflow-guide
Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide/SKILL.md`

### semgrep-rule-creator
Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections.

File: `../external/trailofbits-skills/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md`

### solana-vulnerability-scanner
Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use when auditing Solana/Anchor programs.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md`

### sox-testing
Generate SOX sample selections, testing workpapers, and control assessments. Use when planning quarterly or annual SOX 404 testing, pulling a sample for a control (revenue, P2P, ITGC, close), building a testing workpaper template, or evaluating and classifying a control deficiency.

File: `../external/anthropic-knowledge-work-plugins/finance/skills/sox-testing/SKILL.md`

### sql-queries
Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, PostgreSQL, etc.). Use when writing queries, optimizing slow SQL, translating between dialects, or building complex analytical queries with CTEs, window functions, or aggregations.

File: `../external/anthropic-knowledge-work-plugins/data/skills/sql-queries/SKILL.md`

### substrate-vulnerability-scanner
Scans Substrate/Polkadot pallets for 7 critical vulnerabilities including arithmetic overflow, panic DoS, incorrect weights, and bad origin checks. Use when auditing Substrate runtimes or FRAME pallets.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md`

### token-integration-analyzer
Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Context-aware for both token implementations and token integrations.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer/SKILL.md`

### ton-vulnerability-scanner
Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without gas checks. Use when auditing FunC contracts.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md`

### trailmark
Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

File: `../external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`

### trailmark-structural
Runs full Trailmark structural analysis on Trailmark 0.2.x by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, and attack surface. Use when vivisect needs detailed structural data for a target. Triggers: structural analysis, blast radius, taint analysis, complexity hotspots.

File: `../external/trailofbits-skills/plugins/trailmark/skills/trailmark-structural/SKILL.md`

### ui-toolkit/web
Reference skill for Zoom Video SDK UI Toolkit. Use after routing to a web video workflow when you want prebuilt React UI instead of building a fully custom Video SDK interface.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/ui-toolkit/SKILL.md`

### variant-analysis
Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audits after finding an initial issue.

File: `../external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis/SKILL.md`

### vendor-review
Evaluate a vendor — cost analysis, risk assessment, and recommendation. Use when reviewing a new vendor proposal, deciding whether to renew or replace a contract, comparing two vendors side-by-side, or building a TCO breakdown and negotiation points before procurement sign-off.

File: `../external/anthropic-knowledge-work-plugins/operations/skills/vendor-review/SKILL.md`

### write-query
Write optimized SQL for your dialect with best practices. Use when translating a natural-language data need into SQL, building a multi-CTE query with joins and aggregations, optimizing a query against a large partitioned table, or getting dialect-specific syntax for Snowflake, BigQuery, Postgres, etc.

File: `../external/anthropic-knowledge-work-plugins/data/skills/write-query/SKILL.md`

### zoom-apps-sdk
Reference skill for Zoom Apps SDK. Use after routing to an in-client app workflow when building web apps that run inside Zoom meetings, webinars, the main client, or Zoom Phone.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-apps-sdk/SKILL.md`
