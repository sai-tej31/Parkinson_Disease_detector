#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Let Us Import some libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import metrics
from sklearn.linear_model import LogisticRegression


# In[3]:


# reading data from CSV file which is created from datasets using the datafile.py
data = pd.read_csv("file.csv")


# In[11]:


data


# In[5]:


# Let us now split the data into train and test before it shuffle the data

X_train, X_test, y_train, y_test = train_test_split(data, data.status,test_size=0.2, random_state=42, shuffle=True)


# In[9]:


print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)


# In[12]:


'''
RANDOM FOREST MODEL FOR CLASSIFICATION
'''

features = ["pressure","grip_angle","timestamp","state"]

X = pd.get_dummies(X_train[features])
X_test = pd.get_dummies(X_test[features])

model = RandomForestClassifier(n_estimators = 50,max_depth = 5 ,random_state=0 ) 
model.fit(X,y_train)
y_pred = model.predict(X_test)
print("Accuracy of Random Forest:",metrics.accuracy_score(y_test, y_pred))


# In[21]:


'''
LOGISTIC REGRESSION MODEL FOR CLASSIFICATION
'''
model2 = LogisticRegression(penalty= 'none' ,random_state=0 ,max_iter=100,solver='lbfgs').fit(X,y_train)
y_pred2 = model2.predict(X_test)

print("Accuracy regression:",metrics.accuracy_score(y_test, y_pred2))


# In[ ]:




