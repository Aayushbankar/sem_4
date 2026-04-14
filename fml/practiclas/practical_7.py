"""
Practical 7: K-Nearest Neighbor Classification
Unit: IV | Hours: 2

Objectives:
- Implement K-Nearest Neighbor (KNN) algorithm
- Use KNN to predict class labels of test data
- Training and test data must be provided explicitly
- use iris dataset 
"""
# practical_7
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X, y = iris.data, iris.target

def knn(X_train, y_train, test_point, k=3):
    distances = []

    # Calculate distance from test_point to every point in training set
    for i in range(len(X_train)):
        dist = np.sqrt(np.sum((X_train[i] - test_point)**2))
        distances.append((dist, y_train[i]))

    # Sort by distance (first element of tuple)
    distances.sort(key=lambda x: x[0])

    # Get labels of top K neighbors
    neighbors = [dist[1] for dist in distances[:k]]

    # Return the most common label (Majority Vote)
    return max(set(neighbors), key=neighbors.count)

# Explicitly provide training and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pick a test point
test_flower = X_test[0]
true_label = y_test[0]

# Make prediction
prediction = knn(X_train, y_train, test_flower, k=3)
print(f"Predicted Class: {prediction}")
print(f"True Class: {true_label}")
