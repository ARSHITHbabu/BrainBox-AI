from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query: str):
    response = client.search(query=query, search_depth="advanced", include_answer=True)
    return response['results']
