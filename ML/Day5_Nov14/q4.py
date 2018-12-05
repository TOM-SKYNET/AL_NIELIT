"""
	4) The sinking of the Titanic is one of the most infamous shipwrecks in history.
	On April 15, 1912, during her maiden voyage, the Titanic sank after colliding
	with an iceberg, killing 1502 out of 2224 passengers and crew. This
	sensational tragedy shocked the international community and led to better
	safety regulations for ships.
	One of the reasons that the shipwreck led to such a loss of life was that there
	were not enough lifeboats for the passengers and crew. Although there was
	some element of luck involved in surviving the sinking, some groups of
	people were more likely to survive than others, such as women, children, and
	the upper-class.
	Develop an ML model to predict the survival of passengers. (Use titanic.csv file)
"""

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from  sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
from sklearn import preprocessing

# Label Encoding 
le=preprocessing.LabelEncoder()
data=pd.read_csv("titanic.csv")
for col in data.columns.values:
	if data[col].dtypes=='object':
		le.fit(data[col].values)
       		data[col]=le.transform(data[col])

# droping NaN 
data=data.dropna(axis=0, how='any')
print data
data=data.as_matrix()
X=data[:,[0,2,4,5,6,7,8,9,10,11]]
y=data[:,1]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
lr=LogisticRegression()
lr.fit(X_train,y_train)
p=lr.predict(X_test)
print "Mean Absolute Error",metrics.mean_absolute_error(y_test,p)
print "Mean Squared Error",metrics.mean_squared_error(y_test,p)
print "Root Mean Squared Error",np.sqrt(metrics.mean_squared_error(y_test,p))
