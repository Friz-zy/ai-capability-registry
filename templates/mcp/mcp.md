# MCP Capability Registry

## MCP Resolution Protocol

1. **Extract intent** - identify the target technology, service, SaaS product, data domain, action type, and sensitivity.
2. **Route by task first** - match the request to one task listed in `mcp.md`; select a second task only for clearly mixed workflows.
3. **Use role as context** - select at most one role listed in `mcp.md` only when it disambiguates service/platform scope.
4. **Read selected indexes only** - open only the matched `mcp/catalog/tasks/<task-id>/servers.md` and optional `mcp/catalog/roles/<role-id>/servers.md`.
5. **Choose keywords** - select 1-3 exact keywords from those indexes; prefer service names over broad domains.
6. **Read keyword catalogs** - open only selected `mcp/catalog/keywords/<keyword>/servers.md` files.
7. **Read server files** - follow `mcp/servers/<server>/SKILL.md`.
8. **Select MCP only if you can work with it** - Select a hosted HTTPS MCP channel only when the current agent can connect to HTTPS through built-in MCP/web tools or approved commands such as `curl`. Select a docker MCP only when the current agent can run docker commands.
9. **Confirm authorization** - if OAuth, API keys, tokens, account access, or workspace access are required, ask the user before connecting.
10. **Connect safely** - use only allowed transport and never hardcode secrets. Use environment variables or vault integration.

## MCP Runtime Instructions

After selecting an MCP server via the resolution protocol above, read the appropriate runtime guide:

- **No prior MCP knowledge**: Only if you don't know about MCP servers, read `mcp/common.md` for general MCP concepts, tool discovery, response handling, and error diagnostics.
- **HTTPS / SSE MCP server**: Read `mcp/web.md` for HTTPS API connection, authentication methods, and health checks.
- **Docker MCP server**: Read `mcp/docker.md` for container naming, lifecycle management, connection, and cleanup.

### Roles (category groupings)

{{roles}}

### Tasks (workflow entry points)

{{tasks}}

## Policy

- Use an MCP server only when the task directly involves its technology, service, SaaS product, or data domain.
- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default. Ask before write operations unless the user explicitly requested them.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- If authentication, OAuth, API keys, tokens, or account access are required, ask the user before connecting or requesting credentials.
- Never expose secret values in prompts, logs, commits, or generated docs.
- Do not use direct `node`, `npx`, `python`, `pip`, or `uvx` MCP runners.