import os
import mysql.connector
from mysql.connector import Error


def stream_users():
    """
    Generator that yields rows from the user_data table one by one.
    Uses a single loop and minimizes memory usage.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database="ALX_prodev"
        )

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT user_id, name, email, age FROM user_data")

        for row in cursor:
            yield row

    except Error as err:
        print(f"[ERROR] Database error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()