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
