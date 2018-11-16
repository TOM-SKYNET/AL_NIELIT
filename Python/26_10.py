#!/usr/bin/env python
def fact(n):
 if n == 1:
  return 1
 else:
  return n * fact(n-1)

num  = input('Enter a number')
print 'Factorial Value',fact(num)



