

def build(input_message, output_message, memory):
    memory.save_context({"input": input_message},{"output": output_message})
    return memory
