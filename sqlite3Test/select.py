import sqlite3 as lite

con = None
query = "select sqlite_version()"

try:
    con = lite.connect("backup.db")
    cur = con.cursor()
    cur.execute(query)

    data = cur.fetchone()

    print("sqlite version is: %s." % data)
except lite.Error as e:
    print(e)
finally:
    if con:
        con.close()
