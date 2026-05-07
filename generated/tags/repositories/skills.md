# repositories

## Skills
Load skill and **use it** when task matches.

### claude-md-improver
Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization".

File: `../external/anthropic-claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver/SKILL.md`

### openai-security-ownership-map
Analyze git repositories to build a security ownership topology (people-to-file), compute

File: `../external/trailofbits-skills-curated/plugins/openai-security-ownership-map/skills/openai-security-ownership-map/SKILL.md`

### security-ownership-map
Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

File: `../external/openai-skills/skills/.curated/security-ownership-map/SKILL.md`
