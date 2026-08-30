---
name: "cloudflare-workers-mcp"
description: "Software Development MCP server by Cloudflare."
keywords:
  - cloudflare
  - bindings
  - workers
  - cloudflare-workers
  - development
---

# Cloudflare Workers

Software Development MCP server by Cloudflare.

## When to use

- Use Cloudflare Workers only when the task directly involves Software Development.

## Connection

### Hosted endpoint

```json
{
  "type": "sse",
  "url": "https://bindings.mcp.cloudflare.com/sse"
}
```

## MCP instructions





## References

- https://bindings.mcp.cloudflare.com/sse

## Security policy

- Trust: `trusted`
- Default mode: `ask_before_write`
- Permission default: `ask_before_write`
- Authentication: `OAuth2.1`
- **Posture:** Follow the declared defaults; this generated record does not replace server-specific review.
