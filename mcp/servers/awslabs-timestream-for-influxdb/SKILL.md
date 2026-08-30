---
name: "awslabs-timestream-for-influxdb-mcp"
description: "Time-series database operations."
keywords:
  - awslabs
  - timestream
  - influxdb
  - awslabs-timestream-influxdb
  - amazon
  - database
  - aws
  - operations
---

# Amazon Timestream for InfluxDB

Time-series database operations.

## When to use

- Use Amazon Timestream for InfluxDB only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/timestream-for-influxdb-mcp-server"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/timestream-for-influxdb-mcp-server`.

## References

- https://github.com/awslabs/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/awslabs-timestream-for-influxdb

## Security policy

- Trust: `reviewed`
- Default mode: `manual_review`
- Permission default: `manual_review`
- Authentication: `Unspecified in source metadata`
- **Warning:** Default mode is `manual_review`.
- **Warning:** Permission default is `manual_review`.
- **Required posture:** Complete manual review before connecting or invoking tools; this generated record does not grant approval.
