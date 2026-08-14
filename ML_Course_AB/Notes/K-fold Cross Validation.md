

#  K-Fold Cross Validation (Complete Notes)

---

# 1. What is Cross Validation?

## Definition

**Cross Validation** is a model evaluation technique used to measure how well a Machine Learning model performs on **unseen data**.

Instead of evaluating the model on only one train-test split, Cross Validation repeatedly trains and tests the model using different subsets of the dataset.

---

## Technical Definition (Exam Definition)

> Cross Validation is a resampling technique used to evaluate the performance and generalization ability of a machine learning model by dividing the dataset into multiple subsets and performing multiple rounds of training and testing.

---

## Simple Definition

Suppose a teacher wants to know whether a student has actually learned.

Instead of conducting **one exam**, the teacher conducts **five different exams**.

If the student performs well in all five exams, the teacher concludes that the student has learned well.

Cross Validation works in the same way.

---

# Why Do We Need Cross Validation?

If we evaluate a model using only one train-test split,

- Accuracy may be too high.
- Accuracy may be too low.
- Results depend on how data was divided.

Cross Validation solves this problem by testing the model multiple times.

---

## Problems Solved by Cross Validation

- Overfitting
- Underfitting
- Data bias
- Poor generalization
- Unstable accuracy

---

# What is K-Fold Cross Validation?

## Definition

**K-Fold Cross Validation** is a model evaluation technique in which the dataset is divided into **K equal parts (folds)**.

One fold is used for **testing**, while the remaining **K−1 folds** are used for **training**.

This process is repeated **K times**, so every fold becomes the testing set exactly once.

Finally, the average accuracy is calculated.

---

## Technical Definition

> K-Fold Cross Validation is a resampling technique that divides the dataset into K equal subsets and performs K iterations of training and testing, ensuring that every sample is used once for testing and K−1 times for training.

---

# Working of K-Fold Cross Validation

Suppose

```
K = 5
```

Dataset

```
100 Samples
```

Each fold contains

```
20 Samples
```

---

## Iteration 1

```text
Fold1 → Testing

Fold2

Fold3

Fold4

Fold5 → Training
```

---

## Iteration 2

```text
Fold2 → Testing

Fold1

Fold3

Fold4

Fold5 → Training
```

---

## Iteration 3

```text
Fold3 → Testing

Fold1

Fold2

Fold4

Fold5 → Training
```

---

## Iteration 4

```text
Fold4 → Testing

Fold1

Fold2

Fold3

Fold5 → Training
```

---

## Iteration 5

```text
Fold5 → Testing

Fold1

Fold2

Fold3

Fold4 → Training
```

---

## Final Step

Average Accuracy


$$
\text{Average Accuracy}
=
\frac{\text{Accuracy}_1+\text{Accuracy}_2+\cdots+\text{Accuracy}_K}{K}
$$


---

# Flow Diagram

```text
Complete Dataset

      │

Divide into K Folds

      │

Train on K−1 folds

      │

Test on Remaining Fold

      │

Repeat K Times

      │

Calculate Average Accuracy
```

---

# Example

Suppose

```
K = 5
```

Accuracy obtained

```
Iteration 1 = 95%

Iteration 2 = 93%

Iteration 3 = 96%

Iteration 4 = 94%

Iteration 5 = 92%
```

Average Accuracy


$$
\frac{95+93+96+94+92}{5}
=
94\%
$$


Therefore,

```
Final Accuracy = 94%
```

---

# Choosing the Value of K

Common values

| K | Description |
|----|-------------|
|3|Less computation|
|5|Most commonly used|
|10|Higher accuracy estimation|
|N|Leave-One-Out Cross Validation|

---

# Advantages of Larger K

- Better use of data
- Lower bias
- More reliable accuracy

---

# Disadvantages of Larger K

- More computation
- Longer training time
- Higher processing cost

---

# Types of Cross Validation

## 1. K-Fold Cross Validation

Most popular method.

Dataset divided into K equal parts.

---

## 2. Stratified K-Fold Cross Validation

Used for **imbalanced datasets**.

Maintains the same class distribution in every fold.

Example

Original Dataset

```
90% Healthy

10% Diseased
```

Each fold also contains

```
90% Healthy

10% Diseased
```

---

## Advantages

- Better class balance
- Higher accuracy
- Preferred for classification problems

---

## Applications

- Disease Prediction
- Fraud Detection
- Spam Detection

---

## 3. Leave-One-Out Cross Validation (LOOCV)

Special case of K-Fold.

```
K = Number of Samples
```

Suppose

```
100 Samples
```

Then

```
K = 100
```

Each iteration

```
99 Training Samples

1 Testing Sample
```

---

### Advantages

- Maximum use of data
- Low bias

---

### Disadvantages

- Extremely slow
- Computationally expensive

---

## 4. Repeated K-Fold Cross Validation

K-Fold is repeated multiple times using different random splits.

Example

```
5-Fold

Repeated 10 Times
```

Provides more reliable evaluation.

---

## 5. Hold-Out Validation (Train-Test Split)

Simplest evaluation method.

Example

```
80% Training

20% Testing
```

Used when dataset is very large.

---

# Train-Test Split vs K-Fold Cross Validation

| Feature | Train-Test Split | K-Fold Cross Validation |
|----------|-----------------|--------------------------|
|Training|One Time|K Times|
|Testing|One Time|K Times|
|Accuracy|Less Reliable|More Reliable|
|Computation|Low|Higher|
|Dataset Usage|Limited|Efficient|
|Generalization|Moderate|Better|

---

# Advantages of K-Fold Cross Validation

- Better model evaluation
- Reduces overfitting
- Efficient use of data
- Reliable accuracy
- Less biased evaluation
- Every sample is used for both training and testing

---

# Disadvantages

- Time-consuming
- Higher computational cost
- Slower for large datasets
- Difficult for extremely large deep learning models

---

# Applications

- Medical Diagnosis
- Stock Price Prediction
- Customer Churn Prediction
- Image Classification
- Recommendation Systems
- Sentiment Analysis
- Fraud Detection
- Face Recognition

---

# When Should We Use K-Fold?

Use when

- Dataset is small
- Accurate evaluation is required
- Model comparison is needed
- Avoiding overfitting is important

---

# When Should We Avoid K-Fold?

Avoid when

- Dataset is extremely large
- Training takes many hours
- Deep Learning models are computationally expensive

---

# Real-Life Example

Suppose a college has

```
100 Students
```

Teacher wants to evaluate performance fairly.

Instead of conducting only one exam,

Teacher divides students into

```
5 Groups
```

Each group becomes the test group once.

Finally,

Average Marks are calculated.

This is exactly how K-Fold Cross Validation works.

---

# Interview / Viva Questions

### What is Cross Validation?

A technique used to evaluate machine learning models using multiple train-test splits.

---

### What is K-Fold Cross Validation?

A model evaluation technique where the dataset is divided into K folds and each fold is used once for testing.

---

### Why is K-Fold better than Train-Test Split?

Because it provides a more reliable estimate of model performance.

---

### What is Stratified K-Fold?

A K-Fold technique that preserves the class distribution in every fold.

---

### What is LOOCV?

Leave-One-Out Cross Validation where

```
K = Number of Samples
```

---

### What are common values of K?

```
5

10
```

---

### Why is K=5 commonly used?

It provides a good balance between computation time and evaluation accuracy.

---

# Expected University Questions

## 2 Marks

1. Define Cross Validation.
2. Define K-Fold Cross Validation.
3. What is Stratified K-Fold?
4. What is LOOCV?
5. Why is Cross Validation used?

---

## 5 Marks

1. Explain the working of K-Fold Cross Validation.
2. Differentiate Train-Test Split and K-Fold Cross Validation.
3. Explain Stratified K-Fold.

---

## 10 Marks

1. Explain K-Fold Cross Validation with diagram, algorithm, advantages, disadvantages, and applications.
2. Explain different types of Cross Validation.
3. Compare Hold-Out Validation and K-Fold Cross Validation.

---

# Quick Revision

## Cross Validation

- Evaluates model performance
- Uses multiple train-test splits
- Reduces overfitting

---

## K-Fold

- Divide dataset into K folds
- Train on K−1 folds
- Test on remaining fold
- Repeat K times
- Calculate average accuracy

---

## Types

- K-Fold
- Stratified K-Fold
- Leave-One-Out (LOOCV)
- Repeated K-Fold
- Hold-Out Validation

---

## Common Values of K

```
5

10
```

---

## Formula

Average Accuracy


$$
\text{Average Accuracy}
=
\frac{\text{Accuracy}_1+\text{Accuracy}_2+\cdots+\text{Accuracy}_K}{K}
$$


---

## Advantages

- Better accuracy estimation
- Less overfitting
- Better generalization
- Efficient use of data

---

## Disadvantages

- Time-consuming
- Computationally expensive
- Slower on very large datasets

---

# Markdown Formulas (Copy Directly)

## Average Accuracy


$$
\text{Average Accuracy}
=
\frac{\text{Accuracy}_1+\text{Accuracy}_2+\cdots+\text{Accuracy}_K}{K}
$$


## K-Fold Condition


$$
\text{Training Samples} = K-1 \text{ folds}
$$



$$
\text{Testing Samples} = 1 \text{ fold}
$$


## LOOCV


$$
K = N
$$


Where

- \(K\) = Number of folds
- \(N\) = Total number of samples

---

# Complete Unit Summary

## Logistic Regression

- Supervised Learning
- Classification Algorithm
- Uses Sigmoid Function
- Predicts Probability (0–1)
- Types: Binary, Multinomial, Ordinal

## K-Fold Cross Validation

- Model Evaluation Technique
- Dataset divided into K folds
- Every fold used once for testing
- Average performance calculated
- Common values: K = 5 or K = 10

---