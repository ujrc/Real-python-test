import sqlite3

with sqlite3.connect("cars.db") as connection:
    c=connection.cursor()
    my_cars=[
    ('Ford','Taurus',20),
    ('Ford','Fusion',12),
    ('Ford','Lightning',16),
    ('Honda','Fit',22),
    ('Honda','Insight',18)]
    c.executemany('insert into inventory values(?,?,?)',my_cars)
