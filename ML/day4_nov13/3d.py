from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('sample.csv', delimiter =",")
f1 = data['x'].values
f2 = data['y'].values
f3 = data['z'].values


X = np.array(zip(f1,f2,f3))

kmeans = KMeans(n_clusters=5)
kmeans.fit(X)
y_means = kmeans.predict(X)
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.scatter3D(f1,f2,f3, c=y_means, cmap='viridis')
#centers = kmeans.cluster_centers_
#plt.scatter(centers[:,0],centers[:,1],s=200,c='red')
plt.show()
