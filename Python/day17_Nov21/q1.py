"""

	1. open a python interpreter
	2. import numpy
	3. create a 1D array having 5 elements (integers) using array method
	4. do 3 using arange
	5. create a 3 dimensional array containing 1s(integers), there should be 40 members
	6. print the total number of elements (size) for the above array
	7. Check and explain the difference between array and asarray
	8. Create an identity mtrix of a given specification.
	9. Create an array containing 0s inheriting shape from the array created in Q.No.5
	10.Print the size,shape,dimensions and datatype of all the above arrays.

"""



# Q2
import numpy as np

# Q3
a1 = np.array([1,2,3,4,5])
print(a1)
print(a1.dtype)

# Q4
a2 = np.arange(1,6)
print(a2)
print(a2.dtype)
print("a1 is a2 =", a1 is a2)

# Q5
a3 = np.ones([2,2,10])
print(a3)

# Q6
print("Size:", a3.size)

# Q7. Check and explain the difference between array and asarray

a4 = np.asarray(a3)
print("a4 is a3 =", a4 is a3)
a5 = np.array(a3)
print("a5 is a3 =", a5 is a3)

# Q8. Create an identity mtrix of a given specification.

n =4
#n = input("Enter Identify Matrix:")
a6 = np.identity(n)
print("Identity Matrix:\n",a6)
print("Size:", a6.size)
print("Shape:",a6.shape)
print("Dimension:", a6.ndim)
print("Data Type:",a6.dtype)

# Q9.Create an array containing 0s inheriting shape from the array created in Q.No.5
a7 = np.zeros_like(a3)
print(a7)


# Q10.Print the size,shape,dimensions and datatype of all the above arrays. 
print("Size:", a7.size)
print("Shape:",a7.shape)
print("Dimension:", a7.ndim)
print("Data Type:",a7.dtype)
