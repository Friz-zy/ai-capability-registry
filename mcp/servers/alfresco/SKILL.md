---
name: "alfresco-mcp"
description: "A minimal Model Context Protocol (MCP) server for Alfresco providing tools via the Alfresco REST API"
keywords:
  - alfresco
---

# Alfresco

A minimal Model Context Protocol (MCP) server for Alfresco providing tools via the Alfresco REST API

## When to use

- Use Alfresco only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "angelborroy/alfresco-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i angelborroy/alfresco-mcp-server`.

## References

- https://github.com/AlfrescoLabs/alfresco-mcp-server
- https://github.com/docker/mcp-registry/tree/main/servers/alfresco

## Security policy

- Authentication: `Open or unspecified`
