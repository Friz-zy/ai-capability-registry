# static-analysis

## Skills
Select only the most relevant skills by description. If a skill matches, read its `SKILL.md` and use it before acting.

### codeql
Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. Triggers on "run codeql", "codeql scan", "codeql analysis", "build codeql database", or "find vulnerabilities with codeql". Supports "run all" (security-and-quality + security-experimental suites) and "important only" (high-precision security findings) scan modes. Also handles creating data extension models and processing CodeQL SARIF output.

File: `external/trailofbits-skills/plugins/static-analysis/skills/codeql/SKILL.md`

### sarif-parsing
Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on "parse sarif", "read scan results", "aggregate findings", "deduplicate alerts", or "process sarif output". Handles filtering, deduplication, format conversion, and CI/CD integration of SARIF data. Does NOT run scans — use the Semgrep or CodeQL skills for that.

File: `external/trailofbits-skills/plugins/static-analysis/skills/sarif-parsing/SKILL.md`

### semgrep
Run Semgrep static analysis scan on a codebase using parallel subagents. Supports two scan modes — "run all" (full ruleset coverage) and "important only" (high-confidence security vulnerabilities). Automatically detects and uses Semgrep Pro for cross-file taint analysis when available. Use when asked to scan code for vulnerabilities, run a security audit with Semgrep, find bugs, or perform static analysis. Spawns parallel workers for multi-language codebases.

File: `external/trailofbits-skills/plugins/static-analysis/skills/semgrep/SKILL.md`

### semgrep-rule-creator
Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections.

File: `external/trailofbits-skills/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md`

### semgrep-rule-variant-creator
Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for each language.

File: `external/trailofbits-skills/plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md`

### variant-analysis
Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audits after finding an initial issue.

File: `external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis/SKILL.md`
