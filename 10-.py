# -*- coding: utf-8 -*-
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


    def two_table_merge():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT products.name, product_types.type_name
            FROM products JOIN product_types
            ON products.type_id = product_types.id;
            """)

            print([(i[0], i[1].encode('utf-8')) for i in cursor.fetchall()])

            table_name = cursor.fetchall()
            for row in table_name:
                print(row.encode('utf-8'))


    two_table_merge()
#ENDING
except Exception as _ex:
    print("[INFO] Error while workibg with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")

