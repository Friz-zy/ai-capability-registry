---
name: "markitdown-mcp"
description: "A lightweight MCP server for calling MarkItDown."
keywords:
  - markitdown
  - audio
  - docx
  - html
  - pdf
  - pptx
  - productivity
  - xlsx
  - youtube
---

# Markitdown

A lightweight MCP server for calling MarkItDown.

## When to use

- Use Markitdown only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/markitdown"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/markitdown`.

## References

- https://github.com/microsoft/markitdown
- https://github.com/docker/mcp-registry/tree/main/servers/markitdown

## Security policy

- Authentication: `Open or unspecified`
