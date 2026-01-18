from mcp import tool

@tool
def generate_report(analysis: str, data: dict = None) -> str:
    return f"## Quarterly Report\n\n{analysis}"