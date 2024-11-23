from ollama import chat
from ollama import ChatResponse

from ProcessedOutput import processingOutput

def run():
    user_input = input("Please enter your question: ")

    print("\n\nGenerating SQL Query...\n\n")

    response: ChatResponse = chat(model='llama-nl2sql', messages=[
        {
            'role': 'user',
            'content': user_input,
        },
    ])
    
    processed_output = processingOutput(response.message.content)
    print(processed_output)