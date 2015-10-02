import sqlite3
from _config import DATABASE_PATH
with sqlite3.connect('flasktaskr.db') as connection:
    c=connection.cursor()
    # Create dummy data into table
    c.execute("""create table tasks (task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)""")
    # Insert table
    c.execute("insert into tasks (name, due_date, priority,status)"
    "Values('Finish this tutorial','03/25/2015',10,1 )")
    c.execute('insert into tasks(name, due_date,priority,status)'
    'Values("Finish Real Python course 2 ","03/25/2015",10,1)')
