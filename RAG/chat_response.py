from langchain.agents import AgentType, initialize_agent
from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI

from RAG.util import faiss, serp

tools = [
    Tool(
        name="Tool의 용도 1",
        func=faiss.faiss.run,
        description="Tool의 용도 1 detail"
    ),
    Tool(
        name="Tool의 용도 3",
        func=serp.serp.run,
        description="Tool의 용도 3 detail"
    )
]


def agent(human_input, memory):
    agent_chain = initialize_agent(tools, ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0, max_tokens=10000,
                                                     openai_api_key='your openai api key'),
                                   agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory,
                                   handle_parsing_errors=True
                                   )
    response = agent_chain.run(human_input)

    return [str(response)]
