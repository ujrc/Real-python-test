import sqlite3
with sqlite3.connect("cars.db") as connection:
    c=connection.cursor()
    c.execute("select *from inventory where make='Ford'")
    rows=c.fetchall()
    for row in rows:
        print row[0],row[1],row[2]
