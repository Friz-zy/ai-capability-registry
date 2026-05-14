# Capability Routing Protocol

Use this protocol before selecting workflows, skills, or MCP servers from this registry.

## Instruction Priority

When instructions conflict, use this priority order:

1. **User and project instructions**: direct user requests, `AGENTS.md`, local repo rules, and explicit constraints.
2. **Selected workflows and process skills**: task-level guidance for how to approach the work.
3. **Selected implementation and domain skills**: technology, tool, and artifact-specific execution guidance.
4. **Generic agent behavior**: fallback behavior only when no more specific instruction applies.

Process guidance determines how to approach the task; implementation guidance determines how to execute it.

## Routing Pattern

For each capability registry:

1. **Extract intent**: identify action, domain, stack/tool/service, artifact, constraints, likely task, and optional role.
2. **Route by task first**: match one task; select a second task only for clearly mixed requests.
3. **Use role as context**: select at most one role only when the user asks from that role perspective or it disambiguates routing.
4. **Read selected entries only**: open only matched indexes, catalogs, guides, or server files. Do not browse registry directories broadly.
5. **Select specific capabilities**: prefer exact stack, tool, service, product, or artifact matches over broad category matches.
6. **Apply loaded guidance**: follow selected instructions within user, project, safety, and runtime constraints.

## Subagent Scope

If dispatched as a subagent, do not restart top-level routing. Follow the parent task instructions and already selected workflows, skills, or MCP servers. Resolve more capabilities only when directly needed for the assigned subtask.
