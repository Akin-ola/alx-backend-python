import mysql.connector
from seed import connect_to_prodev

def paginate_users(page_size, offset):
    conn = connect_to_prodev()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
    cursor.execute(query, (page_size, offset))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def lazy_paginate(page_size):
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size