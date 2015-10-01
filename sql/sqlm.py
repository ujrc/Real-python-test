import sqlite3
with sqlite3.connect("new.db") as connection:
    c=connection.cursor()
    sql={
    "Average": "select avg(population) from population",
    "Maximum":"select max(population) from population",
    "Minimun":"select min(population) from population",
    "Sum":"select sum(population)from population",
    "Count":"select count(city) from population"
    }
    for keys, values in sql.iteritems():
        c.execute(values) # run sql
        result=c.fetchone()
        print keys+ ":", result[0]
