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

- Trust: `reviewed`
- Default mode: `manual_review`
- Permission default: `manual_review`
- Authentication: `Unspecified in source metadata`
- **Warning:** Default mode is `manual_review`.
- **Warning:** Permission default is `manual_review`.
- **Required posture:** Complete manual review before connecting or invoking tools; this generated record does not grant approval.
