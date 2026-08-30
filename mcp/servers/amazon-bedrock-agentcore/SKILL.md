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

- Trust: `reviewed`
- Default mode: `manual_review`
- Permission default: `manual_review`
- Authentication: `Unspecified in source metadata`
- **Warning:** Default mode is `manual_review`.
- **Warning:** Permission default is `manual_review`.
- **Required posture:** Complete manual review before connecting or invoking tools; this generated record does not grant approval.
