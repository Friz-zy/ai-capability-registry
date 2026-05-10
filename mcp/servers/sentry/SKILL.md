---
name: "sentry-mcp"
description: "Official hosted MCP for Sentry issues, errors, projects, and incident analysis."
keywords:
  - sentry
  - issues
  - incident
  - error-analysis
  - observability
---

# Sentry MCP

Official hosted MCP for Sentry issues, errors, projects, and incident analysis.

## When to use

- Use Sentry MCP only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Hosted endpoint

```json
{
  "type": "streamable_http",
  "url": "https://mcp.sentry.dev/mcp"
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.



## References

- https://mcp.sentry.dev/mcp

## Security policy

- Authentication: `OAuth`
