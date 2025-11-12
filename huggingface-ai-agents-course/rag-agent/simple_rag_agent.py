from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel

search_tool = DuckDuckGoSearchTool()
model = InferenceClientModel()
agent = CodeAgent(model=model, tools=[search_tool])

response = agent.run(
    "Search for luxury superhero-themed party ideas, including decorations, entertainment, and catering."
)
print(response)