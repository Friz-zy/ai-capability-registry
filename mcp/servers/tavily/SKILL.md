---
name: "tavily-mcp"
description: "Official Tavily MCP for search and extraction research workflows."
keywords:
  - tavily
  - extract
  - search
  - research
---

# Tavily MCP

Official Tavily MCP for search and extraction research workflows.

## When to use

- Use Tavily MCP only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Hosted endpoint

```json
{
  "type": "streamable_http",
  "url": "https://mcp.tavily.com/mcp"
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.



## References

- https://mcp.tavily.com/mcp

## Security policy

- Trust: `trusted`
- Default mode: `search_extract_only`
- Permission default: `search_extract_only`
- Authentication: `Unspecified in source metadata`
- **Posture:** Follow the declared defaults; this generated record does not replace server-specific review.
