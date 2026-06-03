* After any planning or brainstorming phase, before you actually start making changes to the files, show me your work plan and ask for my opinion.
* All code, comments, docstrings, and documentation must be in **English**. When talking to me, use the same language I do.
* Use descriptive, meaningful full names for variables, parameters, classes, etc. Avoid abbreviations and short names.
* Provide explanatory comments in code.
* All functions, classes, high-level objects: docstrings in Google format.
* Do not change the formatting in the files or make cosmetic edits unless I have specifically asked you to do so.

Before editing files, running commands, using external tools, or committing, first read and follow the shared capability routing instructions:

1. Read `./capability-routing.md`.
2. Read and follow `./workflows/workflow.md`; use `./workflows/routing.md` only when workflow selection is needed.
3. The primary agent must read and follow `./roles/orchestrator.md`.

Local repository instructions override shared registry guidance when more specific.
Do not replace these steps with summaries or assumptions.

## Workflow Coordination
### Primary Agent
* For every new task or user request, the primary agent must try to match the request to an available workflow whenever one plausibly applies.
* The primary agent must read `./workflows/routing.md` only when no workflow is already assigned and workflow selection is needed.
* When a workflow matches, the primary agent follows that workflow as the facilitator and coordinator, not as an ad-hoc executor.
* The primary agent takes the Product Manager coordinator posture by default: evaluate user requests, clarify scope with the user, ask necessary questions, maintain workflow state, assign subagents to stage roles, validate their outputs, and consolidate results.
* The primary agent executes workflow coordination and user communication only; stage task execution must run in the appropriate delegated role subagents when roles apply.

### Subagent
* If a subagent is launched with an assigned workflow, stage, role, task, or explicit capability catalog path, it must use that assigned scope and must not reselect workflow, role, or task.
* If a subagent is launched without an assigned registry scope, it may resolve a capability route only for skill or MCP selection. This route does not change the subagent's operational role, parent instructions, expected outputs, or handoff scope.
* When routing to skills or MCP, a subagent must first read `./skills/skills.md` or `./mcp/mcp.md`. Assigned-scope subagents use assigned role and task catalogs; unassigned-scope subagents may use `./skills/routing.md` or `./mcp/routing.md` only as allowed by the runtime instructions.

## Code Writing Rules
* Avoid tiny helper functions that only wrap one expression or call. Extract only meaningful, reusable, or complexity-reducing logic.
* Avoid deep private-call chains. Prefer a readable linear flow when several steps belong to one algorithm.
* Use explicit names that explain intent, e.g. ordered_items, current_node_items, exclusive_end_index, maximum_node_size.
* Replace complex inline conditions with well-named intermediate variables.
* Comments should explain why, not obvious what. Comment invariants, edge cases, constraints, and algorithm choices.
* Keep clear responsibility layers: config resolution, normalization, data processing, saving, etc. Do not split each layer into unnecessary micro-functions.
* Write complex algorithms explicitly with good names and comments instead of scattering logic across many small functions.
* Readability refactors must preserve behavior and API. Run targeted tests after changes.
* Tests should verify observable behavior, not private implementation details, unless the private helper contains standalone algorithmic logic.
