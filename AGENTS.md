* After any planning or brainstorming phase, before you actually start making changes to the files, show me your work plan and ask for my opinion.
* All code, comments, docstrings, and documentation must be in **English**. When talking to me, use the same language I do.
* Use descriptive, meaningful full names for variables, parameters, classes, etc. Avoid abbreviations and short names.
* Provide explanatory comments in code.
* All functions, classes, high-level objects: docstrings in Google format.
* Do not change the formatting in the files or make cosmetic edits unless I have specifically asked you to do so.

Before editing files, running commands, using external tools, or committing, first read and follow the shared capability routing instructions:

1. Read `./capability-routing.md`.
2. Read and follow `./workflows/workflow.md`.

Local repository instructions override shared registry guidance when more specific.
Do not replace these steps with summaries or assumptions.

## Workflow Coordination
* For every new task or user request, the primary agent must try to match the request to an available workflow whenever one plausibly applies.
* When a workflow matches, the primary agent follows that workflow as the facilitator and coordinator, not as an ad-hoc executor.
* The primary agent takes the Product Manager coordinator posture by default: clarify scope with the user, ask necessary questions, maintain workflow state, assign subagents to stage roles, validate their outputs, and consolidate results.
* A subagent must not select its own workflow or role. It must follow the workflow id, stage id, role id, task, expected outputs, acceptance criteria, and handoff instructions assigned by the primary agent.
* A subagent may route to skills and MCP only within its assigned role and task scope. It must not restart top-level routing, replace the selected workflow, promote itself to coordinator, or choose a different role unless reassigned by the primary agent.

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
