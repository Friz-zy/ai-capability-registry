---
name: "cloudflare-observability-mcp"
description: "Observability MCP server by Cloudflare."
keywords:
  - cloudflare
  - observability
  - cloudflare-observability
  - incident
---

# Cloudflare Observability

Observability MCP server by Cloudflare.

## When to use

- Use Cloudflare Observability only when the task directly involves Observability.

## Connection

### Hosted endpoint

```json
{
  "type": "sse",
  "url": "https://observability.mcp.cloudflare.com/sse"
}
```

## MCP instructions





## References

- https://observability.mcp.cloudflare.com/sse

## Security policy

- Trust: `trusted`
- Default mode: `ask_before_write`
- Permission default: `ask_before_write`
- Authentication: `OAuth2.1`
- **Posture:** Follow the declared defaults; this generated record does not replace server-specific review.
