import mysql.connector
import yaml
from mysql.connector import Error

def getConnection(database_name=None):
    try:
        with open('./config.yml', 'r') as file:
            config = yaml.safe_load(file)['database']  # Assuming config has database section

        connection_params = {
            'host': config['host'],
            'port': config['port'],
            'user': config['user'],
            'password': config['password'],
            'charset': config['charset']
        }
        
        if database_name:
            connection_params['database'] = database_name

        return mysql.connector.connect(**connection_params)

    except Error as e:
        print(f"Error connecting to MySQL: {e.msg} ({e.errno})")
        return None


def execute_query(query, multi=False):
    try:
        connection = getConnection()
        if not connection:
            print("Failed to establish a connection.")
            return None  # Return early if no connection is established

        cursor = connection.cursor()
        
        if multi:
            # Execute multiple statements
            for result in cursor.execute(query, multi=True):
                if result.with_rows:
                    print(result.fetchall())
        else:
            cursor.execute(query)
            if cursor.with_rows:
                return cursor.fetchall()
            
        connection.commit()
        return True

    except Error as e:
        print(f"Error executing query: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
