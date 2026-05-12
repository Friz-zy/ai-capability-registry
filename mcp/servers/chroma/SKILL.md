---
name: "chroma-mcp"
description: "No description."
keywords:
  - chroma
---

# Chroma

No description.

## When to use

- Use Chroma only when the task directly involves the relevant service, SaaS product, platform, or technology.

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
    "CHROMA_API_KEY",
    "mcp/chroma"
  ]
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.

## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i -e CHROMA_API_KEY mcp/chroma`.
- Confirm required environment variables before launch: CHROMA_API_KEY.

## References

- https://github.com/chroma-core/chroma-mcp
- https://github.com/docker/mcp-registry/tree/main/servers/chroma

## Security policy

- Authentication: `Environment variables`
