"""
	3. Try clustering with some suitable datasets in the link
	http://cs.joensuu.fi/sipu/datasets/
"""

from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('s1.txt', delimiter ="\s+")
data = data.as_matrix()

X = np.array(zip(data[:,0],data[:,1]))

kmeans = KMeans(n_clusters=15)
kmeans.fit(X)
y_means = kmeans.predict(X)
plt.scatter(X[:,0],X[:,1],s=50, c=y_means, cmap='viridis')
plt.show()
