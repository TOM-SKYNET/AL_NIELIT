"""
	4. Identify a suitable dataset from your area of interest for a classification problem
	(Should not be the same as Day1 solution). Develop an ML model to do prediction.
	Print confusion matrix and accuracy score.
"""

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt

train1 = pd.read_csv('/home/ai29/Desktop/Programming/ML/day2_nov9/bank.txt')
print(train1)

train = train1.as_matrix()
print(train)

X = train[:,0:3]
y = train[:,4]
print('y', y)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)


accuracy = []
for i in range(1,25):
    knn = KNeighborsClassifier(n_neighbors =i)
    knn.fit(X_train,y_train)
    p = knn.predict(X_test)
    a = accuracy_score(y_test,p)
    accuracy.append(a)
    
print('Accuracy:',accuracy)

print('Confusion Matrix:' , confusion_matrix(y_test,p))
plt.plot(range(1,25),accuracy)
plt.show()
