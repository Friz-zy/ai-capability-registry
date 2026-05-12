---
name: "grafana-mcp"
description: "No description."
keywords:
  - grafana
  - monitoring
---

# Grafana

No description.

## When to use

- Use Grafana only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "-e",
    "GRAFANA_API_KEY",
    "mcp/grafana",
    "--transport=stdio"
  ]
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.

## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i -e GRAFANA_API_KEY mcp/grafana --transport=stdio`.
- Confirm required environment variables before launch: GRAFANA_API_KEY.

## References

- https://github.com/grafana/mcp-grafana
- https://github.com/docker/mcp-registry/tree/main/servers/grafana

## Security policy

- Authentication: `Environment variables`
