---
name: "square-mcp"
description: "Payments MCP server by Square."
keywords:
  - squareup
  - square
  - payments
  - finance
---

# Square

Payments MCP server by Square.

## When to use

- Use Square only when the task directly involves Payments.

## Connection

### Hosted endpoint

```json
{
  "type": "sse",
  "url": "https://mcp.squareup.com/sse"
}
```

## MCP instructions





## References

- https://mcp.squareup.com/sse

## Security policy

- Trust: `trusted`
- Default mode: `ask_before_write`
- Permission default: `ask_before_write`
- Authentication: `OAuth2.1`
- **Posture:** Follow the declared defaults; this generated record does not replace server-specific review.
