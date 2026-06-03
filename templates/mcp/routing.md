# MCP Capability Routing

Read `../capability-routing.md` and `mcp/mcp.md` first.

Use this file only when no registry role, task, or catalog path is assigned and an MCP server route must be selected.

## Routing Protocol

1. Follow the shared routing pattern in `../capability-routing.md`, including service, product, and data-domain sensitivity.
2. Match by task first, then use role only as context or when it disambiguates the request.
3. Read the selected task or role server index before keyword catalogs.
4. Select 1-3 exact keywords from matched indexes, preferring service names over broad domains.
5. Continue selection and safety checks through `mcp/mcp.md`.

For an unassigned subagent, this route selects MCP catalogs only; it does not change assigned role, workflow, parent instructions, expected outputs, or handoff scope.

### Path Templates

- Role index: `mcp/catalog/roles/<role-id>/servers.md`
- Task index: `mcp/catalog/tasks/<task-id>/servers.md`
- Keyword catalog: `mcp/catalog/keywords/<keyword>/servers.md`
- Server guide: `mcp/servers/<server>/SKILL.md`

### Runtime Indexes

{{runtime_catalogs}}

### Roles (category groupings)

{{roles}}

### Tasks (workflow entry points)

{{tasks}}
