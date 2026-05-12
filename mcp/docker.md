# MCP Connector — Docker Mode

## Transport Modes

Docker MCP servers use one of two transports:

| Mode | Transport | Sharing | Launch flags |
|------|-----------|---------|-------------|
| **stdio** | stdin/stdout pipe | **No** — one container per session | `docker run --rm -i` (foreground) |
| **Network** | localhost TCP port | **Yes** — one container, many sessions | `docker run -d --rm -p` (detached) |

### stdio Mode (Default)

The MCP server reads JSON-RPC from stdin and writes responses to stdout. This is the primary mode for Docker MCP.

**Session sharing**: stdio is a point-to-point pipe — only the launching process can communicate with the server. Each concurrent session **must** start its own container. Reuse is not possible; the container is tied to a single session for its entire lifetime.

**Required launch flags**:

| Flag | Purpose |
|------|---------|
| `--rm` | Auto-remove container on exit |
| `-i` | Keep stdin attached (critical — without this, the server gets EOF immediately) |

**Do NOT use** with stdio: `-d` (detached — breaks stdin), `-t` (pseudo-TTY — may corrupt JSON-RPC framing).

### Network Mode (Port Exposure)

The MCP server listens on a localhost TCP port, usually exposing SSE or Streamable HTTP. Multiple sessions connect via `http://localhost:<port>`.

**Session sharing**: one container can serve many concurrent sessions. Start once, reuse across tasks.

**Required launch flags**:

| Flag | Purpose |
|------|---------|
| `-d` | Run detached in background |
| `--rm` | Auto-remove container on exit |
| `-p <host>:<container>` | Map container port to localhost |

**Do NOT use** with network mode: `-i` (not needed, the server listens on a socket, not stdin).

## Container Naming

Format: `mcp-<server-id>-<session-id>-<purpose>`. Generate session-id with `openssl rand -hex 3`.

## stdio Launch (Single-Session)

```bash
docker run --rm -i \
  --name "${CONTAINER_NAME}" \
  -e API_KEY="${MCP_API_KEY}" \
  -e GITHUB_TOKEN="${GITHUB_TOKEN}" \
  org/mcp-server:latest
```

The container runs in the foreground. JSON-RPC messages go over stdin/stdout.

## Network Launch (Multi-Session, Shared)

```bash
CONTAINER_NAME="mcp-postgres-shared-$(date +%Y%m%d)"

if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
  docker run -d --rm \
    --name "${CONTAINER_NAME}" \
    -e POSTGRES_URL="${DB_URL}" \
    -p 8811:8811 \
    org/mcp-postgres-server:latest
  echo "Started new container: ${CONTAINER_NAME}"
else
  echo "Reusing existing container: ${CONTAINER_NAME}"
fi
```

Connect to the shared container via its localhost port:
```javascript
mcp_servers: [{ type: "url", url: "http://localhost:8811/sse", name: "mcp-docker-local" }]
```

## Cleanup

```bash
# stdio mode (--rm): container auto-removes on exit, force-kill if stuck
docker kill "${CONTAINER_NAME}"

# Network mode: stop — --rm auto-removes
docker stop "${CONTAINER_NAME}"

# Check status
docker inspect "${CONTAINER_NAME}" --format '{{.State.Status}}'
```

## Policy

- Confirm required environment variables before launching the container.
- For stdio mode, keep stdin attached with `-i` and run the container in the foreground. Do not use `-d`.
- Name containers clearly as `mcp-<server-id>-<session-id>-<purpose>`.
- Before starting, check `docker ps` for an existing matching MCP container. For network-mode containers, reuse if already running. For stdio, start a fresh container.
- Stop or remove Docker MCP containers you started at the end of the session, unless they were already running before the session or the user explicitly asks to keep them.
- Do NOT use unsafe Docker options: `--privileged`, host filesystem mounts (`-v /:/host`), host networking (`--network host`), or mounts to `/var/run/docker.sock`, `~/.ssh`, or cloud credential directories.