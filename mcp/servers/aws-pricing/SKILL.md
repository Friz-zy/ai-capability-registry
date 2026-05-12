---
name: "aws-pricing-mcp"
description: "AWS service pricing and cost estimates."
keywords:
  - aws
  - pricing
  - aws-pricing
  - awslabs
  - cost
---

# AWS Pricing

AWS service pricing and cost estimates.

## When to use

- Use AWS Pricing only when the task directly involves the relevant service, SaaS product, platform, or technology.

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
    "AWS_SECRET_ACCESS_KEY",
    "-e",
    "AWS_SESSION_TOKEN",
    "mcp/aws-pricing-mcp-server"
  ]
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.

## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i -e AWS_SECRET_ACCESS_KEY -e AWS_SESSION_TOKEN mcp/aws-pricing-mcp-server`.
- Confirm required environment variables before launch: AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/aws-pricing

## Security policy

- Authentication: `Environment variables`
