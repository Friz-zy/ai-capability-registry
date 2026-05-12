---
name: "awslabs-cloudtrail-mcp"
description: "AWS CloudTrail audit logging and monitoring."
keywords:
  - awslabs
  - cloudtrail
  - awslabs-cloudtrail
  - aws
  - audit
  - monitoring
---

# AWS CloudTrail

AWS CloudTrail audit logging and monitoring.

## When to use

- Use AWS CloudTrail only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/cloudtrail-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/cloudtrail-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/awslabs-cloudtrail

## Security policy

- Authentication: `Open or unspecified`
