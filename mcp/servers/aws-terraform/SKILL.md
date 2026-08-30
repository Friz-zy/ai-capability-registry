---
name: "aws-terraform-mcp"
description: "Terraform on AWS best practices, infrastructure as code patterns, and security compliance with Checkov"
keywords:
  - aws
  - terraform
  - aws-terraform
  - security
  - awslabs
  - code
  - compliance
---

# AWS Terraform

Terraform on AWS best practices, infrastructure as code patterns, and security compliance with Checkov

## When to use

- Use AWS Terraform only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/aws-terraform"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/aws-terraform`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/aws-terraform

## Security policy

- Trust: `reviewed`
- Default mode: `manual_review`
- Permission default: `manual_review`
- Authentication: `Unspecified in source metadata`
- **Warning:** Default mode is `manual_review`.
- **Warning:** Permission default is `manual_review`.
- **Required posture:** Complete manual review before connecting or invoking tools; this generated record does not grant approval.
