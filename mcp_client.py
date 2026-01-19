import asyncio
from app.mcp_app import mcp

async def main():
    result = await mcp.call_tool("fetch_report_data", {"report_type": "sales"})
    print("fetch_report_data output:")
    print(result)

    result2 = await mcp.call_tool(
        "generate_report",
        {"analysis": "| Month | Revenue |\n| Oct | 12000 |"}
    )
    print("\ngenerate_report output:")
    print(result2)

if __name__ == "__main__":
    asyncio.run(main())
