from langchain.memory import ConversationBufferWindowMemory


def build(input_message, output_message):
    memory = ConversationBufferWindowMemory(k=10, memory_key='chat_history', return_messages=True)
    memory.save_context({"input": input_message},{"output": output_message})

    return memory
