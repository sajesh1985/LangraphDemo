from app.mcp_app import mcp

@mcp.tool()
def fetch_report_data(report_type: str) -> dict:
    """
    Fetches raw report data
    """
    return {
        "months": ["Oct", "Nov", "Dec"],
        "revenue": [12000, 15000, 18000]
    }
