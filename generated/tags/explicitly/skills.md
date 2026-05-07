# explicitly

## Navigation
Read skill files below to understand capabilities.
Load skill file when task matches.

## Skills

### openai-screenshot
Use when the user explicitly asks for a desktop or system screenshot (full screen, specific

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/trailofbits-skills-curated/plugins/openai-screenshot/skills/openai-screenshot/SKILL.md`

### openai-yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/trailofbits-skills-curated/plugins/openai-yeet/skills/openai-yeet/SKILL.md`

### screenshot
Use when the user explicitly asks for a desktop or system screenshot (full screen, specific app or window, or a pixel region), or when tool-specific capture capabilities are unavailable and an OS-level capture is needed.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.curated/screenshot/SKILL.md`

### security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.curated/security-best-practices/SKILL.md`

### security-ownership-map
Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.curated/security-ownership-map/SKILL.md`

### security-threat-model
Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.curated/security-threat-model/SKILL.md`

### yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.curated/yeet/SKILL.md`
