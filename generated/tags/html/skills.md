# html

## Navigation
Read skill files below to understand capabilities.
Load skill file when task matches.

## Skills

### build-dashboard
Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results into a shareable self-contained report, building a team monitoring snapshot, or needing multiple charts with filters in one browser-openable file.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/data/skills/build-dashboard/SKILL.md`

### competitive-intelligence
Research your competitors and build an interactive battlecard. Outputs an HTML artifact with clickable competitor cards and a comparison matrix. Trigger with "competitive intel", "research competitors", "how do we compare to [competitor]", "battlecard for [competitor]", or "what's new with [competitor]".

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/sales/skills/competitive-intelligence/SKILL.md`

### frontend-design
Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-skills/skills/frontend-design/SKILL.md`

### imagegen
Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.system/imagegen/SKILL.md`

### openai-develop-web-game
Use when the agent is building or iterating on a web game (HTML/JS) and needs a reliable

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/trailofbits-skills-curated/plugins/openai-develop-web-game/skills/openai-develop-web-game/SKILL.md`

### playground
Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-claude-plugins-official/plugins/playground/skills/playground/SKILL.md`

### session-report
Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-claude-plugins-official/plugins/session-report/skills/session-report/SKILL.md`

### theme-factory
Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-skills/skills/theme-factory/SKILL.md`

### web-artifacts-builder
Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-skills/skills/web-artifacts-builder/SKILL.md`

### xlsx
Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-skills/skills/xlsx/SKILL.md`
