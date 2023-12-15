#!/usr/bin/python3
"""list all states from database(hbtn_0e_0_usa)"""


def list_states_filter():
    """function to list all states"""
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    database = MySQLdb.connect(
        host='localhost',
        user=username,
        password=password,
        database=database, port=3306
        )
    q = f'select * from states where name like "N%"'
    cursor = database.cursor()
    cursor.execute(q)
    for row in cursor:
        print(row)
    cursor.close()
    database.close()


if __name__ == "__main__":
    list_states_filter()
