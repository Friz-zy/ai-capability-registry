# Workflow Capability Routing

Read `../capability-routing.md`, `workflow.md`, and `../roles/orchestrator.md` before selecting a workflow.

Use this file only for primary-agent workflow selection when no workflow scope is assigned.

## Routing Protocol

1. Follow the shared routing pattern in `../capability-routing.md`.
2. Match by task first, then role, category, and tags.
3. Read only the selected workflow markdown guide and YAML manifest.
4. If no workflow applies, state that and follow the no-workflow fallback in `workflow.md`.

Do not browse workflow directories broadly. Use the smallest matching index, then read only the selected workflow guide and manifest.

Generated narrow indexes may exist under these paths:

- `workflows/catalog/tasks/<task-id>/workflows.md`
- `workflows/catalog/roles/<role-id>/workflows.md`
- `workflows/catalog/categories/<category>/workflows.md`
- `workflows/catalog/tags/<tag>/workflows.md`

Use a catalog index when it gives a narrower view than this dispatcher. The manifest remains the source for stage order, roles, outputs, gates, and acceptance criteria.

## Workflows

{{workflows}}

All other roles and tasks have no workflow unless another registry entry adds one.
