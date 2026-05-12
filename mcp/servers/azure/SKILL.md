---
name: "azure-mcp"
description: "No description."
keywords:
  - azure
---

# Azure

No description.

## When to use

- Use Azure only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcr.microsoft.com/azure-sdk/azure-mcp"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcr.microsoft.com/azure-sdk/azure-mcp`.

## References

- https://github.com/microsoft/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/azure

## Security policy

- Authentication: `Open or unspecified`
