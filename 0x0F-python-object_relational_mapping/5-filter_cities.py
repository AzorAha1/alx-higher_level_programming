#!/usr/bin/python3
"""list all states from database(hbtn_0e_0_usa)"""


def list_cities_filter_safe():
    """function to list all cities with filter"""
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    sn = sys.argv[4]
    database = MySQLdb.connect(
        host='localhost',
        user=username,
        password=password,
        database=database, port=3306
        )
    q = f'select name from cities ' \
        f'where cities.state_id in ' \
        f'(select states.id from states where name = %s)' \
        f'order by cities.id ASC'
    cursor = database.cursor()
    cursor.execute(q, (sn,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    database.close()


if __name__ == "__main__":
    list_cities_filter_safe()
