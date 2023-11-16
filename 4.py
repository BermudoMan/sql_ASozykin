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
#        connection.autocommit = True
        print("Connection to PostgreSQL DB successful")
        print(connection.get_dsn_parameters(), "\n")
    except OperationalError as e:
        print(r"The error '{e}' occurred")
    return connection


cursor = create_connection('postgres', 'postgres', '121200986q', '', "5432").cursor()
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("Вы подключены к - ", record, "\n")
#cursor.commit()

insert_query = """ALTER TABLE superheroes_mine ADD COLUMN woow INTEGER;"""
insert_query2 = """\d superheroes_mine"""
#insert_query = """ALTER TABLE superheroes_mine DROP COLUMN year"""
cursor.execute(insert_query)




