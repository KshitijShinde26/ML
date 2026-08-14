#------------------------------------------------------------------------------#
# Date: 2026-07-28                                                             #
# Author: Kshitij Shinde                                                       # 
# File : "Linear_Regression.py"                                                #
# Assignment 2:Assignment based on Linear regression using python.Assess the   #
# performance of model using evaluation metrics.                               #
#------------------------------------------------------------------------------#

import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, explained_variance_score

csv_path = Path(__file__).parent / "gta_v_worldwide_sales_player_analytics_2013_2026-selected-columns.csv"
if not csv_path.exists():
    raise FileNotFoundError(f"Dataset not found: {csv_path}")

df = pd.read_csv(csv_path)

print("First Five Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe(include="all"))

target_column = "quarter" if "quarter" in df.columns else None
if target_column is None:
    target_column = "month" if "month" in df.columns else None
if target_column is None:
    target_column = "year" if "year" in df.columns else None
if target_column is None:
    raise ValueError("Target column not found. Expected one of: quarter, month, year.")

print(f"\nUsing target column: {target_column}")

df[target_column] = pd.to_numeric(df[target_column], errors="coerce")

df = df.drop(columns=["transaction_id"], errors="ignore")

feature_df = df.drop(columns=[target_column], errors="ignore")
categorical_cols = feature_df.select_dtypes(include=["string", "object", "category"]).columns.tolist()
print("Categorical columns to encode:", categorical_cols)

feature_df = pd.get_dummies(feature_df, columns=categorical_cols, drop_first=True)
print("Feature matrix shape:", feature_df.shape)

if feature_df.empty:
    raise ValueError("No feature columns available after preprocessing.")

X = feature_df
Y = df[target_column]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

print("\nActual Value\tPredicted Value")
for actual, predicted in zip(Y_test.values, Y_pred):
    print(f"{actual}\t\t{predicted:.2f}")

mae = mean_absolute_error(Y_test, Y_pred)
mse = mean_squared_error(Y_test, Y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(Y_test, Y_pred)
explained_var = explained_variance_score(Y_test, Y_pred)

print("\nModel Evaluation")
print("MAE :", mae)
print("MSE :", mse)
print("RMSE :", rmse)
print("R² :", r2)
print("Explained Variance :", explained_var)
