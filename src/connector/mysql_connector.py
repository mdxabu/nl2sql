import mysql.connector
import yaml

# Load the YAML file
with open("config.yml", 'r') as file:
    config = yaml.safe_load(file)

class MySQLConnector:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=config['mysql']['host'],
                user=config['mysql']['user'],
                password=config['mysql']['password']
            )
            print(f"Connected to MySQL server successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection = None

    def get_connection(self):
        return self.connection
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")
    
    def execute_query(self, query, multi=False):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, multi=multi)  

            if query.lower().startswith("create database"):
                db_name = query.split()[2]  
                print(f"Creating and switching to database: {db_name}")
                self.connection.database = db_name

            if multi:
                results = []
                for result in cursor:
                    results.append(result)
                return results

            return cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            return None
        finally:
            cursor.close()  
