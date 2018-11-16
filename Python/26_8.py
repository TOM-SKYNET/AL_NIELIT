#!/usr/bin/env python
def func(n):
 if n == 1:
  print n
 else:
  print n , func(n-1)

num  = input('Enter a number')
func(num)



