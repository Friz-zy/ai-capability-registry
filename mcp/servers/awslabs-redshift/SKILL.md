---
name: "awslabs-redshift-mcp"
description: "Data warehouse operations and queries."
keywords:
  - awslabs
  - redshift
  - awslabs-redshift
  - amazon
  - aws
  - data
  - operations
---

# Amazon Redshift

Data warehouse operations and queries.

## When to use

- Use Amazon Redshift only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/redshift-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/redshift-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/awslabs-redshift

## Security policy

- Authentication: `Open or unspecified`
