# Tag: contract

Skills with tag `contract`:

## entry-point-analyzer

Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer`
- **Skill file**: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`
- **Tags**: `access`, `admin`, `analyzer`, `analyzes`, `asked`, `audit`, `auditing`, `callable`, `categorizes`, `changing`, `codebases`, `contract`, `contracts`, `control`, `cosmwasm`, `detects`, `entry`, `entry-point-analyzer`, `excludes`, `externally`, `find`, `flows`, `functions`, `generates`, `identify`, `level`, `modify`, `move`, `operations`, `point`, `points`, `privileged`, `public`, `pure`, `reports`, `restricted`, `role`, `role-restricted`, `rust`, `security`, `smart`, `solana`, `solidity`, `state`, `state-changing`, `structured`, `them`, `ton`, `view`, `vyper`

## guidelines-advisor

Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Provides actionable recommendations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor/SKILL.md`
- **Tags**: `actionable`, `advisor`, `analyzes`, `architecture`, `assess`, `building`, `building-secure-contracts`, `codebase`, `contract`, `contracts`, `dependencies`, `development`, `documentation`, `evaluate`, `guidelines`, `guidelines-advisor`, `identify`, `implementation`, `pitfalls`, `practices`, `provides`, `quality`, `recommendations`, `review`, `secure`, `smart`, `specifications`, `testing`, `upgradeability`

## legal-risk-assessment

Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria. Use when evaluating contract risk, assessing deal exposure, classifying issues by severity, or determining whether a matter needs senior counsel or outside legal review.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/legal/skills/legal-risk-assessment`
- **Skill file**: `external/anthropic-knowledge-work-plugins/legal/skills/legal-risk-assessment/SKILL.md`
- **Tags**: `assess`, `assessing`, `assessment`, `classify`, `classifying`, `contract`, `counsel`, `criteria`, `deal`, `determining`, `escalation`, `evaluating`, `exposure`, `framework`, `issues`, `legal`, `legal-risk-assessment`, `likelihood`, `matter`, `needs`, `outside`, `review`, `risk`, `risks`, `senior`, `severity`, `severity-by-likelihood`, `whether`

## meeting-briefing

Prepare structured briefings for meetings with legal relevance and track resulting action items. Use when preparing for contract negotiations, board meetings, compliance reviews, or any meeting where legal context, background research, or action tracking is needed.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/legal/skills/meeting-briefing`
- **Skill file**: `external/anthropic-knowledge-work-plugins/legal/skills/meeting-briefing/SKILL.md`
- **Tags**: `background`, `board`, `briefing`, `briefings`, `compliance`, `context`, `contract`, `items`, `legal`, `meeting`, `meeting-briefing`, `meetings`, `needed`, `negotiations`, `prepare`, `preparing`, `relevance`, `research`, `resulting`, `reviews`, `structured`, `track`, `tracking`, `where`

## review-contract

Review a contract against your organization's negotiation playbook — flag deviations, generate redlines, provide business impact analysis. Use when reviewing vendor or customer agreements, when you need clause-by-clause analysis against standard positions, or when preparing a negotiation strategy with prioritized redlines and fallback positions.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/legal/skills/review-contract`
- **Skill file**: `external/anthropic-knowledge-work-plugins/legal/skills/review-contract/SKILL.md`
- **Tags**: `against`, `agreements`, `analysis`, `business`, `clause`, `clause-by-clause`, `contract`, `customer`, `deviations`, `fallback`, `flag`, `impact`, `legal`, `negotiation`, `organization`, `playbook`, `positions`, `preparing`, `prioritized`, `provide`, `redlines`, `review`, `review-contract`, `reviewing`, `standard`, `strategy`, `vendor`

## scv-scan

Audits Solidity codebases for smart contract vulnerabilities using a four-phase workflow (cheatsheet loading, codebase sweep, deep validation, reporting) covering 36 vulnerability classes. Use when auditing Solidity contracts for security issues, performing smart contract vulnerability scans, or reviewing Solidity code for common exploit patterns.

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/scv-scan/skills/scv-scan`
- **Skill file**: `external/trailofbits-skills-curated/plugins/scv-scan/skills/scv-scan/SKILL.md`
- **Tags**: `auditing`, `audits`, `cheatsheet`, `classes`, `code`, `codebase`, `codebases`, `contract`, `contracts`, `covering`, `deep`, `exploit`, `four`, `four-phase`, `issues`, `loading`, `performing`, `phase`, `reporting`, `reviewing`, `scan`, `scans`, `scv`, `scv-scan`, `security`, `smart`, `solidity`, `sweep`, `validation`, `vulnerabilities`, `vulnerability`

## signature-request

Prepare and route a document for e-signature — run a pre-signature checklist, configure signing order, and send for execution. Use when a contract is finalized and ready to sign, when verifying entity names, exhibits, and signature blocks before sending, or when setting up an envelope with sequential or parallel signers.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/legal/skills/signature-request`
- **Skill file**: `external/anthropic-knowledge-work-plugins/legal/skills/signature-request/SKILL.md`
- **Tags**: `blocks`, `checklist`, `configure`, `contract`, `document`, `e-signature`, `entity`, `envelope`, `execution`, `exhibits`, `finalized`, `legal`, `names`, `order`, `parallel`, `pre`, `pre-signature`, `prepare`, `ready`, `request`, `route`, `send`, `sending`, `sequential`, `setting`, `sign`, `signature`, `signature-request`, `signers`, `signing`, `verifying`

## token-integration-analyzer

Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Context-aware for both token implementations and token integrations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer/SKILL.md`
- **Tags**: `analysis`, `analyzer`, `analyzes`, `assesses`, `aware`, `both`, `building`, `building-secure-contracts`, `chain`, `checklist`, `checks`, `composition`, `conformity`, `context`, `context-aware`, `contract`, `contracts`, `erc20`, `erc721`, `evaluates`, `handle`, `implementation`, `implementations`, `integration`, `integrations`, `non`, `non-standard`, `on-chain`, `owner`, `performs`, `privileges`, `protocols`, `scarcity`, `secure`, `standard`, `token`, `token-integration-analyzer`, `tokens`, `weird`

## vendor-review

Evaluate a vendor — cost analysis, risk assessment, and recommendation. Use when reviewing a new vendor proposal, deciding whether to renew or replace a contract, comparing two vendors side-by-side, or building a TCO breakdown and negotiation points before procurement sign-off.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/operations/skills/vendor-review`
- **Skill file**: `external/anthropic-knowledge-work-plugins/operations/skills/vendor-review/SKILL.md`
- **Tags**: `analysis`, `assessment`, `breakdown`, `building`, `comparing`, `contract`, `cost`, `deciding`, `evaluate`, `negotiation`, `off`, `operations`, `points`, `procurement`, `proposal`, `recommendation`, `renew`, `replace`, `review`, `reviewing`, `risk`, `side`, `side-by-side`, `sign`, `sign-off`, `tco`, `two`, `vendor`, `vendor-review`, `vendors`, `whether`
