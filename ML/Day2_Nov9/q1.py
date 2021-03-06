"""
	1. Prepare an ML model using KNN Classifier to predict the Species information for
	a given iris flower using Sepal Length, Sepal Width, Petal Length & Petal Width. Use
	the complete iris dataset for training. Use it to predict the species of an iris flower.
"""

# import pakages
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()
print(iris.data)
print(iris.target)

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors =1)
knn.fit(X_train,y_train)
p = knn.predict(X_test)
print(confusion_matrix(y_test,p))
print(accuracy_score(y_test,p))


    
