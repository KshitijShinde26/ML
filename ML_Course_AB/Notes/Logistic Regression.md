

# Logistic Regression (Complete Notes)

---

# 1. What is Logistic Regression?

## Definition

**Logistic Regression** is a **Supervised Machine Learning Classification Algorithm** used to predict **categorical outcomes**, especially **binary outcomes** such as **Yes/No**, **0/1**, **True/False**, etc.

Unlike Linear Regression, Logistic Regression predicts the **probability** that an input belongs to a particular class.

---

## Technical Definition (Exam Definition)

> Logistic Regression is a supervised learning algorithm that uses the **sigmoid (logistic) function** to estimate the probability that an input belongs to a particular class.

---

## Simple Definition

Logistic Regression answers questions like:

- Will the student pass or fail?
- Is the email spam or not spam?
- Does the patient have diabetes?
- Will the customer buy the product?

Instead of predicting a number like **₹50,000**, it predicts

```
Probability = 0.91

↓

Yes
```

or

```
Probability = 0.20

↓

No
```

---

# Why is it called Regression?

Many students think:

> "If Logistic Regression is used for Classification, why is it called Regression?"

Answer:

It uses a regression equation internally to calculate probability.

The final output is converted into classes using the Sigmoid Function.

Therefore,

- Mathematical model → Regression
- Final prediction → Classification

---

# Why Not Use Linear Regression for Classification?

Suppose we want to predict whether an email is Spam.

Possible outputs should be

```
0

or

1
```

But Linear Regression may predict

```
-2

1.8

5.6
```

These values are impossible for classification.

Logistic Regression solves this problem by restricting output between

```
0 and 1
```

which represents probability.

---

# Sigmoid (Logistic) Function

The Sigmoid Function converts any real number into a probability between **0 and 1**.

## Formula


$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$


Where

| Symbol | Meaning |
|---------|----------|
| \( \sigma(z) \) | Predicted Probability |
| \( e \) | Euler's Number (≈2.718) |
| \( z \) | Linear Equation |

---

## Linear Equation


$$
z=b_0+b_1x
$$


or for multiple variables


$$
z=b_0+b_1x_1+b_2x_2+\cdots+b_nx_n
$$


---

## Combined Logistic Regression Equation


$$
P(Y=1)=\frac{1}{1+e^{-(b_0+b_1x)}}
$$


For multiple variables

$$
P(Y=1)=\frac{1}{1+e^{-(b_0+b_1x_1+b_2x_2+\cdots+b_nx_n)}}
$$


---

## Sigmoid Curve

```text
Probability

1.0 |                            ********
    |                         ***
0.8 |                      ***
    |                   ***
0.6 |                ***
    |             ***
0.5 |-----------***
    |        ***
0.3 |     ***
    |   **
0.1 | **
    |*
0.0 +---------------------------------------->

             Linear Output (z)
```

Properties

- S-shaped Curve
- Output always between 0 and 1
- Converts linear equation into probability

---

# Working of Logistic Regression

## Step 1

Collect labeled data.

Example

| Study Hours | Pass |
|-------------|------|
|2|0|
|3|0|
|5|1|
|7|1|

---

## Step 2

Train the Logistic Regression model.

---

## Step 3

Calculate


$$
z=b_0+b_1x
$$


---

## Step 4

Apply Sigmoid Function


$$
P(Y=1)=\frac{1}{1+e^{-z}}
$$


---

## Step 5

Compare probability with threshold.

Usually

```
Threshold = 0.5
```

If

```
Probability ≥ 0.5

↓

Class = 1
```

Otherwise

```
Probability < 0.5

↓

Class = 0
```

---

# Decision Boundary

The **Decision Boundary** is the line or value that separates different classes.

Usually

```
Probability = 0.5
```

Example

```
Probability = 0.82

↓

Yes
```

```
Probability = 0.13

↓

No
```

---

# Flow Diagram

```text
Input Data

      │

      ▼

Linear Equation

      │

      ▼

Sigmoid Function

      │

      ▼

Probability

      │

      ▼

Threshold (0.5)

      │

      ▼

Class Prediction
```

---

# Types of Logistic Regression

## 1. Binary Logistic Regression

Only two classes.

Examples

- Yes / No
- Pass / Fail
- Spam / Not Spam

---

## 2. Multinomial Logistic Regression

More than two classes.

Example

Predict

```
Dog

Cat

Horse
```

---

## 3. Ordinal Logistic Regression

Classes have an order.

Example

```
Poor

Average

Good

Excellent
```

---

# Assumptions of Logistic Regression

1. Dependent variable should be categorical.
2. Independent variables should not be highly correlated.
3. Observations should be independent.
4. Large dataset improves performance.
5. Relationship between log-odds and independent variables should be linear.

---

# Cost Function

Unlike Linear Regression, Logistic Regression **does not use Mean Squared Error (MSE)** because the sigmoid function makes the optimization non-convex with MSE.

Instead, it uses **Log Loss (Binary Cross-Entropy)**.

## Formula

$$
J(\theta)
=
-\frac{1}{m}
\sum_{i=1}^{m}
\left[
y^{(i)}\log(\hat y^{(i)})
+
(1-y^{(i)})
\log(1-\hat y^{(i)})
\right]
$$


Where

- \(m\) = Number of training examples
- \(y\) = Actual class
- \(\hat{y}\) = Predicted probability

---

# Advantages

- Easy to implement
- Fast training
- Produces probability
- Works well for binary classification
- Interpretable model
- Less computational cost

---

# Disadvantages

- Cannot model complex nonlinear relationships
- Sensitive to outliers
- Requires sufficient data
- Assumes linear relationship in log-odds
- Lower performance on very complex datasets

---

# Applications

- Disease Prediction
- Credit Card Fraud Detection
- Spam Detection
- Customer Churn Prediction
- Loan Approval
- Face Recognition
- Marketing Campaign Prediction
- Sentiment Analysis

---

# Logistic Regression vs Linear Regression

| Feature | Linear Regression | Logistic Regression |
|----------|-------------------|---------------------|
|Purpose|Regression|Classification|
|Output|Continuous Value|Probability|
|Output Range|(-∞, +∞)|0 to 1|
|Function|Straight Line|Sigmoid Curve|
|Algorithm Type|Regression|Classification|
|Example|House Price|Spam Detection|

---

# Comparison with Other Classification Algorithms

| Algorithm | Output | Best For |
|-----------|---------|----------|
|Logistic Regression|Probability|Binary Classification|
|Decision Tree|Class|Complex Rules|
|KNN|Nearest Neighbors|Small Datasets|
|Naive Bayes|Probability|Text Classification|
|SVM|Class|High-Dimensional Data|

---

# Real-Life Example

Suppose a bank wants to predict whether a customer will repay a loan.

Input

- Salary
- Age
- Credit Score
- Existing Loan

Model Output

```
Probability = 0.92

↓

Loan Approved
```

or

```
Probability = 0.18

↓

Loan Rejected
```

---

# Interview / Viva Questions

### What is Logistic Regression?

A supervised learning classification algorithm used to predict categorical outcomes using the sigmoid function.

---

### Why is Logistic Regression used instead of Linear Regression?

Because it predicts probabilities between 0 and 1, making it suitable for classification.

---

### What is the Sigmoid Function?

A mathematical function that converts any real number into a probability between 0 and 1.

---

### What is the output of Logistic Regression?

Probability.

---

### What is the default threshold?

0.5

---

### Can Logistic Regression perform Regression?

No.

It is mainly used for classification despite its name.

---

### What are the types of Logistic Regression?

- Binary
- Multinomial
- Ordinal

---

# Expected University Questions

## 2 Marks

1. Define Logistic Regression.
2. What is the Sigmoid Function?
3. What is Decision Boundary?
4. What is Binary Logistic Regression?
5. What is the default threshold in Logistic Regression?

---

## 5 Marks

1. Explain the working of Logistic Regression.
2. Explain the Sigmoid Function.
3. Differentiate between Linear Regression and Logistic Regression.
4. Explain the types of Logistic Regression.

---

## 10 Marks

1. Explain Logistic Regression with architecture, equations, working, advantages, disadvantages, assumptions, and applications.
2. Explain the Sigmoid Function with diagram and formula.
3. Compare Logistic Regression with Linear Regression.

---

# Quick Revision

## Logistic Regression

- Supervised Learning
- Classification Algorithm
- Predicts Probability
- Uses Sigmoid Function
- Output between 0 and 1

## Sigmoid Function

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

## Linear Equation

$$
z=b_0+b_1x
$$

## Logistic Regression Equation

$$
P(Y=1)=\frac{1}{1+e^{-(b_0+b_1x)}}
$$

## Threshold

Usually

```
0.5
```

Above 0.5 → Class 1

Below 0.5 → Class 0

## Types

- Binary
- Multinomial
- Ordinal

## Applications

- Spam Detection
- Fraud Detection
- Disease Prediction
- Loan Approval
- Customer Churn

---

# Markdown Formulas (Copy Directly)

## Sigmoid Function


$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$


## Linear Equation


$$
z=b_0+b_1x
$$


## Multiple Variable Equation


$$
z=b_0+b_1x_1+b_2x_2+\cdots+b_nx_n
$$


## Logistic Regression Equation


$$
P(Y=1)=\frac{1}{1+e^{-(b_0+b_1x)}}
$$


## Multiple Logistic Regression Equation


$$
P(Y=1)=\frac{1}{1+e^{-(b_0+b_1x_1+b_2x_2+\cdots+b_nx_n)}}
$$


## Binary Cross-Entropy (Log Loss)


$$
J(\theta)
=
-\frac{1}{m}
\sum_{i=1}^{m}
\left[
y^{(i)}\log(\hat y^{(i)})
+
(1-y^{(i)})
\log(1-\hat y^{(i)})
\right]
$$


---