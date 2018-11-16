#!/usr/bin/env python
def findGreatest(n1,n2,n3):
 if n1 > n2 :
  if n1 > n3 :
   print 'Greatest value', n1
  else:
   print 'Greatest value', n3
 elif n2 > n3 :
  print 'Greatest value', n2
 else:
  print 'Greatest value', n3

n1 = input('Enter 1st value')
n2 = input('Enter 2 value')
n3 = input('Enter 3 value')
findGreatest(n1,n2,n3)


