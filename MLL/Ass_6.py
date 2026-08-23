# ============================================================
# CUSTOMER CHURN PREDICTION USING DECISION TREE CLASSIFIER
# ============================================================

# Step 1: Import Required Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    classification_report
)
from sklearn import tree


# ============================================================
# Step 2: Load Dataset
# ============================================================

df = pd.read_csv("Telco-Customer-Churn.csv")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nChurn Distribution:")
print(df["Churn"].value_counts())


# ============================================================
# Step 3: Exploratory Data Analysis
# ============================================================

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()


# ============================================================
# Step 4: Data Cleaning and Preprocessing
# ============================================================

# Remove customer ID because it is only an identifier
df.drop("customerID", axis=1, inplace=True)

# Convert TotalCharges from string to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Remove rows containing missing values
df.dropna(inplace=True)

# Convert Churn:
# Yes -> 1
# No  -> 0
df["Churn"] = df["Churn"].map({
    "Yes": 1,
    "No": 0
})

# Convert categorical columns into numerical columns
df = pd.get_dummies(df, drop_first=True)


# ============================================================
# Step 5: Define Features and Target
# ============================================================

X = df.drop("Churn", axis=1)
y = df["Churn"]


# ============================================================
# Step 6: Split Dataset
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)


# ============================================================
# Step 7: Create and Train Decision Tree Model
# ============================================================

dt_model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

dt_model.fit(X_train, y_train)


# ============================================================
# Step 8: Make Predictions
# ============================================================

y_pred = dt_model.predict(X_test)


# ============================================================
# Step 9: Model Evaluation
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

print("\n==============================")
print("MODEL EVALUATION")
print("==============================")

print(f"Accuracy: {accuracy * 100:.2f}%")

print(f"F1-Score: {f1:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ============================================================
# Step 10: Confusion Matrix
# ============================================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["No Churn", "Churn"],
    yticklabels=["No Churn", "Churn"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()


# ============================================================
# Step 11: Feature Importance
# ============================================================

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": dt_model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n==============================")
print("FEATURE IMPORTANCE")
print("==============================")

print(feature_importance.head(10))


# Plot Feature Importance

plt.figure(figsize=(10, 6))

sns.barplot(
    data=feature_importance.head(10),
    x="Importance",
    y="Feature"
)

plt.title("Top 10 Feature Importances")

plt.show()


# ============================================================
# Step 12: Visualize Decision Tree
# ============================================================

plt.figure(figsize=(20, 10))

tree.plot_tree(
    dt_model,
    feature_names=X.columns,
    class_names=["No Churn", "Churn"],
    filled=True,
    fontsize=8
)

plt.title("Decision Tree for Customer Churn Prediction")

plt.savefig(
    "decision_tree.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# Step 13: Final Results
# ============================================================

print("\n==============================")
print("FINAL RESULTS")
print("==============================")

print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"F1-Score: {f1:.4f}")

print("\nTop 5 Important Features:")
print(feature_importance.head(5))