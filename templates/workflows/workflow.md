# Workflow Runtime Instructions

## Follow these instructions if you are the user-facing Primary Agent

1. Follow `../capability-routing.md` and `../roles/orchestrator.md`.
2. Read `routing.md` when no workflow is already assigned, then match by task first, then role, category, and tags.
3. Read only the selected workflow markdown guide and YAML manifest.
4. Follow the workflow instructions.
5. Delegate each stage to subagents assigned a role from `../roles/`. Include expected outputs, acceptance criteria, and handoff instructions; each subagent MUST read `../roles/<role-id>.md`.
6. Validate gates before advancing, request targeted revisions when needed, and resolve role conflicts through the YAML manifest.
7. Communicate with the user, including needed clarifications and consolidated results.
8. If no workflow applies, state that and continue with ordinary task handling.

## Follow these instructions if you are a delegated Subagent

Subagents MUST stay within the workflow, stage, role, task, expected outputs, acceptance criteria, and handoff instructions assigned by the primary agent.

A workflow-delegated subagent may route to skills through `../skills/skills.md` or MCP through `../mcp/mcp.md` only within its assigned role and task scope. It MUST NOT reselect workflow, role, or task unless reassigned by the primary agent.
