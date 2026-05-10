---
name: "linear-mcp"
description: "Official Linear remote MCP for issues, projects, comments, and planning workflows."
keywords:
  - linear
  - issues
  - project-management
  - planning
---

# Linear MCP

Official Linear remote MCP for issues, projects, comments, and planning workflows.

## When to use

- Use Linear MCP only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Hosted endpoint

```json
{
  "type": "sse",
  "url": "https://mcp.linear.app/sse"
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.



## References

- https://mcp.linear.app/sse

## Security policy

- Authentication: `OAuth`
