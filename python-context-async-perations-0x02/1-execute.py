import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'database': os.getenv('DB_NAME'),
    'password': os.getenv('DB_PASSWORD'),
}

class ExecuteQuery:
    def __init__(self, query, params=None):
        self.query = query
        self.params = params
        self.conn = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self.result
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conn.close()

query = "SELECT * FROM user_data WHERE age > %s"
params = (25,)
with ExecuteQuery(query, params) as result:
    for row in result:
        print (row)