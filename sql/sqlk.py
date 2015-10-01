import sqlite3
with sqlite3.connect("new.db") as connection:
    c=connection.cursor()
    c.execute("""select population.city, population.population, regions.city
    from population,regions
    where population.city=regions.city""")
    rows=c.fetchall()
    for r in rows:
        print r[0],r[1],r[2]
