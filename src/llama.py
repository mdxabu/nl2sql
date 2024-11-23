from ollama import chat
from ollama import ChatResponse

from MySQLConnector import execute_query
from ProcessedOutput import processingOutput

def run():
    user_input = input("Please enter your question: ")

    print("\n\nGenerating SQL Query...\n\n")

    response: ChatResponse = chat(model='llama-nl2sql', messages=[{
        'role': 'user',
        'content': user_input,
    }])

    # Process the output from the chat model
    processed_output = processingOutput(response.message.content)
    print(f"Generated SQL Query: {processed_output}")

    # Execute the generated query
    result = execute_query(processed_output)
    
    if result:
        print(f"Query Result: {result}")
    else:
        print("No result returned or query failed.")