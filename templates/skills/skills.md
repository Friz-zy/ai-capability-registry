# AI Capability Registry

Read `../capability-routing.md` first. This file defines skill-specific routing.

## Skill Sources

Skills may be agent-native or registry-indexed. Treat both as one capability pool. Prefer an already-available trusted native skill when equivalent; otherwise use this registry's catalogs and read the referenced `SKILL.md`. Do not assume both sources mirror each other.

## Skill Resolution Protocol

Before starting work, resolve skills from both agent-native skills and this registry with progressive disclosure:

1. Follow the shared routing pattern in `../capability-routing.md`.
2. If a task or role matches, read its index before acting.
3. Select 1-3 specific keywords from matched indexes, preferring exact stack/tool keywords over broad category keywords.
4. If a keyword matches, read `skills/catalog/keywords/<keyword>/skills.md` before acting.
5. Choose 1-3 best matching skill descriptions per keyword.
6. If a skill matches, read its `SKILL.md` and use it within project conventions.

### Routing Scope

Paths in keyword catalogs are relative to this registry root.
`external/` is a sibling of the root `skills/` directory at `<registry-root>/external/`; do not look for it under `skills/external/`.

Use `skills/catalog/` only for skill selection.
Use `skills/packs/` only when configuring agents with preselected skill directories.
Do not browse `skills/catalog/` or `skills/packs/` broadly during task execution.

### Path Templates

- Role index: `skills/catalog/roles/<role-id>/skills.md`
- Task index: `skills/catalog/tasks/<task-id>/skills.md`
- Keyword catalog: `skills/catalog/keywords/<keyword>/skills.md`

### Roles (category groupings)

{{roles}}

### Tasks (entry points)

{{tasks}}

## Policy

- Use trusted or reviewed skill sources only.
- Never execute untrusted scripts.
