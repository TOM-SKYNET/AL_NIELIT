import mymod

while 1:
    print '1. Initialize \n 2. Show \n 3. Reload \n 0. Exit'
    i = input('Enter your choice')
    if i == 0:
        break
    elif i == 1:
        a = input('Enter value of a')
        b = input('Enter value of b')
        c = input('Enter value of c')
        d = input('Enter value of d')
        e = input('Enter value of e')
        mymod.a = a
        mymod.b = b
        mymod.c = c
        mymod.d = d
        mymod.e = e
    elif i ==2:
        con = mymod.a + (10 * mymod.b *mymod.c) - (5*mymod.d)/mymod.e
        print 'Result ::',con
    elif i == 3:
        print 'reloading'
        reload (mymod)


