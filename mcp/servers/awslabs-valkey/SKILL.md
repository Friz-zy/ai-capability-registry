---
name: "awslabs-valkey-mcp"
description: "Advanced data structures with Valkey."
keywords:
  - awslabs
  - valkey
  - awslabs-valkey
  - amazon
  - elasticache
  - aws
  - data
---

# Amazon ElastiCache/MemoryDB for Valkey

Advanced data structures with Valkey.

## When to use

- Use Amazon ElastiCache/MemoryDB for Valkey only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/valkey-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/valkey-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/awslabs-valkey

## Security policy

- Trust: `reviewed`
- Default mode: `manual_review`
- Permission default: `manual_review`
- Authentication: `Unspecified in source metadata`
- **Warning:** Default mode is `manual_review`.
- **Warning:** Permission default is `manual_review`.
- **Required posture:** Complete manual review before connecting or invoking tools; this generated record does not grant approval.
