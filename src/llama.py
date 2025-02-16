from ollama import chat
from ollama import ChatResponse
from connector.mysql_connector import MySQLConnector
from processed_output import processingOutput

def run():
    user_input = input("Please enter your question: ")

    connector = MySQLConnector()
    connection = connector.get_connection()

    if connection is None:
        print("Unable to connect to the database. Exiting.")
        return
    
    prompt = f"""Generate SQL query for: {user_input}
    If this is a database creation request, include all necessary CREATE DATABASE and USE DATABASE and CREATE TABLE statements.
    Make sure to use valid MySQL syntax."""
    
    try:
        response: ChatResponse = chat(model='llama-nl2sql', messages=[{
            'role': 'user',
            'content': prompt,
        }])
    except Exception as e:
        print(f"Error in generating SQL query: {e}")
        return

    processed_output = response.message.content
    print(f"Generated SQL Query:\n{processed_output}")
    
    # Clean the generated query (e.g., remove unwanted formatting like backticks)
    cleaned_output = processingOutput(processed_output)
    print(f"Cleaned SQL Query:\n{cleaned_output}")

    try:
        result = connector.execute_query(cleaned_output, multi=True)
        if result:
            print("Database operations completed successfully.")
            print("Query Results:")
            for res in result:
                print(res)
        else:
            print("Error during database operations.")
    except Exception as e:
        print(f"Error executing query: {e}")
    
    connector.close_connection()

# Run the main function
if __name__ == "__main__":
    run()
