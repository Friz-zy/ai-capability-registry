---
name: "notion-mcp"
description: "Official Notion MCP integration controlled by workspace permissions."
keywords:
  - notion
  - documents
  - knowledge
  - databases
---

# Notion MCP

Official Notion MCP integration controlled by workspace permissions.

## When to use

- Use Notion MCP only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Hosted endpoint

```json
{
  "type": "streamable_http",
  "url": "https://mcp.notion.com/mcp"
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.



## References

- https://mcp.notion.com/mcp

## Security policy

- Authentication: `OAuth`
