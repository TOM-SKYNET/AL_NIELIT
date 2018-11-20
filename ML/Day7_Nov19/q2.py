#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
from sklearn.svm import SVR
from sklearn.metrics import accuracy_score,mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[31]:


data = pd.read_csv('bikerental.txt',delim_whitespace=True)


# In[32]:


data.head()


# In[33]:


data.dropna(inplace=True)
X = data.drop('cnt',axis=1)
y = data['cnt']
X_train,X_test,y_train,y_test = train_test_split(X,y)


# In[40]:


model = SVR()
lmodel = LinearRegression()


# In[41]:


model.fit(X_train,y_train)
lmodel.fit(X_train,y_train)


# In[43]:


models= [model,lmodel]
for i in models:
    print "\n",i
    pred = i.predict(X_test)
    print "MSE: ",mean_squared_error(y_test,pred),"\n"


# In[ ]:





# In[ ]:




