---
name: "awslabs-dynamodb-mcp"
description: "Complete DynamoDB operations and table management."
keywords:
  - awslabs
  - dynamodb
  - awslabs-dynamodb
  - amazon
  - aws
  - management
  - operations
---

# Amazon DynamoDB

Complete DynamoDB operations and table management.

## When to use

- Use Amazon DynamoDB only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/dynamodb-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/dynamodb-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/awslabs-dynamodb

## Security policy

- Authentication: `Open or unspecified`
