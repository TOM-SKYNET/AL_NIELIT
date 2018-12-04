"""
Open python interpreter/ipython and do the following.

	0.import pandas
	1.Create a (4,4) 2D array  consisting of integers.
	2.Create a masked array from the above array by making numbers which are divisible by 3 as invalid values.
	3.Create a dataframe from the above masked array.
	4.Create a series of your own choice and do reindexing by exploring ffill,bfill,nearest etc
	5.Create a Dataframe object of your own choice and do reindexing.
	6.Create a (4,4)2D array  consisting of integers.
	7.create a dataframe object from the above array by making c1,c2,c3,c4 as column indices and r1,r2,r3,r4 as row indices.
		2.1 Using integer based indexing print the very first element(row 0, column 0) as a scalar,as a series,and as a dataframe.
		2.2 do 2.1 using label based indexing
		2.3 Print last two rows and columns

	8.Create another (4,4) 2D array  consisting of integers, with c1,c2,c5,c6 as column indices and r3,r4,r5,r6 as row indices
		Create a dataframe from this array and do the following,
		a) add the two dataframes(QNo.7) using '+' operator,withoou any NaN in the result
		b) add the two dataframes using 'add' method,withoou any NaN in the result
	9.Create DataFrame obj(shape 3,4) and from that create two Series objs(one for axis 0,other for axis 1)
		perform subtraction operation for both cases(along the two axes)

"""

import pandas as pd
import numpy as np
import re

# Q 1.Create a (4,4) 2D array  consisting of integers.
ar = np.arange(1,17).reshape(4,4)
print ar

# Q 2.Create a masked array from the above array by making numbers which are divisible by 3 as invalid values.
ma = np.ma.masked_array(ar, mask=ar%3==0)
print ma

# Q 3.Create a dataframe from the above masked array.
df = pd.DataFrame(ma)
print df

# Q Create a series of your own choice and do reindexing by exploring ffill,bfill,nearest etc
l = (11,12,np.nan,34,np.nan,28, np.nan)
s = pd.Series(l)
s.index=list('abcdefg')
s1 = s.copy()

print s1.reindex(list('abcdefg'), method='ffill')

s2 = s.copy()
print s2.reindex(list('abcdefg'), method='bfill')

s3 = s.copy()
print s3.reindex(list('abcdefg'), method='pad')

# Q 5.Create a Dataframe object of your own choice and do reindexing.
ar = np.arange(1,21).reshape(4,5)
df = pd.DataFrame(ar, index = ['a','b','c','d'], columns=['Col1','Col2','Col3','Col4','Col5'])
print df
df1 = df.reindex(index = ['a','b','c','d','e'], columns=['Col1','Col2','Col3','Col4','Col5','Col6'])
print df1

# Q 6.Create a (4,4)2D array  consisting of integers.
ar = np.random.randint(1,17,16).reshape(4,4)
print ar

# Q 7.create a dataframe object from the above array by making c1,c2,c3,c4 as column indices and r1,r2,r3,r4 as row indices.

df = pd.DataFrame(ar, index="r1 r2 r3 r4".split(), columns="c1 c2 c3 c4".split())
print df

# 		2.1 Using integer based indexing print the very first element(row 0, column 0) as a scalar,as a series,and as a dataframe.
print df.iloc[0][0]
print df.iloc[0]
print df.iloc[[0]]
# 		2.2 do 2.1 using label based indexing
print df.loc['r1'][0]
print df.loc['r1']
print df.loc[['r1']]

# 2.3 Print last two rows and columns
print df.loc[['r3','r4'],['c3','c4']]

# Q 8.Create another (4,4) 2D array  consisting of integers, with c1,c2,c5,c6 as column indices and r3,r4,r5,r6 as row indices
# 		Create a dataframe from this array and do the following,

df1 = pd.DataFrame(ar, index="r3 r4 r4 r6".split(), columns="c1 c2 c5 c6".split())
print df1

# 		a) add the two dataframes(QNo.7) using '+' operator,withoou any NaN in the result
df3 = df + df1
#df3 = df3.applymap(lambda n: re.sub('[^0-9\.]','',str(n)))
df3 = df3.fillna(0)
print df3


# 		b) add the two dataframes using 'add' method,withoou any NaN in the result
df4 = df.add(df1,fill_value=0)
print df4

# Q 9.Create DataFrame obj(shape 3,4) and from that create two Series objs(one for axis 0,other for axis 1)
# 		perform subtraction operation for both cases(along the two axes)
idx = "r1 r2 r3"
cols = "c1 c2 c3 c4"
df = pd.DataFrame(np.arange(1,13).reshape(3,4), index=idx.split(),columns=cols.split())
print df
sr1 = df.iloc[0]
print sr1
sc1 = df['c1']
print sc1

print 'df - sr1\n', df - sr1 # just for testing what will happen
print 'df - sc1\n', df - sc1 # just for testing what will happen
print 'sub axis =0\n', df.sub(sc1, axis=0)
print 'sub axis =1\n', df.sub(sr1, axis=1)