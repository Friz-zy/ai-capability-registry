# MCP Connector — HTTPS / SSE Mode

## Authentication (HTTPS)

Methods in order of priority:

```javascript
// Option A: Bearer token in header
authorization_token: "Bearer eyJhbGci..."

// Option B: API key as query param
url: "https://mcp.example.com/sse?api_key=KEY"

// Option C: Basic auth
authorization_token: "Basic " + btoa("user:password")
```

Check the server's documentation first. If unspecified — try Bearer.

## Health Check

```bash
curl -I https://mcp.example.com/sse
# Expect: 200 OK, Content-Type: text/event-stream

# For Streamable HTTP:
curl -X POST https://mcp.example.com/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{}}}'
```