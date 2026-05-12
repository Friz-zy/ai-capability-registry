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

- Authentication: `Open or unspecified`
