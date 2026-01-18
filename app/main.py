import json
from app.graph import graph

def handler(event, context):
    body = json.loads(event.get("body", "{}"))
    query = body.get("query", "")
    result = graph.invoke({"query": query})
    return {
        "statusCode": 200,
        "body": json.dumps(result.get("report"))
    }