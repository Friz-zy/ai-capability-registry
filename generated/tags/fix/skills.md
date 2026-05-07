# fix

## Skills
Load skill file when task matches.

### claude-in-chrome-troubleshooting
Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratically.

File: `../external/trailofbits-skills/plugins/claude-in-chrome-troubleshooting/skills/claude-in-chrome-troubleshooting/SKILL.md`

### claude-md-improver
Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization".

File: `../external/anthropic-claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver/SKILL.md`

### debug
Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected and the cause isn't obvious.

File: `../external/anthropic-knowledge-work-plugins/engineering/skills/debug/SKILL.md`

### debug-zoom-integration
Debug broken Zoom implementations quickly. Use when auth, webhooks, SDK joins, MCP transport, or real-time media workflows are failing and you need to isolate the layer before proposing a fix.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom-integration/SKILL.md`

### draft-response
Draft a professional customer-facing response tailored to the situation and relationship. Use when answering a product question, responding to an escalation or outage, delivering bad news like a delay or won't-fix, declining a feature request, or replying to a billing issue.

File: `../external/anthropic-knowledge-work-plugins/customer-support/skills/draft-response/SKILL.md`

### gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

File: `../external/openai-skills/skills/.curated/gh-fix-ci/SKILL.md`

### openai-gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions;

File: `../external/trailofbits-skills-curated/plugins/openai-gh-fix-ci/skills/openai-gh-fix-ci/SKILL.md`

### process-optimization
Analyze and improve business processes. Trigger with "this process is slow", "how can we improve", "streamline this workflow", "too many steps", "bottleneck", or when the user describes an inefficient process they want to fix.

File: `../external/anthropic-knowledge-work-plugins/operations/skills/process-optimization/SKILL.md`

### skill-improver
Iteratively reviews and fixes Claude Code skill quality issues until they meet standards. Runs automated fix-review cycles using the skill-reviewer agent. Use to fix skill quality issues, improve skill descriptions, run automated skill review loops, or iteratively refine a skill. Triggers on 'fix my skill', 'improve skill quality', 'skill improvement loop'. NOT for one-time reviews—use /skill-reviewer directly.

File: `../external/trailofbits-skills/plugins/skill-improver/skills/skill-improver/SKILL.md`

### xlsx
Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

File: `../external/anthropic-skills/skills/xlsx/SKILL.md`
