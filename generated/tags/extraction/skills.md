# extraction

## Navigation
Read skill files below to understand capabilities.
Load skill file when task matches.

## Skills

### interpreting-culture-index
Interprets Culture Index (CI) surveys, behavioral profiles, and personality assessment data. Supports individual profile interpretation, team composition analysis (gas/brake/glue), burnout detection, profile comparison, hiring profiles, manager coaching, interview transcript analysis for trait prediction, candidate debrief, onboarding planning, and conflict mediation. Accepts extracted JSON or PDF input via OpenCV extraction script.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/trailofbits-skills/plugins/culture-index/skills/interpreting-culture-index/SKILL.md`

### pdf
Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.curated/pdf/SKILL.md`

### playwright
Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.curated/playwright/SKILL.md`

### view-pdf
Interactive PDF viewer. Use when the user wants to open, show, or view a PDF and collaborate on it visually — annotate, highlight, stamp, fill form fields, place signature/initials, or review markup together. Not for summarization or text extraction (use native Read instead).

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/pdf-viewer/skills/view-pdf/SKILL.md`
