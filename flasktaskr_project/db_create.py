from project import db
from project._config import DATABASE_PATH
import sqlite3
#create the  database and the db table
db.create_all()
with sqlite3.connect(DATABASE_PATH) as connection:
    c=connection.cursor()
    c.execute ("""UPDATE users
    SET name=?,role=?
    WHERE id=?
    """, ('admin','admin',4))

#commit changes
db.session.commit()
