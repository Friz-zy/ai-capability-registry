---
name: "cloud-run-mcp-mcp"
description: "MCP server to deploy apps to Cloud Run"
keywords:
  - run
  - deploy
---

# Cloud Run

MCP server to deploy apps to Cloud Run

## When to use

- Use Cloud Run only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/cloud-run-mcp"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/cloud-run-mcp`.

## References

- https://github.com/GoogleCloudPlatform/cloud-run-mcp
- https://github.com/docker/mcp-registry/tree/main/servers/cloud-run-mcp

## Security policy

- Authentication: `Open or unspecified`
