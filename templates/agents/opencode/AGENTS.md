# OpenCode — Project Instructions Template

> Place this file at `<project-root>/AGENTS.md`
> Config instructions go in the `instructions` key of opencode.json.

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

## Notes

- Global config: `~/.config/opencode/opencode.json`
- Project config: `opencode.json` or `.opencode/opencode.json`
- Global agents: `~/.config/opencode/agents/<name>.md`
- Project agents: `.opencode/agents/<name>.md`
- Precedence: agent.prompt > config instructions > AGENTS.md
- Env vars: `OPENCODE_CONFIG`, `OPENCODE_CONFIG_CONTENT`, `OPENCODE_CONFIG_DIR`
- Schema: `https://opencode.ai/config.json`