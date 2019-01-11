
"""
Open python interpreter and do the following.

	1.Create an integer(32bit) array of shape 2,3

	2.Create another array using the values from the above array (Qno.1) but with a type of float64

	3.Create another array using the values from the above array (Qno.1) but with a type of int64

	4.Create another array using the values from the above array (Qno.1) but with a type of str

	5.Create another array using the values from the above array (Qno.4) but with a type of str


	6. create a 2 dimensional array conating 4 rows and 3 columns each and do different slicing operations and note your findings
		 	-> select first row
			-> select third row
			-> select second column
		   	-> select first two elements of second and third rows
			-> select last element of each row
				etc.


	7.Create a numpy array(with a suitable shape) to store numbers from 11 to 50.
		using boolean indexing, replace all the numbers that are multiples of 5 with -1.


	8.Write a function to return diagonal elements of an array(NxN) as an array.

	9.Write a function to return the number of occurences of a given element in a numpy array.

	10.Modify the above function (Q.No.8) to accept array of any shape and to return the
 	    diagonal elements of the highest possible NxN array constructed from the given array.
"""


import numpy as np

# Q1 Create an integer(32bit) array of shape 2,3

a1 = np.array([[1,2,3],[4,5,6]],dtype="i4")
print("----------------------------------------------------------------")
print("Shape:", a1.shape)
print("Dimension:",a1.ndim)
print("Dtype:",a1.dtype)
print a1

#Q2 Create another array using the values from the above array (Qno.1) but with a type of float64
a2 = np.array(a1, dtype="f8")
print("----------------------------------------------------------------")
print("Shape:", a2.shape)
print("Dimension:",a2.ndim)
print("Dtype:",a2.dtype)
print a2

#Q3 Create another array using the values from the above array (Qno.1) but with a type of int64
a3 = np.array(a1, dtype="i8")
print("----------------------------------------------------------------")
print("Shape:", a3.shape)
print("Dimension:",a3.ndim)
print("Dtype:",a3.dtype)
print a3

#Q4 Create another array using the values from the above array (Qno.1) but with a type of str
a4 = a1.astype(np.str)
print("----------------------------------------------------------------")
print("Shape:", a4.shape)
print("Dimension:",a4.ndim)
print("Dtype:",a4.dtype)
print a4

#Q5 Create another array using the values from the above array (Qno.4) but with a type of str
a5 = a3.astype(np.str)
print("----------------------------------------------------------------")
print("Shape:", a5.shape)
print("Dimension:",a5.ndim)
print("Dtype:",a5.dtype)
print a5

#Q6 Create a 2 dimensional array conating 4 rows and 3 columns each and do different slicing operations and note your findings
a6 = np.ones((4,3))
print("----------------------------------------------------------------")
print("Shape:", a6.shape)
print("Dimension:",a6.ndim)
print("Dtype:",a6.dtype)
#print a6
#print a6[0,0:]
for i in range(4):
    for j in range(3):
        a6[i][j] =  i * 3 + j
print a6
print 'First Row :', a6[0,:]
print 'Third Row : ', a6[2][:]
print "Second Column 2-D: ", a6[:,[1]] # 2d
print "Second Column 1-D: ", a6[:,1] # 1d
print "First 2 Elements of 2 , 3 rows : \n", a6[1:3,:2]
print "Last Element of each row \n", a6[:,2:]

#Q7 Create a numpy array(with a suitable shape) to store numbers from 11 to 50.
#   using boolean indexing, replace all the numbers that are multiples of 5 with -1.
a7 = np.arange(11,51)
print len(a7)
a7 = a7.reshape(10,4)
print a7

a7[a7%5 == 0]= -1
print "a7[a7%5 == 0]= -1 \n" , a7


# Q8 Write a function to return diagonal elements of an array(NxN) as an array.
def diag(arr):
    arrc = np.zeros((arr.shape[0],arr.shape[0]))
    for i in range(arr.shape[1]):
        arrc[i,i] = arr[i,i]
    return arrc

def diag1(arr):
    ar = np.array(arr).reshape(arr.shape[0],arr.shape[0])
    ar[1,0] = arr[0,1]
    return ar


a8 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Shape 0:", a8.shape[0])
print("Shape 1:", a8.shape[1])
print("np.newaxis :", np.newaxis)
print("Dimension:", a8.ndim)
print a8
print diag(a8)
print "-------------------------------"
print diag1(a8)

# Q9 Write a function to return the number of occurences of a given element in a numpy array.
def noofOccuOfMatrix(mat,n):
    return np.count_nonzero(mat == n)
    #return np.where(mat == n)


a9 = np.array([[1,4,3],[4,5,6],[4,8,9],[10,11,12]])
print a9
print "No of Occurences :", noofOccuOfMatrix(a9,4)

# Q10 Modify the above function (Q.No.8) to accept array of any shape and to return the
#  	  diagonal elements of the highest possible NxN array constructed from the given array.
# Solu: Find factor and reshape the array