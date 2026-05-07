# Security Policy

This project curates AI skills, MCP servers, workflows, and agent integrations for secure multi-agent development.

## Security Model

- Registry entries are declarative metadata, not install scripts.
- Generated artifacts are derived from `registry/*.yaml`.
- MCP servers must use hosted HTTPS/OAuth or Docker isolation.
- Local arbitrary execution is denied by default.
- Read-only and ask-before-write modes are preferred.
- Upstream sources should be pinned by tag and commit.

## Denied Patterns

- `curl | sh`
- Global random package execution such as `npm install -g random-mcp`
- Unknown `python server.py` MCP runtimes
- Unrestricted shell MCP servers
- Unrestricted filesystem access
- Browser automation without sandboxing

## Reporting Issues

Open a private security advisory or contact the repository owner before publishing exploit details.
