---
name: "playwright-mcp"
description: "No description."
keywords:
  - playwright
---

# Playwright

No description.

## When to use

- Use Playwright only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/playwright"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/playwright`.

## References

- https://github.com/microsoft/playwright-mcp
- https://github.com/docker/mcp-registry/tree/main/servers/playwright

## Security policy

- Authentication: `Open or unspecified`
