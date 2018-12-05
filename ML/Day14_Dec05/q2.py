"""
	2) Implement MLPRegressor for boston dataset in sklearn . Print performance metrics like RMSE, MAE , etc.
"""

# importing packages
from sklearn.datasets import load_boston
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.metrics import confusion_matrix
import numpy as np

data = load_boston()
type(data)
X=data.data
y=data.target

# Activation function  - "tanh" , solver = sgd
knn=MLPClassifier(activation='tanh',hidden_layer_sizes=(100),solver='sgd',learning_rate_init=0.01,max_iter=500,verbose=True)
print(knn)

knn.fit(X,y)
print(knn.predict([[3,5,4,2]]))
p=knn.predict(X)
print(mean_absolute_error(y,p))
print(mean_absolute_error(y,p))
print(np.sqrt(mean_squared_error(y,p)))

# Activation Function -- relu , solver = sgd
knn=MLPClassifier(activation='relu',hidden_layer_sizes=(100),solver='sgd',learning_rate_init=0.01,max_iter=500,verbose=True)
print(knn)
knn.fit(X,y)
print(knn.predict([[3,5,4,2]]))
p=knn.predict(X)
print(mean_absolute_error(y,p))
print(mean_absolute_error(y,p))
print(np.sqrt(mean_squared_error(y,p)))

#print(knn.coefs_)


