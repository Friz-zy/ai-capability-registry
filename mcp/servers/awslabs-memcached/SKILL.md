---
name: "awslabs-memcached-mcp"
description: "High-speed caching with Memcached."
keywords:
  - awslabs
  - memcached
  - awslabs-memcached
  - amazon
  - elasticache
  - aws
---

# Amazon ElastiCache for Memcached

High-speed caching with Memcached.

## When to use

- Use Amazon ElastiCache for Memcached only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/memcached-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/memcached-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/awslabs-memcached

## Security policy

- Authentication: `Open or unspecified`
