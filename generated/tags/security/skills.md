# Tag: security

Skills with tag `security`:

## agentic-actions-auditor

Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor`
- **Skill file**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`
- **Tags**: `actions`, `agentic`, `agentic-actions-auditor`, `allowlists`, `attack`, `attacker`, `attacker-controlled`, `auditing`, `auditor`, `audits`, `cli`, `code`, `codex`, `coding`, `configurations`, `controlled`, `dangerous`, `detects`, `direct`, `env`, `evaluating`, `expression`, `gemini`, `github`, `including`, `inference`, `injection`, `input`, `integrations`, `intermediary`, `invoke`, `pipeline`, `pipelines`, `prompt`, `reaches`, `reviewing`, `risks`, `running`, `sandbox`, `security`, `var`, `vectors`, `vulnerabilities`, `where`, `wildcard`

## audit-prep-assistant

Prepares codebases for security review using Trail of Bits' checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation (flowcharts, user stories, inline comments).

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md`
- **Tags**: `accessibility`, `analysis`, `audit`, `audit-prep`, `building`, `building-secure-contracts`, `checklist`, `code`, `codebases`, `comments`, `contracts`, `coverage`, `dead`, `documentation`, `ensures`, `flowcharts`, `generates`, `goals`, `helps`, `increases`, `inline`, `prep`, `prepares`, `removes`, `review`, `runs`, `secure`, `security`, `set`, `static`, `stories`, `test`

## burpsuite-project-parser

Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or analyzing HTTP traffic captured in a Burp project.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/burpsuite-project-parser/skills/burpsuite-project-parser`
- **Skill file**: `external/trailofbits-skills/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md`
- **Tags**: `analyzing`, `audit`, `bodies`, `burp`, `burpsuite`, `burpsuite-project-parser`, `captured`, `command`, `data`, `dumping`, `explores`, `extracting`, `findings`, `headers`, `history`, `http`, `line`, `map`, `parser`, `project`, `proxy`, `regex`, `response`, `searches`, `searching`, `security`, `site`, `suite`, `traffic`

## c-review

Performs comprehensive C/C++ security review for memory corruption, integer overflows, race conditions, and platform-specific vulnerabilities. Use when auditing native C/C++ applications, reviewing daemons or services for memory safety, or hunting integer overflow / use-after-free / race conditions in userspace code.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/c-review/skills/c-review`
- **Skill file**: `external/trailofbits-skills/plugins/c-review/skills/c-review/SKILL.md`
- **Tags**: `applications`, `auditing`, `c-review`, `code`, `comprehensive`, `conditions`, `corruption`, `daemons`, `free`, `hunting`, `integer`, `memory`, `native`, `overflow`, `overflows`, `performs`, `platform`, `race`, `review`, `reviewing`, `safety`, `security`, `services`, `userspace`, `vulnerabilities`

## code-review

Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/code-review`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/code-review/SKILL.md`
- **Tags**: `cases`, `change`, `changes`, `checking`, `code`, `code-review`, `correctness`, `diff`, `edge`, `engineering`, `error`, `gaps`, `handling`, `injection`, `merge`, `missing`, `performance`, `queries`, `review`, `risks`, `safe`, `security`, `trigger`, `url`

## cosmos-vulnerability-scanner

Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md`
- **Tags**: `assessing`, `auditing`, `blockchain`, `building`, `building-secure-contracts`, `chain`, `consensus`, `consensus-critical`, `contracts`, `core`, `cosmos`, `cosmos-vulnerability-scanner`, `cosmwasm`, `critical`, `custom`, `divergence`, `evm`, `fund`, `halts`, `ibc`, `integrations`, `launch`, `loss`, `modules`, `pre`, `pre-launch`, `reviewing`, `scanner`, `scans`, `sdk`, `secure`, `security`, `state`, `updated`, `vulnerabilities`, `vulnerability`

## entry-point-analyzer

Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer`
- **Skill file**: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`
- **Tags**: `access`, `admin`, `analyzer`, `analyzes`, `asked`, `audit`, `auditing`, `callable`, `categorizes`, `changing`, `codebases`, `contract`, `contracts`, `control`, `cosmwasm`, `detects`, `entry`, `entry-point-analyzer`, `excludes`, `externally`, `find`, `flows`, `functions`, `generates`, `identify`, `level`, `modify`, `move`, `operations`, `point`, `points`, `privileged`, `public`, `pure`, `reports`, `restricted`, `role`, `role-restricted`, `rust`, `security`, `smart`, `solana`, `solidity`, `state`, `state-changing`, `structured`, `them`, `ton`, `view`, `vyper`

## firebase-apk-scanner

Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase vulnerabilities, performing mobile app security audits, or testing Firebase endpoint security. For authorized security research only.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/firebase-apk-scanner/skills/firebase-apk-scanner`
- **Skill file**: `external/trailofbits-skills/plugins/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md`
- **Tags**: `analyzing`, `android`, `apk`, `apks`, `app`, `audits`, `authentication`, `authorized`, `buckets`, `cloud`, `databases`, `endpoint`, `exposed`, `firebase`, `firebase-apk-scanner`, `functions`, `including`, `issues`, `misconfigurations`, `mobile`, `open`, `performing`, `research`, `scanner`, `scans`, `security`, `storage`, `testing`, `vulnerabilities`

## fp-check

Systematically verifies suspected security bugs to eliminate false positives. Produces TRUE POSITIVE or FALSE POSITIVE verdicts with documented evidence for each bug.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/fp-check/skills/fp-check`
- **Skill file**: `external/trailofbits-skills/plugins/fp-check/skills/fp-check/SKILL.md`
- **Tags**: `bug`, `bugs`, `documented`, `eliminate`, `evidence`, `false`, `positive`, `positives`, `produces`, `security`, `suspected`, `systematically`, `true`, `verdicts`, `verifies`

## insecure-defaults

Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults`
- **Skill file**: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults/SKILL.md`
- **Tags**: `allow`, `analyzing`, `apps`, `auditing`, `auth`, `config`, `defaults`, `detects`, `environment`, `fail`, `fail-open`, `handling`, `hardcoded`, `insecure`, `insecure-defaults`, `insecurely`, `management`, `open`, `permissive`, `production`, `reviewing`, `secrets`, `security`, `variable`, `weak`

## mermaid-to-proverif

Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, forward secrecy), checking for replay attacks, or producing a .pv file from a sequence diagram.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif/SKILL.md`
- **Tags**: `attacks`, `authentication`, `checking`, `converting`, `cryptographic`, `describing`, `diagram`, `formal`, `formally`, `forward`, `generating`, `mermaid`, `mermaid-to-proverif`, `model`, `models`, `producing`, `properties`, `protocol`, `protocols`, `proverif`, `replay`, `secrecy`, `security`, `sequence`, `sequencediagrams`, `trailmark`, `translates`, `verification`, `verifying`

## openai-security-best-practices

Perform language and framework specific security best-practice reviews and suggest improvements.

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-security-best-practices/skills/openai-security-best-practices`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-security-best-practices/skills/openai-security-best-practices/SKILL.md`
- **Tags**: `framework`, `improvements`, `language`, `perform`, `practice`, `practices`, `reviews`, `security`, `security-practices`, `suggest`

## openai-security-ownership-map

Analyze git repositories to build a security ownership topology (people-to-file), compute

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-security-ownership-map/skills/openai-security-ownership-map`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-security-ownership-map/skills/openai-security-ownership-map/SKILL.md`
- **Tags**: `analyze`, `build`, `compute`, `git`, `map`, `ownership`, `people`, `people-to`, `repositories`, `security`, `security-ownership-map`, `topology`

## openai-security-threat-model

Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities,

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-security-threat-model/skills/openai-security-threat-model`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-security-threat-model/skills/openai-security-threat-model/SKILL.md`
- **Tags**: `assets`, `attacker`, `boundaries`, `capabilities`, `enumerates`, `grounded`, `model`, `modeling`, `repository`, `repository-grounded`, `security`, `security-threat-model`, `threat`, `trust`

## scv-scan

Audits Solidity codebases for smart contract vulnerabilities using a four-phase workflow (cheatsheet loading, codebase sweep, deep validation, reporting) covering 36 vulnerability classes. Use when auditing Solidity contracts for security issues, performing smart contract vulnerability scans, or reviewing Solidity code for common exploit patterns.

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/scv-scan/skills/scv-scan`
- **Skill file**: `external/trailofbits-skills-curated/plugins/scv-scan/skills/scv-scan/SKILL.md`
- **Tags**: `auditing`, `audits`, `cheatsheet`, `classes`, `code`, `codebase`, `codebases`, `contract`, `contracts`, `covering`, `deep`, `exploit`, `four`, `four-phase`, `issues`, `loading`, `performing`, `phase`, `reporting`, `reviewing`, `scan`, `scans`, `scv`, `scv-scan`, `security`, `smart`, `solidity`, `sweep`, `validation`, `vulnerabilities`, `vulnerability`

## secure-workflow-guide

Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide/SKILL.md`
- **Tags**: `areas`, `building`, `building-secure-contracts`, `checks`, `conformance`, `contracts`, `development`, `diagrams`, `document`, `erc`, `features`, `fuzzing`, `generates`, `guides`, `helps`, `integration`, `manual`, `properties`, `reviews`, `runs`, `scans`, `secure`, `security`, `slither`, `special`, `token`, `upgradeability`, `verification`, `visual`

## security-awareness

>

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/security-awareness/skills/security-awareness`
- **Skill file**: `external/trailofbits-skills-curated/plugins/security-awareness/skills/security-awareness/SKILL.md`
- **Tags**: `awareness`, `security`, `security-awareness`

## security-best-practices

Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-best-practices`
- **Skill file**: `external/openai-skills/skills/.curated/security-best-practices/SKILL.md`
- **Tags**: `code`, `coding`, `curated`, `debugging`, `default`, `explicitly`, `framework`, `general`, `guidance`, `improvements`, `javascript`, `language`, `languages`, `non`, `non-security`, `perform`, `practice`, `practices`, `python`, `report`, `requests`, `review`, `reviews`, `secure`, `secure-by-default`, `security`, `security-practices`, `suggest`, `supported`, `trigger`, `typescript`

## security-ownership-map

Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-ownership-map`
- **Skill file**: `external/openai-skills/skills/.curated/security-ownership-map/SKILL.md`
- **Tags**: `analysis`, `analyze`, `build`, `bus`, `bus-factor`, `checks`, `clusters`, `code`, `codeowners`, `compute`, `csv`, `curated`, `databases`, `explicitly`, `export`, `factor`, `general`, `git`, `graph`, `grounded`, `history`, `hotspots`, `lists`, `maintainer`, `maintainers`, `map`, `non`, `non-security`, `oriented`, `orphaned`, `ownership`, `people`, `people-to`, `questions`, `reality`, `repositories`, `risk`, `security`, `security-oriented`, `security-ownership-map`, `sensitive`, `sensitive-code`, `topology`, `trigger`, `visualization`

## security-threat-model

Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-threat-model`
- **Skill file**: `external/openai-skills/skills/.curated/security-threat-model/SKILL.md`
- **Tags**: `abuse`, `appsec`, `architecture`, `asks`, `assets`, `attacker`, `boundaries`, `capabilities`, `code`, `codebase`, `concise`, `curated`, `design`, `enumerate`, `enumerates`, `explicitly`, `general`, `grounded`, `markdown`, `mitigations`, `model`, `modeling`, `non`, `non-security`, `path`, `paths`, `perform`, `repository`, `repository-grounded`, `review`, `security`, `security-threat-model`, `summaries`, `threat`, `threats`, `trigger`, `trust`, `writes`

## semgrep-rule-creator

Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/semgrep-rule-creator/skills/semgrep-rule-creator`
- **Skill file**: `external/trailofbits-skills/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md`
- **Tags**: `analysis`, `bug`, `building`, `code`, `creates`, `creator`, `custom`, `detecting`, `detections`, `rule`, `security`, `semgrep`, `semgrep-rule-creator`, `static`, `vulnerabilities`

## setup-zoom-websockets

Reference skill for Zoom WebSockets. Use after routing to a low-latency event workflow when persistent connections, faster event delivery, or security constraints make WebSockets preferable to webhooks.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/websockets`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/websockets/SKILL.md`
- **Tags**: `connections`, `constraints`, `delivery`, `event`, `faster`, `latency`, `low`, `low-latency`, `make`, `partner`, `persistent`, `preferable`, `routing`, `security`, `webhooks`, `websockets`, `zoom`, `zoom-websockets`

## sharp-edges

Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges`
- **Skill file**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges/SKILL.md`
- **Tags**: `api`, `apis`, `code`, `configuration`, `configurations`, `cryptographic`, `dangerous`, `default`, `defaults`, `designs`, `edges`, `enable`, `ergonomics`, `error`, `error-prone`, `evaluating`, `follows`, `footgun`, `identifies`, `library`, `mistakes`, `misuse`, `misuse-resistant`, `pit`, `principles`, `prone`, `resistant`, `reviewing`, `schemas`, `secure`, `security`, `sharp`, `sharp-edges`, `success`, `triggers`, `usability`, `whether`

## supply-chain-risk-auditor

Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagements.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor`
- **Skill file**: `external/trailofbits-skills/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md`
- **Tags**: `assessing`, `attack`, `auditor`, `chain`, `dependencies`, `dependency`, `engagements`, `evaluating`, `exploitation`, `health`, `heightened`, `identifies`, `risk`, `scoping`, `security`, `supply`, `supply-chain-risk-auditor`, `surface`, `takeover`

## trailmark

Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`
- **Tags**: `analysis`, `analyzing`, `attack`, `audit`, `auto`, `blast`, `boundaries`, `building`, `builds`, `call`, `code`, `complexity`, `detect`, `detect-languages`, `entry`, `enumerating`, `enumeration`, `finding`, `graph`, `graphs`, `hotspots`, `includes`, `language`, `languages`, `mapping`, `measuring`, `multi`, `multi-language`, `parse`, `passes`, `paths`, `point`, `points`, `polyglot`, `pre`, `pre-analysis`, `prefer`, `prioritization`, `privilege`, `propagation`, `queries`, `radius`, `security`, `surface`, `taint`, `target`, `tracing`, `trailmark`, `unknown`

## variant-analysis

Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audits after finding an initial issue.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis/SKILL.md`
- **Tags**: `analysis`, `analyzing`, `audits`, `bug`, `bugs`, `building`, `code`, `codebases`, `codeql`, `find`, `finding`, `hunting`, `initial`, `issue`, `performing`, `queries`, `security`, `semgrep`, `similar`, `systematic`, `variant`, `variant-analysis`, `variants`, `vulnerabilities`
