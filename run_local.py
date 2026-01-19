from app.graph import graph

result = graph.invoke({
    "query": "Create Q4 sales report"
})

print(result["report"])
