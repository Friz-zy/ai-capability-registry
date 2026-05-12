---
name: "aws-bedrock-data-automation-mcp"
description: "Analyze documents, images, videos, and audio."
keywords:
  - aws
  - bedrock
  - aws-bedrock
  - automation
  - awslabs
  - audio
  - data
  - documents
---

# AWS Bedrock Data Automation

Analyze documents, images, videos, and audio.

## When to use

- Use AWS Bedrock Data Automation only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/aws-bedrock-data-automation-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/aws-bedrock-data-automation-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/aws-bedrock-data-automation

## Security policy

- Authentication: `Open or unspecified`
