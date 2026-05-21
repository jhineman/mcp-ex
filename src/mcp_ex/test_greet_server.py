import asyncio
from fastmcp import Client
from dotenv import dotenv_values

config = dotenv_values(".env")
client = Client("https://lexical-sapphire-wildfowl.fastmcp.app/mcp", auth=config["HORIZON_API_KEY"])

async def main():
    async with client:
        # Ensure client can connect
        await client.ping()

        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()

        # Ex. execute a tool call
        result = await client.call_tool("greet", {"name": "Ford"})
        print(result)

asyncio.run(main())