"""
				Exercises 15
		2. Develop a model to do classification in the sonar.csv dataset.
"""


from keras.models import Sequential
from keras.layers import Dense
import numpy as np

np.random.seed(10)
dataset = np.loadcsv("sonar.csv", delimiter=",")
print dataset.head
X = dataset[:,0:8]
y = dataset[:,8]
print X
print y