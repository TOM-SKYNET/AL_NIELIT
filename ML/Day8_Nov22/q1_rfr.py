
from sklearn.datasets import load_boston
from sklearn.metrics import accuracy_score,confusion_matrix, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import numpy as np

iris = load_boston()
X=iris.data
y=iris.target


rf = RandomForestRegressor()
rf.fit(X,y)
p=rf.predict(X)

print(mean_squared_error(y,p))
print(np.sqrt(mean_squared_error(y,p)))

plt.scatter(y,p)
plt.show()
