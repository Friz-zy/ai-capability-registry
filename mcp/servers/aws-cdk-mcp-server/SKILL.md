---
name: "aws-cdk-mcp-server-mcp"
description: "AWS Cloud Development Kit (CDK) best practices, infrastructure as code patterns, and security compliance with CDK Nag."
keywords:
  - aws
  - cdk
  - aws-cdk
  - security
  - awslabs
  - code
  - compliance
  - development
---

# AWS CDK

AWS Cloud Development Kit (CDK) best practices, infrastructure as code patterns, and security compliance with CDK Nag.

## When to use

- Use AWS CDK only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/aws-cdk-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/aws-cdk-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/aws-cdk-mcp-server

## Security policy

- Trust: `reviewed`
- Default mode: `manual_review`
- Permission default: `manual_review`
- Authentication: `Unspecified in source metadata`
- **Warning:** Default mode is `manual_review`.
- **Warning:** Permission default is `manual_review`.
- **Required posture:** Complete manual review before connecting or invoking tools; this generated record does not grant approval.
