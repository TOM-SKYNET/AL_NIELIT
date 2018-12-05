"""
	1. Develop an ML model to predict the house price for the boston
	housing dataset included in sklearn. Find out the RMSE values for
	models developed using different algorithms and select the best one.
	Also plot the scatter diagrams showing the actual and predicted values
"""

# Using KNN

from sklearn.datasets import load_boston
from sklearn.metrics import accuracy_score,confusion_matrix, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import numpy as np

iris = load_boston()
X=iris.data
y=iris.target


rf = KNeighborsRegressor()
rf.fit(X,y)
p=rf.predict(X)

print(mean_squared_error(y,p))
print(np.sqrt(mean_squared_error(y,p)))

plt.scatter(y,p)
plt.show()
