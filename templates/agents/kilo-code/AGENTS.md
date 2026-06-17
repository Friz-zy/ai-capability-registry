# Kilo Code — Project Instructions Template

> Place this file at `<project-root>/AGENTS.md`
> Global instructions go in the `instructions` key of kilo.jsonc.
> Per-directory AGENTS.md files are also supported (hierarchical).

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

<!-- Any security-sensitive areas the agent must handle carefully -->

## Notes

- Global config: `~/.config/kilo/kilo.jsonc`
- Project config: `kilo.jsonc` or `.kilo/kilo.jsonc`
- Global agents: `~/.config/kilo/agent/<name>.md`
- Project agents: `.kilo/agent/<name>.md`
- Precedence: agent.prompt > config instructions > AGENTS.md
- Env vars: `KILO_CONFIG`, `KILO_CONFIG_CONTENT`