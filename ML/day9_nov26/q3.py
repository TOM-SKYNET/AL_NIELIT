'''
    Apply Standardization/ Normalization for the immunotherapy problem
    (day2) and check whether the accuracy is improved.

'''

import cv2 as cv
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn import preprocessing
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/ai29/Desktop/LABS/ML/day2_nov9/Immunotherapy.csv', delimiter=',')
print(df.head)
data = df.as_matrix()
X = data[:,0:7]
y = data[:,7]
#print 'X', X
#print 'Y' , y
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train,y_train)
p = knn.predict(X_test)
a = accuracy_score(y_test,p)
print "------------- Un Normalized Data ------------------"
print('Accuracy:',a)
print("Classification report")
print classification_report(y_test,p)

# Standardiztion 
scaler = preprocessing.StandardScaler().fit(X)
#print "scaler" , scaler

print "------------------------"
#print 'Scaled',scaler

Xs = scaler.transform(X)
#print 'Xs', Xs


X_train1, X_test1, y_train1, y_test1 = train_test_split(Xs,y, test_size=0.2)
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train1,y_train1)
p1 = knn.predict(X_test1)
a1 = accuracy_score(y_test1,p1)
print "------------- Normalized Data ------------------"
print('Accuracy:',a1)
print("Classification report")
print classification_report(y_test1,p1)
