

def div_f(d1,d,d2=2):
    di1 = d1/d
    di2 = d2/2
    return [di1,di2]

d1 = input('Enter 1 number')
d2 = input('Enter 2 number')
d = input('Enter the divisor')

r = div_f(d1,d,d2)
print 'Result of 1 ==' , r[0]
print 'Result of 2 ==' , r[1]

r = div_f(d1,d)
print 'Result of 1 ==' , r[0]
print 'Result of 2 ==' , r[1]
