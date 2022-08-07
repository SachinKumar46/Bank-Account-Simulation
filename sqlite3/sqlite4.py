            # input by user

import sqlite3
con = sqlite3.connect(database="mysql.sqlite")
cur = con.cursor()
empid = int(input("enter id  :  "))
empnam = input("enter name  :  ")
empsal = int(input("enter sal  :   "))
cur.execute("insert into empl values(?,?,?)", (empid, empnam, empsal))
con.commit()

# attribute error
