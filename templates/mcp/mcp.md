# MCP Capability Registry

## MCP Resolution Protocol

Before connecting an MCP server, resolve it with progressive disclosure:

1. **Extract intent** - identify the target technology, service, SaaS product, data domain, action type, and sensitivity.
2. **Route by task first** - match the request to one task listed in `mcp.md`; select a second task only for clearly mixed workflows.
3. **Use role as context** - select at most one role listed in `mcp.md` only when it disambiguates service/platform scope.
4. **Read selected indexes only** - open only the matched `mcp/catalog/tasks/<task-id>/servers.md` and optional `mcp/catalog/roles/<role-id>/servers.md`.
5. **Choose keywords** - select 1-3 exact keywords from those indexes; prefer service names over broad domains.
6. **Read keyword catalogs** - open only selected `mcp/catalog/keywords/<keyword>/servers.md` files.
7. **Read server files** - follow `mcp/servers/<server>/SKILL.md`.
8. **Confirm authorization** - if OAuth, API keys, tokens, account access, or workspace access are required, ask the user before connecting.
9. **Connect safely** - use only allowed transport and never hardcode secrets. Use environment variables or vault integration.

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
- Use only public HTTPS endpoints or Docker stdio commands that start with `docker run --rm`.
- Select a hosted HTTPS MCP channel only when the current agent can connect to HTTPS through built-in MCP/web tools or approved commands such as `curl`.
- Select a Docker stdio MCP channel only when the current agent can run Docker commands in the current environment.
- Do not use direct `node`, `npx`, `python`, `pip`, or `uvx` MCP runners.
- For Docker servers, launch only through the generated `docker run --rm ...` command. Confirm required environment variables before launching the container.
- For Docker stdio mode, keep stdin attached with `-i` and run the container in the foreground; do not use detached mode (`-d`) for stdio MCP servers.
- Give MCP docker containers clear names such as `mcp-<server-id>` when a named container is needed, so running containers can be identified safely.
- Before starting a Docker MCP container, check `docker ps` for an existing matching MCP container and reuse it when the server supports stdio attach/exec; otherwise start a fresh generated stdio command.
- Stop or remove Docker MCP containers you started at the end of the session unless they were already running before the session or the user explicitly asks to keep them.
- Do not use unsafe Docker options for MCP servers, including `--privileged`, host filesystem mounts such as `-v /:/host` or `--mount type=bind,source=/`, host networking with `--network host`, or mounting sensitive paths like `/var/run/docker.sock`, `~/.ssh`, or cloud credential directories.
