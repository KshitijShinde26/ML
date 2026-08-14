# **Introduction to Machine Learning & Evaluation Metrics**

---

# 1. What is Machine Learning and its Terminology?

## Definition

**Machine Learning (ML)** is a branch of Artificial Intelligence (AI) that enables computers to learn from data and improve their performance without being explicitly programmed.

### Technical Definition (Exam Definition)

> **Machine Learning is a field of computer science that uses algorithms and statistical models to enable computers to learn patterns from historical data and make predictions or decisions without explicit programming.**

---

## Simple Definition

Machine Learning teaches a computer **how to learn from examples** instead of writing every rule manually.

### Example

Instead of writing:

```
If email contains "Win Money"
then Spam
```

We give the computer thousands of spam and non-spam emails.

The computer learns the pattern by itself.

---

# Need for Machine Learning

Traditional programming cannot solve every problem because rules become very complex.

Machine Learning can

* Learn from data
* Improve accuracy with experience
* Handle huge datasets
* Discover hidden patterns
* Automate decision making

---

# Real-Life Applications

* Face Recognition
* Speech Recognition
* Netflix Recommendations
* Amazon Product Recommendation
* Medical Diagnosis
* Fraud Detection
* Self-driving Cars
* Weather Forecasting

---

# How Machine Learning Works

```
Collect Data
      ↓
Clean Data
      ↓
Choose ML Algorithm
      ↓
Train Model
      ↓
Test Model
      ↓
Evaluate Accuracy
      ↓
Deploy Model
```

---

# Basic Terminology in Machine Learning

---

## 1. Dataset

A collection of data used for training or testing.

Example

| Age | Salary | Bought Laptop |
| --- | ------ | ------------- |
| 22  | 25000  | No            |
| 35  | 60000  | Yes           |

---

## 2. Features (Independent Variables)

Input variables used to predict the output.

Example

Age

Salary

Education

Experience

---

## 3. Label / Target (Dependent Variable)

Output that we want to predict.

Example

Bought Laptop

Yes/No

---

## 4. Instance / Sample

One row of a dataset.

---

## 5. Model

A mathematical representation learned from data.

Example

Spam Classifier

Price Predictor

---

## 6. Training Data

Data used to teach the model.

Usually

70%

80%

90%

---

## 7. Testing Data

Used to check model performance.

Usually

20%

30%

---

## 8. Algorithm

A procedure used for learning patterns.

Examples

Decision Tree

Random Forest

Linear Regression

KNN

SVM

Naïve Bayes

---

## 9. Prediction

Output produced by trained model.

---

## 10. Training

Process of learning patterns from data.

---

## 11. Inference

Using trained model on new unseen data.

---

## 12. Overfitting

Model memorizes training data.

High Training Accuracy

Low Testing Accuracy

---

## 13. Underfitting

Model fails to learn patterns.

Low Training Accuracy

Low Testing Accuracy

---

## 14. Accuracy

Percentage of correct predictions.

---

## 15. Hyperparameters

Settings decided before training.

Examples

Learning Rate

Number of Trees

Epochs

Batch Size

---

## Diagram

```
                Machine Learning

                      │

              Historical Data

                      │

                ML Algorithm

                      │

             Learns Relationships

                      │

              Trained Model

                      │

          Prediction on New Data
```

---

# Advantages of Machine Learning

* Automates decision making
* Handles huge data
* Improves with more data
* High prediction accuracy
* Finds hidden patterns
* Reduces manual effort
* Useful in many industries

---

# Disadvantages

* Needs large amount of data
* Expensive training
* Can be biased
* Difficult to interpret
* Requires powerful hardware
* Sensitive to poor-quality data

---

# Viva Questions

### What is Machine Learning?

Machine Learning is a subset of AI where computers learn patterns from data without explicit programming.

---

### What is a feature?

Input variable used for prediction.

---

### What is a label?

Output variable.

---

### Difference between AI and ML?

AI is broader.

ML is a subset of AI.

---

# 2. Classification vs Regression

Both are **Supervised Learning** techniques.

---

## Classification

Predicts **categorical outputs**.

Example

Spam or Not Spam

Yes or No

Healthy or Diseased

Pass or Fail

---

### Output

Discrete

Finite classes

Example

Dog

Cat

Horse

---

### Algorithms

Decision Tree

Naïve Bayes

Random Forest

Logistic Regression

SVM

KNN

---

## Regression

Predicts **continuous values**.

Example

House Price

Temperature

Stock Price

Salary Prediction

---

### Output

Continuous Numbers

Example

25.6

78.4

450000

---

### Algorithms

Linear Regression

Polynomial Regression

Decision Tree Regression

Random Forest Regression

---

# Comparison Table

| Feature    | Classification              | Regression             |
| ---------- | --------------------------- | ---------------------- |
| Output     | Categorical                 | Continuous             |
| Prediction | Class Label                 | Numeric Value          |
| Example    | Spam Detection              | House Price Prediction |
| Evaluation | Accuracy, Precision, Recall | MAE, MSE, RMSE         |
| Algorithms | Decision Tree, SVM          | Linear Regression      |

---

## Examples

### Classification

Email

Spam

Not Spam

---

### Regression

House Area

Predict House Price

---

## Diagram

```
Classification

Input → Model → Class

Email → Spam Detector → Spam



Regression

Input → Model → Value

House → Price Predictor → ₹55 Lakhs
```

---

# Advantages

Classification

* Easy interpretation
* Useful for decision making
* High accuracy

Regression

* Predicts exact values
* Useful for forecasting
* Continuous prediction

---

# Viva Questions

What is Classification?

Predicting categories.

---

What is Regression?

Predicting continuous values.

---

Give one example of Classification.

Disease Detection.

---

Give one example of Regression.

House Price Prediction.

---

# 3. Classification Error Metrics

Evaluation metrics measure how well a classification model performs.

---

## Confusion Matrix

A table that compares predicted and actual values.

| Actual \ Predicted | Positive | Negative |
| ------------------ | -------- | -------- |
| Positive           | TP       | FN       |
| Negative           | FP       | TN       |

---

### TP (True Positive)

Correct Positive Prediction

Example

Patient has disease

Model predicts disease

---

### TN

Correct Negative Prediction

---

### FP

Model predicts disease

Actually healthy

False Alarm

---

### FN

Model predicts healthy

Actually diseased

Dangerous error

---

## 1. Accuracy

Measures overall correctness.

**Formula**

$$
\text{Accuracy}=\frac{TP+TN}{TP+TN+FP+FN}
$$

Interpretation: Higher accuracy means more correct predictions.

---

## 2. Precision

Measures how many predicted positives are actually positive.

**Formula**

$$
\text{Precision}=\frac{TP}{TP+FP}
$$

Useful when **false positives are costly** (e.g., spam detection).

---

## 3. Recall (Sensitivity)

Measures how many actual positives are correctly detected.

**Formula**

$$
\text{Recall}=\frac{TP}{TP+FN}
$$

Useful when **missing a positive case is dangerous** (e.g., disease detection).

---

## 4. F1 Score

Balances Precision and Recall.

**Formula**

$$
F_1 = 2 \times \frac{\text{Precision}\times\text{Recall}}{\text{Precision}+\text{Recall}}
$$

Useful for **imbalanced datasets**.

---

## 5. Specificity

Measures correctly identified negatives.

**Formula**

$$
\text{Specificity}=\frac{TN}{TN+FP}
$$

---

## Importance of Classification Metrics

* Measures model quality
* Compares models
* Helps choose the best algorithm
* Detects model weaknesses

---

## Applications

* Cancer Detection
* Spam Detection
* Face Recognition
* Fraud Detection

---

# Viva Questions

What is TP?

Correct positive prediction.

---

What is Recall?

Ability to detect actual positives.

---

When is Precision important?

When false positives should be minimized.

---

# 4. Regression Metrics

Regression metrics evaluate how close predicted values are to actual values.

---

## 1. Mean Absolute Error (MAE)

Average of absolute errors.

**Formula**

$$
MAE=\frac{1}{n}\sum_{i=1}^{n}\left|y_i-\hat{y}_i\right|
$$

* Easy to understand
* Less affected by outliers than MSE

---

## 2. Mean Squared Error (MSE)

Average of squared errors.

**Formula**

$$
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$  

* Penalizes large errors more heavily.
* Useful when large mistakes should be discouraged.

---

## 3. Root Mean Squared Error (RMSE)

Square root of MSE.

**Formula**

$$
RMSE=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
$$

* Expressed in the same units as the target variable.
* Commonly used for model comparison.

---

## 4. R² Score (Coefficient of Determination)

Measures how well the model explains the variation in the data.

**Formula**

$$
R^2 = 1-\frac{\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}{\sum_{i=1}^{n}(y_i-\bar{y})^2}
$$

* (R^2 = 1): Perfect prediction
* (R^2 = 0): Model performs like predicting the average
* (R^2 < 0): Model performs worse than predicting the average

And extra formula:

$$
\bar{y}=\frac{1}{n}\sum_{i=1}^{n}y_i
$$

* For Mean
---

## Comparison of Regression Metrics

| Metric   | Meaning                | Best Value |
| -------- | ---------------------- | ---------- |
| MAE      | Average absolute error | 0          |
| MSE      | Average squared error  | 0          |
| RMSE     | Square root of MSE     | 0          |
| R² Score | Explained variance     | 1          |

---

## Applications

* House Price Prediction
* Stock Price Forecasting
* Weather Prediction
* Sales Forecasting
* Demand Prediction

---

## Advantages of Regression Metrics

* Quantify prediction error
* Compare multiple regression models
* Help improve model performance
* Evaluate forecasting accuracy

---

## Viva Questions

**What is MAE?**
Average absolute difference between actual and predicted values.

**What is MSE?**
Average of squared prediction errors.

**Why is RMSE preferred sometimes?**
Because it is in the same units as the predicted variable and penalizes large errors.

**What does an R² score of 1 indicate?**
The model perfectly explains the variation in the data.

---

# ⭐ Quick Revision (Exam Points)

### Machine Learning

* Subset of AI
* Learns from data
* No explicit programming
* Uses algorithms to make predictions

### Classification

* Predicts categories
* Examples: Spam detection, disease diagnosis

### Regression

* Predicts continuous values
* Examples: House price, salary prediction

### Classification Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Specificity
* Confusion Matrix (TP, TN, FP, FN)

### Regression Metrics

* MAE
* MSE
* RMSE
* R² Score

---

# Expected University Exam Questions

### 2 Marks

1. Define Machine Learning.
2. What is a feature in Machine Learning?
3. Define classification.
4. Define regression.
5. What is a confusion matrix?
6. What is MAE?

### 5 Marks

1. Explain the terminology used in Machine Learning.
2. Differentiate between classification and regression.
3. Explain the confusion matrix with an example.
4. Explain MAE, MSE, and RMSE.

### 10 Marks

1. Explain Machine Learning with its terminology, workflow, advantages, disadvantages, and applications.
2. Compare classification and regression with suitable examples and algorithms.
3. Explain classification error metrics (Accuracy, Precision, Recall, F1 Score, Specificity) with formulas.
4. Explain regression metrics (MAE, MSE, RMSE, and R² Score) with formulas, interpretations, and applications.
