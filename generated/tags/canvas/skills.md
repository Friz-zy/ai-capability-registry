# canvas

## Skills
Load skill and **use it** when task matches.

### canvas-design
Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

File: `../external/anthropic-skills/skills/canvas-design/SKILL.md`

### figma-code-connect-components
Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code connect", "connect this component to code", "map this component", "link component to code", "create code connect mapping", or wants to establish mappings between Figma designs and code implementations. For canvas writes via `use_figma`, use `figma-use`.

File: `../external/openai-skills/skills/.curated/figma-code-connect-components/SKILL.md`

### figma-implement-design
Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementing UI code from Figma files, when user mentions "implement design", "generate code", "implement component", provides Figma URLs, or asks to build components matching Figma specs. For Figma canvas writes via `use_figma`, use `figma-use`.

File: `../external/openai-skills/skills/.curated/figma-implement-design/SKILL.md`

### imagegen
Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.

File: `../external/openai-skills/skills/.system/imagegen/SKILL.md`
