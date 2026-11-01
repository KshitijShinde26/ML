import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix
)

# Load the dataset from the same folder

df = pd.read_csv("breast-cancer-selected-columns.csv")

# Check dataset columns
print("Columns:", df.columns.tolist())

# Features: all columns except 'id' and 'diagnosis'
X = df.drop(columns=["id", "diagnosis"])

# Target: diagnosis (M = malignant, B = benign)
y = df["diagnosis"]

# Encode labels: M -> 1, B -> 0
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=109, stratify=y
)

# Create SVM classifier
clf = SVC(kernel="linear")

# Train the model
clf.fit(X_train, y_train)

# Predict on test data
y_pred = clf.predict(X_test)

# Evaluate model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

