import mysql.connector
import yaml
from mysql.connector import Error

def getConnection():
    try:
        # Load configuration from the YAML file
        with open('./config.yml', 'r') as file:
            config = yaml.safe_load(file)

        # Attempt to connect to the database
        connection = mysql.connector.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            password=config['password'],
            charset=config['charset'],
            connection_timeout=config['timeout']
        )

        if connection.is_connected():
            print("Connected to MySQL server")
        return connection.cursor()

    except Error as err:
        print(f"Error: {err}")
        return None

def execute_query(query):
    cursor = getConnection()
    if cursor:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error executing query: {err}")
        finally:
            cursor.connection.close()
    else:
        print("Unable to connect to the database.")