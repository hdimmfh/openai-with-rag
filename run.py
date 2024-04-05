from RAG.chat_response import agent
from RAG.build_memory import build
from langchain.memory import ConversationBufferWindowMemory

memory_instance = ConversationBufferWindowMemory(k=10, memory_key='chat_history', return_messages=True)

while True:
    # human input
    input_message = input()
    # agency output
    output_message = agent(human_input=input_message, memory=memory_instance)
    print(output_message)
    # update memory
    memory_instance = build(input_message, output_message, memory_instance)
