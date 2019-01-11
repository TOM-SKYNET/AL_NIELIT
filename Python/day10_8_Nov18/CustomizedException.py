
"""
    Customized Exception
"""


class MyNegError:
    pass
try:
    a = input("Number 1")
    b = input("Number 2")
    if (a == 0):
        raise MyNegError
except MyNegError:
    print "can not do the opertaion"
else:
    print 'Result:', a/b
finally:
    print 'Completed without any error'