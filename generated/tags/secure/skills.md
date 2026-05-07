# Tag: secure

Skills with tag `secure`:

## algorand-vulnerability-scanner

Scans Algorand smart contracts for 11 common vulnerabilities including rekeying attacks, unchecked transaction fees, missing field validations, and access control issues. Use when auditing Algorand projects (TEAL/PyTeal).

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/algorand-vulnerability-scanner`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md`
- **Tags**: `access`, `algorand`, `algorand-vulnerability-scanner`, `attacks`, `auditing`, `building`, `building-secure-contracts`, `contracts`, `control`, `fees`, `field`, `including`, `issues`, `missing`, `projects`, `pyteal`, `rekeying`, `scanner`, `scans`, `secure`, `smart`, `teal`, `transaction`, `unchecked`, `validations`, `vulnerabilities`, `vulnerability`

## audit-prep-assistant

Prepares codebases for security review using Trail of Bits' checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation (flowcharts, user stories, inline comments).

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md`
- **Tags**: `accessibility`, `analysis`, `audit`, `audit-prep`, `building`, `building-secure-contracts`, `checklist`, `code`, `codebases`, `comments`, `contracts`, `coverage`, `dead`, `documentation`, `ensures`, `flowcharts`, `generates`, `goals`, `helps`, `increases`, `inline`, `prep`, `prepares`, `removes`, `review`, `runs`, `secure`, `security`, `set`, `static`, `stories`, `test`

## cairo-vulnerability-scanner

Scans Cairo/StarkNet smart contracts for 6 critical vulnerabilities including felt252 arithmetic overflow, L1-L2 messaging issues, address conversion problems, and signature replay. Use when auditing StarkNet projects.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cairo-vulnerability-scanner`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md`
- **Tags**: `address`, `arithmetic`, `auditing`, `building`, `building-secure-contracts`, `cairo`, `cairo-vulnerability-scanner`, `contracts`, `conversion`, `critical`, `felt252`, `including`, `issues`, `l1-l2`, `messaging`, `overflow`, `problems`, `projects`, `replay`, `scanner`, `scans`, `secure`, `signature`, `smart`, `starknet`, `vulnerabilities`, `vulnerability`

## code-maturity-assessor

Systematic code maturity assessment using Trail of Bits' 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level code, and testing. Produces professional scorecard with evidence-based ratings and actionable recommendations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/code-maturity-assessor`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/code-maturity-assessor/SKILL.md`
- **Tags**: `access`, `actionable`, `analyzes`, `arithmetic`, `assessment`, `assessor`, `auditing`, `building`, `building-secure-contracts`, `category`, `code`, `code-maturity-assessor`, `codebase`, `complexity`, `contracts`, `controls`, `decentralization`, `documentation`, `evidence`, `framework`, `level`, `low`, `low-level`, `maturity`, `mev`, `practices`, `produces`, `professional`, `ratings`, `recommendations`, `risks`, `safety`, `scorecard`, `secure`, `systematic`, `testing`

## cosmos-vulnerability-scanner

Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md`
- **Tags**: `assessing`, `auditing`, `blockchain`, `building`, `building-secure-contracts`, `chain`, `consensus`, `consensus-critical`, `contracts`, `core`, `cosmos`, `cosmos-vulnerability-scanner`, `cosmwasm`, `critical`, `custom`, `divergence`, `evm`, `fund`, `halts`, `ibc`, `integrations`, `launch`, `loss`, `modules`, `pre`, `pre-launch`, `reviewing`, `scanner`, `scans`, `sdk`, `secure`, `security`, `state`, `updated`, `vulnerabilities`, `vulnerability`

## guidelines-advisor

Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Provides actionable recommendations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor/SKILL.md`
- **Tags**: `actionable`, `advisor`, `analyzes`, `architecture`, `assess`, `building`, `building-secure-contracts`, `codebase`, `contract`, `contracts`, `dependencies`, `development`, `documentation`, `evaluate`, `guidelines`, `guidelines-advisor`, `identify`, `implementation`, `pitfalls`, `practices`, `provides`, `quality`, `recommendations`, `review`, `secure`, `smart`, `specifications`, `testing`, `upgradeability`

## secure-workflow-guide

Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide/SKILL.md`
- **Tags**: `areas`, `building`, `building-secure-contracts`, `checks`, `conformance`, `contracts`, `development`, `diagrams`, `document`, `erc`, `features`, `fuzzing`, `generates`, `guides`, `helps`, `integration`, `manual`, `properties`, `reviews`, `runs`, `scans`, `secure`, `security`, `slither`, `special`, `token`, `upgradeability`, `verification`, `visual`

## security-best-practices

Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-best-practices`
- **Skill file**: `external/openai-skills/skills/.curated/security-best-practices/SKILL.md`
- **Tags**: `code`, `coding`, `curated`, `debugging`, `default`, `explicitly`, `framework`, `general`, `guidance`, `improvements`, `javascript`, `language`, `languages`, `non`, `non-security`, `perform`, `practice`, `practices`, `python`, `report`, `requests`, `review`, `reviews`, `secure`, `secure-by-default`, `security`, `security-practices`, `suggest`, `supported`, `trigger`, `typescript`

## sharp-edges

Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges`
- **Skill file**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges/SKILL.md`
- **Tags**: `api`, `apis`, `code`, `configuration`, `configurations`, `cryptographic`, `dangerous`, `default`, `defaults`, `designs`, `edges`, `enable`, `ergonomics`, `error`, `error-prone`, `evaluating`, `follows`, `footgun`, `identifies`, `library`, `mistakes`, `misuse`, `misuse-resistant`, `pit`, `principles`, `prone`, `resistant`, `reviewing`, `schemas`, `secure`, `security`, `sharp`, `sharp-edges`, `success`, `triggers`, `usability`, `whether`

## solana-vulnerability-scanner

Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use when auditing Solana/Anchor programs.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/solana-vulnerability-scanner`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md`
- **Tags**: `anchor`, `arbitrary`, `auditing`, `building`, `building-secure-contracts`, `checks`, `contracts`, `cpi`, `critical`, `improper`, `including`, `missing`, `ownership`, `pda`, `programs`, `scanner`, `scans`, `secure`, `signer`, `solana`, `solana-vulnerability-scanner`, `spoofing`, `sysvar`, `validation`, `vulnerabilities`, `vulnerability`

## substrate-vulnerability-scanner

Scans Substrate/Polkadot pallets for 7 critical vulnerabilities including arithmetic overflow, panic DoS, incorrect weights, and bad origin checks. Use when auditing Substrate runtimes or FRAME pallets.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/substrate-vulnerability-scanner`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md`
- **Tags**: `arithmetic`, `auditing`, `bad`, `building`, `building-secure-contracts`, `checks`, `contracts`, `critical`, `dos`, `frame`, `including`, `incorrect`, `origin`, `overflow`, `pallets`, `panic`, `polkadot`, `runtimes`, `scanner`, `scans`, `secure`, `substrate`, `substrate-vulnerability-scanner`, `vulnerabilities`, `vulnerability`, `weights`

## token-integration-analyzer

Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Context-aware for both token implementations and token integrations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer/SKILL.md`
- **Tags**: `analysis`, `analyzer`, `analyzes`, `assesses`, `aware`, `both`, `building`, `building-secure-contracts`, `chain`, `checklist`, `checks`, `composition`, `conformity`, `context`, `context-aware`, `contract`, `contracts`, `erc20`, `erc721`, `evaluates`, `handle`, `implementation`, `implementations`, `integration`, `integrations`, `non`, `non-standard`, `on-chain`, `owner`, `performs`, `privileges`, `protocols`, `scarcity`, `secure`, `standard`, `token`, `token-integration-analyzer`, `tokens`, `weird`

## ton-vulnerability-scanner

Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without gas checks. Use when auditing FunC contracts.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/ton-vulnerability-scanner`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md`
- **Tags**: `auditing`, `boolean`, `building`, `building-secure-contracts`, `checks`, `contracts`, `critical`, `fake`, `forward`, `func`, `gas`, `including`, `integer`, `integer-as-boolean`, `jetton`, `misuse`, `network`, `open`, `scanner`, `scans`, `secure`, `smart`, `ton`, `ton-vulnerability-scanner`, `vulnerabilities`, `vulnerability`, `without`
