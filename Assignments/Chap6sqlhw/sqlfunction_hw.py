import sqlite3
with sqlite3.connect("cars.db") as connection:
    c=connection.cursor()
    c.execute("select inventory.make, inventory.model, inventory.quantity,\
     count(orders.order_date) as count from orders,inventory  where inventory.model=orders.model group by orders.model")
    rows=c.fetchall()
    for r in rows:
        print "Make: {}  Model: {}".format(r[0],r[1])
        print "quantity: {}".format(r[2])
        print "Count: {} ".format(r[3])
