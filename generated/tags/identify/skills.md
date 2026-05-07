# Tag: identify

Skills with tag `identify`:

## entry-point-analyzer

Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer`
- **Skill file**: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`
- **Tags**: `access`, `admin`, `analyzer`, `analyzes`, `asked`, `audit`, `auditing`, `callable`, `categorizes`, `changing`, `codebases`, `contract`, `contracts`, `control`, `cosmwasm`, `detects`, `entry`, `entry-point-analyzer`, `excludes`, `externally`, `find`, `flows`, `functions`, `generates`, `identify`, `level`, `modify`, `move`, `operations`, `point`, `points`, `privileged`, `public`, `pure`, `reports`, `restricted`, `role`, `role-restricted`, `rust`, `security`, `smart`, `solana`, `solidity`, `state`, `state-changing`, `structured`, `them`, `ton`, `view`, `vyper`

## genotoxic

Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circomvent and cairo-mutants), or using necessist.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/genotoxic`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/genotoxic/SKILL.md`
- **Tags**: `analyzing`, `cairo`, `cairo-mutants`, `call`, `circomvent`, `codebases`, `coverage`, `data`, `false`, `finding`, `frameworks`, `fuzzing`, `gaps`, `genotoxic`, `graph`, `graph-informed`, `identify`, `identifying`, `including`, `informed`, `missing`, `mutants`, `mutation`, `necessist`, `parses`, `positives`, `running`, `runs`, `statements`, `survived`, `targets`, `test`, `testing`, `tests`, `then`, `trailmark`, `triage`, `triaging`, `unnecessary`, `weak`

## guidelines-advisor

Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Provides actionable recommendations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor/SKILL.md`
- **Tags**: `actionable`, `advisor`, `analyzes`, `architecture`, `assess`, `building`, `building-secure-contracts`, `codebase`, `contract`, `contracts`, `dependencies`, `development`, `documentation`, `evaluate`, `guidelines`, `guidelines-advisor`, `identify`, `implementation`, `pitfalls`, `practices`, `provides`, `quality`, `recommendations`, `review`, `secure`, `smart`, `specifications`, `testing`, `upgradeability`

## risk-assessment

Identify, assess, and mitigate operational risks. Trigger with "what are the risks", "risk assessment", "risk register", "what could go wrong", or when the user is evaluating risks associated with a project, vendor, process, or decision.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/operations/skills/risk-assessment`
- **Skill file**: `external/anthropic-knowledge-work-plugins/operations/skills/risk-assessment/SKILL.md`
- **Tags**: `assess`, `assessment`, `associated`, `could`, `decision`, `evaluating`, `identify`, `mitigate`, `operational`, `operations`, `process`, `project`, `register`, `risk`, `risk-assessment`, `risks`, `trigger`, `vendor`, `wrong`

## tech-debt

Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or when the user asks about code quality, refactoring priorities, or maintenance backlog.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/tech-debt`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/tech-debt/SKILL.md`
- **Tags**: `asks`, `audit`, `backlog`, `categorize`, `code`, `debt`, `engineering`, `health`, `identify`, `maintenance`, `priorities`, `prioritize`, `quality`, `refactor`, `refactoring`, `tech`, `tech-debt`, `technical`, `trigger`

## vector-forge

Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`
- **Tags**: `algorithm`, `code`, `compares`, `coverage`, `creating`, `cross`, `cross-implementation`, `crypto`, `cryptographic`, `deliberately`, `driven`, `effectiveness`, `escaped`, `exercise`, `finding`, `finds`, `forge`, `gaps`, `generates`, `generating`, `generation`, `identify`, `implementation`, `implementations`, `improving`, `kill`, `measuring`, `mutants`, `mutation`, `mutation-driven`, `paths`, `primitives`, `protocol`, `prove`, `rates`, `runs`, `suites`, `test`, `testing`, `then`, `trailmark`, `uncovered`, `vector`, `vector-forge`, `vectors`, `wycheproof`
