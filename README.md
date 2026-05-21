# mcp-ex
MCP examples and experiments using [fastmcp](https://gofastmcp.com/getting-started/welcome) and [Prefect Horizon](https://gofastmcp.com/deployment/prefect-horizon).

# running servers

## `greet_server.py`
Run locally with http (remove options to run as stdio)
```bash
uv run fastmcp run src/mcp_ex/greet_server.py:mcp --transport http --port 8000
```

Example communication with greet server.
```bash
uv run src/mcp_ex/test_greet_server.py
```

Working with horizon deployed (api key in .env):
```bash
uv run --env-file .env src/mcp/test_greet_server.py
```