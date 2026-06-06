Before resolving `~/` or `$HOME`, discover the actual home directory from the environment instead of assuming `/root/`.

## Follow these instructions if you are the user-facing Primary Agent

Read and apply the shared workflow runtime file listed below before acting:

1. `~/.ai-registry/workflows/workflow.md`

Then perform workflow capability routing before acting:

* Decide whether a workflow applies.
* If a workflow applies, follow the selected workflow.
* If no workflow applies, explicitly use the no-workflow fallback from `~/.ai-registry/workflows/workflow.md`.

For trivial conversational requests, still obey the registry files, but no workflow delegation is required unless the routing instructions require it.

## Mandatory Registry Bootstrap

Before any substantive response, tool use, planning, analysis, implementation, review, or command execution, read and apply the shared registry runtime files listed below in order:

1. `~/.ai-registry/capability-routing.md`
2. `~/.ai-registry/skills/skills.md`

This bootstrap is mandatory when these files are listed. Do not rely on memory, prior summaries, or assumptions about their contents.

After reading them, perform skill capability routing before acting:

* Select skills only according to `~/.ai-registry/skills/skills.md`.
* Do not dynamically route to MCP servers unless local instructions separately enable MCP routing.

Local repository instructions override shared registry guidance when more specific.
These shared registry files are the source of truth. Do not replace them with summaries or assumptions.
If `~/.ai-registry` is unavailable, state that and continue with local instructions only.

## Common Rules
* After any planning or brainstorming phase, before you actually start making changes to the files, show me your work plan and ask for my opinion.
* All code, comments, docstrings, and documentation must be in **English**. When talking to me, use the same language I do.
* Use descriptive, meaningful full names for variables, parameters, classes, etc. Avoid abbreviations and short names.
* Provide explanatory comments in code.
* All functions, classes, high-level objects: docstrings in Google format.
* Do not change the formatting in the files or make cosmetic edits unless I have specifically asked you to do so.

## Registry Source Of Truth

* Define roles, workflows, tasks, skills, MCP servers, tags, categories, and routing metadata in `registry/*.yaml` first.
* Treat generated runtime files under `roles/`, `workflows/`, `skills/catalog/`, `skills/packs/`, `mcp/`, and root catalog files as generator outputs.
* After changing registry source files, run the existing generator scripts instead of manually maintaining generated catalogs.

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
