#===================================================#
# Date : 1st Sept 2026                              #
# Name : Kshitij Shinde                             #
# Roll_no : 60                                      #
# Exam : Mid_Term Lab                               #
# Topic : Naive Bayes  (Assgniment 4)               #
# Dataset : UniversalBank.csv                       #
#===================================================#

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score , recall_score, precision_score ,ConfusionMatrixDisplay
import matplotlib.pyplot as plt

df = pd.read_csv("loan_data.csv")

for c in df.select_dtypes(include="object"):
    df[c] = df[c].fillna(df[c].mode()[0])

for c in df.select_dtypes(exclude="object"):
    df[c] = df[c].fillna(df[c].median())

df["Dependents"] = df["Dependents"].replace("3+", "3")


df["Loan_Status"] = df["Loan_Status"].map({"Y": 1, "N": 0})

df.drop("Loan_ID", axis=1, inplace=True)

df = pd.get_dummies(df, drop_first=True)

X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("Recall Score:", recall_score(y_test, y_pred))
print("Precision Score:", precision_score(y_test, y_pred))

print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

dis = ConfusionMatrixDisplay(confusion_matrix=cm)
dis.plot()
plt.show()