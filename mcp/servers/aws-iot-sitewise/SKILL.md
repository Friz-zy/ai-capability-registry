---
name: "aws-iot-sitewise-mcp"
description: "Industrial IoT asset management."
keywords:
  - aws
  - iot
  - sitewise
  - aws-iot-sitewise
  - awslabs
  - management
---

# AWS IoT SiteWise

Industrial IoT asset management.

## When to use

- Use AWS IoT SiteWise only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/aws-iot-sitewise-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/aws-iot-sitewise-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/aws-iot-sitewise

## Security policy

- Trust: `reviewed`
- Default mode: `manual_review`
- Permission default: `manual_review`
- Authentication: `Unspecified in source metadata`
- **Warning:** Default mode is `manual_review`.
- **Warning:** Permission default is `manual_review`.
- **Required posture:** Complete manual review before connecting or invoking tools; this generated record does not grant approval.
