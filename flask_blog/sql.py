import sqlite3
with sqlite3.connect("blog.db") as connection:
    c=connection.cursor()
    #create table
    c.execute("""create table posts (Title TEXT, post TEXT)""")
    # insert some data
    my_values=[
    ("Good", "I'm good."),
    ("Well", "I'm well."),
    ("Excellent", "I'm Excellent"),
    ("Okay", "I'm okay.")
    ]
    c.executemany("insert into posts values(?,?)",my_values)
