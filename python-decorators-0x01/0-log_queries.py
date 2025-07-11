import functools
import sqlite3
from datetime import datetime

#### decorator to lof SQL queries

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        connection = kwargs.get('connection')
        cursor = connection.cursor()

        result = func(cursor, *args, **kwargs)
        if hasattr(cursor, 'statement'):
            print(f"[QUERY] {cursor.statement}")
        return result
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")