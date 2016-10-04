import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect("Car2.db")
    cur = con.cursor()

    cur.executescript(
                '''
                DROP TABLE IF EXISTS Cars;
                CREATE TABLE Cars (ID INT, NAME TEXT, PRICE INT);
                INSERT INTO Cars VALUES(1, "Audi", 345);
                INSERT INTO Cars VALUES(1, "Mercedes", 345);
                INSERT INTO Cars VALUES(1, "Volvo", 345, "error");
                INSERT INTO Cars VALUES(1, "Skoda", 345);
                INSERT INTO Cars VALUES(1, "Hummer", 345);
                '''
            )
    con.commit()
except lite.Error as e:
    if con:
        con.rollback()

    print("Error: %s" % e.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()
