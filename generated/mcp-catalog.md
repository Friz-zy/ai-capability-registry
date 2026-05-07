# MCP Catalog

Generated from `registry/mcp.yaml`.

| ID | Name | Trust | Runtime | Default Mode | Enabled |
| --- | --- | --- | --- | --- | --- |
| `docker-mcp-gateway` | Docker MCP Gateway | `trusted_runtime_layer` | `docker` | `allowlisted_images_only` | yes |
| `firecrawl` | Firecrawl MCP | `reviewed` | `hosted_https` | `scrape_extract_only` | no |
| `github` | GitHub MCP | `trusted` | `hosted_or_docker` | `read_only` | yes |
| `linear` | Linear MCP | `trusted` | `hosted_https_oauth` | `ask_before_write` | yes |
| `notion` | Notion MCP | `trusted` | `hosted_https_oauth` | `restricted_workspace` | yes |
| `posthog` | PostHog MCP | `trusted` | `hosted_https` | `read_only` | yes |
| `sentry` | Sentry MCP | `trusted` | `hosted_https_oauth` | `read_only` | yes |
| `tavily` | Tavily MCP | `trusted` | `hosted_https_oauth` | `search_extract_only` | yes |

## Security Defaults

- **Docker MCP Gateway**: Docker-managed runtime layer for orchestrating allowlisted MCP servers with container isolation.
  Data risk: `depends_on_configured_server`. Permission default: `allowlisted_images_only`.
- **Firecrawl MCP**: Firecrawl MCP for search, scrape, and structured extraction, with browser/session tools disabled by default.
  Data risk: `web_prompt_injection`. Permission default: `scrape_extract_only`.
- **GitHub MCP**: Official GitHub MCP server for repositories, issues, pull requests, Actions, and security findings.
  Data risk: `repository_data`. Permission default: `read_only`.
- **Linear MCP**: Official Linear remote MCP for issues, projects, comments, and planning workflows.
  Data risk: `product_planning_data`. Permission default: `ask_before_write`.
- **Notion MCP**: Official Notion MCP integration controlled by workspace permissions.
  Data risk: `private_workspace_data`. Permission default: `restricted_workspace`.
- **PostHog MCP**: Official PostHog MCP for product analytics and operational insight workflows.
  Data risk: `analytics_user_data`. Permission default: `read_only`.
- **Sentry MCP**: Official hosted MCP for Sentry issues, errors, projects, and incident analysis.
  Data risk: `production_error_data`. Permission default: `read_only`.
- **Tavily MCP**: Official Tavily MCP for search and extraction research workflows.
  Data risk: `web_prompt_injection`. Permission default: `search_extract_only`.
