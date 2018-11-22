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

