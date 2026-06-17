# Claude Code — Project Instructions Template

> Place this file at `<project-root>/CLAUDE.md`
> Project-specific: `.claude/CLAUDE.md`
> Local overrides (gitignored): `CLAUDE.local.md`

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

## Rules

<!-- Path-scoped rules go in .claude/rules/<name>.md -->

## Notes

- Global instructions: `~/.claude/CLAUDE.md`
- Project instructions: `CLAUDE.md` or `.claude/CLAUDE.md`
- Local overrides: `CLAUDE.local.md` (gitignored)
- Precedence: `.claude/CLAUDE.md` > root `CLAUDE.md` > global `~/.claude/CLAUDE.md`