'''
Write a python script(using numpy) to solve the following.

		A group of people took a trip on a bus at Rs.3.00 per child and Rs.3.20 per adult for 
 		a total of Rs.118.40
 		They took the train back at Rs.3.50 per child and Rs.3.60 per adult for 
		a total of Rs.135.20
		Print the number of children and adults.
		(hint : matrix multiplication and inverse to get the effect of division)
'''


import numpy as np

a = np.array([[3.0,3.2],[3.5,3.6]])
print "Fares \n"
print "------------------------ \n",a
c = np.array([118.4,135.2])
#print "Total Fares \n"
print "------------------------ \n",c
ai = np.linalg.inv(a)
xy = np.dot(ai,c)
print "------------------------ \n"
print "Inversse \n", ai
print "------------------------ \n"
print "No of Children , Adults\n"
print "\t", np.rint(xy)
