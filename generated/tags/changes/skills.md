# changes

## Skills
Load skill and **use it** when task matches.

### code-review
Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.

File: `../external/anthropic-knowledge-work-plugins/engineering/skills/code-review/SKILL.md`

### docx
Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

File: `../external/anthropic-skills/skills/docx/SKILL.md`

### second-opinion
Runs external LLM code reviews (OpenAI Codex or Google Gemini CLI) on uncommitted changes, branch diffs, or specific commits. Use when the user asks for a second opinion, external review, codex review, gemini review, or mentions /second-opinion.

File: `../external/trailofbits-skills/plugins/second-opinion/skills/second-opinion/SKILL.md`

### variance-analysis
Decompose financial variances into drivers with narrative explanations and waterfall analysis. Use when analyzing budget vs. actual, period-over-period changes, revenue or expense variances, or preparing variance commentary for leadership.

File: `../external/anthropic-knowledge-work-plugins/finance/skills/variance-analysis/SKILL.md`
