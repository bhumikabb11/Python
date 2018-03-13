#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import scikit-learn as sklearn
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

dataset = pd.read_csv("Data2.csv")
#print (dataset.head())

x = dataset.iloc[:,:-1].values
#print(x)
y = dataset.iloc[:,4].values
#print(y)


# Categorical data Encoding (label encoder)
# To give lables to the character data
labelencoder_x = LabelEncoder()
x[:,3] = labelencoder_x.fit_transform(x[:,3]) # 3- column index

onehotencoder = OneHotEncoder(categorical_features = [3]) # 0 stands for the 1st index of Data Table
x = onehotencoder.fit_transform(x).toarray() # create dummy variable for all country
x = x.astype(int)
#print(x)

#Avoiding the Dummy variable trap
# x = x[:,1:] - always consider 1 less dummy variable for the regression modeling



# Training and testing data
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 1/3, random_state = 0)

#print(x_train)

# Fitting Multiple Linear Regression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

#Predicting the Test set results

y_pred = regressor.predict(x_test)
print(y_pred)
print(y_test)