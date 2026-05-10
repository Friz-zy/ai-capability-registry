---
name: "amazon-kendra-index-mcp"
description: "Enterprise search and RAG enhancement."
keywords:
  - amazon
  - kendra
  - index
  - amazon-kendra-index
  - awslabs
  - search
  - aws
  - rag
---

# Amazon Kendra Index

Enterprise search and RAG enhancement.

## When to use

- Use Amazon Kendra Index only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/amazon-kendra-index-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/amazon-kendra-index-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/amazon-kendra-index

## Security policy

- Authentication: `Open or unspecified`
