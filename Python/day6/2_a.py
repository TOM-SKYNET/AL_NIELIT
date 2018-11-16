

# 2-a
def div_f(**d):
    q = d['a']/d['c']
    r = d['b']/d['c']
    return [q,r]

# c
def div_q_r(**d):
    q = d['a']/d['c']
    r = d['a']%d['c']
    return [q,r]
d1 = input('Enter 1 number')
d2 = input('Enter 2 number')
d = input('Enter the divisor')

r = div_f(a=d1,b=d2,c=d)
print 'Result of 1 ==' , r[0]
print 'Result of 2 ==' , r[1]


r = div_q_r(a=d1,b=d2,c=d)
print 'Quotient ==' , r[0]
print 'Remider ==' , r[1]
