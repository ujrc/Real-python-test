import sqlite3
import csv

with sqlite3.connect("new.db") as connection:
    c=connection.cursor()
    employees=csv.reader(open("employees.csv","rU")) # open csv file
    c.execute("create table employees (firstname TEXT, lastname TEXT)")#create employees table
    c.executemany('insert into employees values(?,?)',employees)# insert recods from employees csv into employees table
