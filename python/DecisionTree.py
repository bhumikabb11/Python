#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import scikit-learn as sklearn
#from sklearn.linear_model import LinearRegression
#from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor


dataset = pd.read_csv("Data1.csv")
#print (dataset.head())

x = dataset.iloc[:,1:2].values
#print(x)

y = dataset.iloc[:,2].values
#print(y)


#x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 1/3, random_state = 0)

#print(x_train)
#print(x_test)
#print(y_train)
#print(y_test)

# Linear Regression
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(x,y)



# Predicting the Test Set results
y_pred = regressor.predict(6.5)

#print(y_pred) - output generated by the linear model
#print(y_test) - output which we are going to test which is approximately equal to y_pred

#Visualising the Decision Tree results
plt.scatter(x, y, color = 'red')
plt.plot(x, regressor.predict(x), color = 'blue')
plt.title('Decision Tree Regression')
plt.xlabel('Position Level')
plt.ylabel('salary')
plt.show()