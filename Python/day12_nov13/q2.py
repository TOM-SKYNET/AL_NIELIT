
import xml.dom.minidom as dom
import pandas as pd
import MySQLdb as db



data = pd.read_csv("emp.csv")
data = data.as_matrix()
print data
try:
    con = db.connect("127.0.0.1","ai","ai","ai")
    cur = con.cursor()
    for i in range(4):
        qs1 = "INSERT INTO emp_ai29 VALUES (%s, %s, %s, %s)", (data[i,0],data[i,1],data[i,2],round(data[i,3],2))
        cur.execute(*qs1)
        con.commit()
except Exception, e:
    print e
else:
    print 'Table created'
