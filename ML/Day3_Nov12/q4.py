"""
	4. Apply Linear Regression on any suitable dataset from this
	(https://people.sc.fsu.edu/~jburkardt/datasets/regression/regression.html)
	link
	Split the data as train and test sets before developing the model. Plot the actual
	and predicted points for test data. Obtain mean squared error & RMSE value
"""
# using LinearRegression

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from  sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv("x06.txt" , delimiter ="\s+")
print (data.head())
data=data.as_matrix()
print(data)
X = data[:,[1,2]]
y = data[:,-1]
print(X)
print(y)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
lr = LinearRegression()
lr.fit(X_train,y_train)
p = lr.predict(X_test)
print('Mean Absolute Error' ,round(metrics.mean_absolute_error(y_test,p),2))
print('Mean Squred Error',round(metrics.mean_squared_error(y_test,p),2))
print('SQRT Mean Squred Error',np.sqrt(metrics.mean_squared_error(y_test,p)))

plt.scatter(y_test,p)
plt.show()
