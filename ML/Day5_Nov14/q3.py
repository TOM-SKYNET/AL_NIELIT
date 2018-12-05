"""
	3) Suppose that you are the administrator of a university department and you
	want to determine applicants’ chance to get admitted to a course.
	Admission is based on the scores of two exams. You have the historical data
	of earlier students. The data contains the marks of two exams and their
	admission status. Data is available in the file ex3.txt.
		a)Visualize the data using scatterplot (score1 in X axis , score2 in Y axis and
		two different colours for admitted and non admitted students)
		b)Develop an ML model to predict the admission status of a new set of students.

"""

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from  sklearn import metrics
from  sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv("ex3.txt")
print (data.head())
data=data.as_matrix()
print(data)
X=data[:,[0,1]]
y=data[:,2]
print(X)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
lr=LogisticRegression()
lr.fit(X_train,y_train)
p=lr.predict(X_test)

print(np.sqrt(metrics.mean_squared_error(y_test,p)))
print(classification_report(y_test,p))

cols = ['red','green']

plt.scatter(y_test,p, c=y_test)
plt.xlabel("Score 1")
plt.ylabel("Score 2")
plt.show()
