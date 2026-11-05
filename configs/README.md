# Config templates

| File | Use |
|---|---|
| `remote-server.template.json` | A starting point for any vendor-hosted remote MCP server in a Claude Code style `.mcp.json`. Replace the endpoint with the one in the vendor's own documentation |
| `stacksync.mcp.json` | The Stacksync MCP server: `https://mcp.stacksync.com/mcp`, OAuth sign in |

Other clients (Claude, ChatGPT, Cursor, VS Code, Codex, Windsurf, Gemini CLI) take the same URL through their own settings. See the [Stacksync MCP setup docs](https://docs.stacksync.com/mcp).

Rules for any server: merge into your existing config, never overwrite it, and never commit a key. Prefer OAuth.
