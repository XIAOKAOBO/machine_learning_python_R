# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')
print(dataset)
X=dataset.iloc[:,:-1].values
print(X)
Y=dataset.iloc[:,3].values
print(Y)
print(dataset.size)
# print(dataset.empty)

# get rid of the NaN value
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])
print(X)

# encoding categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
LabelEncoder_X = LabelEncoder()
X[:,0]=LabelEncoder_X.fit_transform(X[:,0])
# print(X)
onehotencoder = OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()
# print(X)

print(dataset.ndim)

#splitting set to training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)