#!/usr/bin/env python
import sys
fd = open(sys.argv[1],'w')
l1 = [x*int(sys.argv[2]) for x in range(1,11)]
s = str()
for i in range(1,11):
    s = s + str(i)+'x'+str(n) +'='+str(l1[i]) +'\n'

fd.write(s)
fd.close()
