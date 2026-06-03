# Skill Capability Routing

Read `../capability-routing.md` and `skills/skills.md` first.

Use this file only when no registry role, task, or catalog path is assigned and a skill route must be selected.

## Routing Protocol

1. Follow the shared routing pattern in `../capability-routing.md`.
2. Match by task first, then use role only as context or when it disambiguates the request.
3. Read the selected task or role index before keyword catalogs.
4. Select 1-3 specific keywords from matched indexes, preferring exact stack or tool keywords over broad category keywords.
5. Continue selection through `skills/skills.md`.

For an unassigned subagent, this route selects skill catalogs only; it does not change assigned role, workflow, parent instructions, expected outputs, or handoff scope.

### Path Templates

- Role index: `skills/catalog/roles/<role-id>/skills.md`
- Task index: `skills/catalog/tasks/<task-id>/skills.md`
- Keyword catalog: `skills/catalog/keywords/<keyword>/skills.md`

### Roles (category groupings)

{{roles}}

### Tasks (entry points)

{{tasks}}
