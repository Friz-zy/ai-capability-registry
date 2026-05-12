---
name: "genai-toolbox-mcp"
description: "Open source MCP server for databases that simplifies AI agent access to database resources. Handles connection pooling, authentication, and observability with OpenTelemetry support. Supports PostgreSQL, MySQL, BigQuery, Cloud SQL, Spanner, and more. Enables natural language queries and context-aware code generation based on live database schemas."
keywords:
  - genai
  - toolbox
  - genai-toolbox
  - sql
  - databases
  - googleapis
  - database
  - access
  - agent
  - ai-assistant
  - authentication
---

# GenAI Toolbox for Databases

Open source MCP server for databases that simplifies AI agent access to database resources. Handles connection pooling, authentication, and observability with OpenTelemetry support. Supports PostgreSQL, MySQL, BigQuery, Cloud SQL, Spanner, and more. Enables natural language queries and context-aware code generation based on live database schemas.

## When to use

- Use GenAI Toolbox for Databases only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "mcp/genai-toolbox",
    "--stdio",
    "--log-level",
    "ERROR",
    "--tools-file",
    "/tmp/tools.yaml"
  ]
}
```

## MCP instructions



## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i mcp/genai-toolbox --stdio --log-level ERROR --tools-file /tmp/tools.yaml`.

## References

- https://github.com/googleapis/genai-toolbox
- https://github.com/docker/mcp-registry/tree/main/servers/genai-toolbox

## Security policy

- Authentication: `Open or unspecified`
