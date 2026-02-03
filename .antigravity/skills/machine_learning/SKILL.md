---
name: machine_learning
description: ML algorithms, Python implementations, scikit-learn usage, and model evaluation
---

# Machine Learning Assistant

**Purpose:** Explain ML concepts, implement algorithms in Python, and guide practical FML work.

---

## Algorithm Coverage

### Supervised Learning
| Algorithm           | Type           | Use Case              | Key Parameters       |
| ------------------- | -------------- | --------------------- | -------------------- |
| Linear Regression   | Regression     | Continuous prediction | fit_intercept        |
| Logistic Regression | Classification | Binary/multi-class    | C, solver            |
| Decision Tree       | Both           | Interpretable models  | max_depth, criterion |
| Random Forest       | Both           | Ensemble accuracy     | n_estimators         |
| KNN                 | Both           | Pattern matching      | n_neighbors, metric  |
| SVM                 | Both           | High-dimensional      | C, kernel, gamma     |
| Naive Bayes         | Classification | Text, probabilistic   | var_smoothing        |

### Unsupervised Learning
| Algorithm    | Use Case                 | Key Parameters              |
| ------------ | ------------------------ | --------------------------- |
| K-Means      | Clustering               | n_clusters, init            |
| Hierarchical | Clustering               | linkage, n_clusters         |
| PCA          | Dimensionality reduction | n_components                |
| Apriori      | Association rules        | min_support, min_confidence |

---

## Standard Code Template

```python
# 1. Import
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.[module] import [Algorithm]
from sklearn.metrics import accuracy_score, confusion_matrix

# 2. Load Data
df = pd.read_csv('data.csv')
X = df.drop('target', axis=1)
y = df['target']

# 3. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train
model = [Algorithm]()
model.fit(X_train, y_train)

# 5. Predict
y_pred = model.predict(X_test)

# 6. Evaluate
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(confusion_matrix(y_test, y_pred))
```

---

## Evaluation Metrics

| Metric    | Formula               | When to Use            |
| --------- | --------------------- | ---------------------- |
| Accuracy  | (TP+TN)/(TP+TN+FP+FN) | Balanced classes       |
| Precision | TP/(TP+FP)            | False positives costly |
| Recall    | TP/(TP+FN)            | False negatives costly |
| F1 Score  | 2×(P×R)/(P+R)         | Imbalanced classes     |
| MSE       | Σ(y-ŷ)²/n             | Regression             |
| R²        | 1 - (SS_res/SS_tot)   | Regression fit         |

---

## Explanation Rules

- Always show complete runnable code
- Include data preprocessing steps
- Explain hyperparameter choices
- Show both training and evaluation
- Use real datasets (iris, digits, boston) for examples
- Include visualization when helpful
