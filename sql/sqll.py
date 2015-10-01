import sqlite3
with sqlite3.connect("new.db") as connection:
    c=connection.cursor()
    c.execute("""select distinct population.city, population.population, regions.city
    from population,regions where population.city=regions.city
    order by population.city asc""")
    rows=c.fetchall()
    for r in rows:
        print "Cities",r[0]
        print "population",str(r[1])
        print "Region",r[2]
        print
