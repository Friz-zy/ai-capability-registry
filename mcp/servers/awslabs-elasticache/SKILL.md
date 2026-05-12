---
name: "awslabs-elasticache-mcp"
description: "ElastiCache control plane operations."
keywords:
  - awslabs
  - elasticache
  - awslabs-elasticache
  - amazon
  - aws
  - control
  - operations
  - plane
---

# Amazon ElastiCache

ElastiCache control plane operations.

## When to use

- Use Amazon ElastiCache only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/elasticache-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/elasticache-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/awslabs-elasticache

## Security policy

- Authentication: `Open or unspecified`
