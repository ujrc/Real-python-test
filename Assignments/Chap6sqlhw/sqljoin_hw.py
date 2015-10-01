import sqlite3
import time
from datetime import date
with sqlite3.connect("cars.db") as connection:
    c=connection.cursor()
    c.execute("""create table Orders(make TEXT, model TEXT, order_date date)""")
    my_cars=[
    ('Ford','Taurus','2014-05-18'),
    ('Ford','Taurus','2015-01-30'),
    ('Ford','Taurus','2014-02-34'),
    ('Ford','Fusion','2014-08-12'),
    ('Ford','Fusion','2014-08-30'),
    ('Ford','Fusion','2014-12-13'),
    ('Ford','Lightning','2012-09-12'),
    ('Ford','Lightning','2013-03-23'),
    ('Ford','Lightning','2013-04-16'),
    ('Honda','Fit','2015-03-22'),
    ('Honda','Fit','2015-04-12'),
    ('Honda','Fit','2015-08-21'),
    ('Honda','Insight','2013-07-18'),
    ('Honda','Insight','2011-06-28'),
    ('Honda','Insight','2015-11-19')
    ]
    c.executemany("insert into orders values(?,?,?)",my_cars)
    c.execute("select inventory.make, inventory.model,\
     inventory.quantity, orders.order_date from inventory, orders where inventory.make=orders.make")
    rows=c.fetchall()
    for r in rows:
         print "Make: {}, Model:{}".format(r[0],r[1])
         print "Quantity: {}".format(r[2])
         print "Order Date: {}".format(r[3])
         print
