# languages

## Skills
Load skill and **use it** when task matches.

### property-based-testing
Provides guidance for property-based testing across multiple languages and smart contracts. Use when writing tests, reviewing code with serialization/validation/parsing patterns, designing features, or when property-based testing would provide stronger coverage than example-based tests.

File: `../external/trailofbits-skills/plugins/property-based-testing/skills/property-based-testing/SKILL.md`

### security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

File: `../external/openai-skills/skills/.curated/security-best-practices/SKILL.md`

### semgrep-rule-variant-creator
Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for each language.

File: `../external/trailofbits-skills/plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md`

### trailmark
Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

File: `../external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`

### trailmark-summary
Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview.

File: `../external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary/SKILL.md`
