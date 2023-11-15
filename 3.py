import psycopg2
from psycopg2 import OperationalError



def create_connection(dbname, dbuser, dbpassword, dbhost, dbport):
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=dbuser,
            password=dbpassword,
            host=dbhost,
            port=dbport
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(r"The error '{e}' occurred")
    return connection


conn = create_connection('postgres', 'postgres', password, '', "5432")
cursor = conn.cursor()

# SERIAL - автоматический подбор ключа для строки MySQL
MY_TABLE = """ DROP TABLE IF EXISTS superheroes_mine;
               CREATE TABLE superheroes_mine(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    align VARCHAR(30), 
                    eye VARCHAR(30),
                    hair VARCHAR(30),
                    gender VARCHAR(30),
                    appearances INT,
                    year INT,
                    universe VARCHAR(10)
            )"""
#MY_TABLE2 = """DROP TABLE superheroes_mine"""

cursor.execute(MY_TABLE)
conn.commit()

insert_query = """ALTER TABLE superheroes ADD COLUMN alive BOOLEAN"""
cursor.execute(insert_query)

