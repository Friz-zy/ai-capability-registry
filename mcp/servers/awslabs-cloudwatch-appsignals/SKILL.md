---
name: "awslabs-cloudwatch-appsignals-mcp"
description: "Application performance monitoring and insights."
keywords:
  - awslabs
  - cloudwatch
  - appsignals
  - awslabs-cloudwatch-appsignals
  - amazon
  - signals
  - aws
  - insights
  - monitoring
---

# Amazon CloudWatch Application Signals

Application performance monitoring and insights.

## When to use

- Use Amazon CloudWatch Application Signals only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/cloudwatch-appsignals-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/cloudwatch-appsignals-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/awslabs-cloudwatch-appsignals

## Security policy

- Authentication: `Open or unspecified`
