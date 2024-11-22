from ollama import chat
from ollama import ChatResponse

def run():
    user_input = input("Please enter your question: ")

    response: ChatResponse = chat(model='llama-nl2sql', messages=[
        {
            'role': 'user',
            'content': user_input,
        },
    ])
    print("Generating SQL Query...")

    print(response.message.content)