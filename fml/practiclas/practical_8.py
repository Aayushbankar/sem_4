# practical_8
import pandas as pd
import os, warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# a. Load
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'music.csv'))

# b. Split
X, y = df[['age', 'gender']], df['genre']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# c. Train
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Predict
print("21 Male:", model.predict([[21, 1]])[0])
print("22 Female:", model.predict([[22, 0]])[0])

# d. Accuracy
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))

# e. Synthetic test
syn_df = pd.concat([df]*10)
print("Synthetic Accuracy:", accuracy_score(syn_df['genre'], model.predict(syn_df[['age', 'gender']])))
