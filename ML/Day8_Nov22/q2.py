"""
	2. Apply different ML models for regression to suitable dataset from the
	below link. Obtain RMSE values and scatter plots.
	link ( https://people.sc.fsu.edu/~jburkardt/datasets/regression/regression.html )
"""

from sklearn.datasets import load_boston
from sklearn.metrics import accuracy_score,confusion_matrix, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Ridge, Lasso
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# url = "https://people.sc.fsu.edu/~jburkardt/datasets/regression/x03.txt"
# https://people.sc.fsu.edu/~jburkardt/datasets/regression/x28.txt

data = pd.read_csv("x28.txt", delimiter="\s+")
print data.head()
d = data.as_matrix()
X = d[:,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
y = d[:,[16]]
print(data.head)

# Models RandonForestRegression
rfr = RandomForestRegressor()
rfr.fit(X,y)
rfrp=rfr.predict(X)

print(mean_squared_error(y,rfrp))
print(np.sqrt(mean_squared_error(y,rfrp)))


# Model for KNN
knn = KNeighborsRegressor()
knn.fit(X,y)
knnp=knn.predict(X)

print(mean_squared_error(y,knnp))
print(np.sqrt(mean_squared_error(y,knnp)))

# Model for Ridge
ridge = Ridge(0.5)
ridge.fit(X,y)
ridge_p=ridge.predict(X)

print(mean_squared_error(y,ridge_p))
print(np.sqrt(mean_squared_error(y,ridge_p)))

# Model for Lasso
lasso = Lasso()
lasso.fit(X,y)
lasso_p=lasso.predict(X)

print(mean_squared_error(y,lasso_p))
print(np.sqrt(mean_squared_error(y,lasso_p)))

f, axaee = plt.subplots(2,2)
f.suptitle('--Regression Methods--')
axaee[0,0].scatter(y,rfrp)
axaee[0,0].set_title("RandonForestRegression")
axaee[0,1].scatter(y,knnp)
axaee[0,1].set_title("KNN")
axaee[1,0].scatter(y,ridge_p)
axaee[1,0].set_title("RIDGE")
axaee[1,1].scatter(y,lasso_p)
axaee[1,1].set_title("LASSO")
plt.show()

