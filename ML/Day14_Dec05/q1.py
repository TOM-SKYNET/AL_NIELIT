"""
	1) Implement MLPClassifier for iris dataset in sklearn.
		a. Print confusion matrix for different activation functions	- tanh , relu
		b. Study the reduction in loss based on the number of iterations.
"""

# importing packages
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error

iris = load_iris()
type(iris)
print(iris.feature_names)
print(iris.data)
X=iris.data
y=iris.target

# Activation function  - "tanh" , solver = sgd
knn=MLPClassifier(activation='tanh',hidden_layer_sizes=(100),solver='sgd',learning_rate_init=0.01,max_iter=500,verbose=True)
print(knn)

knn.fit(X,y)
print(knn.predict([[3,5,4,2]]))
p=knn.predict(X)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y,p))
print(knn.coefs_)

# Activation Function -- relu , solver = sgd
knn=MLPClassifier(activation='relu',hidden_layer_sizes=(100),solver='sgd',learning_rate_init=0.01,max_iter=500,verbose=True)
print(knn)
knn.fit(X,y)
print(knn.predict([[3,5,4,2]]))
p=knn.predict(X)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y,p))
print(knn.coefs_)


# Activation function  - "tanh" , solver = adam
knn=MLPClassifier(activation='tanh',hidden_layer_sizes=(100),solver='adam',learning_rate_init=0.01,max_iter=700,verbose=True)
print(knn)

knn.fit(X,y)
print(knn.predict([[3,5,4,2]]))
p=knn.predict(X)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y,p))
print(knn.coefs_)

# Activation Function -- relu ,   solver = adam
knn=MLPClassifier(activation='relu',hidden_layer_sizes=(100),solver='adam',learning_rate_init=0.01,max_iter=700,verbose=True)
print(knn)
knn.fit(X,y)
print(knn.predict([[3,5,4,2]]))
p=knn.predict(X)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y,p))
print(knn.coefs_)

