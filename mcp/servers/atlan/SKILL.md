---
name: "atlan-mcp"
description: "MCP server for interacting with Atlan services including asset search, updates, and lineage traversal for comprehensive data governance and discovery."
keywords:
  - atlan
  - search
  - comprehensive
  - data
  - discovery
  - governance
---

# Atlan

MCP server for interacting with Atlan services including asset search, updates, and lineage traversal for comprehensive data governance and discovery.

## When to use

- Use Atlan only when the task directly involves the relevant service, SaaS product, platform, or technology.

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
    "ATLAN_API_KEY",
    "-e",
    "ATLAN_BASE_URL",
    "mcp/atlan"
  ]
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.

## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i -e ATLAN_API_KEY -e ATLAN_BASE_URL mcp/atlan`.
- Confirm required environment variables before launch: ATLAN_API_KEY, ATLAN_BASE_URL.

## References

- https://github.com/atlanhq/agent-toolkit
- https://github.com/docker/mcp-registry/tree/main/servers/atlan

## Security policy

- Authentication: `Environment variables`
