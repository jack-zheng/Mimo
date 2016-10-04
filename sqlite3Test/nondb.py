# before test delete the nondb.db
# run this script, it will create a new db file if there is no such db exist.
import sqlite3 as lite

con = None
query = "select sqlite_version()"

try:
    con = lite.connect("nondb.db")
    cur = con.cursor()
    cur.execute(query)

    data = cur.fetchone()

    print("sqlite version is: %s" % data)
except lite.Error as e:
    print(e)
finally:
    if con:
        con.close()
