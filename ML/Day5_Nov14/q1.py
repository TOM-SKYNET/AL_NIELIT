"""
	1) Suppose you are the CEO of a restaurant franchise and are considering
	different cities for opening a new outlet. The chain already has outlets in
	various cities and you have data for profits and populations from the cities.
	You would like to use this data to help you select which city to expand to
	next. The file ex1.txt contains data for the problem. The first column is
	population of a city and second column is profit. Both values are in 10,000s.
	A negative value of profit indicates a loss.
		a) Create a scatterplot between population and profits
		b) Develop an ML model to predict profit for a given city (by providing population)
"""
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from  sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("ex1.txt", delimiter = ",")
data = data.as_matrix()
print data
profit=data[:,[1]]
population=data[:,0]
print(population)
print(profit)

plt.scatter(profit,population)
plt.show()

X_train,X_test,y_train,y_test=train_test_split(population,profit,test_size=0.2)
lr=LinearRegression()
lr.fit(X_train,y_train)
p=lr.predict(X_test)

print(metrics.mean_absolute_error(y_test,p))
print(metrics.mean_squared_error(y_test,p))
print(np.sqrt(metrics.mean_squared_error(y_test,p)))

#plt.scatter(y_test,p)
#plt.show()




