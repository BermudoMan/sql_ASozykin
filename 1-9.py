import psycopg2
from config import host, user, password, db_name

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    # the cursor for performing database operations
    # AS variable cursor = connection.cursor()

    # AS context manager
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version {cursor.fetchone()}")

    # Print all data
    def select_from(query):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM %s;" % query)
            table_name = cursor.fetchall()
            for row in table_name:
                print(row)
    # create a new table
    def table_creation(query):
        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE %s(
                id serial PRIMARY KEY,
                name varchar(50) NOT NULL,
                nick_name varchar(50) NOT NULL);""" % query
            )
            print("[INFO] Table created succesfully")

    # insert data into a table
    def add_row(query):
        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO animals (name, nick_name) VALUES
                (%s);""" % query
            )

    # adding some column
    def add_column():
        with connection.cursor() as cursor:
            cursor.execute("""
                ALTER TABLE animals ADD COLUMN some_data VARCHAR(30);
                """
            )

    def del_column():
        with connection.cursor() as cursor:
            cursor.execute("""
                ALTER TABLE animals DROP COLUMN some_data;
                """
            )

    def rename_column():
        with connection.cursor() as cursor:
            cursor.execute("""
                 ALTER TABLE animals RENAME COLUMN alive TO some_data; 
                 """
            )

    def add_data():
        with connection.cursor() as cursor:
            cursor.execute("""
            INSERT INTO animals(name, nick_name)
            VALUES ('Tom', 'Psina');""")

    def add_data2():
        with connection.cursor() as cursor:
            cursor.execute("""
            INSERT INTO animals
            VALUES (20, 'Jerry', 'J', False, False, False);""")

    def changing_data():
        with connection.cursor() as cursor:
            cursor.execute("""
            UPDATE animals
            SET nick_name='Teddy'
            WHERE id=7
            """)
    def changing_data_full_column():
        with connection.cursor() as cursor:
            cursor.execute("""
            UPDATE animals
            SET some_data='wild'
            WHERE nick_name='c';
            """)
    def del_row():
        with connection.cursor() as cursor:
            cursor.execute("""
            DELETE FROM animals
            WHERE id=8;
            """)
    #agg functions
    def count_sum():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT align, COUNT(*), SUM(appearances)
            FROM superheroes
            GROUP BY align;
            """)
            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def avg():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT align, AVG(appearances),
                SUM(appearances)/COUNT(*) AS average
            FROM superheroes
            GROUP BY align;
            """)
            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def min_max():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT year, MIN(appearances), MAX(appearances) AS max_ap
            FROM superheroes
            GROUP BY year
            ORDER BY max_ap DESC
            LIMIT 10;
            """)
            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def filter_count():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT hair, COUNT(*)
            FROM superheroes
            WHERE gender='Female Characters'
            GROUP BY hair
            HAVING COUNT(*) BETWEEN 50 AND 300
            LIMIT 10;
            """)
            table_name = cursor.fetchall()
            for row in table_name:
                print(row)
    ###=====Actual instructions=====###
    #add_row("'bear', 'c'")
    #add_column()
    #add_column()
    #rename_column()
    #add_data2()
    #changing_data()
    #del_row()

    count_sum()
    print('-----------')
    avg()
    print('-----------')
    min_max()
    print('-----------')
    print('-----------')
    filter_count()
    #select_from('superheroes')


except Exception as _ex:
    print("[INFO] Error while workibg with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")


