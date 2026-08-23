# ===============================================
# Roll no : 60       PRN: 0124UITM1060
# Name : Kshitij Shinde
# Dept. : Information Technology (Third Year)
# ===============================================
# Assignment 4:
# Loan Application Prediction using Gaussian Naive Bayes
# ===============================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score , recall_score, precision_score
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("loan_data.csv")

# Handle missing values
for c in df.select_dtypes(include="object"):
    df[c] = df[c].fillna(df[c].mode()[0])

for c in df.select_dtypes(exclude="object"):
    df[c] = df[c].fillna(df[c].median())

# Convert Dependents
df["Dependents"] = df["Dependents"].replace("3+", "3")

# Convert target
df["Loan_Status"] = df["Loan_Status"].map({"Y": 1, "N": 0})

# Remove Loan_ID
df.drop("Loan_ID", axis=1, inplace=True)
print(df.shape)
# Convert categorical columns
df = pd.get_dummies(df, drop_first=True)

# Features and target
X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# Naive Bayes
model = GaussianNB()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("Recall Score:", recall_score(y_test, y_pred))
print("Precision Score:", precision_score(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Graph: Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
plt.imshow(cm, cmap="Blues")
plt.title("Confusion Matrix")
plt.colorbar()

plt.xticks([0, 1], ["Not Approved", "Approved"])
plt.yticks([0, 1], ["Not Approved", "Approved"])
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", va="center", color="black")

plt.tight_layout()
plt.show()