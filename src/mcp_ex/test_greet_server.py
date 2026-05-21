import asyncio
import argparse
from fastmcp import Client
from dotenv import dotenv_values

def parse_args():
    parser = argparse.ArgumentParser(description="Test MCP Greet Server")
    parser.add_argument("--url", help="Direct URL to the MCP server")
    parser.add_argument("--local", action="store_true", help="Test local server (http://localhost:8000/mcp)")
    return parser.parse_args()

async def main():
    args = parse_args()
    config = dotenv_values(".env")

    # Default Horizon URL
    url = "https://lexical-sapphire-wildfowl.fastmcp.app/mcp"
    auth = config.get("HORIZON_API_KEY")

    if args.local:
        url = "http://localhost:8000/mcp"
        auth = None
    elif args.url:
        url = args.url
        # Only use auth if it looks like a Horizon URL, or just pass it if it exists
        # For simplicity, if a URL is explicitly provided, we'll try to use the key if available
        # unless it's obviously local.
        if "localhost" in url or "127.0.0.1" in url:
            auth = None

    print(f"Connecting to: {url}")
    client = Client(url, auth=auth)

    async with client:
        # Ensure client can connect
        await client.ping()

        # List available operations
        tools = await client.list_tools()
        print(f"Found {len(tools)} tools")

        # Ex. execute a tool call
        result = await client.call_tool("greet", {"name": "Ford"})
        print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())