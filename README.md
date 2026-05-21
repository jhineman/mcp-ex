# mcp-ex
MCP examples and experiments using [fastmcp](https://gofastmcp.com/getting-started/welcome) and [Prefect Horizon](https://gofastmcp.com/deployment/prefect-horizon).

# running servers

## `greet_server.py`
Run locally with http (remove options to run as stdio)
```bash
uv run fastmcp run src/mcp_ex/greet_server.py:mcp --transport http --port 8000
```

Example communication with greet server:

**Test Locally:**
First, start the server:
```bash
uv run fastmcp run src/mcp_ex/greet_server.py:mcp --transport http --port 8000
```
Then run the test client:
```bash
uv run src/mcp_ex/test_greet_server.py --local
```

**Test Horizon Deployed (API key in .env):**
```bash
uv run src/mcp_ex/test_greet_server.py
```

**Test Custom URL:**
```bash
uv run src/mcp_ex/test_greet_server.py --url http://127.0.0.1:8000/mcp
```