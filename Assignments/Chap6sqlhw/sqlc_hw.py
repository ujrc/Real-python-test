import sqlite3

with sqlite3.connect("cars.db") as connection:
    c=connection.cursor()
    c.execute("update inventory set quantity=? where model= ?",(32,"Lightning"))
    c.execute("update inventory set quantity=35 where model='Insight'")
    print "\nNew Records: \n"
    c.execute("select *from inventory")
    rows=c.fetchall()
    for row in rows:
        print row[0],row[1],row[2]
