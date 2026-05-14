# Workflow Capability Registry

## Instruction Priority

When instructions conflict, use this priority order:

1. **User and project instructions** - direct user requests, `AGENTS.md`, local repo rules, and explicit constraints have highest priority.
2. **Selected workflows and process skills** - loaded workflow guidance defines how to approach the task when it matches.
3. **Selected implementation and domain skills** - loaded technology, tool, and artifact-specific guidance shapes execution.
4. **Generic agent behavior** - use only when no more specific instruction applies.

Prefer workflows and process skills before implementation and domain skills. Process guidance determines how to approach the task; implementation guidance determines how to execute it.

## Workflow Resolution Protocol

Before ordinary skill routing, decide whether a workflow applies by task first and role second:

1. **Extract intent** - identify action, domain, stack/tool, artifact, constraints, likely task, and optional role.
2. **Match task first** - match the request to one Task below; select a second Task only for clearly mixed requests.
3. **Use role as context** - select at most one Role below only when the user asks from that role perspective or it disambiguates the process.
4. **Read selected workflow guides** - read only the guide files for workflows matched by the selected task or role.
5. **Apply workflow guidance** - use the workflow to choose relevant process skills before implementation skills.
6. **Continue capability routing** - after workflow selection, resolve concrete skills through `skills/skills.md` and MCP servers through `mcp/mcp.md` when those entrypoints are available.

Read only workflow files that match the current task or role. Do not browse `workflows/` broadly.

### Subagent Scope

If you were dispatched as a subagent to execute a specific task, do not restart top-level workflow resolution. Follow the parent task instructions and any workflow or skill choices already provided.

Resolve additional workflows or skills only when they are directly needed for the assigned subtask.

### Skill Use Requirement

If a trusted or reviewed workflow or process skill plausibly matches the task after routing, use it before acting. Do not skip it because the task looks simple, because you want to inspect files first, or because the workflow feels like overhead.

If the loaded skill does not actually fit the task, stop using it and continue with the next best match.

## Roles

{{roles}}

## Tasks

{{tasks}}

## Workflows

{{workflows}}
