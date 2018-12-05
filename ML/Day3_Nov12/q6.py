"""
	6. Develop a KNN model and do accuracy computation with cross validation. Also
	obtain Precision , Recall and F1 Score using classification report.
"""
# Using KNN

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
print(iris.data)
print(iris.target)

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors =1)
score = cross_val_score(knn,X,y,cv=20)
print(score)

knn.fit(X_train,y_train)
p= knn.predict(X_test)
print(classification_report(y_test,p))
