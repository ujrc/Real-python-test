import sqlite3
conn= sqlite3.connect ("new.db") #create new database
cursor= conn.cursor()
# Create a table
cursor.execute("""create table population
(city TEXT, state TEXT, population INT)""")

conn.close()
