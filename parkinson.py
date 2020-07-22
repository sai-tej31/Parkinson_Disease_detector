# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:08:40 2020

@author: sai_tej
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import missingno as msno 
from sklearn.model_selection import train_test_split



#input data is stored in file and retrieved as data from it
data = pd.read_csv("file.csv")



#finding missing data
#msno.matrix(data)


# Let us now split the data into train and test

X_train, X_test, y_train, y_test = train_test_split(data, data.status,test_size=0.2, random_state=42, shuffle=True)

'''
RANDOM FOREST MODEL FOR CLASSIFICATION
'''


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import metrics


features = ["pressure","grip_angle","timestamp","state"]

X = pd.get_dummies(X_train[features])
X_test = pd.get_dummies(X_test[features])

model = RandomForestClassifier(n_estimators = 50,max_depth = 5 ,random_state=0 ) 
model.fit(X,y_train)
y_pred = model.predict(X_test)
print("Accuracy of Random Forest:",metrics.accuracy_score(y_test, y_pred))

'''
LOGISTIC REGRESSION MODEL FOR CLASSIFICATION
'''


from sklearn.linear_model import LogisticRegression
model2 = LogisticRegression(penalty= 'l1' ,random_state=0 ,max_iter=150).fit(X,y_train)
y_pred2 = model2.predict(X_test)

print("Accuracy regression:",metrics.accuracy_score(y_test, y_pred2))