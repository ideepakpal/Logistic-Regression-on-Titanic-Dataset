# -*- coding: utf-8 -*-
"""Deep L.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_N1PZlA2lPG-Y4OUC8oKYSv8jsxWieoq
"""

import pandas as pd
import numpy as np
df=pd.read_csv("titanic.csv")

df.head()

df=df.dropna()

y=df["Survived"] 
x=df[["Age","Fare"]]

x

y





from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.15)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)

from sklearn.metrics import accuracy_score
y_predict=model.predict(x_test)
print(accuracy_score(y_predict,y_test))

a=np.array([[6,26.550]])
model.predict(a)