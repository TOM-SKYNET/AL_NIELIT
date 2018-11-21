import psycopg2 as psql
import sys

con = None
try:
    con = psql.connect(host="127.0.0.1", dbname="krista", user="krista", password="krista")
    cur = con.cursor()
    cur.execute("insert into company values(101,'Krista',5,'Kodanchery',9999.95)")
    con.commit()
    print("1 row inserted")
except Exception,e:
    print(e)

finally:
    if con:
        con.close()

