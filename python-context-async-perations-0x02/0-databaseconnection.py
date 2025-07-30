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
class DatabaseConnection:
    def __enter__(self):
        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()
        print ("Connection Created...")
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        print("Connection Closed...")


with DatabaseConnection() as cursor:
    cursor.execute("SELECT * FROM user_data")
    result = cursor.fetchall()
    print(result)