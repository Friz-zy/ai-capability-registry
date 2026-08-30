---
name: "cloudflare-docs-mcp"
description: "Documentation MCP server by Cloudflare."
keywords:
  - cloudflare
  - documentation
---

# Cloudflare Docs

Documentation MCP server by Cloudflare.

## When to use

- Use Cloudflare Docs only when the task directly involves Documentation.

## Connection

### Hosted endpoint

```json
{
  "type": "sse",
  "url": "https://docs.mcp.cloudflare.com/sse"
}
```

## MCP instructions





## References

- https://docs.mcp.cloudflare.com/sse

## Security policy

- Trust: `trusted`
- Default mode: `ask_before_write`
- Permission default: `ask_before_write`
- Authentication: `Open`
- **Posture:** Follow the declared defaults; this generated record does not replace server-specific review.
