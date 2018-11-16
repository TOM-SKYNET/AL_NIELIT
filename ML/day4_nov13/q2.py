from sklearn.datasets.samples_generator import make_blobs, make_moons
from sklearn.cluster import KMeans, SpectralClustering
import matplotlib.pyplot as plt

#X, y_ture = make_blobs(n_samples = 300, centers =4, cluster_std = 0.80)
X,y_true = make_moons(200,noise=0.05)
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
y_means = kmeans.predict(X)
plt.scatter(X[:,0],X[:,1],s=50, c=y_means, cmap='viridis')
plt.show()
