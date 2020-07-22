```python
# Let Us Import some libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import metrics
from sklearn.linear_model import LogisticRegression


```


```python
# reading data from CSV file which is created from datasets using the datafile.py
data = pd.read_csv("file.csv")

```


```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pressure</th>
      <th>grip_angle</th>
      <th>timestamp</th>
      <th>state</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>884.200931</td>
      <td>794.317300</td>
      <td>115.650000</td>
      <td>static</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>910.966791</td>
      <td>662.641217</td>
      <td>115.650000</td>
      <td>dynamic</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>788.450502</td>
      <td>782.556671</td>
      <td>1052.316667</td>
      <td>static</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>926.910511</td>
      <td>902.801802</td>
      <td>1052.316667</td>
      <td>dynamic</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>843.550013</td>
      <td>903.502152</td>
      <td>1228.116667</td>
      <td>static</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>75</th>
      <td>520.355333</td>
      <td>1060.966411</td>
      <td>1171.950000</td>
      <td>dynamic</td>
      <td>0</td>
    </tr>
    <tr>
      <th>76</th>
      <td>899.069890</td>
      <td>1474.577348</td>
      <td>1307.450000</td>
      <td>static</td>
      <td>0</td>
    </tr>
    <tr>
      <th>77</th>
      <td>899.257785</td>
      <td>1432.905643</td>
      <td>1307.450000</td>
      <td>dynamic</td>
      <td>0</td>
    </tr>
    <tr>
      <th>78</th>
      <td>607.163567</td>
      <td>879.065934</td>
      <td>1417.933333</td>
      <td>static</td>
      <td>0</td>
    </tr>
    <tr>
      <th>79</th>
      <td>409.578713</td>
      <td>941.002075</td>
      <td>1417.933333</td>
      <td>dynamic</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>80 rows × 5 columns</p>
</div>




```python
# Let us now split the data into train and test before it shuffle the data

X_train, X_test, y_train, y_test = train_test_split(data, data.status,test_size=0.2, random_state=42, shuffle=True)

```


```python
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
```

    (64, 5)
    (64,)
    (16, 5)
    (16,)
    


```python
'''
RANDOM FOREST MODEL FOR CLASSIFICATION
'''

features = ["pressure","grip_angle","timestamp","state"]

X = pd.get_dummies(X_train[features])
X_test = pd.get_dummies(X_test[features])

model = RandomForestClassifier(n_estimators = 50,max_depth = 4 ,random_state=0 ) 
model.fit(X,y_train)
y_pred = model.predict(X_test)
print("Accuracy of Random Forest:",metrics.accuracy_score(y_test, y_pred))

```

    Accuracy of Random Forest: 0.875
    


```python
'''
LOGISTIC REGRESSION MODEL FOR CLASSIFICATION
'''
model2 = LogisticRegression(penalty= 'none' ,random_state=0 ,max_iter=100,solver='lbfgs').fit(X,y_train)
y_pred2 = model2.predict(X_test)

print("Accuracy regression:",metrics.accuracy_score(y_test, y_pred2))
```

    Accuracy regression: 0.875
    


```python

```
