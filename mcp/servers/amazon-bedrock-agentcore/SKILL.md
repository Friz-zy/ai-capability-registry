---
name: "amazon-bedrock-agentcore-mcp"
description: "Documentation on AgentCore platform services."
keywords:
  - amazon
  - bedrock
  - agentcore
  - amazon-bedrock-agentcore
  - aws
  - awslabs
  - documentation
---

# AWS Bedrock AgentCore

Documentation on AgentCore platform services.

## When to use

- Use AWS Bedrock AgentCore only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/amazon-bedrock-agentcore-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/amazon-bedrock-agentcore-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/amazon-bedrock-agentcore

## Security policy

- Authentication: `Open or unspecified`
