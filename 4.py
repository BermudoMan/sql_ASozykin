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
        print(connection.get_dsn_parameters(), "\n")
    except OperationalError as e:
        print(r"The error '{e}' occurred")
    return connection


cursor = create_connection('postgres', 'postgres', '121200986q', '', "5432").cursor()
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("Вы подключены к - ", record, "\n")

insert_query = """ALTER TABLE superheroes_mine ADD COLUMN shittt1 INT\n;"""
insert_query2 = """\d superheroes_mine"""
#insert_query = """ALTER TABLE superheroes_mine DROP COLUMN year"""
cursor.execute(insert_query)

#cursor.commit()
superheroes_mine = cursor.fetchall()
for row in superheroes_mine:
    print(row)


#cursor.execute(insert_query2)



