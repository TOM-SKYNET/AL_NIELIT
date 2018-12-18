
# coding: utf-8

# In[3]:


"""
    1.Apply K-Means clustering for the following dataset for two clusters and plot the result.
      dataset:{2,4,10,12,3,20,30,11,25}
"""

import numpy as np
import scipy as sp
from scipy.cluster.vq import vq
from scipy.cluster.vq import kmeans
from matplotlib import pyplot as plt

dset = np.array([2,4,10,12,3,20,30,11,25])
dset = sp.cast['f'](dset)
no_of_clusters = 2

centr1,dist1 = kmeans(dset, no_of_clusters)
clustrs, distances = vq(dset,centr1)
print dist1
print distances


# In[4]:


cx = np.arange(1, dset.size+1)
print cx
c1 = dset[clustrs==0]
c2 = dset[clustrs==1]
print c1
print c2


# In[8]:


plt.scatter(cx[clustrs==0],c1,color="r", label ="Cluster 1")
plt.scatter(cx[clustrs==1],c2,color="b", label ="Cluster 2")
plt.legend(loc="upper left")
plt.show()

