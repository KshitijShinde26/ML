# ===============================================
# Roll no : 60       PRN: 0124UITM1060
# Name : Kshitij Shinde
# Dept. : Information Technology (Third Year)
# ===============================================
# Assignment 5:
# Support Vector Machine algorithm using python.
# ===============================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.inspection import DecisionBoundaryDisplay

# Load dataset
df = pd.read_csv("UniversalBank.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# Select only 2 features for 2D graph
X = df[["Income", "CCAvg"]]

# Target column
y = df["Personal Loan"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

# Feature Scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create Linear SVM model
model = SVC(kernel="linear")

# Train model
model.fit(X_train_scaled, y_train)

# Prediction
y_pred = model.predict(X_test_scaled)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

# Plot decision boundary
plt.figure(figsize=(10, 6))

DecisionBoundaryDisplay.from_estimator(
    model,
    X_train_scaled,
    response_method="predict",
    alpha=0.3,
    cmap="coolwarm"
)

# Plot Fail / No Personal Loan
plt.scatter(
    X_train_scaled[y_train == 0, 0],
    X_train_scaled[y_train == 0, 1],
    label="No Personal Loan",
    edgecolors="black"
)

# Plot Personal Loan
plt.scatter(
    X_train_scaled[y_train == 1, 0],
    X_train_scaled[y_train == 1, 1],
    label="Personal Loan",
    edgecolors="black"
)

plt.xlabel("Income (Scaled)")
plt.ylabel("CCAvg (Scaled)")
plt.title("Linear SVM - Personal Loan Classification")
plt.legend()

plt.show()