# practical_9
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Import vgsales.csv
df = pd.read_csv('vgsales.csv')

# a. Find rows and columns
print(df.shape)

# b. Find basic information using describe
print(df.describe())

# c. Find values using values command
print(df.values)

# d. Apply logistic regression (Predicting hit game)
df['Hit'] = (df['Global_Sales'] > 1).astype(int)
X = df[['NA_Sales', 'EU_Sales']]
y = df['Hit']

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression().fit(X_train, y_train)
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))
