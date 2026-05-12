---
name: "aws-dataprocessing-mcp"
description: "Data processing and transformation services."
keywords:
  - aws
  - dataprocessing
  - aws-dataprocessing
  - processing
  - awslabs
  - data
---

# AWS Data Processing

Data processing and transformation services.

## When to use

- Use AWS Data Processing only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/aws-dataprocessing-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/aws-dataprocessing-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/aws-dataprocessing

## Security policy

- Authentication: `Open or unspecified`
