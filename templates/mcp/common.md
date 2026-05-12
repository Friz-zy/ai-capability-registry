# MCP Connector — General Guide

## Tool Discovery

After connecting, use JSON-RPC to discover capabilities:

- **`tools/list`** — enumerate available tools with parameters
- **`resources/list`** — enumerate available resources
- **`resources/read`** — read a resource by URI (`{"uri": "file:///..."}`)
- **`tools/call`** — invoke a tool:

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "tool_name", "arguments": {}}}
```

## Response Content Types

MCP responses return a `content` array with typed blocks:

- **`text`** — plain text from the model or server
- **`mcp_tool_use`** — a tool was called (`name`, `input` fields)
- **`mcp_tool_result`** — result of a tool call (`content[0].text`)

## Errors & Diagnostics

| Error | Cause | Fix |
|-------|-------|-----|
| `401 Unauthorized` | Wrong token | Check format: `Bearer <token>` vs raw key |
| `404 Not Found` | Wrong URL | Check path: `/sse` vs `/mcp` vs `/` |
| `connection refused` | Docker not running | `docker ps` — verify the container is alive |
| `tool not found` | Typo in tool name | `tools/list` — check exact names |
| `timeout` | SSE connection dropped | Switch to Streamable HTTP or reconnect |