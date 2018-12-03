
"""
	0.import pandas
	1.create a dataframe object from a (10,4)2D array  consisting of random integers between 10 and 20 by making c1,c2,c3,c4 as column indices.
	2.Sort the above oject based on the key 'c1' in ascending and then by 'c3' in descending order.
	3.write script to store item,place and total sale in a dataframe object.There should be 3 or more places and 4 or more items in the set.
	     Based on the choice entered by user,
           (ii) show placewise rank for a particular item (for a given item name).
	   (iii)Show itemwise rank for a particular place (for a given place name).
	4.switch to home directory and send the output of ls -l command to a file named lsf1
	5.create another file lsf2 by replacing all the spaces with ',' use tr command tr ' ' ',' < lsf1 > lsf2
	6.create another file lsf3 by squeezing multiple ',' use tr command - tr -s ',' < lsf2 > lsf3
	7.using pandas read the file lsf3 and sort it based on file size (fifth column)
	8.write the above dataframe obj (sorted) to a new file named lsf5
"""
import numpy as np
import pandas as pd
from pandas import Series as s
from pandas import DataFrame as df

# Q1
df1 = df(np.random.randint(10,20,40).reshape(10,4))
df1.columns=list("C1 C2 C3 C4".split())
print (df1)

# Q2
print("---------------------------------")
print(df1.sort_values(['C1','C3'],ascending=[True,False]))

# Q3
d = {'Item' : s(["Item 1", "Item 2", "Item 3", "Item 4"]),
     'Place' : s(["Calicut", "Kochi", "Kollam", "Trivandrum"]),
     'Total Sales' : s([100,200,150,175])}
df2 = df(d)
print("---------------------------------")
print (df2)
print ("----------------Ranking----------------")
df2['Rank by Item'] = df2['Item'].rank(method='dense')
df2['Rank by Place'] = df2['Place'].rank()
print(df2)

# Q4, 5, 6, 7
df3 = pd.read_csv("lsf3",header=None, names='dir id owner group size month day time file_name'.split())

print(df3)
print("------------ Sorted ---------")
df5 = df3.sort_values(['size'])
print(df5)


# Q8
df5.to_csv("lsf5.csv")
print("Dataframe object saved to lsf5.csv")