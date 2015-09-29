import sqlite3
conn= sqlite3.connect("new.db")
cursor=conn.cursor()
cursor.execute("insert into population Values('New York City',\
'NY',8200000)")
cursor.execute("Insert into population values('San Francisco',\
'CA',800000)")
conn.commit()
conn.close()
