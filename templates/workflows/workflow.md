# Workflow Runtime Instructions

## Follow these instructions if you are the user-facing Primary Agent

1. Follow `../capability-routing.md` and `../roles/orchestrator.md`.
2. Read `routing.md` when no workflow is already assigned, then match by task first, then role, category, and tags.
3. Read only the selected workflow markdown guide and YAML manifest.
4. Follow the workflow instructions.
5. Delegate each stage to subagents assigned a role selected from the role catalog in `../roles/roles.md`; do not list the `../roles/` directory to discover roles. Include expected outputs, acceptance criteria, and handoff instructions; each subagent MUST read `../roles/<role-id>.md`, assume that role, and follow its instructions.
6. Validate gates before advancing, request targeted revisions when needed, and resolve role conflicts through the YAML manifest.
7. Communicate with the user, including needed clarifications and consolidated results.
8. If no workflow applies, follow the no-workflow fallback below.

## No-Workflow Fallback

Use this protocol when `../capability-routing.md` or `routing.md` cannot be read, or when no workflow matches.

1. You MUST state that workflow routing is unavailable or that no workflow applies.
2. Handle simple, single-domain, low-risk requests directly without delegation.
3. For ambiguous or underspecified work, ask only the minimum blocking clarification; otherwise state assumptions and proceed.
4. For non-trivial work, create a short plan with goal, scope, likely files or areas, ordered tasks, acceptance criteria, and validation commands when known.
5. Break large work into independently testable tasks, dispatch fresh subagents when delegation helps, parallelize only independent tasks, and make every subagent prompt self-contained.
6. Use `middle` for clear implementation, `senior` for complex integration/debugging/review, and `lead` for architecture or high-impact decisions.
7. When implementation is assigned to `middle`, the quality gate MUST be assigned to `senior` or `lead`.
8. After delegated implementation, run a read-only quality gate that checks acceptance/spec compliance first, then code quality and maintainability.
9. If a subagent needs context or is blocked, provide context, raise the role level, split the task, or stop and report the blocker.
10. Never accept incomplete work when acceptance criteria or quality gates fail.

## Follow these instructions if you are a delegated Subagent

Subagents MUST stay within the workflow, stage, role, task, expected outputs, acceptance criteria, and handoff instructions assigned by the primary agent.

A workflow-delegated subagent may route to skills through `../skills/skills.md` or MCP through `../mcp/mcp.md` only within its assigned role and task scope. It MUST NOT reselect workflow, role, or task unless reassigned by the primary agent.
