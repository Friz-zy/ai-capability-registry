---
name: "dockerhub-mcp"
description: "Docker Hub official MCP server"
keywords:
  - dockerhub
  - docker
  - hub
---

# Docker Hub

Docker Hub official MCP server

## When to use

- Use Docker Hub only when the task directly involves the relevant service, SaaS product, platform, or technology.

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
    "HUB_PAT_TOKEN",
    "mcp/dockerhub",
    "--transport=stdio",
    "--username={{dockerhub.username}}"
  ]
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.

## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i -e HUB_PAT_TOKEN mcp/dockerhub --transport=stdio '--username={{dockerhub.username}}'`.
- Confirm required environment variables before launch: HUB_PAT_TOKEN.

## References

- https://github.com/docker/hub-mcp
- https://github.com/docker/mcp-registry/tree/main/servers/dockerhub

## Security policy

- Authentication: `Environment variables`
