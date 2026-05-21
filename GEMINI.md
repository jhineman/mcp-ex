# mcp-ex: MCP Examples and Experiments

This project explores the Model Context Protocol (MCP) using `fastmcp` and `Prefect Horizon`.

## Core Tooling & Standards

- **Dependency Management:** Use `uv`. Always update `pyproject.toml` and `uv.lock` when adding dependencies.
- **Linting & Formatting:** Use `ruff` for both linting and formatting.
- **Type Safety:** Type-hinted Python is strictly preferred. Ensure all new code includes proper type annotations.
- **Framework:** Leveraging [fastmcp](https://gofastmcp.com/) for building MCP servers.

## Development Workflows

- **Environment:** Use `uv venv` to manage the local virtual environment.
- **Testing:** Add tests for new features using `pytest` (standard for Python projects, though not explicitly in pyproject.toml yet, it's the idiomatic choice).
- **Style:** Adhere to modern Python (3.12+) idioms and clean code principles.
