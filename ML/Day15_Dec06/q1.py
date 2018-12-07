"""
										Exercises 15
		1. Develop a model to do iris classification problem using Keras Sequential model. 
		Run the model for varying number of epochs and batch sizes and observe the accuracy
"""

# importing packages
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.datasets import load_iris
from sklearn.preprocessing import OneHotEncoder

iris = load_iris()
X = iris.data
y = iris.target.reshape(-1,1)
print y
encoder = OneHotEncoder()
y = encoder.fit_transform(y)

# model and different layers
model = Sequential()
model.add(Dense(10,input_shape = (4,), activation = 'relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(3,activation='softmax'))

# Optimizer
optimizer = Adam(lr=0.001)

# Model Summary Info
print model.summary()

# Complie Model
model.compile(optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
# Fit the model
model.fit(X,y,verbose =2, epochs =100)

# Print loss and accuracy 
results = model.evaluate(X,y)
print "Loss ::::::::::::", results[0]
print "Accuracy ::::", results[1]



