#Working with multiple tables
import sqlite3
with sqlite3.connect("new.db") as connection:
    c=connection.cursor()
    cities=[
('Boston', 'MA', 600000),
('Los Angeles', 'CA', 38000000),
('Houston', 'TX', 2100000),
('Philadelphia', 'PA', 1500000),
('San Antonio', 'TX', 1400000),
('San Diego', 'CA', 130000),
('Dallas', 'TX', 1200000),
('San Jose', 'CA', 900000),
('Jacksonville', 'FL', 800000),
('Indianapolis', 'IN', 800000),
('Austin', 'TX', 800000),
('Detroit', 'MI', 700000)
]
    c.executemany("Insert into population values(?,?,?)",cities)
    c.execute("select *from population where population>1000000")
    rows=c.fetchall()
    for row in rows:
        print row[0],row[1],row[2]
