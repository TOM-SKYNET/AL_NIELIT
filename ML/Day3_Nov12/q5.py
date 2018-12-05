"""
	5. Develop an ML model to predict the average parking rates per month for a city
	from the city related data (city.csv)
"""
# Using Linear Regression

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from  sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv("city.csv")
print (data.head())
data=data.as_matrix()
print(data)
X=data[:,[2,3,4,5]]
y=data[:,-2]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
lr=LinearRegression()
lr.fit(X_train,y_train)
p=lr.predict(X_test)

plt.scatter(y_test,p)
plt.show()
