from app.mcp_app import mcp

@mcp.tool()
def generate_report(analysis: str) -> str:
    return f"## Quarterly Report\n\n{analysis}"
