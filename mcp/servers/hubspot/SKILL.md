---
name: "hubspot-mcp"
description: "CRM MCP server by HubSpot."
keywords:
  - hubspot
  - crm
---

# HubSpot

CRM MCP server by HubSpot.

## When to use

- Use HubSpot only when the task directly involves CRM.

## Connection

### Hosted endpoint

```json
{
  "type": "streamable_http",
  "url": "https://app.hubspot.com/mcp/v1/http"
}
```

## MCP instructions





## References

- https://app.hubspot.com/mcp/v1/http

## Security policy

- Trust: `trusted`
- Default mode: `ask_before_write`
- Permission default: `ask_before_write`
- Authentication: `API Key`
- **Posture:** Follow the declared defaults; this generated record does not replace server-specific review.
