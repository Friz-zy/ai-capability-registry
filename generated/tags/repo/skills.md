# repo

## Navigation
Read skill files below to understand capabilities.
Load skill file when task matches.

## Skills

### cli-creator
Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.curated/cli-creator/SKILL.md`

### imagegen
Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.system/imagegen/SKILL.md`

### netlify-deploy
Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.curated/netlify-deploy/SKILL.md`

### plugin-creator
Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders you can edit before publishing or testing. Use when Codex needs to create a new local plugin, add optional plugin structure, or generate or update repo-root `.agents/plugins/marketplace.json` entries for plugin ordering and availability metadata.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.system/plugin-creator/SKILL.md`

### skill-installer
Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.system/skill-installer/SKILL.md`
