---
name: "awslabs-billing-cost-management-mcp"
description: "Billing and cost management."
keywords:
  - awslabs
  - billing
  - cost
  - awslabs-billing-cost
  - aws
  - management
---

# AWS Billing and Cost Management

Billing and cost management.

## When to use

- Use AWS Billing and Cost Management only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/billing-cost-management-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/billing-cost-management-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/awslabs-billing-cost-management

## Security policy

- Authentication: `Open or unspecified`
