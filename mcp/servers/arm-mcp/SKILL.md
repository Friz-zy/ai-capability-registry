---
name: "arm-mcp-mcp"
description: "Provides AI assistants with specialized tools for Arm architecture development, migration, optimization, and profiling. Includes knowledge base search, code migration analysis, container architecture inspection, Arm Performix workload profiling, and assembly performance analysis."
keywords:
  - arm
  - search
  - analysis
  - architecture
  - code
  - container
  - development
  - docker
  - knowledge
  - migration
---

# Arm

Provides AI assistants with specialized tools for Arm architecture development, migration, optimization, and profiling. Includes knowledge base search, code migration analysis, container architecture inspection, Arm Performix workload profiling, and assembly performance analysis.

## When to use

- Use Arm only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "armlimited/arm-mcp:2.0.0"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i armlimited/arm-mcp:2.0.0`.

## References

- https://github.com/arm/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/arm-mcp

## Security policy

- Authentication: `Open or unspecified`
