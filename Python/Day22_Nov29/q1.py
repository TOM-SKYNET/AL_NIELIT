'''
    1.import pandas library
    2.create a dataframe obj from a dict of lists of your own choice(other than population)  
'''

from pandas import DataFrame as df
from pandas import Series as s
import numpy as np

ds = {'Name':['Raj','Rony','Roy','Tom'],'No':[28,29,30,32],'Salary':[10000,11000,12000,13000]}

df1 = df(ds)
print ds
print df1

# Q 3.Add another column on the above object and insert values.

df1 = df(ds,columns="Name No Salary HRA".split())
print df1
df1['HRA'] = [1200,1300,1400,1500]
print df1

# Q 4.create a dataframe obj from a series obj of your own choice.

li = (10,20,30,40,50)
s1 = s(li)
print "----------------------------------"
print s1
s1.index = list('abcde')
print s1

# Q 5.create a dataframe obj from the above series obj(Qno.4) after assigning a value for name attribute.

s1.name ="Frequency"
df2 = df(s1)
print "----------------------------------"
print df2

# Q 6.create a dataframe object from a numpy 2D array by giving values for columns and index of your own choice.
ar = np.array([1,2,3],[4,5,6][7,8,9])
print "------------------------------------"
print ar
df3 = df(ar)
print "------------------------------------"
print df3
