# BrainBox AI - Deep Research AI Agent System

An intelligent **AI-driven research agentic system** powered by **LangChain**, **LangGraph**, and **Tavily API** that performs deep web research and structured drafting of responses. Designed for advanced knowledge extraction and answer generation with agent collaboration.

---

## Project Overview

**BrainBox AI** performs autonomous online research to answer queries using a dual-agent system:

- **Research Agent**: Gathers information from the web via Tavily.
- **Draft Agent**: Crafts well-structured answers using LangChain LLM chains.
- **LangGraph Integration**: Organizes the research and drafting process into a composable graph.

Key Features:
- Real-time information gathering from the internet
- Flexible response styles: summary, bullets, or paragraph
- Modular dual-agent architecture
- Uses LangGraph for defining AI workflows
- Easy-to-use CLI interface for querying
- Open-source, extendable architecture for further research tasks

---

## Tech Stack

- **AI Frameworks:** LangChain, LangGraph
- **Web Crawling API:** Tavily
- **Model Backend:** ChatOllama (Mistral)
- **Environment Management:** Python-dotenv
- **Language:** Python 3.8+

---

## Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- Ollama (Mistral model should be available locally)
- Git CLI

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd deep-research-agent
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file and include:
```env
TAVILY_API_KEY=your_tavily_api_key_here
```

---

## Run the System

### 1. Ensure Ollama is Running with Mistral
```bash
ollama run mistral
```

### 2. Run the Graph-based AI Workflow
```bash
python graph_runner.py
```

You'll be prompted to enter your question and choose a response style (`summary`, `bullets`, or `paragraph`).

---

## Code Structure Overview

### `graph_runner.py`
> Entry point that runs the LangGraph-based pipeline using state transitions between research and drafting agents.

### `agents/research_agent.py`
> Defines the `research_agent` function that searches the web using Tavily and returns summaries and URLs.

### `agents/draft_agent.py`
> Defines the `draft_agent` function that creates final answers from research data using LangChain's LLMChain and a prompt template.

### `utils/tavily_api.py`
> Utility module for handling Tavily API requests.

### `.env`
> Stores API keys and other environment variables securely.

---

## LangGraph Flow Diagram

```text
[Input Question]
      ↓
[Research Agent - Tavily Search]
      ↓
[Draft Agent - LLM Answer Drafting]
      ↓
[Final Output: Styled Answer + Sources]
```

LangGraph manages the transitions and state between agents using `StateGraph`, making the system composable and scalable.

---

## Sample Output

```bash
Enter your question: What are the latest advancements in quantum computing?
Enter response style: summary

--- Final Answer ---
1. Improved qubit stability and error correction...
2. New quantum algorithms for cryptography and ML...
3. Practical use cases over benchmark focus...

Sources:
- Quantum Update 2024: https://example.com/quantum1
- Research Insights: https://example.com/quantum2
```

---

## Future Enhancements

🔹 Add citation linking in the answer text  
🔹 Extend to multi-agent reasoning chains  
🔹 Add vector DB for context memory  
🔹 Support more customizable prompt templates  
🔹 Add GUI interface using Streamlit or Gradio  
🔹 Deploy as an API microservice  

---

## License

This project is licensed under the **MIT License**.

---
