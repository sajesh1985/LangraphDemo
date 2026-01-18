from langgraph.graph import StateGraph, END
from app.state import ReportState
from app.llm import invoke_bedrock
from app.prompts import TABULAR_ANALYSIS_PROMPT
from app.tools.data_fetch import fetch_report_data
from app.tools.report_gen import generate_report

def parse_query(state: ReportState):
    return {"report_type": "sales"}

def analyze_data(state: ReportState):
    prompt = TABULAR_ANALYSIS_PROMPT.format(data=state["data"])
    table = invoke_bedrock(prompt)
    return {"analysis": table}

builder = StateGraph(ReportState)
builder.add_node("parse", parse_query)
builder.add_node("fetch", fetch_report_data)
builder.add_node("analyze", analyze_data)
builder.add_node("report", generate_report)
builder.set_entry_point("parse")
builder.add_edge("parse", "fetch")
builder.add_edge("fetch", "analyze")
builder.add_edge("analyze", "report")
builder.add_edge("report", END)
graph = builder.compile()