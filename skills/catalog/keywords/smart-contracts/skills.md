# smart-contracts

## Skills
Select only the most relevant skills by description, then read only those `SKILL.md` files.

### algorand-vulnerability-scanner
Scans Algorand smart contracts for 11 common vulnerabilities including rekeying attacks, unchecked transaction fees, missing field validations, and access control issues. Use when auditing Algorand projects (TEAL/PyTeal).

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md`

### audit-context-building
Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding.

File: `external/trailofbits-skills/plugins/audit-context-building/skills/audit-context-building/SKILL.md`

### audit-prep-assistant
Prepares codebases for security review using Trail of Bits' checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation (flowcharts, user stories, inline comments).

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md`

### cairo-vulnerability-scanner
Scans Cairo/StarkNet smart contracts for 6 critical vulnerabilities including felt252 arithmetic overflow, L1-L2 messaging issues, address conversion problems, and signature replay. Use when auditing StarkNet projects.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md`

### code-maturity-assessor
Systematic code maturity assessment using Trail of Bits' 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level code, and testing. Produces professional scorecard with evidence-based ratings and actionable recommendations.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/code-maturity-assessor/SKILL.md`

### cosmos-vulnerability-scanner
Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md`

### dimensional-analysis
Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol, offchain code, or other blockchain-related codebase with arithmetic. Prevents dimensional mismatches and catches formula bugs early.

File: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis/SKILL.md`

### entry-point-analyzer
Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

File: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`

### genotoxic
Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circomvent and cairo-mutants), or using necessist.

File: `external/trailofbits-skills/plugins/trailmark/skills/genotoxic/SKILL.md`

### guidelines-advisor
Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Provides actionable recommendations.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor/SKILL.md`

### scv-scan
Audits Solidity codebases for smart contract vulnerabilities using a four-phase workflow (cheatsheet loading, codebase sweep, deep validation, reporting) covering 36 vulnerability classes. Use when auditing Solidity contracts for security issues, performing smart contract vulnerability scans, or reviewing Solidity code for common exploit patterns.

File: `external/trailofbits-skills-curated/plugins/scv-scan/skills/scv-scan/SKILL.md`

### secure-workflow-guide
Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide/SKILL.md`

### solana-vulnerability-scanner
Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use when auditing Solana/Anchor programs.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md`

### substrate-vulnerability-scanner
Scans Substrate/Polkadot pallets for 7 critical vulnerabilities including arithmetic overflow, panic DoS, incorrect weights, and bad origin checks. Use when auditing Substrate runtimes or FRAME pallets.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md`

### token-integration-analyzer
Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Context-aware for both token implementations and token integrations.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer/SKILL.md`

### ton-vulnerability-scanner
Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without gas checks. Use when auditing FunC contracts.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md`
