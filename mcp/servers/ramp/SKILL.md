---
name: "ramp-mcp"
description: "Payments MCP server by Ramp."
keywords:
  - ramp
  - ramp-mcp-remote
  - payments
  - finance
---

# Ramp

Payments MCP server by Ramp.

## When to use

- Use Ramp only when the task directly involves Payments.

## Connection

### Hosted endpoint

```json
{
  "type": "streamable_http",
  "url": "https://ramp-mcp-remote.ramp.com/mcp"
}
```

## MCP instructions





## References

- https://ramp-mcp-remote.ramp.com/mcp

## Security policy

- Trust: `trusted`
- Default mode: `ask_before_write`
- Permission default: `ask_before_write`
- Authentication: `OAuth2.1`
- **Posture:** Follow the declared defaults; this generated record does not replace server-specific review.
