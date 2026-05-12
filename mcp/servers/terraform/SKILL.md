---
name: "terraform-mcp"
description: "No description."
keywords:
  - terraform
---

# Hashicorp Terraform

No description.

## When to use

- Use Hashicorp Terraform only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "hashicorp/terraform-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i hashicorp/terraform-mcp-server`.

## References

- https://github.com/hashicorp/terraform-mcp-server
- https://github.com/docker/mcp-registry/tree/main/servers/terraform

## Security policy

- Authentication: `Open or unspecified`
