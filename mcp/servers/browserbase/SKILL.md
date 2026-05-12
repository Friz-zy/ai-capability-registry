---
name: "browserbase-mcp"
description: "Allow LLMs to control a browser with Browserbase and Stagehand for AI-powered web automation, intelligent data extraction, and screenshot capture."
keywords:
  - browserbase
  - extract
  - automation
  - control
  - data
  - screenshot
  - web-scraping
---

# Browserbase

Allow LLMs to control a browser with Browserbase and Stagehand for AI-powered web automation, intelligent data extraction, and screenshot capture.

## When to use

- Use Browserbase only when the task directly involves the relevant service, SaaS product, platform, or technology.

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
    "BROWSERBASE_API_KEY",
    "-e",
    "BROWSERBASE_PROJECT_ID",
    "-e",
    "GEMINI_API_KEY",
    "mcp/browserbase"
  ]
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.

## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i -e BROWSERBASE_API_KEY -e BROWSERBASE_PROJECT_ID -e GEMINI_API_KEY mcp/browserbase`.
- Confirm required environment variables before launch: BROWSERBASE_API_KEY, BROWSERBASE_PROJECT_ID, GEMINI_API_KEY.

## References

- https://github.com/browserbase/mcp-server-browserbase
- https://github.com/docker/mcp-registry/tree/main/servers/browserbase

## Security policy

- Authentication: `Environment variables`
