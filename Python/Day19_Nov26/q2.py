'''
Write a python script to solve the following.

		A local shop sells three types of Laptops on Monday to Thursday- hp,sony and dell
		and the prices are 30000,35000 and 40000 respectively.
		The sales of items are
		
			Mon	Tue	wed	Thu
		hp	1	5	2	3
	
		sony	5	6	3	1	

		dell 	7	6	2	1
		
		using numpy, calculate the sales collection for each day

		(hint : matrix maltiplication)
'''


import numpy as np

price = np.array([30000,35000,40000])
print "Price \n", price
sales = np.array([[1,5,2,3],[5,6,3,1],[7,6,2,1]])
print "Sales\n", sales

s = np.dot(price,sales)
print "Ttoal Sales\n", s
