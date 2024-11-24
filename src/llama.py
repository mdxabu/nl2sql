from ollama import chat
from ollama import ChatResponse

from MySQLConnector import execute_query
from ProcessedOutput import processingOutput

def run():
    user_input = input("Please enter your question: ")
    

    
    # Add context for database creation
    prompt = f"""Generate SQL query for: {user_input}
    If this is a database creation request, include all necessary CREATE DATABASE and USE DATABASE and CREATE TABLE statements.
    Make sure to use valid MySQL syntax."""
    
    response: ChatResponse = chat(model='llama-nl2sql', messages=[{
        'role': 'user',
        'content': prompt,
    }])

    processed_output = response.message.content
    print(f"Generated SQL Query:\n{processed_output}")

    # Process the output to remove unnecessary formatting
    cleaned_output = processingOutput(processed_output)

    # Execute queries with multi=True to handle multiple statements
    result = execute_query(cleaned_output, multi=True)
    
    if result:
        print("Database operations completed successfully.")
    else:
        print("Error during database operations.")
