#!/usr/bin/env python
import sys
n = int(sys.argv[2])
l1 = [x*n for x in range(1,11)]
s = str()
for i in range(1,10):
   # print i,'x',n ,'=',l1[i]
    s = s + str(i)+'x'+str(n) +'='+str(l1[i]) +'\n'

fd = open(sys.argv[1],'w')
fd.write(s)
fd.close()
