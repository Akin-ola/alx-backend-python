import mysql.connector
from seed2 import config


def with_db_connection(func):
    def wrapper(*args ,**kwargs):
        try:
            conn = mysql.connector.connect(**config)
            result = func(conn, args, kwargs)
            conn.close()
            return result

        except mysql.connector.Error as e:
            print (f"[ERROR] Connection failed {e}")
            return None
    return wrapper