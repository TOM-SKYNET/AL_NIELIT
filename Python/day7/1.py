#!/usr/bin/env python
n = input('Enter a number')
l1 = [x*n for x in range(1,11)]
s = str()
for i in range(1,11):
   # print i,'x',n ,'=',l1[i]
    s = s + str(i)+'x'+str(n) +'='+str(l1[i]) +'\n'

fd = open('ml','w')
fd.write(s)
fd.close()
