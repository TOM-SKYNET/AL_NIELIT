from sklearn.datasets.samples_generator import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from  sklearn import metrics
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('ex2.txt', delimiter =",")
print data
f1 = data['area'].values
f2 = data['bedrooms'].values
f3 = data['price'].values


X0 = np.array(zip(f1,f2,f3))

kmeans = KMeans(n_clusters=5)
kmeans.fit(X0)
y_means = kmeans.predict(X0)

fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.scatter3D(f1,f2,f3, c=y_means, cmap='viridis')
plt.show()

data = data.as_matrix()
X=data[:,[1,2]]
y=data[:,-1]

#plt.scatter(X,y)
#plt.show()

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
lr=LinearRegression()
lr.fit(X_train,y_train)
p=lr.predict(X_test)

print(metrics.mean_absolute_error(y_test,p))
print(metrics.mean_squared_error(y_test,p))
print(np.sqrt(metrics.mean_squared_error(y_test,p)))
