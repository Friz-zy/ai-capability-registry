# document

## Skills
Load skill and **use it** when task matches.

### design-system
Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded values across components, writing documentation for a component's variants, states, and accessibility notes, or designing a new pattern that fits the existing system.

File: `../external/anthropic-knowledge-work-plugins/design/skills/design-system/SKILL.md`

### digest
Generate a daily or weekly digest of activity across all connected sources. Use when catching up after time away, starting the day and wanting a summary of mentions and action items, or reviewing a week's decisions and document updates grouped by project.

File: `../external/anthropic-knowledge-work-plugins/enterprise-search/skills/digest/SKILL.md`

### documentation
Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README", "write a runbook", "onboarding guide", or when the user needs help with any form of technical writing — API docs, architecture docs, or operational runbooks.

File: `../external/anthropic-knowledge-work-plugins/engineering/skills/documentation/SKILL.md`

### docx
Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

File: `../external/anthropic-skills/skills/docx/SKILL.md`

### figma-generate-library
Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.

File: `../external/openai-skills/skills/.curated/figma-generate-library/SKILL.md`

### process-doc
Document a business process — flowcharts, RACI, and SOPs. Use when formalizing a process that lives in someone's head, building a RACI to clarify who owns what, writing an SOP for a handoff or audit, or capturing the exceptions and edge cases of how work actually gets done.

File: `../external/anthropic-knowledge-work-plugins/operations/skills/process-doc/SKILL.md`

### search
Search across all connected sources in one query. Trigger with "find that doc about...", "what did we decide on...", "where was the conversation about...", or when looking for a decision, document, or discussion that could live in chat, email, cloud storage, or a project tracker.

File: `../external/anthropic-knowledge-work-plugins/enterprise-search/skills/search/SKILL.md`

### secure-workflow-guide
Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide/SKILL.md`

### signature-request
Prepare and route a document for e-signature — run a pre-signature checklist, configure signing order, and send for execution. Use when a contract is finalized and ready to sign, when verifying entity names, exhibits, and signature blocks before sending, or when setting up an envelope with sequential or parallel signers.

File: `../external/anthropic-knowledge-work-plugins/legal/skills/signature-request/SKILL.md`

### vendor-check
Check the status of existing agreements with a vendor across all connected systems — CLM, CRM, email, and document storage — with gap analysis and upcoming deadlines. Use when onboarding or renewing a vendor, when you need a consolidated view of what's signed and what's missing (MSA, DPA, SOW), or when checking for approaching expirations and surviving obligations.

File: `../external/anthropic-knowledge-work-plugins/legal/skills/vendor-check/SKILL.md`

### write-spec
Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user request into a structured document, scoping a feature with goals and non-goals, defining success metrics and acceptance criteria, or breaking a big ask into a phased spec.

File: `../external/anthropic-knowledge-work-plugins/product-management/skills/write-spec/SKILL.md`

### xlsx
Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

File: `../external/anthropic-skills/skills/xlsx/SKILL.md`
