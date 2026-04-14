"""
Practical 10: Linear Regression Project (home_data.csv)
Unit: IV | Hours: 2

Objectives:
a. Import home_data.csv from Kaggle using pandas
b. Understand data by running head, info and describe commands
c. Plot the price of house with respect to area using matplotlib
d. Apply linear regression model to predict the price of house
e. Highlight the correctness of plot using suitable metrics

Dataset: House Prices (home_data.csv) from Kaggle
"""
# practical_10
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# a. Import home_data.csv
df = pd.read_csv('home_data.csv')

# b. Understand data
print(df.head())
print(df.info())
print(df.describe())

# Assign X (Area) and y (Price) 
# Note: 'sqft_living' is the standard area column for the Kaggle home_data.csv dataset
X = df[['sqft_living']]
y = df['price']

# c. Plot price vs area
plt.scatter(X, y)
plt.title('Price vs Area')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()

# d. Apply linear regression
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = LinearRegression().fit(X_train, y_train)

# e. Highlight correctness using Metrics
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
