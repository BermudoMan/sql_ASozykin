import psycopg2
from psycopg2 import OperationalError

#password = input()

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

cursor = create_connection('postgres', 'postgres', '', '', "5432").cursor()

insert_query = """ALTER TABLE superheroes_mine ADD COLUMN alive BOOLEAN"""
#insert_query = """ALTER TABLE superheroes_mine DROP COLUMN year"""
cursor.execute(insert_query)



