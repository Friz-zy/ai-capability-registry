# supported

## Skills
Load skill file when task matches.

### migrate-to-codex
Migrate supported instruction files, skills, agents, and MCP config into Codex project and global files.

File: `external/openai-skills/skills/.curated/migrate-to-codex/SKILL.md`

### security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

File: `external/openai-skills/skills/.curated/security-best-practices/SKILL.md`

### validate-data
QA an analysis before sharing -- methodology, accuracy, and bias checks. Use when reviewing an analysis before a stakeholder presentation, spot-checking calculations and aggregation logic, verifying a SQL query's results look right, or assessing whether conclusions are actually supported by the data.

File: `external/anthropic-knowledge-work-plugins/data/skills/validate-data/SKILL.md`
