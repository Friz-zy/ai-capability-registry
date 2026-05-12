---
name: "aws-healthomics-mcp"
description: "Generate, run, debug lifescience workflows."
keywords:
  - aws
  - healthomics
  - aws-healthomics
  - awslabs
  - debug
  - generate
  - run
---

# AWS HealthOmics

Generate, run, debug lifescience workflows.

## When to use

- Use AWS HealthOmics only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/aws-healthomics-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/aws-healthomics-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/aws-healthomics

## Security policy

- Authentication: `Open or unspecified`
