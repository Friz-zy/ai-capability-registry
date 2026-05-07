# like

## Skills
Load skill and **use it** when task matches.

### claude-api
Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

File: `../external/anthropic-skills/skills/claude-api/SKILL.md`

### data-visualization
Create effective data visualizations with Python (matplotlib, seaborn, plotly). Use when building charts, choosing the right chart type for a dataset, creating publication-quality figures, or applying design principles like accessibility and color theory.

File: `../external/anthropic-knowledge-work-plugins/data/skills/data-visualization/SKILL.md`

### docx
Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

File: `../external/anthropic-skills/skills/docx/SKILL.md`

### draft-response
Draft a professional customer-facing response tailored to the situation and relationship. Use when answering a product question, responding to an escalation or outage, delivering bad news like a delay or won't-fix, declining a feature request, or replying to a billing issue.

File: `../external/anthropic-knowledge-work-plugins/customer-support/skills/draft-response/SKILL.md`

### explore-data
Profile and explore a dataset to understand its shape, quality, and patterns. Use when encountering a new table or file, checking null rates and column distributions, spotting data quality issues like duplicates or suspicious values, or deciding which dimensions and metrics to analyze.

File: `../external/anthropic-knowledge-work-plugins/data/skills/explore-data/SKILL.md`

### memory-management
Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames, and internal language so Claude understands requests like a colleague would. CLAUDE.md for working memory, memory/ directory for the full knowledge base.

File: `../external/anthropic-knowledge-work-plugins/productivity/skills/memory-management/SKILL.md`

### pipeline-review
Analyze pipeline health — prioritize deals, flag risks, get a weekly action plan. Use when running a weekly pipeline review, deciding which deals to focus on this week, spotting stale or stuck opportunities, auditing for hygiene issues like bad close dates, or identifying single-threaded deals.

File: `../external/anthropic-knowledge-work-plugins/sales/skills/pipeline-review/SKILL.md`

### pptx
Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.

File: `../external/anthropic-skills/skills/pptx/SKILL.md`

### slack-gif-creator
Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack.

File: `../external/anthropic-skills/skills/slack-gif-creator/SKILL.md`

### vercel-deploy
Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

File: `../external/openai-skills/skills/.curated/vercel-deploy/SKILL.md`

### xlsx
Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

File: `../external/anthropic-skills/skills/xlsx/SKILL.md`
