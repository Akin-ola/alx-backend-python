import time
import functools
import mysql.connector
from seed2 import config


#### paste your with_db_decorator here
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

""" your code goes here"""
def retry_on_failure(retries=3, delay=2, exceptions=(Exception, )):
    def retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts=0
            while attempts < retries:
                try:
                    return func(args, kwargs)
                except exceptions as e:
                    attempts +=1
                    print(f"[WARNING] {e} — Retrying {attempts}/{retries}...")
                    time.sleep(delay)
                print("[ERROR] Operation failed after retries.")
            return None
        return wrapper
    return retry

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users) 