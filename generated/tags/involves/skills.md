# involves

## Skills
Load skill file when task matches.

### figma
Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma nodes into production code. Trigger when a task involves Figma URLs, node IDs, design-to-code implementation, or Figma MCP setup and troubleshooting.

File: `../external/openai-skills/skills/.curated/figma/SKILL.md`

### figma-generate-design
Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

File: `../external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`

### openai-doc
Use when the task involves reading, creating, or editing `.docx` documents, especially when

File: `../external/trailofbits-skills-curated/plugins/openai-doc/skills/openai-doc/SKILL.md`
