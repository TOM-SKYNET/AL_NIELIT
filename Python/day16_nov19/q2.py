import psycopg2 as psql
import sys
from Tkinter import *


"""
    Function section for all events - START
"""

def clicked(ch):
    if ch == '+':
        addRecord(db_init(), txtId.get(),txtName.get(),txtAge.get(), txtAddress.get(),txtBasic.get())
    elif ch == 'd':
        displayRecords(db_init())
    elif ch == 'x':
        window.destroy()

def db_init():
    con = None
    cur = None
    try:
        con = psql.connect(host="127.0.0.1", dbname="krista", user="krista", password="krista")
    except psql.DatabaseError as de:
        print(de)
    else:
        return con

def addRecord(con, id , name , age, address, basic):
    try:
        cur = con.cursor()
        sql = "insert into company values(%s, %s, %s, %s, %s)"
        cur.execute(sql, (id, name, age, address, basic))
        con.commit()
        cur.close()
    except psql.DatabaseError as de:
        print(de)
        if con:
            con.rollback()
    else:
        print("1 row inserted")

def displayRecords(con):
    try:
        cur = con.cursor()
        sql = "select id, name, age, address, salary from company order by id"
        cur.execute(sql)
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
    except psql.DatabaseError as de:
        print(de)



"""
    Function section for all events - END
"""

# GUI Section : START

window = Tk()
window.title("Database Entry Application")
window.geometry("400x380")

lblId = Label(window, text="ID")
lblId.grid(column=0, row=1)
txtId = Entry(window,width=10)
txtId.grid(column=1, row=1)

lblName = Label(window, text="Name")
lblName.grid(column=0, row=2)
txtName = Entry(window,width=10)
txtName.grid(column=1, row=2)

lblAge = Label(window, text="Age")
lblAge.grid(column=0, row=3)
txtAge = Entry(window,width=10)
txtAge.grid(column=1, row=3)

lblAddress = Label(window, text="Address")
lblAddress.grid(column=0, row=4)
txtAddress = Entry(window,width=10)
txtAddress.grid(column=1, row=4)

lblBasic = Label(window, text="Salary")
lblBasic.grid(column=0, row=5)
txtBasic = Entry(window,width=10)
txtBasic.grid(column=1, row=5)

# All Action Buttons
btnAdd = Button(window, text="Add Record", command=lambda:clicked('+'))
btnAdd.grid(column=0, row=6)
btnDisp = Button(window, text="Display", command=lambda:clicked('d'))
btnDisp.grid(column=1, row=6)
btnClose = Button(window, text="Close", command=lambda:clicked('x'))
btnClose.grid(column=2, row=6)

window.mainloop()


# GUI Section : END
