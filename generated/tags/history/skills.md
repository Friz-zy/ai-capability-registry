# history

## Skills
Load skill and **use it** when task matches.

### burpsuite-project-parser
Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or analyzing HTTP traffic captured in a Burp project.

File: `../external/trailofbits-skills/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md`

### security-ownership-map
Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

File: `../external/openai-skills/skills/.curated/security-ownership-map/SKILL.md`
