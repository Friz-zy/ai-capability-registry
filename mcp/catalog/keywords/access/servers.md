# access MCP Servers

Select only servers that directly match the current request. If a server matches, read `mcp/servers/<server>/SKILL.md` and apply it only under `mcp.md` safety rules.

- **AWS API** (`aws-api`) — `docker`, `reviewed`: Comprehensive AWS API support with command validation and access to all services.
- **AWS Documentation** (`aws-documentation`) — `docker`, `reviewed`: Tools to access AWS documentation, search for content, and get recommendations.
- **Amazon Q Business** (`amazon-qbusiness-anonymous`) — `docker`, `reviewed`: AI assistant for ingested content with anonymous access.
- **GenAI Toolbox for Databases** (`genai-toolbox`) — `docker`, `reviewed`: Open source MCP server for databases that simplifies AI agent access to database resources. Handles connection pooling, authentication, and observability with OpenTelemetry support. Supports PostgreSQL, MySQL, BigQuery, Cloud SQL, Spanner, and more. Enables natural language queries and context-aware code generation based on live database schemas.
- **Redis** (`redis`) — `docker`, `reviewed`: Access to Redis database operations.
- **mcp** (`com.googleapis.container-mcp`) — `hosted_https`, `trusted`: Provides read access to your GKE and Kubernetes resources.
- **mcp** (`com.googleapis.developerknowledge-mcp`) — `hosted_https`, `trusted`: Provides access to Google's public developer documentation.
