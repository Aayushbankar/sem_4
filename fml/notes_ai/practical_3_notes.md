# Practical 3: Scikit-learn Notes

## Scikit-learn Introduction

Scikit-learn is a free software machine learning library for the Python programming language. It relies on NumPy, SciPy, and Matplotlib.

### Unit 6 Operations

#### 6.4.1 Data Preprocessing

1.  **`train_test_split()`**:
    -   Splits arrays or matrices into random train and test subsets.
    -   **Usage**: `from sklearn.model_selection import train_test_split`
    -   **Syntax**: `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)`

2.  **`StandardScaler()`**:
    -   Standardize features by removing the mean and scaling to unit variance.
    -   **Usage**: `from sklearn.preprocessing import StandardScaler`
    -   **Syntax**: `scaler = StandardScaler(); X_scaled = scaler.fit_transform(X)`

3.  **`LabelEncoder()`**:
    -   Encode target labels with value between 0 and n_classes-1.
    -   **Usage**: `from sklearn.preprocessing import LabelEncoder`
    -   **Syntax**: `le = LabelEncoder(); y_encoded = le.fit_transform(y)`

#### 6.4.2 Classification Algorithms

1.  **`LogisticRegression()`**:
    -   Despite its name, it is a linear model for classification rather than regression. It predicts the probability of an outcome.
    -   **Usage**: `from sklearn.linear_model import LogisticRegression`
    -   **Syntax**: `model = LogisticRegression(); model.fit(X_train, y_train)`

2.  **`KNeighborsClassifier()`**:
    -   Classifier implementing the k-nearest neighbors vote.
    -   **Usage**: `from sklearn.neighbors import KNeighborsClassifier`
    -   **Syntax**: `model = KNeighborsClassifier(n_neighbors=5); model.fit(X_train, y_train)`

3.  **`SVC()` (Support Vector Classification)**:
    -   C-Support Vector Classification.
    -   **Usage**: `from sklearn.svm import SVC`
    -   **Syntax**: `model = SVC(); model.fit(X_train, y_train)`

#### 6.4.3 Regression Algorithms

1.  **`LinearRegression()`**:
    -   Ordinary least squares Linear Regression.
    -   **Usage**: `from sklearn.linear_model import LinearRegression`
    -   **Syntax**: `model = LinearRegression(); model.fit(X_train, y_train)`

#### 6.4.4 Model Evaluation

1.  **`accuracy_score()`**:
    -   Accuracy classification score.
    -   **Usage**: `from sklearn.metrics import accuracy_score`
    -   **Syntax**: `acc = accuracy_score(y_true, y_pred)`

2.  **`confusion_matrix()`**:
    -   Compute confusion matrix to evaluate the accuracy of a classification.
    -   **Usage**: `from sklearn.metrics import confusion_matrix`
    -   **Syntax**: `cm = confusion_matrix(y_true, y_pred)`

3.  **`classification_report()`**:
    -   Build a text report showing the main classification metrics (precision, recall, f1-score).
    -   **Usage**: `from sklearn.metrics import classification_report`
    -   **Syntax**: `report = classification_report(y_true, y_pred)`

#### Clustering

1.  **`KMeans()`**:
    -   K-Means clustering.
    -   **Usage**: `from sklearn.cluster import KMeans`
    -   **Syntax**: `kmeans = KMeans(n_clusters=3); kmeans.fit(X)`
