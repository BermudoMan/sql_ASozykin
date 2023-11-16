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
                ALTER TABLE animals ADD COLUMN alive BOOLEAN;
                """
            )

    def del_column():
        with connection.cursor() as cursor:
            cursor.execute("""
                ALTER TABLE animals DROP COLUMN alive;
                """
            )

    def rename_column():
        with connection.cursor() as cursor:
            cursor.execute("""
                 ALTER TABLE animals RENAME COLUMN alive TO some_data; 
                 """
            )

    ###=====Actual instructions=====###
    #add_row("'bear', 'c'")
    add_column()
    rename_column()
    select_from('animals')


except Exception as _ex:
    print("[INFO] Error while workibg with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")

x = "'bear'"
xx = "'bear'"
print("""INSERT INTO animals (name, nick_name) VALUES
                (%s, %s);""" % (x, xx))
