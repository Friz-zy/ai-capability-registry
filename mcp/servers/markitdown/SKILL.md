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

- Trust: `reviewed`
- Default mode: `manual_review`
- Permission default: `manual_review`
- Authentication: `Unspecified in source metadata`
- **Warning:** Default mode is `manual_review`.
- **Warning:** Permission default is `manual_review`.
- **Required posture:** Complete manual review before connecting or invoking tools; this generated record does not grant approval.
