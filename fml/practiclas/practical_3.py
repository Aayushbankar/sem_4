"""
Practical 3: Scikit-learn Introduction
Unit: VI | Hours: 4

Objectives:
- Basic introduction to Scikit-learn library
- Understand sklearn modules (datasets, preprocessing, model_selection, metrics)
- Perform various sklearn operations
"""
# practical_3
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# a. Load built-in dataset
iris = load_iris()
X = iris.data
y = iris.target

# b. Preprocess data: Encode targets
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# c. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2)

# d. Preprocess data: Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# e. Initialize and Train a model
model = KNeighborsClassifier()
model.fit(X_train_scaled, y_train)

# f. Predict outcomes on the test set
y_pred = model.predict(X_test_scaled)
print("Predicted labels:", y_pred)

# g. Evaluate performance
print("Accuracy:", accuracy_score(y_test, y_pred))
