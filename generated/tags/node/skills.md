# node

## Skills
Load skill and **use it** when task matches.

### build-mcpb
This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb/SKILL.md`

### devcontainer-setup
Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configuring sandboxed Claude Code workspaces.

File: `../external/trailofbits-skills/plugins/devcontainer-setup/skills/devcontainer-setup/SKILL.md`

### figma
Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma nodes into production code. Trigger when a task involves Figma URLs, node IDs, design-to-code implementation, or Figma MCP setup and troubleshooting.

File: `../external/openai-skills/skills/.curated/figma/SKILL.md`

### mcp-builder
Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

File: `../external/anthropic-skills/skills/mcp-builder/SKILL.md`
