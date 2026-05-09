# security

## Skills
Load skill and **use it** when task matches.

### address-sanitizer
AddressSanitizer detects memory errors during fuzzing. Use when fuzzing C/C++ code to find buffer overflows and use-after-free bugs.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/address-sanitizer/SKILL.md`

### aflpp
AFL++ is a fork of AFL with better fuzzing performance and advanced features. Use for multi-core fuzzing of C/C++ projects.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/aflpp/SKILL.md`

### agentic-actions-auditor
Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

File: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`

### algorand-vulnerability-scanner
Scans Algorand smart contracts for 11 common vulnerabilities including rekeying attacks, unchecked transaction fees, missing field validations, and access control issues. Use when auditing Algorand projects (TEAL/PyTeal).

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md`

### atheris
Atheris is a coverage-guided Python fuzzer based on libFuzzer. Use for fuzzing pure Python code and Python C extensions.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/atheris/SKILL.md`

### audit-context-building
Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding.

File: `external/trailofbits-skills/plugins/audit-context-building/skills/audit-context-building/SKILL.md`

### audit-prep-assistant
Prepares codebases for security review using Trail of Bits' checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation (flowcharts, user stories, inline comments).

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md`

### burpsuite-project-parser
Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or analyzing HTTP traffic captured in a Burp project.

File: `external/trailofbits-skills/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md`

### c-review
Performs comprehensive C/C++ security review for memory corruption, integer overflows, race conditions, and platform-specific vulnerabilities. Use when auditing native C/C++ applications, reviewing daemons or services for memory safety, or hunting integer overflow / use-after-free / race conditions in userspace code.

File: `external/trailofbits-skills/plugins/c-review/skills/c-review/SKILL.md`

### cairo-vulnerability-scanner
Scans Cairo/StarkNet smart contracts for 6 critical vulnerabilities including felt252 arithmetic overflow, L1-L2 messaging issues, address conversion problems, and signature replay. Use when auditing StarkNet projects.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md`

### cargo-fuzz
cargo-fuzz is the de facto fuzzing tool for Rust projects using Cargo. Use for fuzzing Rust code with libFuzzer backend.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/cargo-fuzz/SKILL.md`

### code-maturity-assessor
Systematic code maturity assessment using Trail of Bits' 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level code, and testing. Produces professional scorecard with evidence-based ratings and actionable recommendations.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/code-maturity-assessor/SKILL.md`

### code-review
Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.

File: `external/anthropic-knowledge-work-plugins/engineering/skills/code-review/SKILL.md`

### codeql
Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. Triggers on "run codeql", "codeql scan", "codeql analysis", "build codeql database", or "find vulnerabilities with codeql". Supports "run all" (security-and-quality + security-experimental suites) and "important only" (high-precision security findings) scan modes. Also handles creating data extension models and processing CodeQL SARIF output.

File: `external/trailofbits-skills/plugins/static-analysis/skills/codeql/SKILL.md`

### constant-time-analysis
Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or Ruby.

File: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md`

### constant-time-testing
Constant-time testing detects timing side channels in cryptographic code. Use when auditing crypto implementations for timing vulnerabilities.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/constant-time-testing/SKILL.md`

### cosmos-vulnerability-scanner
Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md`

### coverage-analysis
Coverage analysis measures code exercised during fuzzing. Use when assessing harness effectiveness or identifying fuzzing blockers.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/coverage-analysis/SKILL.md`

### crypto-protocol-diagram
Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow, extracting message flow from a spec or RFC, diagramming a ProVerif or Tamarin model, or drawing sequence diagrams for TLS, Noise, Signal, X3DH, Double Ratchet, FROST, DH, or ECDH protocols.

File: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram/SKILL.md`

### dimensional-analysis
Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol, offchain code, or other blockchain-related codebase with arithmetic. Prevents dimensional mismatches and catches formula bugs early.

File: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis/SKILL.md`

### entry-point-analyzer
Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

File: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`

### ffuf-web-fuzzing
Expert guidance for ffuf web fuzzing during authorized penetration testing. Covers directory discovery, subdomain enumeration, parameter fuzzing, authenticated fuzzing with raw requests, auto-calibration, and result analysis. Use when running ffuf scans, analyzing ffuf output, or building fuzzing strategies for web targets.

File: `external/trailofbits-skills-curated/plugins/ffuf-web-fuzzing/skills/ffuf-web-fuzzing/SKILL.md`

### firebase-apk-scanner
Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase vulnerabilities, performing mobile app security audits, or testing Firebase endpoint security. For authorized security research only.

File: `external/trailofbits-skills/plugins/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md`

### fp-check
Systematically verifies suspected security bugs to eliminate false positives. Produces TRUE POSITIVE or FALSE POSITIVE verdicts with documented evidence for each bug.

File: `external/trailofbits-skills/plugins/fp-check/skills/fp-check/SKILL.md`

### fuzzing-dictionary
Fuzzing dictionaries guide fuzzers with domain-specific tokens. Use when fuzzing parsers, protocols, or format-specific code.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-dictionary/SKILL.md`

### fuzzing-obstacles
Techniques for patching code to overcome fuzzing obstacles. Use when checksums, global state, or other barriers block fuzzer progress.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-obstacles/SKILL.md`

### genotoxic
Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circomvent and cairo-mutants), or using necessist.

File: `external/trailofbits-skills/plugins/trailmark/skills/genotoxic/SKILL.md`

### ghidra-headless
Reverse engineers binaries using Ghidra's headless analyzer. Use when decompiling executables, extracting functions, strings, symbols, or analyzing call graphs from compiled binaries without the Ghidra GUI.

File: `external/trailofbits-skills-curated/plugins/ghidra-headless/skills/ghidra-headless/SKILL.md`

### graph-evolution
Compares Trailmark code graphs at two source code snapshots (git commits, tags, or directories) to surface security-relevant structural changes. Detects new attack paths, complexity shifts, blast radius growth, taint propagation changes, and privilege boundary modifications that text diffs miss. Use when comparing code between commits or tags, analyzing structural evolution, detecting attack surface growth, reviewing what changed between audit snapshots, or finding security-relevant changes that text diffs miss.

File: `external/trailofbits-skills/plugins/trailmark/skills/graph-evolution/SKILL.md`

### guidelines-advisor
Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Provides actionable recommendations.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor/SKILL.md`

### harness-writing
Techniques for writing effective fuzzing harnesses across languages. Use when creating new fuzz targets or improving existing harness code.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/harness-writing/SKILL.md`

### insecure-defaults
Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling.

File: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults/SKILL.md`

### last30days
Researches a topic from the last 30 days on Reddit, X, and the web. Surfaces real community discussions with engagement metrics and synthesizes findings into actionable insights. Use when the user wants to know what people are saying about a topic right now.

File: `external/trailofbits-skills-curated/plugins/last30days/skills/last30days/SKILL.md`

### libafl
LibAFL is a modular fuzzing library for building custom fuzzers. Use for advanced fuzzing needs, custom mutators, or non-standard fuzzing targets.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/libafl/SKILL.md`

### mermaid-to-proverif
Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, forward secrecy), checking for replay attacks, or producing a .pv file from a sequence diagram.

File: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif/SKILL.md`

### mutation-testing
Configures mewt or muton mutation testing campaigns — scopes targets, tunes timeouts, and optimizes long-running runs. Use when the user mentions mewt, muton, mutation testing, or wants to configure or optimize a mutation testing campaign.

File: `external/trailofbits-skills/plugins/mutation-testing/skills/mutation-testing/SKILL.md`

### openai-security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements.

File: `external/trailofbits-skills-curated/plugins/openai-security-best-practices/skills/openai-security-best-practices/SKILL.md`

### openai-security-ownership-map
'Analyze git repositories to build a security ownership topology (people-to-file), compute

File: `external/trailofbits-skills-curated/plugins/openai-security-ownership-map/skills/openai-security-ownership-map/SKILL.md`

### openai-security-threat-model
Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities,

File: `external/trailofbits-skills-curated/plugins/openai-security-threat-model/skills/openai-security-threat-model/SKILL.md`

### ossfuzz
OSS-Fuzz provides free continuous fuzzing for open source projects. Use when setting up continuous fuzzing infrastructure or enrolling projects.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/ossfuzz/SKILL.md`

### property-based-testing
Provides guidance for property-based testing across multiple languages and smart contracts. Use when writing tests, reviewing code with serialization/validation/parsing patterns, designing features, or when property-based testing would provide stronger coverage than example-based tests.

File: `external/trailofbits-skills/plugins/property-based-testing/skills/property-based-testing/SKILL.md`

### ruzzy
Ruzzy is a coverage-guided Ruby fuzzer by Trail of Bits. Use for fuzzing pure Ruby code and Ruby C extensions.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/ruzzy/SKILL.md`

### sarif-parsing
Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on "parse sarif", "read scan results", "aggregate findings", "deduplicate alerts", or "process sarif output". Handles filtering, deduplication, format conversion, and CI/CD integration of SARIF data. Does NOT run scans — use the Semgrep or CodeQL skills for that.

File: `external/trailofbits-skills/plugins/static-analysis/skills/sarif-parsing/SKILL.md`

### scv-scan
Audits Solidity codebases for smart contract vulnerabilities using a four-phase workflow (cheatsheet loading, codebase sweep, deep validation, reporting) covering 36 vulnerability classes. Use when auditing Solidity contracts for security issues, performing smart contract vulnerability scans, or reviewing Solidity code for common exploit patterns.

File: `external/trailofbits-skills-curated/plugins/scv-scan/skills/scv-scan/SKILL.md`

### seatbelt-sandboxer
Generates minimal macOS Seatbelt sandbox configurations. Use when sandboxing, isolating, or restricting macOS applications with allowlist-based profiles.

File: `external/trailofbits-skills/plugins/seatbelt-sandboxer/skills/seatbelt-sandboxer/SKILL.md`

### secure-workflow-guide
Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide/SKILL.md`

### security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

File: `external/openai-skills/skills/.curated/security-best-practices/SKILL.md`

### security-ownership-map
Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

File: `external/openai-skills/skills/.curated/security-ownership-map/SKILL.md`

### security-threat-model
Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work.

File: `external/openai-skills/skills/.curated/security-threat-model/SKILL.md`

### semgrep
Run Semgrep static analysis scan on a codebase using parallel subagents. Supports two scan modes — "run all" (full ruleset coverage) and "important only" (high-confidence security vulnerabilities). Automatically detects and uses Semgrep Pro for cross-file taint analysis when available. Use when asked to scan code for vulnerabilities, run a security audit with Semgrep, find bugs, or perform static analysis. Spawns parallel workers for multi-language codebases.

File: `external/trailofbits-skills/plugins/static-analysis/skills/semgrep/SKILL.md`

### semgrep-rule-creator
Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections.

File: `external/trailofbits-skills/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md`

### semgrep-rule-variant-creator
Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for each language.

File: `external/trailofbits-skills/plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md`

### sharp-edges
Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

File: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges/SKILL.md`

### solana-vulnerability-scanner
Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use when auditing Solana/Anchor programs.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md`

### spec-to-code-compliance
Verifies code implements exactly what documentation specifies for blockchain audits. Use when comparing code against whitepapers, finding gaps between specs and implementation, or performing compliance checks for protocol implementations.

File: `external/trailofbits-skills/plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md`

### substrate-vulnerability-scanner
Scans Substrate/Polkadot pallets for 7 critical vulnerabilities including arithmetic overflow, panic DoS, incorrect weights, and bad origin checks. Use when auditing Substrate runtimes or FRAME pallets.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md`

### supply-chain-risk-auditor
Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagements.

File: `external/trailofbits-skills/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md`

### testing-handbook-generator
Meta-skill that analyzes the Trail of Bits Testing Handbook (appsec.guide) and generates Claude Code skills for security testing tools and techniques. Use when creating new skills based on handbook content.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/testing-handbook-generator/SKILL.md`

### token-integration-analyzer
Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Context-aware for both token implementations and token integrations.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer/SKILL.md`

### ton-vulnerability-scanner
Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without gas checks. Use when auditing FunC contracts.

File: `external/trailofbits-skills/plugins/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md`

### trailmark
Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

File: `external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`

### trailmark-structural
Runs full Trailmark structural analysis on Trailmark 0.2.x by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, and attack surface. Use when vivisect needs detailed structural data for a target. Triggers: structural analysis, blast radius, taint analysis, complexity hotspots.

File: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-structural/SKILL.md`

### trailmark-summary
Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview.

File: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary/SKILL.md`

### variant-analysis
Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audits after finding an initial issue.

File: `external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis/SKILL.md`

### vector-forge
Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

File: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`

### wooyun-legacy
Provides web vulnerability testing methodology distilled from 88,636 real-world cases from the WooYun vulnerability database (2010-2016). Use when performing penetration testing, security audits, code reviews for security flaws, or vulnerability research. Covers SQL injection, XSS, command execution, file upload, path traversal, unauthorized access, information disclosure, and business logic flaws.

File: `external/trailofbits-skills-curated/plugins/wooyun-legacy/skills/wooyun-legacy/SKILL.md`

### yara-rule-authoring
Guides authoring of high-quality YARA-X detection rules for malware identification. Use when writing, reviewing, or optimizing YARA rules. Covers naming conventions, string selection, performance optimization, migration from legacy YARA, and false positive reduction. Triggers on: YARA, YARA-X, malware detection, threat hunting, IOC, signature, crx module, dex module.

File: `external/trailofbits-skills/plugins/yara-authoring/skills/yara-rule-authoring/SKILL.md`

### zeroize-audit
Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling secrets, keys, passwords, or other sensitive data.

File: `external/trailofbits-skills/plugins/zeroize-audit/skills/zeroize-audit/SKILL.md`
