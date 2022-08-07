           #fatch all result(with the help of salect*)

import sqlite3
con=sqlite3.connect(database="mysql.sqlite")
cur=con.cursor()
cur.execute("select* from empl")
for i in cur:
    print(i)
con.commit()    
    
#attribute error