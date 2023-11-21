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

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def two_table_merge2():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT p.name, t.type_name 
            FROM products AS p JOIN product_types AS t
            ON p.type_id = t.id;
            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def two_table_merge3():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT p.name AS product_name,
                   t.type_name AS product_type,
                   p.price AS product_price
            FROM products AS p JOIN product_types AS t
            ON p.type_id = t.id
            WHERE t.type_name='Онлайн-курс'
            ORDER BY p.price DESC;
            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

# JOIN types № 11
    def joins():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT products.name, product_types.type_name 
            FROM products JOIN product_types
            ON products.type_id = product_types.id;
            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def outer_join_l():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT products.name, product_types.type_name 
            FROM products LEFT OUTER JOIN product_types
            ON products.type_id = product_types.id;
            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def outer_join_r():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT products.name, product_types.type_name 
            FROM products RIGHT OUTER JOIN product_types
            ON products.type_id = product_types.id;
            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def outer_join_full():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT products.name, product_types.type_name 
            FROM products FULL OUTER JOIN product_types
            ON products.type_id = product_types.id;
            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def cross_join():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT products.name, product_types.type_name 
            FROM products CROSS JOIN product_types;
            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def db_schem():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT p.id,
                   p.name,
                   p.price,
                   s.quantity,
                   p.price * s.quantity AS total               
            FROM products AS p JOIN sales AS s
                ON p.id = s.product_id
            WHERE s.order_id=2
            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def db_schem2():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT p.id,
                   p.name,
                   p.price,
                   s.quantity,
                   p.price * s.quantity AS total               
            FROM products AS p JOIN sales AS s
                ON p.id = s.product_id
                JOIN orders AS o
                ON o.id = s.order_id
            WHERE o.customer_id=1;
            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def sub_issue():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT id, name, price
            FROM products
            WHERE price = (SELECT MAX(price)
                           FROM products);
            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    # products ordered more than 0 time
    def sub_issue2():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT id, name, price
            FROM products
            WHERE id IN (SELECT product_id
                           FROM sales);
            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def sub_issue3():
        with connection.cursor() as cursor:
            cursor.execute("""
            UPDATE products
            SET price = price + 599
            WHERE type_id = (SELECT id
                             FROM product_types
                             WHERE type_name='Книга'));
            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)
    def sub_issue3():
        with connection.cursor() as cursor:
            cursor.execute("""
            UPDATE products
            SET price = price + 599
            WHERE type_id = (SELECT id
                             FROM product_types
                             WHERE type_name='Книга');
            """)

    def sub_issue4():
        with connection.cursor() as cursor:
            cursor.execute("""
            UPDATE products
            SET price = price + 599
            WHERE type_id = (SELECT id
                             FROM product_types
                             WHERE type_name='Книга');
            SELECT * FROM products;
            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)

    def transactions():
        with connection.cursor() as cursor:
            cursor.execute("""

            """)

            table_name = cursor.fetchall()
            for row in table_name:
                print(row)
# RUNNING
    # № 11
    joins() # INNER JOIN is the same
    outer_join_l() # OUTER JOIN 1
    outer_join_r() # OUTER JOIN 2
    outer_join_full() # OUTER JOIN 2
    print('-----')
    cross_join() # CROSS JOIN

    # № 12
    print('====')
    db_schem()
    print('----')
    # all order of the selected customer
    db_schem2()

    # № 13
    print('====')
    sub_issue()
    print('----')
    sub_issue2()
    print('----')
    sub_issue3()
    print('----')
    sub_issue4()

    ## № 14 TRANSACTIONS
    print('====')
    # execution of all sql commands in the block TOGEATHER! <START TRANSACTION;>...</COMMIT>
    # (fix changes in DB) or </ROLLBACK> (for back changes)
    ## № 15 INDEXES
    print('====')
    # apply for separate column\...s in the DB for fast searching needs row data
    # need apply <CREATE INDEX> only one time for a table, in continue applied (for the fast searching) automatically
    ## № 16 CONSTRAIN
    print('====')


# ENDING
except Exception as _ex:
    print("[INFO] Error while workibg with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")

