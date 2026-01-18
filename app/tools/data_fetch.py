from mcp import tool

@tool
def fetch_report_data(report_type: str) -> dict:
    return {
        "months": ["Oct", "Nov", "Dec"],
        "revenue": [12000, 15000, 18000]
    }