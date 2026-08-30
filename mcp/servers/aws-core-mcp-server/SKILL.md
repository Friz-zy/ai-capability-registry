---
name: "aws-core-mcp-server-mcp"
description: "Starting point for using the awslabs MCP servers."
keywords:
  - aws
  - core
  - aws-core
  - awslabs
---

# AWS Core

Starting point for using the awslabs MCP servers.

## When to use

- Use AWS Core only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/aws-core-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/aws-core-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/aws-core-mcp-server

## Security policy

- Trust: `reviewed`
- Default mode: `manual_review`
- Permission default: `manual_review`
- Authentication: `Unspecified in source metadata`
- **Warning:** Default mode is `manual_review`.
- **Warning:** Permission default is `manual_review`.
- **Required posture:** Complete manual review before connecting or invoking tools; this generated record does not grant approval.
