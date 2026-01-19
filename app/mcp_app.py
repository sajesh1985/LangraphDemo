# app/mcp_app.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("reportbuilder")

# Import your tools **after** creating mcp
from app.tools import data_fetch, report_gen

# Register tools with the mcp instance
mcp.tool()(data_fetch.fetch_report_data)
mcp.tool()(report_gen.generate_report)
