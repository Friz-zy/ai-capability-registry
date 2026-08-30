---
name: "posthog-mcp"
description: "Official PostHog MCP for product analytics and operational insight workflows."
keywords:
  - posthog
  - analytics
  - metrics
  - feature-flags
  - product-insights
---

# PostHog MCP

Official PostHog MCP for product analytics and operational insight workflows.

## When to use

- Use PostHog MCP only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Hosted endpoint

```json
{
  "type": "streamable_http",
  "url": "https://mcp.posthog.com/mcp"
}
```

## MCP instructions





## References

- https://mcp.posthog.com/mcp

## Security policy

- Trust: `trusted`
- Default mode: `read_only`
- Permission default: `read_only`
- Authentication: `Unspecified in source metadata`
- **Posture:** Follow the declared defaults; this generated record does not replace server-specific review.
