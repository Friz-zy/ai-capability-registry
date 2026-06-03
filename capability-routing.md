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
4. **Read matched entries**: when a role, task, keyword, guide, skill, server, or other capability entry matches the request, read it before acting. Do not browse registry directories broadly.
5. **Select specific capabilities**: prefer exact stack, tool, service, product, or artifact matches over broad category matches.
6. **Use selected capabilities**: when a loaded workflow, skill, MCP server, or other capability fits the task, apply it within user, project, safety, and runtime constraints.

## Subagent Scope

If dispatched as a subagent with assigned workflow, role, task, skill, MCP server, or explicit catalog scope, do not restart top-level routing. Follow the parent task instructions and already selected capabilities.

If dispatched as a subagent without assigned registry scope, you may resolve a capability route only for skill or MCP selection. This route does not change your operational role, parent instructions, expected outputs, or handoff scope.
