---
name: "com.atlassian-atlassian-mcp-server-mcp"
description: "Atlassian Rovo MCP Server"
keywords:
  - atlassian
  - atlassian-atlassian
---

# atlassian-mcp-server

Atlassian Rovo MCP Server

## When to use

- Use atlassian-mcp-server only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Hosted endpoint

```json
{
  "type": "streamable_http",
  "url": "https://mcp.atlassian.com/v1/mcp"
}
```

## MCP instructions





## References

- https://mcp.atlassian.com/v1/mcp
- https://github.com/atlassian/atlassian-mcp-server
- https://registry.modelcontextprotocol.io/v0/servers

## Security policy

- Trust: `trusted`
- Default mode: `manual_review`
- Permission default: `manual_review`
- Authentication: `Unspecified in source metadata`
- **Warning:** Default mode is `manual_review`.
- **Warning:** Permission default is `manual_review`.
- **Required posture:** Complete manual review before connecting or invoking tools; this generated record does not grant approval.
