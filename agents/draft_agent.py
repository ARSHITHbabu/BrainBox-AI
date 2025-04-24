from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def draft_agent(query, research_data, style):
    template = """
    You are an expert AI researcher writing in a {style} format.

    Based on the following research data:
    {research_data}

    Write a response to the question:
    {query}
    """

    prompt = PromptTemplate(
        input_variables=["query", "research_data", "style"],
        template=template
    )

    llm = ChatOllama(model="mistral", temperature=0.5)
    chain = LLMChain(llm=llm, prompt=prompt)

    return chain.run({
        "query": query,
        "research_data": research_data,
        "style": style
    })
