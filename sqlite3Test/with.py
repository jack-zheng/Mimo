import sqlite3 as lite

con = lite.connect("backup.db")
with con:
    cur = con.cursor()
    cur.execute('select sqlite_version()')

    data = cur.fetchone()

    print("sqlite version is: %s" % data)
