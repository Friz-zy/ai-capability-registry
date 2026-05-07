# pdf

## Skills
Load skill file when task matches.

### canvas-design
Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

File: `../external/anthropic-skills/skills/canvas-design/SKILL.md`

### instrument-data-to-allotrope
Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.

File: `../external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md`

### interpreting-culture-index
Interprets Culture Index (CI) surveys, behavioral profiles, and personality assessment data. Supports individual profile interpretation, team composition analysis (gas/brake/glue), burnout detection, profile comparison, hiring profiles, manager coaching, interview transcript analysis for trait prediction, candidate debrief, onboarding planning, and conflict mediation. Accepts extracted JSON or PDF input via OpenCV extraction script.

File: `../external/trailofbits-skills/plugins/culture-index/skills/interpreting-culture-index/SKILL.md`

### openai-pdf
Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout

File: `../external/trailofbits-skills-curated/plugins/openai-pdf/skills/openai-pdf/SKILL.md`

### pdf
Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

File: `../external/anthropic-skills/skills/pdf/SKILL.md`

### pdf
Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction.

File: `../external/openai-skills/skills/.curated/pdf/SKILL.md`

### react-pdf
No description.

File: `../external/trailofbits-skills-curated/plugins/react-pdf/skills/react-pdf/SKILL.md`

### view-pdf
Interactive PDF viewer. Use when the user wants to open, show, or view a PDF and collaborate on it visually — annotate, highlight, stamp, fill form fields, place signature/initials, or review markup together. Not for summarization or text extraction (use native Read instead).

File: `../external/anthropic-knowledge-work-plugins/pdf-viewer/skills/view-pdf/SKILL.md`
