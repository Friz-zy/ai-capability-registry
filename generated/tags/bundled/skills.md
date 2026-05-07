# bundled

## Skills
Load skill and **use it** when task matches.

### hatch-pet
Create, repair, validate, preview, and package Codex-compatible animated pets and pet spritesheets from character art, screenshots, generated images, or visual references. Use when a user wants to hatch a Codex pet, create a custom animated pet, or build a built-in pet asset with an 8x9 atlas, transparent unused cells, row-by-row animation prompts, QA contact sheets, preview videos, and pet.json packaging. This skill composes the installed $imagegen system skill for visual generation and uses bundled scripts for deterministic spritesheet assembly.

File: `../external/openai-skills/skills/.curated/hatch-pet/SKILL.md`

### jupyter-notebook
Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and run the helper script `new_notebook.py` to generate a clean starting notebook.

File: `../external/openai-skills/skills/.curated/jupyter-notebook/SKILL.md`

### openai-docs
Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.

File: `../external/openai-skills/skills/.curated/openai-docs/SKILL.md`

### openai-docs
Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.

File: `../external/openai-skills/skills/.system/openai-docs/SKILL.md`

### playwright
Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script.

File: `../external/openai-skills/skills/.curated/playwright/SKILL.md`

### speech
Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for live calls. Custom voice creation is out of scope.

File: `../external/openai-skills/skills/.curated/speech/SKILL.md`

### zoom-mcp
Guidance for the bundled Zoom MCP connectors. Use after routing to an MCP workflow when planning or troubleshooting tool-based access to meetings, recordings, meeting assets, or transcripts. Route Zoom Docs requests to the dedicated Docs MCP server and Whiteboard-specific requests to `zoom-mcp/whiteboard`.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-mcp/SKILL.md`
