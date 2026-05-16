# MCP Capability Registry

Read `../capability-routing.md` first. This file defines MCP-specific routing and safety rules.

## MCP Sources

MCP servers may be agent-native or registry-indexed. Treat both as one capability pool. Prefer an already-connected trusted or reviewed native server when equivalent; otherwise use this registry's catalogs and referenced server instructions. Do not assume both sources mirror each other.

## MCP Resolution Protocol

1. Follow the shared routing pattern in `../capability-routing.md`, including service/product/data-domain sensitivity.
2. If a task or role matches, read its server index before acting.
3. Select 1-3 exact keywords from matched indexes, preferring service names over broad domains.
4. If a keyword matches, read `mcp/catalog/keywords/<keyword>/servers.md` before acting.
5. If a server matches, read its `mcp/servers/<server>/SKILL.md` before acting.
6. Use a matched server only when it directly fits the task and transport is available: hosted HTTPS through built-in MCP/web tools or approved commands such as `curl`, Docker only when Docker commands are available.
7. Ask before OAuth, API keys, tokens, account access, workspace access, private data access, or remote mutation.
8. Connect safely using allowed transport and environment variables or vault integration; never hardcode secrets.

## MCP Runtime Instructions

After selecting an MCP server, read the runtime guide that matches the transport:

- `mcp/common.md`: only when MCP concepts, tool discovery, response handling, or error diagnostics are unknown.
- `mcp/web.md`: HTTPS/SSE API connection, authentication methods, and health checks.
- `mcp/docker.md`: container naming, lifecycle management, connection, and cleanup.

### Path Templates

- Role index: `mcp/catalog/roles/<role-id>/servers.md`
- Task index: `mcp/catalog/tasks/<task-id>/servers.md`
- Keyword catalog: `mcp/catalog/keywords/<keyword>/servers.md`
- Server guide: `mcp/servers/<server>/SKILL.md`

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
