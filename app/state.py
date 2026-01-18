from typing import TypedDict, Optional

class ReportState(TypedDict):
    query: str
    report_type: Optional[str]
    data: Optional[dict]
    analysis: Optional[str]
    report: Optional[str]