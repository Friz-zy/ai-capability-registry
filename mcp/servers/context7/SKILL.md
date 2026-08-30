---
name: "context7-mcp"
description: "Trusted hosted MCP for retrieving current library documentation and code examples."
keywords:
  - context7
  - documentation
  - library-documentation
  - code-examples
---

# Context7 MCP

Trusted hosted MCP for retrieving current library documentation and code examples.

## When to use

- Use Context7 MCP only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Hosted endpoint

```json
{
  "type": "streamable_http",
  "url": "https://mcp.context7.com/mcp"
}
```

## MCP instructions





## References

- https://mcp.context7.com/mcp

## Security policy

- Trust: `trusted`
- Default mode: `docs_lookup_only`
- Permission default: `docs_lookup_only`
- Authentication: `Unspecified in source metadata`
- **Posture:** Follow the declared defaults; this generated record does not replace server-specific review.
