

"""
Generator Function, Iterations, Iteration function / expression
"""

def gsq(li):
    for i in li:
        yield i * i

li = range(1,6)
sqrs = gsq(li)
print sqrs.next()
print sqrs.next()


"""
    Generator Expression / List Comprehession
    
"""

yl = (a * a for a in range(1,6))
print yl
print next(yl)
print next(yl)
print next(yl)
print next(yl,'Finished')
print next(yl,'Finished')
print next(yl,'Finished')