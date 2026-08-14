# Applied Machine Learning Notes

# Part: Data Preprocessing & Feature Engineering

# 1. Feature Engineering

## Definition

Feature Engineering is the process of creating, selecting, and
transforming features to improve machine learning model performance.

## Types

-   Feature Creation
-   Feature Selection
-   Feature Transformation
-   Feature Extraction

## Advantages

-   Improves accuracy
-   Reduces overfitting
-   Faster training

------------------------------------------------------------------------

# 2. Outlier Detection

## Definition

Outliers are data points that differ significantly from the rest of the
dataset.

## Detection Methods

-   Box Plot
-   Z-Score
-   IQR Method

### IQR Formula

IQR = Q3 − Q1

Lower Limit = Q1 − 1.5 × IQR

Upper Limit = Q3 + 1.5 × IQR

## Handling Outliers

-   Remove
-   Replace
-   Transform
-   Cap values

------------------------------------------------------------------------

# 3. Data Preprocessing

## Definition

Data preprocessing converts raw data into clean and usable data.

## Steps

1.  Data Cleaning
2.  Missing Value Handling
3.  Outlier Treatment
4.  Encoding
5.  Feature Scaling
6.  Data Splitting

------------------------------------------------------------------------

# 4. One-Hot Encoding

## Definition

One-Hot Encoding converts categorical variables into binary columns.

### Example

  Color   Red   Blue   Green
  ------- ----- ------ -------
  Red     1     0      0
  Blue    0     1      0

### Python

``` python
import pandas as pd
pd.get_dummies(df["Color"])
```

------------------------------------------------------------------------

# 5. Feature Scaling

## Definition

Feature Scaling brings all numerical features to a similar scale.

## Methods

-   Standardization
-   Normalization
-   Robust Scaling

### Standardization

z = (x - mean) / std

### Python

``` python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

------------------------------------------------------------------------

# 6. Train-Test Split

## Definition

Train-Test Split divides data into training and testing datasets.

## Common Ratio

-   80 : 20
-   70 : 30

### Python

``` python
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)
```

## Advantages

-   Fair model evaluation
-   Prevents overfitting

## Viva Questions

1.  What is Feature Engineering?
2.  What are Outliers?
3.  What is One-Hot Encoding?
4.  Why Feature Scaling is required?
5.  What is Train-Test Split?
