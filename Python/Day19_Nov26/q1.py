'''
Write a python script to create and store a 2D array as a file by receiving 
    start and end numbers from user. The array should contain elements from 
    start to end incremented by 1. A suitable shape can be 
    decided by the programmer.0 can be used to fill columns if required.
    From this array, using conditional logic, create two new arrays , consisting of
    elements which are divisible by a given number,say dn1, in the first array
    and not divisible by dn1 in the second array.
'''


import numpy as np

s, e = input("Enter start and end of 2-D Array (start,end) :")
r, c = input("Enter the dimesion (r,c) : ")
ar = np.zeros([r*c])
index = 0
for i in range(s, e+1):
    ar[index] = i
    index +=1
ar = ar.reshape(r,c)
print ar

d = input("Enter a number as divisor:")
ar1 = ar[ar%d==0]
ar2 = ar[ar%d!=0]
print("Divisble:\n",ar1)
print("Not Divisble:\n",ar2)
