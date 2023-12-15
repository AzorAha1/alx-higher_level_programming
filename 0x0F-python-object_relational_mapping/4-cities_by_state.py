#!/usr/bin/python3
"""this is a function"""


def list_all_cities():
    """class to list all cities"""
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    database = MySQLdb.connect(
        user=username,
        host='localhost',
        database=database,
        password=password,
        port=3306
    )
    query = f'select * from cities order by cities.id ASC'
    cursor = database.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    database.close()


if __name__ == "__main__":
    list_all_cities()
