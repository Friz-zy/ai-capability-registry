# Tag: checks

Skills with tag `checks`:

## gh-fix-ci

Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/gh-fix-ci`
- **Skill file**: `external/openai-skills/skills/.curated/gh-fix-ci/SKILL.md`
- **Tags**: `actions`, `approval`, `asks`, `buildkite`, `checks`, `context`, `curated`, `debug`, `draft`, `explicit`, `failing`, `failure`, `fix`, `gh-fix-ci`, `github`, `implement`, `inspect`, `logs`, `out`, `plan`, `providers`, `report`, `scope`, `summarize`, `treat`, `url`

## legal-response

Generate a response to a common legal inquiry using configured templates, with built-in escalation checks for situations that shouldn't use a templated reply. Use when responding to data subject requests, litigation hold notices, vendor legal questions, NDA requests from business teams, or subpoenas.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/legal/skills/legal-response`
- **Skill file**: `external/anthropic-knowledge-work-plugins/legal/skills/legal-response/SKILL.md`
- **Tags**: `business`, `checks`, `configured`, `data`, `escalation`, `hold`, `inquiry`, `legal`, `legal-response`, `litigation`, `nda`, `notices`, `questions`, `reply`, `requests`, `responding`, `response`, `shouldn`, `situations`, `subject`, `subpoenas`, `teams`, `templated`, `vendor`

## openai-gh-fix-ci

Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions;

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-gh-fix-ci/skills/openai-gh-fix-ci`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-gh-fix-ci/skills/openai-gh-fix-ci/SKILL.md`
- **Tags**: `actions`, `asks`, `checks`, `debug`, `failing`, `fix`, `gh-fix-ci`, `github`

## pdf

Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/pdf`
- **Skill file**: `external/openai-skills/skills/.curated/pdf/SKILL.md`
- **Tags**: `checks`, `creating`, `curated`, `extraction`, `generation`, `involve`, `layout`, `matter`, `pages`, `pdf`, `pdfplumber`, `poppler`, `prefer`, `pypdf`, `python`, `reading`, `rendering`, `reportlab`, `reviewing`, `such`, `visual`, `where`

## secure-workflow-guide

Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide/SKILL.md`
- **Tags**: `areas`, `building`, `building-secure-contracts`, `checks`, `conformance`, `contracts`, `development`, `diagrams`, `document`, `erc`, `features`, `fuzzing`, `generates`, `guides`, `helps`, `integration`, `manual`, `properties`, `reviews`, `runs`, `scans`, `secure`, `security`, `slither`, `special`, `token`, `upgradeability`, `verification`, `visual`

## security-ownership-map

Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-ownership-map`
- **Skill file**: `external/openai-skills/skills/.curated/security-ownership-map/SKILL.md`
- **Tags**: `analysis`, `analyze`, `build`, `bus`, `bus-factor`, `checks`, `clusters`, `code`, `codeowners`, `compute`, `csv`, `curated`, `databases`, `explicitly`, `export`, `factor`, `general`, `git`, `graph`, `grounded`, `history`, `hotspots`, `lists`, `maintainer`, `maintainers`, `map`, `non`, `non-security`, `oriented`, `orphaned`, `ownership`, `people`, `people-to`, `questions`, `reality`, `repositories`, `risk`, `security`, `security-oriented`, `security-ownership-map`, `sensitive`, `sensitive-code`, `topology`, `trigger`, `visualization`

## seo-audit

Run a comprehensive SEO audit — keyword research, on-page analysis, content gaps, technical checks, and competitor comparison. Use when assessing a site's SEO health, when finding keyword opportunities and content gaps competitors own, or when you need a prioritized action plan split into quick wins and strategic investments.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/marketing/skills/seo-audit`
- **Skill file**: `external/anthropic-knowledge-work-plugins/marketing/skills/seo-audit/SKILL.md`
- **Tags**: `analysis`, `assessing`, `audit`, `checks`, `comparison`, `competitor`, `competitors`, `comprehensive`, `content`, `finding`, `gaps`, `health`, `investments`, `keyword`, `marketing`, `on-page`, `opportunities`, `own`, `page`, `plan`, `prioritized`, `research`, `seo`, `seo-audit`, `site`, `split`, `strategic`, `technical`, `wins`

## solana-vulnerability-scanner

Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use when auditing Solana/Anchor programs.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/solana-vulnerability-scanner`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md`
- **Tags**: `anchor`, `arbitrary`, `auditing`, `building`, `building-secure-contracts`, `checks`, `contracts`, `cpi`, `critical`, `improper`, `including`, `missing`, `ownership`, `pda`, `programs`, `scanner`, `scans`, `secure`, `signer`, `solana`, `solana-vulnerability-scanner`, `spoofing`, `sysvar`, `validation`, `vulnerabilities`, `vulnerability`

## spec-to-code-compliance

Verifies code implements exactly what documentation specifies for blockchain audits. Use when comparing code against whitepapers, finding gaps between specs and implementation, or performing compliance checks for protocol implementations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/spec-to-code-compliance/skills/spec-to-code-compliance`
- **Skill file**: `external/trailofbits-skills/plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md`
- **Tags**: `against`, `audits`, `between`, `blockchain`, `checks`, `code`, `comparing`, `compliance`, `documentation`, `exactly`, `finding`, `gaps`, `implementation`, `implementations`, `implements`, `performing`, `protocol`, `spec`, `spec-to-code-compliance`, `specifies`, `specs`, `verifies`, `whitepapers`

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

## validate-data

QA an analysis before sharing -- methodology, accuracy, and bias checks. Use when reviewing an analysis before a stakeholder presentation, spot-checking calculations and aggregation logic, verifying a SQL query's results look right, or assessing whether conclusions are actually supported by the data.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/data/skills/validate-data`
- **Skill file**: `external/anthropic-knowledge-work-plugins/data/skills/validate-data/SKILL.md`
- **Tags**: `accuracy`, `actually`, `aggregation`, `analysis`, `assessing`, `bias`, `calculations`, `checking`, `checks`, `conclusions`, `data`, `logic`, `look`, `methodology`, `presentation`, `query`, `reviewing`, `right`, `sharing`, `spot`, `spot-checking`, `sql`, `stakeholder`, `supported`, `validate`, `validate-data`, `verifying`, `whether`
