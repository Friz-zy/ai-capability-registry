---
name: "github-official-mcp"
description: "Official GitHub MCP Server, by GitHub. Provides seamless integration with GitHub APIs, enabling advanced automation and interaction capabilities for developers and tools."
keywords:
  - github
  - automation
  - integration
---

# GitHub Official

Official GitHub MCP Server, by GitHub. Provides seamless integration with GitHub APIs, enabling advanced automation and interaction capabilities for developers and tools.

## When to use

- Use GitHub Official only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "-e",
    "GITHUB_PERSONAL_ACCESS_TOKEN",
    "ghcr.io/github/github-mcp-server"
  ]
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.

## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i -e GITHUB_PERSONAL_ACCESS_TOKEN ghcr.io/github/github-mcp-server`.
- Confirm required environment variables before launch: GITHUB_PERSONAL_ACCESS_TOKEN.

## References

- https://github.com/github/github-mcp-server
- https://github.com/docker/mcp-registry/tree/main/servers/github-official

## Security policy

- Authentication: `Environment variables`
