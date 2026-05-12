---
name: "stripe-mcp"
description: "Interact with Stripe services over the Stripe API."
keywords:
  - stripe
  - finance
---

# Stripe

Interact with Stripe services over the Stripe API.

## When to use

- Use Stripe only when the task directly involves the relevant service, SaaS product, platform, or technology.

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
    "STRIPE_SECRET_KEY",
    "mcp/stripe",
    "--tools=all"
  ]
}
```

## MCP instructions

- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- This server requires authorization or environment-provided credentials; ask the user before connecting or requesting access.

## Docker launch notes

- Launch through Docker stdio with `docker run --rm -i -e STRIPE_SECRET_KEY mcp/stripe --tools=all`.
- Confirm required environment variables before launch: STRIPE_SECRET_KEY.

## References

- https://github.com/stripe/agent-toolkit
- https://github.com/docker/mcp-registry/tree/main/servers/stripe

## Security policy

- Authentication: `Environment variables`
