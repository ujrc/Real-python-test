import sqlite3
with sqlite3.connect("new.db")as connection:
    c=connection.cursor()
    #c.execute("""create table Regions (City TEXT,Region TEXT)""")
    cities=[
    ('New York City', 'Northeast'),
('San Francisco', 'West'),
('Chicago', 'Midwest'),
('Houston', 'South'),
('Phoenix', 'West'),
('Boston', 'Northeast'),
('Los Angeles', 'West'),
('Houston', 'South'),
('Philadelphia', 'Northeast'),
('San Antonio', 'South'),
('San Diego', 'West'),
('Dallas', 'South'),
('San Jose', 'West'),
('Jacksonville', 'South'),
('Indianapolis', 'Midwest'),
('Austin', 'South'),
('Detroit', 'Midwest')
]
    c.executemany("insert into  Regions values(?,?)",cities)
    c.execute("select *from Regions Order by region asc")
    rows=c.fetchall()
    for row in rows:
        print row[0],row[1]
