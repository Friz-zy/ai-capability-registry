# integration

## Skills
Select only the most relevant skills by description, then read only those `SKILL.md` files.

### add-remote-skill
This skill should be used when the user wants to add one or more skills from GitHub repositories to the kilo-marketplace. It handles parsing GitHub URLs, cloning skill directories, and updating SKILL.md frontmatter with source metadata.

File: `external/kilo-marketplace-skills/.kilocode/skills/add-remote-skill/SKILL.md`

### chatgpt-apps
Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold. Prefer a docs-first workflow by invoking the openai-docs skill or OpenAI developer docs MCP tools before generating code.

File: `external/openai-skills/skills/.curated/chatgpt-apps/SKILL.md`

### cli-creator
Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

File: `external/openai-skills/skills/.curated/cli-creator/SKILL.md`

### cowork-plugin-customizer
Customize a Claude Code plugin for a specific organization's tools and workflows. Use when: customize plugin, set up plugin, configure plugin, tailor plugin, adjust plugin settings, customize plugin connectors, customize plugin skill, tweak plugin, modify plugin configuration.

File: `external/anthropic-knowledge-work-plugins/cowork-plugin-management/skills/cowork-plugin-customizer/SKILL.md`

### create-cowork-plugin
Guide users through creating a new plugin from scratch in a cowork session. Use when users want to create a plugin, build a plugin, make a new plugin, develop a plugin, scaffold a plugin, start a plugin from scratch, or design a plugin. This skill requires Cowork mode with access to the outputs directory for delivering the final .plugin file.

File: `external/anthropic-knowledge-work-plugins/cowork-plugin-management/skills/create-cowork-plugin/SKILL.md`

### mcp-builder
Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

File: `external/anthropic-skills/skills/mcp-builder/SKILL.md`

### ossfuzz
OSS-Fuzz provides free continuous fuzzing for open source projects. Use when setting up continuous fuzzing infrastructure or enrolling projects.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/ossfuzz/SKILL.md`

### skill-share
A skill that creates new agent skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery.

File: `external/kilo-marketplace-skills/skills/skill-share/SKILL.md`
