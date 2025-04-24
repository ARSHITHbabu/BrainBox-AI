from utils.tavily_api import search_web

def research_agent(query):
    print("[Research Agent] Searching the web...")
    results = search_web(query)
    data = "\n".join([f"- {r['title']}: {r['url']}" for r in results[:5]])
    content_summary = "\n".join([r['content'] for r in results[:5]])
    return {
        "summary": content_summary,
        "sources": data
    }
