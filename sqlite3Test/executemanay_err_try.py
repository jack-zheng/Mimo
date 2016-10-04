# executemany can roll back but executescript can't
import sqlite3 as lite
import sys

cars = (
            (1, 'Audi', 52642),
            (2, 'Mercedes', 52642),
            (3, 'Skoda', 52642),
            (4, 'Volvo', 52642),
            (5, 'Bentley', 52642),
            (6, 'Hummer', 52642, 'error'),
            (7, 'Volkswagen', 52642),
        )

try:
    con = lite.connect('Car.db')

    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS CARS')
    cur.execute('CREATE TABLE CARS (ID INT, NAME TEXT, PRICE INT)')
    cur.executemany('INSERT INTO CARS VALUES (?, ?, ?)', cars)
    con.commit()

except lite.Error as e:
    if con:
        con.rollback()

    print("Error: %s" % e.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()
