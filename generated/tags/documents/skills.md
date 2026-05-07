# documents

## Skills
Load skill file when task matches.

### canvas-design
Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

File: `../external/anthropic-skills/skills/canvas-design/SKILL.md`

### docx
Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

File: `../external/anthropic-skills/skills/docx/SKILL.md`

### openai-doc
Use when the task involves reading, creating, or editing `.docx` documents, especially when

File: `../external/trailofbits-skills-curated/plugins/openai-doc/skills/openai-doc/SKILL.md`

### plugin-settings
This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content.

File: `../external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-settings/SKILL.md`
