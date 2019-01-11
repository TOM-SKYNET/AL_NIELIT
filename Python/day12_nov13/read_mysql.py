"""
    Read from MySQL database

    To connect the host : mysql -u ai -p
"""

import MySQLdb as db


try:
    con = db.connect('127.0.0.1',"ai","ai","ai")
    cur = con.cursor()
    sql = "select curdate"
    res = cur.execute(sql).fetchall() # fetchll returns tuple object
except Exception, e:
    print e
else:
    print res