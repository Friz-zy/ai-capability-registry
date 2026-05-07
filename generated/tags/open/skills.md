# open

## Skills
Load skill and **use it** when task matches.

### firebase-apk-scanner
Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase vulnerabilities, performing mobile app security audits, or testing Firebase endpoint security. For authorized security research only.

File: `../external/trailofbits-skills/plugins/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md`

### gh-address-comments
Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.

File: `../external/openai-skills/skills/.curated/gh-address-comments/SKILL.md`

### insecure-defaults
Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling.

File: `../external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults/SKILL.md`

### openai-gh-address-comments
Help address review/issue comments on the open GitHub PR for the current branch using gh

File: `../external/trailofbits-skills-curated/plugins/openai-gh-address-comments/skills/openai-gh-address-comments/SKILL.md`

### openai-yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request

File: `../external/trailofbits-skills-curated/plugins/openai-yeet/skills/openai-yeet/SKILL.md`

### start
Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your existing task list, or decoding the shorthand (nicknames, acronyms, project codenames) you use in your todos.

File: `../external/anthropic-knowledge-work-plugins/productivity/skills/start/SKILL.md`

### ton-vulnerability-scanner
Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without gas checks. Use when auditing FunC contracts.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md`

### view-pdf
Interactive PDF viewer. Use when the user wants to open, show, or view a PDF and collaborate on it visually — annotate, highlight, stamp, fill form fields, place signature/initials, or review markup together. Not for summarization or text extraction (use native Read instead).

File: `../external/anthropic-knowledge-work-plugins/pdf-viewer/skills/view-pdf/SKILL.md`

### xlsx
Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

File: `../external/anthropic-skills/skills/xlsx/SKILL.md`

### yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).

File: `../external/openai-skills/skills/.curated/yeet/SKILL.md`
