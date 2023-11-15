import psycopg2
from psycopg2 import OperationalError

password = input()

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

cursor = create_connection('postgres', 'postgres', password, '', "5432").cursor()

insert_query = "SELECT * FROM superheroes"
cursor.execute(insert_query)
print("Выбор строк из таблицы mobile с помощью cursor.fetchall")
superheroes = cursor.fetchall()
print("Вывод каждой строки и ее столбцов")
for row in superheroes:
    print(row)





