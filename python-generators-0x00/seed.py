import os
import sys
import csv
import uuid
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
}

DB_NAME= 'ALX_prodev'

TABLES = {}

TABLES ['user_data'] = (
    "CREATE TABLE user_data ("
    " user_id CHAR(36) PRIMARY KEY,"
    " name VARCHAR(55) NOT NULL,"
    " email VARCHAR(55) NOT NULL,"
    " age DECIMAL NOT NULL)"
)

def connect_db():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as exc:
        print(f"[ERROR] Cannot connect: {exc}", file=sys.stderr)
        return None

connection = connect_db()
if connection:
    cursor = connection.cursor()

def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")


def connect_to_prodev(cursor):
    try:
        cursor.execute(f"USE {DB_NAME}")
    except mysql.connector.Error:
        create_database(cursor)
        cursor.execute(f"USE {DB_NAME}")

def create_table(cursor):
    for table_name, create_statement in TABLES.items():
        try:
            print(f"Creating table `{table_name}`...")
            cursor.execute(create_statement)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            print("Table successfully created.")


def insert_data(cursor):
    insert_query = """
        INSERT INTO user_data (user_id, name, email, age)
        VALUES (%s, %s, %s, %s)
    """
    df = pd.read_csv('https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2024/12/3888260f107e3701e3cd81af49ef997cf70b6395.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20250706%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250706T181822Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=38ce508ea6690679c16bca8781b23f9e8320f41ab925b6793e2406f20e0a45a7')  # Make sure this file is in the same directory or provide full path

    for _, row in df.iterrows():
        user_id = str(uuid.uuid4())
        values = (
            user_id,
            row['name'],
            row['email'],
            row['age']
        )
        cursor.execute(insert_query, values)


connection = connect_db()
if connection:
    cursor = connection.cursor()
    connect_to_prodev(cursor)
    create_table(cursor)
    insert_data(cursor)
    connection.commit()
    cursor.close()
    connection.close()