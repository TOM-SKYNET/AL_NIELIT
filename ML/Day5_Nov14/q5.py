"""
	5). Predicting rock facies (classes of rocks) from well log data
	Well log data is recorded either during drilling operations or after the drilling via
	tools either on the drill string or wireline tools descended into the well.
	Typically, geoscientists would take the logs and make correlations by hand. They
	would have to draw lines from log to log to get a holistic view of the rock
	type/facies, their characteristics, and their content. This can get tedious in
	mature fields and is prone to likely misinterpretation in new fields.
	Train a machine learning model that is able to predict the facies for wells not in
	the training set. Data set (mining.csv)
	The data set we will use comes from University of Kansas. This dataset was taken
	from nine wells with 3232 examples, consisting of a set of seven predictor variables and a rock facies (class).
"""
# Using KNN

from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score

# Label Ending 
le=preprocessing.LabelEncoder()
data=pd.read_csv("mining.csv")
print data.head()
for c in data.columns.values:
	if data[c].dtypes=='object':
		le.fit(data[c].values)
		data[c]=le.transform(data[c])

data=data.as_matrix()
X=data[:,1:10]
y=data[:,0]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
knn=KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train,y_train)
yp=knn.predict(X_test)
print accuracy_score(yp,y_test)
print confusion_matrix(yp,y_test)

