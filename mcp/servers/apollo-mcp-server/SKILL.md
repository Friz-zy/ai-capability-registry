---
name: "apollo-mcp-server-mcp"
description: "Enable graph-based API orchestration with AI"
keywords:
  - apollo
  - ai
---

# Apollo

Enable graph-based API orchestration with AI

## When to use

- Use Apollo only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "ghcr.io/apollographql/apollo-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i ghcr.io/apollographql/apollo-mcp-server`.

## References

- https://github.com/apollographql/apollo-mcp-server
- https://github.com/docker/mcp-registry/tree/main/servers/apollo-mcp-server

## Security policy

- Trust: `reviewed`
- Default mode: `manual_review`
- Permission default: `manual_review`
- Authentication: `Unspecified in source metadata`
- **Warning:** Default mode is `manual_review`.
- **Warning:** Permission default is `manual_review`.
- **Required posture:** Complete manual review before connecting or invoking tools; this generated record does not grant approval.
