# identify

## Skills
Load skill and **use it** when task matches.

### entry-point-analyzer
Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

File: `../external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`

### genotoxic
Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circomvent and cairo-mutants), or using necessist.

File: `../external/trailofbits-skills/plugins/trailmark/skills/genotoxic/SKILL.md`

### guidelines-advisor
Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Provides actionable recommendations.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor/SKILL.md`

### risk-assessment
Identify, assess, and mitigate operational risks. Trigger with "what are the risks", "risk assessment", "risk register", "what could go wrong", or when the user is evaluating risks associated with a project, vendor, process, or decision.

File: `../external/anthropic-knowledge-work-plugins/operations/skills/risk-assessment/SKILL.md`

### tech-debt
Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or when the user asks about code quality, refactoring priorities, or maintenance backlog.

File: `../external/anthropic-knowledge-work-plugins/engineering/skills/tech-debt/SKILL.md`

### vector-forge
Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

File: `../external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`
