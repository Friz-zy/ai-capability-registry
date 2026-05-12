---
name: "redis-mcp"
description: "Access to Redis database operations."
keywords:
  - redis
  - database
  - access
  - operations
---

# Redis

Access to Redis database operations.

## When to use

- Use Redis only when the task directly involves the relevant service, SaaS product, platform, or technology.

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
    "REDIS_PWD",
    "mcp/redis"
  ]
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.

## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i -e REDIS_PWD mcp/redis`.
- Confirm required environment variables before launch: REDIS_PWD.

## References

- https://github.com/redis/mcp-redis
- https://github.com/docker/mcp-registry/tree/main/servers/redis

## Security policy

- Authentication: `Environment variables`
