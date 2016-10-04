import sqlite3 as lite

cars = (
            (1, 'Audi', 52642),
            (2, 'Mercedes', 52642),
            (3, 'Skoda', 52642),
            (4, 'Volvo', 52642),
            (5, 'Bentley', 52642),
            (6, 'Hummer', 52642),
            (7, 'Volkswagen', 52642),
        )

con = lite.connect('Car.db')

with con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS CARS')
    cur.execute('CREATE TABLE CARS (ID INT, NAME TEXT, PRICE INT)')
    cur.executemany('INSERT INTO CARS VALUES (?, ?, ?)', cars)
