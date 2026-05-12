---
name: "aws-diagram-mcp"
description: "Seamlessly create diagrams using the Python diagrams package DSL. This server allows you to generate AWS diagrams, sequence diagrams, flow diagrams, and class diagrams using Python code."
keywords:
  - aws
  - diagram
  - aws-diagram
  - awslabs
  - code
  - generate
  - python
---

# AWS Diagram

Seamlessly create diagrams using the Python diagrams package DSL. This server allows you to generate AWS diagrams, sequence diagrams, flow diagrams, and class diagrams using Python code.

## When to use

- Use AWS Diagram only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/aws-diagram"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/aws-diagram`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/aws-diagram

## Security policy

- Authentication: `Open or unspecified`
