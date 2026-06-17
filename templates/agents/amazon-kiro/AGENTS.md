# Amazon Kiro — Project Instructions Template

> Place this file at `<project-root>/AGENTS.md`
> Steering files go in `.kiro/steering/<name>.md` (project)
> or `~/.kiro/steering/<name>.md` (global)
> AGENTS.md is always active (equivalent to `mode: always`).

## Project Overview

<!-- Describe your project briefly -->

## Code Style

<!-- Language conventions, formatting rules -->

## Testing

<!-- How to run tests, coverage expectations -->

## Architecture

<!-- Key directories, module boundaries -->

## Key Decisions

<!-- Architectural or product decisions the agent should respect -->

## Security

<!-- Any security-sensitive areas the agent should handle carefully -->

## Steering Modes

Kiro supports four steering modes:

- **always**: Always loaded into context (use for critical rules)
- **conditional**: Loaded when matching glob patterns (e.g., `condition: "*.ts"`)
- **manual**: Only loaded when referenced by `#name`
- **auto**: Loaded when description matches the user prompt

## Notes

- Global steering: `~/.kiro/steering/<name>.md`
- Project steering: `.kiro/steering/<name>.md`
- Global agents: `~/.kiro/agents/<name>.json`
- Project agents: `.kiro/agents/<name>.json`
- MCP config: `.kiro/settings/mcp.json` (project) or `~/.kiro/settings/mcp.json` (global)
- AGENTS.md = always active (no mode needed)
- Precedence: workspace steering > global steering; AGENTS.md always loaded