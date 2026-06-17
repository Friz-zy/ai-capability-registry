---
description: >
  Template slash command for Claude Code.
  Replace with a description of what this command does.
argument-hint: "[arg1] [arg2]"
allowed-tools:
  - Read
  - Bash(git:*)
model: sonnet
---

# Command Title

You are executing the `$COMMAND_NAME` command.

## Arguments

- $1: [description of first argument]
- $2: [description of second argument]
- $ARGUMENTS: [all arguments as a string]

## Instructions

1. Step-by-step instructions for what the command should do.
2. Use @path/to/file to reference files in the prompt.
3. Use !`command here` for shell execution within the prompt.

## Output

Describe the expected output format.

## Notes

- Command directory: `.claude/commands/<command-name>.md` (project)
  or `~/.claude/commands/<command-name>.md` (global)
- The filename (sans .md) becomes the command name: `/project:<command-name>`
- Global commands are available as: `/user:<command-name>`