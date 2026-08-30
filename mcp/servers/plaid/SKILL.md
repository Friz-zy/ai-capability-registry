---
name: "plaid-mcp"
description: "Payments MCP server by Plaid."
keywords:
  - plaid
  - dashboard
  - payments
  - finance
---

# Plaid

Payments MCP server by Plaid.

## When to use

- Use Plaid only when the task directly involves Payments.

## Connection

### Hosted endpoint

```json
{
  "type": "sse",
  "url": "https://api.dashboard.plaid.com/mcp/sse"
}
```

## MCP instructions





## References

- https://api.dashboard.plaid.com/mcp/sse

## Security policy

- Trust: `trusted`
- Default mode: `ask_before_write`
- Permission default: `ask_before_write`
- Authentication: `OAuth2.1 restricted`
- **Posture:** Follow the declared defaults; this generated record does not replace server-specific review.
