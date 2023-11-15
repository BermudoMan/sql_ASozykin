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

insert_query = """SELECT name AS hero_name, appearances 
               FROM superheroes"""
insert_query2 = """SELECT DISTINCT(align) 
               FROM superheroes"""
insert_query3 = """SELECT DISTINCT(eye) 
               FROM superheroes"""
insert_query4 = """SELECT DISTINCT(hair) 
               FROM superheroes
               LIMIT 10"""
# Фильтры
insert_query5 = """SELECT * 
               FROM superheroes
               WHERE gender = 'Female Characters'"""
insert_query6 = """SELECT * 
               FROM superheroes
               WHERE align = 'Reformed Criminals'"""
insert_query7 = """SELECT * 
               FROM superheroes
               WHERE year BETWEEN 2000 AND 2005"""
insert_query8 = """SELECT * 
               FROM superheroes
               WHERE hair IN ('Strawberry Blond Hair', 'Red Hair', 'Auburn Hair')"""
insert_query9 = """SELECT * 
               FROM superheroes
               WHERE hair LIKE ('%Blond%')"""
insert_query10 = """SELECT * 
               FROM superheroes
               WHERE gender = 'Female Characters'
               AND
               align = 'Bad Characters'"""
insert_query11 = """SELECT * 
               FROM superheroes
               WHERE hair = 'Auburn Hair'
               OR hair = 'Red Hair'
               OR hair = 'Strawberry Blond Hair'"""
insert_query12 = """SELECT * 
               FROM superheroes
               WHERE hair NOT IN ('Strawberry Blond Hair', 'Red Hair', 'Auburn Hair')
               """
# Сортировка
insert_query13 = """SELECT * 
               FROM superheroes
               ORDER BY year"""
insert_query14 = """SELECT * 
               FROM superheroes
               WHERE align = 'Bad Characters'
               ORDER BY appearances DESC
               LIMIT 5"""
insert_query15 = """SELECT * 
               FROM superheroes
               ORDER BY year DESC, appearances DESC
               LIMIT 15"""

# Печатается последний запрос
cursor.execute(insert_query15)


print("Выбор строк из таблицы mobile с помощью cursor.fetchall")
superheroes = cursor.fetchall()
print("Вывод каждой строки и ее столбцов")
for row in superheroes:
    print(row)


