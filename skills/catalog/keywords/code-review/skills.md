# code-review

## Skills
Select only the most relevant skills by description. If a skill matches, read its `SKILL.md` and use it before acting.

### code-review
Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.

File: `external/anthropic-knowledge-work-plugins/engineering/skills/code-review/SKILL.md`

### finishing-a-development-branch
Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup

File: `external/superpowers-skills/skills/finishing-a-development-branch/SKILL.md`

### openai-security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements.

File: `external/trailofbits-skills-curated/plugins/openai-security-best-practices/skills/openai-security-best-practices/SKILL.md`

### openai-security-ownership-map
'Analyze git repositories to build a security ownership topology (people-to-file), compute

File: `external/trailofbits-skills-curated/plugins/openai-security-ownership-map/skills/openai-security-ownership-map/SKILL.md`

### receiving-code-review
Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation

File: `external/superpowers-skills/skills/receiving-code-review/SKILL.md`

### requesting-code-review
Use when completing tasks, implementing major features, or before merging to verify work meets requirements

File: `external/superpowers-skills/skills/requesting-code-review/SKILL.md`

### second-opinion
Runs external LLM code reviews (OpenAI Codex or Google Gemini CLI) on uncommitted changes, branch diffs, or specific commits. Use when the user asks for a second opinion, external review, codex review, gemini review, or mentions /second-opinion.

File: `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion/SKILL.md`

### security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

File: `external/openai-skills/skills/.curated/security-best-practices/SKILL.md`

### security-ownership-map
Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

File: `external/openai-skills/skills/.curated/security-ownership-map/SKILL.md`

### verification-before-completion
Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always

File: `external/superpowers-skills/skills/verification-before-completion/SKILL.md`
