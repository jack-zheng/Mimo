import sqlite3 as lite

taskInsert = '''
           INSERT INTO DAY_TASK
           ("TITLE", "CONTENT", "SCORE", "COMMENT", "TIME")
           VALUES (?, ?, ?, ?, datetime("now", "localtime"))
           '''
dbPath = "./mimo.db"


def insertTask(tupleValue):
    if len(tupleValue) != 4:
        # TODO throw exception
        pass
    else:
        con = lite.connect(dbPath)
        with con:
            cur = con.cursor()
            cur.execute(taskInsert, tupleValue)
            con.commit()
