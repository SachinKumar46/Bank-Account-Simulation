import sqlite3
con=sqlite3.connect(database="mydb.sqlite")
cur=con.cursor()
#cur.execute("create table emp(empid integer primary key,empname text,empsal integer)")
cur.execute("insert into emp values(12,'sachin',12000)")
cur.execute("insert into emp values(11,'mayank',1000)")
cur.execute("insert into emp values(34,'raghav',234000)")
con.commit()
#attribute error