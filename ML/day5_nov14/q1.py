from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from  sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("ex1.txt", delimiter = ",")
data = data.as_matrix()
print data
profit=data[:,[1]]
population=data[:,0]
print(population)
print(profit)

plt.scatter(profit,population)
plt.show()

X_train,X_test,y_train,y_test=train_test_split(population,profit,test_size=0.2)
lr=LinearRegression()
lr.fit(X_train,y_train)
p=lr.predict(X_test)

print(metrics.mean_absolute_error(y_test,p))
print(metrics.mean_squared_error(y_test,p))
print(np.sqrt(metrics.mean_squared_error(y_test,p)))

#plt.scatter(y_test,p)
#plt.show()




