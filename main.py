from agents.research_agent import research_agent
from agents.draft_agent import draft_agent

if __name__ == "__main__":
    query = input("Enter your question: ")
    print("\nChoose response style: summary | bullets | paragraph")
    style = input("Enter response style: ").strip().lower()

    research_data = research_agent(query)
    final_answer = draft_agent(query, research_data, style)

    print("\n--- Final Answer ---")
    print(final_answer)
    print("\nSources:")
    print(research_data['sources'])
