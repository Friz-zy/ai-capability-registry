# documents

## Skills
Select only the most relevant skills by description. If a skill matches, read its `SKILL.md` before applying it.

### brief
Generate contextual briefings for legal work — daily summary, topic research, or incident response. Use when starting your day and need a scan of legal-relevant items across email, calendar, and contracts, when researching a specific legal question across internal sources, or when a developing situation (data breach, litigation threat, regulatory inquiry) needs rapid context.

File: `external/anthropic-knowledge-work-plugins/legal/skills/brief/SKILL.md`

### doc-coauthoring
Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

File: `external/anthropic-skills/skills/doc-coauthoring/SKILL.md`

### docx
Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

File: `external/anthropic-skills/skills/docx/SKILL.md`

### openai-doc
Use when the task involves reading, creating, or editing `.docx` documents, especially when

File: `external/trailofbits-skills-curated/plugins/openai-doc/skills/openai-doc/SKILL.md`

### openai-pdf
Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout

File: `external/trailofbits-skills-curated/plugins/openai-pdf/skills/openai-pdf/SKILL.md`

### pdf
Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

File: `external/anthropic-skills/skills/pdf/SKILL.md`

### pdf
Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction.

File: `external/openai-skills/skills/.curated/pdf/SKILL.md`

### pptx
Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions "deck," "slides," "presentation," or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.

File: `external/anthropic-skills/skills/pptx/SKILL.md`

### view-pdf
Interactive PDF viewer. Use when the user wants to open, show, or view a PDF and collaborate on it visually — annotate, highlight, stamp, fill form fields, place signature/initials, or review markup together. Not for summarization or text extraction (use native Read instead).

File: `external/anthropic-knowledge-work-plugins/pdf-viewer/skills/view-pdf/SKILL.md`
