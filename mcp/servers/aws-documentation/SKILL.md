---
name: "aws-documentation-mcp"
description: "Tools to access AWS documentation, search for content, and get recommendations."
keywords:
  - aws
  - awslabs
  - documentation
  - search
  - access
  - content
---

# AWS Documentation

Tools to access AWS documentation, search for content, and get recommendations.

## When to use

- Use AWS Documentation only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/aws-documentation"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/aws-documentation`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/aws-documentation

## Security policy

- Trust: `reviewed`
- Default mode: `manual_review`
- Permission default: `manual_review`
- Authentication: `Unspecified in source metadata`
- **Warning:** Default mode is `manual_review`.
- **Warning:** Permission default is `manual_review`.
- **Required posture:** Complete manual review before connecting or invoking tools; this generated record does not grant approval.
