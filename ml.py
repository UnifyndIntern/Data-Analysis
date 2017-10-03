# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:27:49 2017

@author: Dhaval
"""
# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading Excel file
df = pd.read_excel('TD.xlsx')


# Dividing the dataset into X and y (Dependent and Independent)
X = df.drop('Present/Absent',axis = 1)
y = df['Present/Absent']

# Label encoding 

# Category
from sklearn.preprocessing import LabelEncoder
category_encoder = LabelEncoder()
X['Category - New format'] = category_encoder.fit_transform(X['Category - New format'])

# Format 
format_encoder = LabelEncoder()
X['Format'] = format_encoder.fit_transform(X['Format'].fillna('0'))

# Floor
floor_encoder = LabelEncoder()
X['Floor'] = floor_encoder.fit_transform(X['Floor'].fillna('0'))

# Checking for null values
sns.heatmap(X.isnull(),yticklabels=False,cbar=False,cmap='viridis')

# Replacing Null with '0'
X.replace(np.nan,0,inplace = True)
X.drop('Brand Name', inplace = True, axis = 1)
X = pd.DataFrame(X).as_matrix()
y = pd.DataFrame(y).as_matrix()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Keras
from keras.models import Sequential
from keras.layers import Dense, Dropout



from sklearn.svm import SVC
svc = SVC()
svc.fit(X_train,y_train)
predictions = svc.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))


param_grid = {'C': [0.1,1, 10, 100, 1000], 'gamma': [1,0.1,0.01,0.001,0.0001], 'kernel': ['rbf']}
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(SVC(),param_grid,refit=True,verbose=3)

grid.fit(X_train,y_train)
grid.best_params_
grid.best_estimator_
grid_predictions = grid.predict(X_test)
print(confusion_matrix(y_test,grid_predictions))
