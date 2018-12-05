from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, train_test_split, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder

file = 'bank.csv'
data = pd.read_csv(file, delim_whitespace=True)

# Transform the data as it has text values, Encoding only categorical variables
le=LabelEncoder()
for col in data.columns.values:
    if data[col].dtypes == 'object':
        le.fit(data[col].values)
        data[col] = le.transform(data[col])

print(data.head)
da = data.as_matrix()
X = da[:,0:20]
y = da[:,-1]

# Model creation
models=[]
models.append(("KNN",KNeighborsClassifier()))
models.append(("NB",GaussianNB()))
models.append(("LG",LogisticRegression()))
models.append(("DT",DecisionTreeClassifier()))
#models.append(("SVM",SVC()))
results=[]
names=[]
scoring='accuracy'
for name,model in models:
	kfold=KFold(n_splits=10,random_state=7) 
	v=cross_val_score(model,X,y,cv=kfold,scoring=scoring)
	results.append(v)
	names.append(name)
	print(name)
	print(v)

# Ploting
fig=plt.figure()
fig.suptitle('Algorithm Comparison')
ax=fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()



