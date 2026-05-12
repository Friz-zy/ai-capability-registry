---
name: "awslabs-cloudwatch-mcp"
description: "Metrics, alarms, and logs analysis."
keywords:
  - awslabs
  - cloudwatch
  - awslabs-cloudwatch
  - metrics
  - amazon
  - analysis
  - aws
---

# Amazon CloudWatch

Metrics, alarms, and logs analysis.

## When to use

- Use Amazon CloudWatch only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/cloudwatch-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/cloudwatch-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/awslabs-cloudwatch

## Security policy

- Authentication: `Open or unspecified`
