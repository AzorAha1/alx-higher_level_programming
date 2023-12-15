#!/usr/bin/python3
"""list all states from database(hbtn_0e_0_usa)"""


def list_states_filter_states():
    """function to list all states with filter"""
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
    q = 'select * from states ' \
        'where name="{}" COLLATE utf8mb4_bin order by states.id ASC'.format(sn)
    cursor = database.cursor()
    cursor.execute(q)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    database.close()


if __name__ == "__main__":
    list_states_filter_states()
