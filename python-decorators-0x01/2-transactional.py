import mysql.connector
import sqlite3 
import functools

"""your code goes here"""
def transactional(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        connection = kwargs.get('connection')
        cursor = connection.cursor()

        try:
            result= func(cursor, args, kwargs)
            connection.commit()
            return result
        
        except mysql.connector.Error as e:
            connection.rollback()
            print(f"[ERROR] Transaction failed: {e}")
            return None
        finally:
            cursor.close()
    return wrapper

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')