#!/usr/bin/env python

num  = input('Enter a number')
p = 0
i = 1
while i <= num:
 if num%i == 0:
  p = p +1
 i = i + 1

if p == 2:
 print 'Its a Prime Number'
else:
 print 'Its not a Prime Number'



