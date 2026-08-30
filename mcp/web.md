# MCP Connector — HTTPS / SSE Mode

## Authentication (HTTPS)

Use only the authentication method and header names documented for the specific reviewed server. Store credential values in the approved secret store or MCP client secret mechanism, and reference them with redacted placeholders.

```json
{
  "headers": {
    "<DOCUMENTED_HEADER_NAME>": "<REDACTED_SECRET_REFERENCE>"
  }
}
```

Never place credentials in URL query strings. Do not guess an authentication scheme or try fallback credentials when the reviewed server documentation does not specify one. Do not log credential values, authorization headers, or URLs derived from secrets.

## Health Check

```bash
curl -I https://mcp.example.com/sse
# Expect: 200 OK, Content-Type: text/event-stream

# For Streamable HTTP:
curl -X POST https://mcp.example.com/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{}}}'
```
