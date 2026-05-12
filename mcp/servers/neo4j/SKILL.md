---
name: "neo4j-mcp"
description: "Official MCP server for Neo4j. Interact with Neo4j using Cypher graph queries."
keywords:
  - neo4j
  - cypher
---

# Neo4j

Official MCP server for Neo4j. Interact with Neo4j using Cypher graph queries.

## When to use

- Use Neo4j only when the task directly involves the relevant service, SaaS product, platform, or technology.

## Connection

### Docker stdio

```json
{
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "-e",
    "NEO4J_PASSWORD",
    "mcp/neo4j"
  ]
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.

## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i -e NEO4J_PASSWORD mcp/neo4j`.
- Confirm required environment variables before launch: NEO4J_PASSWORD.

## References

- https://github.com/neo4j/mcp
- https://github.com/docker/mcp-registry/tree/main/servers/neo4j

## Security policy

- Authentication: `Environment variables`
