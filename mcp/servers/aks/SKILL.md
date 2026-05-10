---
name: "aks-mcp"
description: "Azure Kubernetes Service (AKS) official MCP server"
keywords:
  - aks
  - kubernetes
  - azure
---

# Azure Kubernetes Service (AKS)

Azure Kubernetes Service (AKS) official MCP server

## When to use

- Use Azure Kubernetes Service (AKS) only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/aks",
    "--transport=stdio",
    "--access-level={{aks.access_level}}",
    "--allow-namespaces={{aks.allow_namespaces}}",
    "--additional-tools={{aks.additional_tools}}"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/aks --transport=stdio '--access-level={{aks.access_level}}' '--allow-namespaces={{aks.allow_namespaces}}' '--additional-tools={{aks.additional_tools}}'`.

## References

- https://github.com/Azure/aks-mcp
- https://github.com/docker/mcp-registry/tree/main/servers/aks

## Security policy

- Authentication: `Open or unspecified`
