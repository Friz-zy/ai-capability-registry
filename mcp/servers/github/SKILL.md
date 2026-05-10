---
name: "github-mcp"
description: "Tools for interacting with the GitHub API, enabling file operations, repository management, search functionality, and more."
keywords:
  - github
  - repositories
  - search
  - git
  - pull-requests
  - issues
  - actions
  - security
---

# GitHub (Archived)

Tools for interacting with the GitHub API, enabling file operations, repository management, search functionality, and more.

## When to use

- Use GitHub (Archived) only when the task directly involves the relevant service, SaaS product, platform, or technology.

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
    "mcp/github"
  ]
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.

## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i -e GITHUB_PERSONAL_ACCESS_TOKEN mcp/github`.
- Confirm required environment variables before launch: GITHUB_PERSONAL_ACCESS_TOKEN.

## References

- https://github.com/modelcontextprotocol/servers
- https://github.com/docker/mcp-registry/tree/main/servers/github

## Security policy

- Authentication: `Environment variables`
