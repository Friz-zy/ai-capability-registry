---
name: "awslabs-iam-mcp"
description: "IAM user, role, group, and policy management."
keywords:
  - awslabs
  - iam
  - awslabs-iam
  - aws
  - management
  - policy
  - user
---

# AWS IAM

IAM user, role, group, and policy management.

## When to use

- Use AWS IAM only when the task directly involves the relevant service, SaaS product, platform, or technology.

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
    "mcp/iam-mcp-server"
  ]
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.

## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i -e AWS_SECRET_ACCESS_KEY mcp/iam-mcp-server`.
- Confirm required environment variables before launch: AWS_SECRET_ACCESS_KEY.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/awslabs-iam

## Security policy

- Authentication: `Environment variables`
