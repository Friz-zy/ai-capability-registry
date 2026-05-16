# cloudflare MCP Servers

Select only servers that directly match the current request. If a server matches, read its `mcp/servers/<server>/SKILL.md` and use it only within MCP safety rules.

- **Cloudflare Docs** (`cloudflare-docs`) — `hosted_https`, `trusted`: Documentation MCP server by Cloudflare.
- **Cloudflare Observability** (`cloudflare-observability`) — `hosted_https`, `trusted`: Observability MCP server by Cloudflare.
- **Cloudflare Workers** (`cloudflare-workers`) — `hosted_https`, `trusted`: Software Development MCP server by Cloudflare.
- **mcp** (`com.cloudflare.mcp-mcp`) — `hosted_https`, `trusted`: Cloudflare MCP servers
