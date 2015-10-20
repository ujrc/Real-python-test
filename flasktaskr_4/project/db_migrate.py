from views import db
from _config import DATABASE_PATH
import sqlite3
#from datetime import datetime
#with sqlite3.connect(DATABASE_PATH) as connection:
    #c=connection.cursor()
    #c.execute("""alter table tasks Rename to old_tasks""")
    #db.create_all()
    #c.execute("""select name, due_date, priority, status from old_tasks order by task_id ASC""")
    #data=[(row[0],row[1],row[2],row[3], datetime.now(),1) for row in c.fetchall()]
    #c.executemany("""insert into tasks(name, due_date,priority,status,
    #posted_date,user_id) values(?,?,?,?,?,?)""",data)

    #delete old _tasks
    #c.execute("drop table old_tasks")
with sqlite3.connect(DATABASE_PATH)as connection:
    #Get cursor object used to execute SQL commands
    c=connection.cursor()
    #Temporarily change the name of users table
    #c.execute("""alter table users rename to old_users""")

    # recreate a new users table with updated schema
    db.create_all()
    #retrieve data from old table
    c.execute("""select name, email, password from old_users order by id ASC""")

    #Save all rows as a list of tuples;set role to 'user'
    data=[(row[0],row[1],row[2],'user')for row in c.fetchall()]

    #insert data into table
    c.executemany("""insert into users (name,email,password,role)
    values(?,?,?,?)""",data)
    #delete older_users table
    c.execute("drop table old_users")
