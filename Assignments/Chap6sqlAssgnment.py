import sqlite3

connection= sqlite3.connect("cars.db")
c=connection.cursor()
c.execute("""create table inventory
(Make Text, Model Text, Quantity INT)""")
connection.close()
