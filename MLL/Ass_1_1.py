import pandas as pd
import numpy as np



df = pd.read_csv("Iris.csv")
print(df)

print("\nMissing Values")
print(df.isnull().sum())

numeric_columns = df.select_dtypes(include=np.number).columns

for col in numeric_columns:
    df[col].fillna(df[col].mean(), inplace=True)

print(df)
