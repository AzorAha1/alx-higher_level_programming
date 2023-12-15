#!/usr/bin/python3
"""list all states from database(hbtn_0e_0_usa)"""
if __name__ == "__main__":
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
query = f'select * from states order by states.id ASC'
cursor = database.cursor()
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
database.close()
