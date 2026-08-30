---
name: "paypal-mcp"
description: "Payments MCP server by PayPal."
keywords:
  - paypal
  - payments
  - finance
---

# PayPal

Payments MCP server by PayPal.

## When to use

- Use PayPal only when the task directly involves Payments.

## Connection

### Hosted endpoint

```json
{
  "type": "sse",
  "url": "https://mcp.paypal.com/sse"
}
```

## MCP instructions





## References

- https://mcp.paypal.com/sse

## Security policy

- Trust: `trusted`
- Default mode: `ask_before_write`
- Permission default: `ask_before_write`
- Authentication: `OAuth2.1`
- **Posture:** Follow the declared defaults; this generated record does not replace server-specific review.
