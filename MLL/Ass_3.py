#------------------------------------------------------------------------------#
# Date: 2026-08-11                                                             #
# Author: Kshitij Shinde                                                       # 
# File : "Logistic_Regression.py"                                              #
# Assignment 3:Assignment based on Logistic regression using python.Assess the #
# performance of model using evaluation metrics.                               #
#------------------------------------------------------------------------------#

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

# Load the dataset
df = pd.read_csv("Titanic-Dataset-selected-columns.csv")

# Check missing values
print(df.isnull().sum())

# Prepare features and target
X = df.drop(columns=['Survived'])
Y = df['Survived']

# Fill missing numeric values with median
numeric_cols = X.select_dtypes(include=['number']).columns
X[numeric_cols] = X[numeric_cols].fillna(X[numeric_cols].median())

# Convert categorical columns to numeric (one-hot encoding)
X = pd.get_dummies(X, drop_first=True)

# Optional: remove any remaining NaN if any categorical columns were missing
X = X.fillna(0)

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# Predict
Y_pred = model.predict(X_test)

# Metrics
accuracy = accuracy_score(Y_test, Y_pred)
precision = precision_score(Y_test, Y_pred, zero_division=0)
recall = recall_score(Y_test, Y_pred, zero_division=0)
f1 = f1_score(Y_test, Y_pred, zero_division=0)
cm = confusion_matrix(Y_test, Y_pred)

print("\nEvaluation Metrics: ")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
print("\nConfusion Matrix:")
print(cm)

