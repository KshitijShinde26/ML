# Applied Machine Learning Notes

# Part: CatBoost, Gradient Boosting & Model Deployment

# 1. Gradient Boosting

## Definition

Gradient Boosting is an ensemble learning algorithm that builds multiple
decision trees sequentially. Each new tree corrects the errors made by
the previous trees.

## Working

1.  Train the first decision tree.
2.  Calculate prediction errors (residuals).
3.  Train the next tree on the residuals.
4.  Add predictions from all trees.
5.  Repeat until the desired number of trees is built.

## Advantages

-   High prediction accuracy
-   Handles complex datasets
-   Reduces bias

## Disadvantages

-   Slow training
-   Can overfit if not tuned properly

## Python Example

``` python
from sklearn.ensemble import GradientBoostingClassifier

model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)
model.fit(X_train, y_train)
```

------------------------------------------------------------------------

# 2. CatBoost

## Definition

CatBoost (Categorical Boosting) is a gradient boosting algorithm
developed by Yandex that works efficiently with categorical features.

## Features

-   Handles categorical data automatically
-   Reduces overfitting
-   Fast and accurate
-   Minimal preprocessing required

## Applications

-   Customer churn prediction
-   Fraud detection
-   Recommendation systems
-   Medical diagnosis

## Python Example

``` python
from catboost import CatBoostClassifier

model = CatBoostClassifier(
    iterations=100,
    learning_rate=0.1,
    verbose=False
)
model.fit(X_train, y_train)
```

### CatBoost vs Random Forest

  Feature            CatBoost         Random Forest
  ------------------ ---------------- -------------------
  Ensemble Type      Boosting         Bagging
  Training           Sequential       Parallel
  Categorical Data   Native support   Encoding required
  Speed              Slower           Faster

------------------------------------------------------------------------

# 3. Model Deployment

## Definition

Model Deployment is the process of making a trained machine learning
model available for real-world use.

## Deployment Workflow

``` text
Collect Data
      │
Preprocess Data
      │
Train Model
      │
Evaluate Model
      │
Save Model
      │
Deploy (API/Web App)
      │
Predictions
```

## Popular Deployment Tools

-   Flask
-   FastAPI
-   Streamlit
-   Docker
-   Render
-   Railway
-   Hugging Face Spaces

## Saving a Model

``` python
import joblib

joblib.dump(model, "model.pkl")
```

## Loading a Model

``` python
model = joblib.load("model.pkl")
```

## Advantages

-   Real-time predictions
-   Automation
-   Easy integration with applications

## Viva Questions

1.  What is Gradient Boosting?
2.  Difference between Gradient Boosting and Random Forest.
3.  What is CatBoost?
4.  Why is CatBoost popular?
5.  What is Model Deployment?
6.  Name any deployment framework.
