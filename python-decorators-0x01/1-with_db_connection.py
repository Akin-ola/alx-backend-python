import sqlite3 
import functools
import mysql.connector
from seed2 import config


def with_db_connection(func):
    """ your code goes here"""
    @functools.wraps(func) 
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

@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone()
 
#### Fetch user by ID with automatic connection handling 
user = get_user_by_id(user_id=1)
print(user)