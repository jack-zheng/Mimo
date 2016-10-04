import sqlite3 as lite

query = 'INSERT INTO DAY_TASK ("TASK_NAME", "DETAIL", "STAR", "COMMENT", "TIME") VALUES ("T_NAME", "T_DETAIL", 4, "T_COMMENT", datetime("now", "localtime"))'

con = lite.connect("backup.db")

with con:
    cur = con.cursor()
    cur.execute(query)
    cur.execute(query)
