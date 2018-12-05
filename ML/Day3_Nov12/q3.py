"""
	3. Develop an ML model to predict diabetes(last column in the datset) from the
	pima Indians dataset using Logistic Regression. This dataset is from the
	National Institute of Diabetes and Digestive and Kidney Diseases. The
	objective is to predict based on diagnostic measurements whether a patient
	has diabetes. Several constraints were placed on the selection of these
	instances from a larger database. In particular, all patients here are females
	at least 21 years old of Pima Indian heritage (pimaindians.csv )
"""
# using LogisticRegression

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from  sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv("pimaindians.csv")
print (data.head())
data=data.as_matrix()
print(data)
X=data[:,[1,2,3,4,5,6,7,8]]
y=data[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

lr=LogisticRegression()
lr.fit(X_train,y_train)
p=lr.predict(X_test)

plt.scatter(y_test,p)
plt.show()
