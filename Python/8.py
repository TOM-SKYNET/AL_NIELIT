#!/usr/bin/env python

def dist(x1,y1,x2,y2):
 x=(x2-x1)**2
 y=(y2-y1)**2
 d=(x+y)**.5
 return d

print 'Enter the Cordinates of Ist point'
x1=input()
y1=input() 
print 'Enter the Cordinates of 2st point'
x2=input()
y2=input()
print 'Dist', dist(x1,y1,x2,y2)

