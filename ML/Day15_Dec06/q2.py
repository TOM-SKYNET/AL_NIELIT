#!/usr/bin/env python

"""
				Exercises 15
		2. Develop a model to do classification in the sonar.csv dataset.
"""



# import packages
import pandas as pd
import numpy as np
from sklearn import preprocessing
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam



df = pd.read_csv('sonar.csv')
print(len(df.columns))
X = df[df.columns[0:60]].values
y = df[df.columns[60]]
print ("------------------------- X ---------------------")
print(X)
print ("------------------------- y Before Encode ---------------------")
print(y)
#
encoder = preprocessing.LabelEncoder()
encoder.fit(y)
y = encoder.transform(y)
print("----------- y After Label Encoding -------------------")
print(y)

oneHotEncoder = preprocessing.OneHotEncoder(categories='auto')
y = oneHotEncoder.fit_transform(y.reshape(-1,1))
print("----------- y After oneHotEncoder -------------------")
print(y)

# model and different layers (60 input, 3 hidden)
model = Sequential()
model.add(Dense(60,input_dim=60, activation='relu')) # inner layer
model.add(Dense(30, activation='relu')) # hidden 1
model.add(Dense(12, activation='relu')) # hidden 2
model.add(Dense(6, activation='relu')) # hidden 3
model.add(Dense(3, activation='relu'))  # hidden 4
model.add(Dense(2, activation='softmax')) # outer layer

# Model Summary Info
print model.summary()


# Optimizer
optimizer = Adam(lr=0.001)

# Complie Model
model.compile(optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
# Fit the model
model.fit(X,y,verbose =2, epochs =1000)

# Print loss and accuracy
results = model.evaluate(X,y)
print "Loss ::",(results[0])
print "Accuracy ::",(results[1])

