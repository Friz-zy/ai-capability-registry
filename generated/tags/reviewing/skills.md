# Tag: reviewing

Skills with tag `reviewing`:

## accessibility-review

Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "is this accessible?", or when reviewing a design for color contrast, keyboard navigation, touch target size, or screen reader behavior before handoff.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/design/skills/accessibility-review`
- **Skill file**: `external/anthropic-knowledge-work-plugins/design/skills/accessibility-review/SKILL.md`
- **Tags**: `a11y`, `accessibility`, `accessibility-review`, `accessible`, `audit`, `behavior`, `color`, `contrast`, `design`, `handoff`, `keyboard`, `navigation`, `page`, `reader`, `review`, `reviewing`, `screen`, `size`, `target`, `touch`, `trigger`, `wcag`

## agentic-actions-auditor

Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor`
- **Skill file**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`
- **Tags**: `actions`, `agentic`, `agentic-actions-auditor`, `allowlists`, `attack`, `attacker`, `attacker-controlled`, `auditing`, `auditor`, `audits`, `cli`, `code`, `codex`, `coding`, `configurations`, `controlled`, `dangerous`, `detects`, `direct`, `env`, `evaluating`, `expression`, `gemini`, `github`, `including`, `inference`, `injection`, `input`, `integrations`, `intermediary`, `invoke`, `pipeline`, `pipelines`, `prompt`, `reaches`, `reviewing`, `risks`, `running`, `sandbox`, `security`, `var`, `vectors`, `vulnerabilities`, `where`, `wildcard`

## architecture

Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decision with trade-offs and consequences, reviewing a system design proposal, or designing a new component from requirements and constraints.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/architecture`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/architecture/SKILL.md`
- **Tags**: `adr`, `architecture`, `between`, `choosing`, `component`, `consequences`, `constraints`, `create`, `decision`, `design`, `designing`, `documenting`, `engineering`, `evaluate`, `kafka`, `offs`, `proposal`, `record`, `requirements`, `reviewing`, `sqs`, `technologies`, `trade`, `trade-offs`

## c-review

Performs comprehensive C/C++ security review for memory corruption, integer overflows, race conditions, and platform-specific vulnerabilities. Use when auditing native C/C++ applications, reviewing daemons or services for memory safety, or hunting integer overflow / use-after-free / race conditions in userspace code.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/c-review/skills/c-review`
- **Skill file**: `external/trailofbits-skills/plugins/c-review/skills/c-review/SKILL.md`
- **Tags**: `applications`, `auditing`, `c-review`, `code`, `comprehensive`, `conditions`, `corruption`, `daemons`, `free`, `hunting`, `integer`, `memory`, `native`, `overflow`, `overflows`, `performs`, `platform`, `race`, `review`, `reviewing`, `safety`, `security`, `services`, `userspace`, `vulnerabilities`

## constant-time-analysis

Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or Ruby.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md`
- **Tags**: `analysis`, `branches`, `channel`, `code`, `constant`, `constant-time`, `constant-time-analysis`, `crypto`, `cryptographic`, `dependent`, `detects`, `division`, `encountering`, `implementing`, `java`, `javascript`, `kotlin`, `php`, `programming`, `python`, `questions`, `reviewing`, `ruby`, `rust`, `secret`, `secret-dependent`, `secrets`, `side`, `side-channel`, `swift`, `time`, `timing`, `typescript`, `vulnerabilities`

## cosmos-vulnerability-scanner

Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md`
- **Tags**: `assessing`, `auditing`, `blockchain`, `building`, `building-secure-contracts`, `chain`, `consensus`, `consensus-critical`, `contracts`, `core`, `cosmos`, `cosmos-vulnerability-scanner`, `cosmwasm`, `critical`, `custom`, `divergence`, `evm`, `fund`, `halts`, `ibc`, `integrations`, `launch`, `loss`, `modules`, `pre`, `pre-launch`, `reviewing`, `scanner`, `scans`, `sdk`, `secure`, `security`, `state`, `updated`, `vulnerabilities`, `vulnerability`

## digest

Generate a daily or weekly digest of activity across all connected sources. Use when catching up after time away, starting the day and wanting a summary of mentions and action items, or reviewing a week's decisions and document updates grouped by project.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/digest`
- **Skill file**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/digest/SKILL.md`
- **Tags**: `activity`, `away`, `catching`, `connected`, `daily`, `day`, `decisions`, `digest`, `document`, `enterprise`, `enterprise-search`, `grouped`, `items`, `mentions`, `project`, `reviewing`, `search`, `sources`, `starting`, `summary`, `time`, `updates`, `wanting`, `week`, `weekly`

## insecure-defaults

Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults`
- **Skill file**: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults/SKILL.md`
- **Tags**: `allow`, `analyzing`, `apps`, `auditing`, `auth`, `config`, `defaults`, `detects`, `environment`, `fail`, `fail-open`, `handling`, `hardcoded`, `insecure`, `insecure-defaults`, `insecurely`, `management`, `open`, `permissive`, `production`, `reviewing`, `secrets`, `security`, `variable`, `weak`

## openai-pdf

Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-pdf/skills/openai-pdf`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-pdf/skills/openai-pdf/SKILL.md`
- **Tags**: `creating`, `involve`, `layout`, `pdf`, `reading`, `rendering`, `reviewing`, `where`

## pdf

Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/pdf`
- **Skill file**: `external/openai-skills/skills/.curated/pdf/SKILL.md`
- **Tags**: `checks`, `creating`, `curated`, `extraction`, `generation`, `involve`, `layout`, `matter`, `pages`, `pdf`, `pdfplumber`, `poppler`, `prefer`, `pypdf`, `python`, `reading`, `rendering`, `reportlab`, `reviewing`, `such`, `visual`, `where`

## property-based-testing

Provides guidance for property-based testing across multiple languages and smart contracts. Use when writing tests, reviewing code with serialization/validation/parsing patterns, designing features, or when property-based testing would provide stronger coverage than example-based tests.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/property-based-testing/skills/property-based-testing`
- **Skill file**: `external/trailofbits-skills/plugins/property-based-testing/skills/property-based-testing/SKILL.md`
- **Tags**: `code`, `contracts`, `coverage`, `designing`, `features`, `guidance`, `languages`, `multiple`, `parsing`, `property`, `property-testing`, `provide`, `provides`, `reviewing`, `serialization`, `smart`, `stronger`, `testing`, `tests`, `than`, `validation`, `would`

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

## sharp-edges

Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges`
- **Skill file**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges/SKILL.md`
- **Tags**: `api`, `apis`, `code`, `configuration`, `configurations`, `cryptographic`, `dangerous`, `default`, `defaults`, `designs`, `edges`, `enable`, `ergonomics`, `error`, `error-prone`, `evaluating`, `follows`, `footgun`, `identifies`, `library`, `mistakes`, `misuse`, `misuse-resistant`, `pit`, `principles`, `prone`, `resistant`, `reviewing`, `schemas`, `secure`, `security`, `sharp`, `sharp-edges`, `success`, `triggers`, `usability`, `whether`

## validate-data

QA an analysis before sharing -- methodology, accuracy, and bias checks. Use when reviewing an analysis before a stakeholder presentation, spot-checking calculations and aggregation logic, verifying a SQL query's results look right, or assessing whether conclusions are actually supported by the data.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/data/skills/validate-data`
- **Skill file**: `external/anthropic-knowledge-work-plugins/data/skills/validate-data/SKILL.md`
- **Tags**: `accuracy`, `actually`, `aggregation`, `analysis`, `assessing`, `bias`, `calculations`, `checking`, `checks`, `conclusions`, `data`, `logic`, `look`, `methodology`, `presentation`, `query`, `reviewing`, `right`, `sharing`, `spot`, `spot-checking`, `sql`, `stakeholder`, `supported`, `validate`, `validate-data`, `verifying`, `whether`

## vendor-review

Evaluate a vendor — cost analysis, risk assessment, and recommendation. Use when reviewing a new vendor proposal, deciding whether to renew or replace a contract, comparing two vendors side-by-side, or building a TCO breakdown and negotiation points before procurement sign-off.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/operations/skills/vendor-review`
- **Skill file**: `external/anthropic-knowledge-work-plugins/operations/skills/vendor-review/SKILL.md`
- **Tags**: `analysis`, `assessment`, `breakdown`, `building`, `comparing`, `contract`, `cost`, `deciding`, `evaluate`, `negotiation`, `off`, `operations`, `points`, `procurement`, `proposal`, `recommendation`, `renew`, `replace`, `review`, `reviewing`, `risk`, `side`, `side-by-side`, `sign`, `sign-off`, `tco`, `two`, `vendor`, `vendor-review`, `vendors`, `whether`

## winui-app

Bootstrap, develop, and design modern WinUI 3 desktop applications with C# and the Windows App SDK using official Microsoft guidance, WinUI Gallery patterns, Windows App SDK samples, and CommunityToolkit components. Use when creating a brand new app, preparing a machine for WinUI, reviewing, refactoring, planning, troubleshooting, environment-checking, or setting up WinUI 3 XAML, controls, navigation, windowing, theming, accessibility, responsiveness, performance, deployment, or related Windows app design and development work.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/winui-app`
- **Skill file**: `external/openai-skills/skills/.curated/winui-app/SKILL.md`
- **Tags**: `accessibility`, `app`, `applications`, `bootstrap`, `brand`, `checking`, `communitytoolkit`, `components`, `controls`, `creating`, `curated`, `deployment`, `design`, `desktop`, `develop`, `development`, `environment`, `environment-checking`, `gallery`, `guidance`, `machine`, `microsoft`, `modern`, `navigation`, `performance`, `planning`, `preparing`, `refactoring`, `responsiveness`, `reviewing`, `samples`, `sdk`, `setting`, `theming`, `troubleshooting`, `windowing`, `windows`, `winui`, `winui-app`, `xaml`
