from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from typing import TypedDict
from agents.research_agent import research_agent
from agents.draft_agent import draft_agent

# Step 1: Define TypedDict for the graph's state
class AgentState(TypedDict):
    query: str
    style: str
    research_data: dict
    final_answer: str

# Step 2: Define node logic
def run_research_agent(state: AgentState):
    print("\n[Graph] Running Research Agent...")
    query = state["query"]
    research_data = research_agent(query)
    return {"research_data": research_data}

def run_draft_agent(state: AgentState):
    print("\n[Graph] Running Draft Agent...")
    query = state["query"]
    style = state["style"]
    research_data = state["research_data"]
    final_answer = draft_agent(query, research_data["summary"], style)
    return {"final_answer": final_answer}

# Step 3: Create and compile graph
graph = StateGraph(AgentState)

graph.add_node("research", RunnableLambda(run_research_agent))
graph.add_node("draft", RunnableLambda(run_draft_agent))

graph.set_entry_point("research")
graph.add_edge("research", "draft")
graph.set_finish_point("draft")

app = graph.compile()

# Step 4: Run the pipeline
if __name__ == "__main__":
    query = input("Enter your question: ")
    print("Choose response style: summary | bullets | paragraph")
    style = input("Enter response style: ").strip().lower()

    inputs: AgentState = {
        "query": query,
        "style": style,
        "research_data": {},
        "final_answer": ""
    }

    final_state = app.invoke(inputs)

    print("\n--- Final Answer ---")
    print(final_state['final_answer'])
    print("\nSources:")
    print(final_state['research_data']['sources'])
