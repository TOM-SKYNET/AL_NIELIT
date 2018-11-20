#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


# In[65]:


data = pd.read_csv('bank.csv')


# In[66]:


data.head()


# In[67]:


data= data[(data[list(data.columns)] !='unknown')]
data.dropna(inplace=True)


# In[68]:


job = pd.get_dummies(data.job,drop_first=True)
marital = pd.get_dummies(data.marital,drop_first=True)
education = pd.get_dummies(data.education,drop_first=True)
poutcome = pd.get_dummies(data.poutcome,drop_first=True)
default= pd.get_dummies(data.default,drop_first=True)
housing = pd.get_dummies(data.housing,drop_first=True)
loan = pd.get_dummies(data.loan,drop_first=True)


# In[69]:


data.drop(['job','marital','education','poutcome','default','housing','loan','age', 'contact','month','day_of_week','duration'],inplace=True,axis=1)
X= pd.concat([job,marital,education,poutcome,default,housing,loan,data],axis=1)
X = X.drop('y',axis=1)
y = data['y']


# In[73]:


X_train,X_test,y_train,y_test = train_test_split(X,y)


# In[71]:


knn = KNeighborsClassifier(n_neighbors=1)
svc = SVC()
logistic= LogisticRegression()
nb = GaussianNB()


# In[74]:


knn.fit(X_train,y_train)
svc.fit(X_train,y_train)
logistic.fit(X_train,y_train)
nb.fit(X_train,y_train)


# In[75]:


models=[knn,svc,logistic,nb]


# In[76]:





# In[79]:


for i in models :
    print"\n",i
    pred = i.predict(X_test)
    
    print"\n", classification_report(y_test,pred)


# In[ ]:




