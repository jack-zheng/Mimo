import sqlite3 as lite

# prepare test data
cars = (
            (1, "car1", 1),
            (2, "car2", 1),
            (3, "car3", 1),
            (4, "car4", 1),
            (5, "car5", 1),
        )

# sql
create_sql = "CREATE TABLE CARS (ID INT, NAME TEXT, PRICE INT)"
select_all = "SELECT * FROM CARS"

con = lite.connect(":memory:")

with con:
    cur = con.cursor()

    # create cars table and insert record
    cur.execute(create_sql)

    # insert multiple record and rowcount attribute
    cur.executemany("INSERT INTO CARS VALUES (?, ?, ?)", cars)
    print("rowcount: %d" % cur.rowcount)

    # insert record by script
    cur.execute('INSERT INTO CARS VALUES (233, "car233",  233)')

    # lastrowid: only effect when insert sql
    print("last row id is: %d" % cur.lastrowid)

    # fetchone
    cur.execute(select_all)
    oneRecord = cur.fetchone()
    print("fetch one result: %s" % str(oneRecord))
    oneRecord = cur.fetchone()
    print("fetch one result: %s" % str(oneRecord))

    # fetchmany(int)
    cur.execute(select_all)
    multiRecord = cur.fetchmany(3)
    print("fetch many result: %s" % str(multiRecord))

    # fetchall()
    cur.execute(select_all)
    allRecord = cur.fetchall()
    print("fetch many result: %s" % str(allRecord))
    print("desc content: %s" % str(cur.description))
