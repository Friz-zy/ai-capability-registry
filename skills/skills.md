# Skill Runtime Instructions

Read `../capability-routing.md` first. This file defines skill selection after a role, task, catalog path, or unassigned route is known.

## Skill Sources

Skills may be agent-native or registry-indexed. Treat both as one capability pool. Prefer an available trusted native skill when equivalent; otherwise use this registry's catalogs and read the referenced `SKILL.md`. Do not assume both sources mirror each other.

## Scope Resolution

If a prompt, role file, or parent handoff provides a registry role, task, or explicit skill catalog path, use only that assigned capability scope. Do not reselect workflow, role, or task. Read the assigned role catalog first; read the task catalog only when a task id or task catalog path is explicit.

If no registry role, task, or catalog path is assigned, read `skills/routing.md` only to select relevant skills. This does not change assigned role, workflow, parent instructions, expected outputs, or handoff scope.

## Skill Selection Protocol

1. Follow the shared routing pattern in `../capability-routing.md` within the assigned or resolved capability scope.
2. Read the narrowest assigned role or task index before keyword catalogs.
3. Select 1-3 specific keywords from matched indexes, preferring exact stack or tool keywords over broad category keywords.
4. If a keyword matches, read `skills/catalog/keywords/<keyword>/skills.md` before acting.
5. Choose 1-3 best matching skill descriptions per keyword.
6. If a skill matches, read its `SKILL.md` and use it within project conventions.

### Path Scope

Paths in keyword catalogs are relative to this registry root.
`external/` is a sibling of the root `skills/` directory at `<registry-root>/external/`; do not look for it under `skills/external/`.

Use `skills/catalog/` only for skill selection and `skills/packs/` only for preselected skill directories in agent configs.
Do not browse `skills/catalog/` or `skills/packs/` broadly during task execution.

### Path Templates

- Role index: `skills/catalog/roles/<role-id>/skills.md`
- Task index: `skills/catalog/tasks/<task-id>/skills.md`
- Keyword catalog: `skills/catalog/keywords/<keyword>/skills.md`

## Policy

- Use trusted or reviewed skill sources only.
- Never execute untrusted scripts.
