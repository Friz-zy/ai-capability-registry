# databases MCP Servers

Select only servers that directly match the current request. If a server matches, read its `mcp/servers/<server>/SKILL.md` and use it only within MCP safety rules.

- **GenAI Toolbox for Databases** (`genai-toolbox`) — `docker`, `reviewed`: Open source MCP server for databases that simplifies AI agent access to database resources. Handles connection pooling, authentication, and observability with OpenTelemetry support. Supports PostgreSQL, MySQL, BigQuery, Cloud SQL, Spanner, and more. Enables natural language queries and context-aware code generation based on live database schemas.
- **Notion MCP** (`notion`) — `hosted_https_oauth`, `trusted`: Official Notion MCP integration controlled by workspace permissions.
