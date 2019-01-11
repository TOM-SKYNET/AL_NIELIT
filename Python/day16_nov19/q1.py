"""
    Calculator / calc program in GUI using Tkinter

    	1. Develop a calculator application using Tkinter.


"""

from Tkinter import *
mwin=Tk()

vexp=''
def bhan(ch):
    global vexp
    if ch == '=':
        vexp = str(eval(vexp))
    elif ch == 'C':
        vexp = ''
    else:
        vexp += ch
    t1.set(str(vexp))


mwin.title('CALC')
mwin.geometry('375x380')
t1=StringVar()
e1=Entry(mwin,textvariable=t1)
fnt = ('Times',20,'bold')
e1.config(font=fnt)
b1=Button(mwin,text='1',height=5, width=5,command=lambda:bhan('1'))
b2=Button(mwin,text='2',height=5, width=5,command=lambda:bhan('2'))
b3=Button(mwin,text='3',height=5, width=5,command=lambda:bhan('3'))
b4=Button(mwin,text='4',height=5, width=5,command=lambda:bhan('4'))
b5=Button(mwin,text='5',height=5, width=5,command=lambda:bhan('5'))
b6=Button(mwin,text='6',height=5, width=5,command=lambda:bhan('6'))
b7=Button(mwin,text='7',height=5, width=5,command=lambda:bhan('7'))
b8=Button(mwin,text='8',height=5, width=5,command=lambda:bhan('8'))
b9=Button(mwin,text='9',height=5, width=5,command=lambda:bhan('9'))
b0=Button(mwin,text='0',height=5, width=5,command=lambda:bhan('0'))
bfp=Button(mwin,text='.',height=5, width=5,command=lambda:bhan('.'))
bp=Button(mwin,text='+',height=5, width=5,command=lambda:bhan('+'))
bm=Button(mwin,text='-',height=5, width=5,command=lambda:bhan('-'))
bd=Button(mwin,text='/',height=5, width=5,command=lambda:bhan('/'))
bmu=Button(mwin,text='X',height=5, width=5,command=lambda:bhan('*'))
be=Button(mwin,text='=',height=5, width=5,command=lambda:bhan('='))
bc=Button(mwin,text='C',height=5, width=5,command=lambda:bhan('C'))

e1.grid(row=0,column=0,columnspan=4)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)
b0.grid(row=4,column=0)
bfp.grid(row=4,column=1)
bp.grid(row=4,column=2)
bm.grid(row=5,column=0)
bd.grid(row=5,column=1)
bmu.grid(row=5,column=2)
bc.grid(row=6,column=0)
be.grid(row=6,column=2)

mwin.mainloop()
