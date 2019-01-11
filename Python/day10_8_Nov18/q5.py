""" Exception Handling """
try:
    a = input('Enter a number:')
    b = input('Enter the divisor:')
    c = a /b
except Exception, e:
    print e
else:
    print c


    
