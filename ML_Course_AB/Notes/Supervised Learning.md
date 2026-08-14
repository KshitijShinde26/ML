

---

# 1. What is Supervised Machine Learning?

## Definition

**Supervised Machine Learning** is a type of Machine Learning in which the model is trained using **labeled data**. Each training example contains both the **input (features)** and the **correct output (label)**. The goal is to learn the relationship between inputs and outputs so that the model can accurately predict the output for new, unseen data.

### Technical Definition (Exam Definition)

> **Supervised Machine Learning is a learning technique in which an algorithm is trained on labeled data to learn a mapping function from input variables to output variables, enabling it to predict outputs for unseen data.**

---

## Simple Explanation

Imagine a teacher teaching students.

* Questions = Input Data
* Correct Answers = Labels
* Student = Machine Learning Model

After learning from many solved examples, the student can answer new questions correctly.

Similarly, in supervised learning, the computer learns from examples that already have the correct answer.

---

## How Supervised Learning Works

```text
Training Dataset
(Input + Output)

        │

        ▼

Machine Learning Algorithm

        │

        ▼

Trained Model

        │

        ▼

New Input Data

        │

        ▼

Predicted Output
```

---

## Components of Supervised Learning

### 1. Input (Features)

Independent variables used for prediction.

Example

* Age
* Salary
* Experience

---

### 2. Output (Target/Label)

Dependent variable that the model predicts.

Example

* House Price
* Spam / Not Spam
* Disease / No Disease

---

### 3. Training Dataset

Dataset containing both inputs and correct outputs.

Example

| Age | Salary | Bought Laptop |
| --- | ------ | ------------- |
| 22  | 25000  | No            |
| 35  | 65000  | Yes           |
| 40  | 80000  | Yes           |

---

### 4. Model

A mathematical function learned from the training data.

---

## Types of Supervised Learning

### A. Classification

Predicts **categorical values**.

Examples

* Spam Detection
* Disease Detection
* Face Recognition

Output

```
Yes / No

Cat / Dog

Spam / Not Spam
```

---

### B. Regression

Predicts **continuous values**.

Examples

* House Price
* Temperature
* Salary Prediction

Output

```
₹4,50,000

35.6°C

75.8 kg
```

---

## Popular Supervised Learning Algorithms

* Linear Regression
* Logistic Regression
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)
* Naive Bayes
* K-Nearest Neighbors (KNN)

---

## Advantages

* Easy to evaluate
* High prediction accuracy
* Learns complex relationships
* Suitable for classification and regression
* Widely used in industry

---

## Disadvantages

* Requires labeled data
* Labeling data is expensive
* Can overfit
* Performance depends on data quality

---

## Applications

* Email Spam Detection
* Medical Diagnosis
* Credit Card Fraud Detection
* Stock Price Prediction
* Face Recognition
* Weather Forecasting
* Recommendation Systems

---

## Viva Questions

### What is Supervised Learning?

A machine learning technique where the model learns from labeled data.

---

### Why is it called supervised?

Because the correct answers (labels) are already known during training.

---

### What are labels?

Correct outputs associated with each training example.

---

# 2. Linear Regression Algorithm

## Definition

Linear Regression is a supervised learning algorithm used for predicting **continuous numerical values** by establishing a linear relationship between input variables and the output variable.

---

## Technical Definition

> **Linear Regression is a statistical method that models the relationship between one or more independent variables and a dependent variable by fitting a straight line to the observed data.**

---

## Real-Life Example

Predicting

* House Price
* Student Marks
* Salary
* Temperature

---

## Idea Behind Linear Regression

Suppose we have

| Experience (Years) | Salary  |
| ------------------ | ------- |
| 1                  | ₹25,000 |
| 2                  | ₹30,000 |
| 3                  | ₹40,000 |
| 4                  | ₹50,000 |

As experience increases, salary also increases.

The algorithm draws the **best-fit straight line** through the data.

```text
Salary

^

|                          *

|                     *

|                *

|           *

|      *

+------------------------------------>

           Experience
```

---

## Linear Regression Equation

genui{"inference_regression_ml_learning_block":{"type_id":"LEAST_SQUARE_REGRESSION"}}

The equation of the best-fit line is:


$$
\hat{y}=b_0+b_1x
$$


Where

| Symbol    | Meaning          |
| --------- | ---------------- |
| $\hat{y}$ | Predicted Output |
| $b_0$     | Intercept        |
| $b_1$     | Slope            |
| $x$       | Input Feature    |

---

## Meaning of Slope

Slope tells us how much **Y changes when X changes by one unit**.

Example

```
Slope = 10

Experience increases by 1 year

↓

Salary increases by ₹10,000
```

---

## Types of Linear Regression

### 1. Simple Linear Regression

One independent variable.

Example

Experience → Salary

---

### 2. Multiple Linear Regression

Multiple independent variables.

Example

Age

Experience

Education

↓

Salary

---

## Steps of Linear Regression

1. Collect data.
2. Clean and preprocess data.
3. Train the regression model.
4. Find the best-fit line.
5. Predict output.
6. Evaluate the model using MAE, MSE, RMSE, or R².

---

## Advantages

* Easy to understand
* Fast training
* Simple implementation
* Works well for linear data
* Interpretable model

---

## Disadvantages

* Assumes a linear relationship
* Sensitive to outliers
* Poor performance on nonlinear data
* Can underfit complex datasets

---

## Applications

* House Price Prediction
* Sales Forecasting
* Weather Prediction
* Stock Price Estimation
* Salary Prediction

---

## Viva Questions

### What type of algorithm is Linear Regression?

A supervised learning regression algorithm.

---

### What kind of output does it predict?

Continuous numerical values.

---

### What is the best-fit line?

The line that minimizes the prediction error between actual and predicted values.

---

# 3. Bias-Variance Trade-off

## Definition

The **Bias-Variance Trade-off** is the balance between a model that is **too simple** and a model that is **too complex**. The goal is to achieve the lowest possible prediction error on unseen data.

---

## Understanding Bias

### Definition

Bias is the error caused by making **too many simplifying assumptions**.

A high-bias model cannot learn the true relationship.

Example

Trying to fit a straight line to curved data.

```text
Curved Data

*

    *

         *

             *

-------------------------

Straight Line

-------------------------
```

Result

```
High Bias

↓

Underfitting
```

---

## Understanding Variance

### Definition

Variance is the error caused when the model learns **too much from the training data**, including noise.

```text
Training Points

*     *       *

   *      *

       *

Very Curvy Line

~~~~~^^^^^^~~~~~~
```

Result

```
High Variance

↓

Overfitting
```

---

## Bias vs Variance

| Bias                      | Variance                    |
| ------------------------- | --------------------------- |
| Model too simple          | Model too complex           |
| Underfitting              | Overfitting                 |
| Misses important patterns | Learns noise                |
| Low training accuracy     | Very high training accuracy |
| Poor testing accuracy     | Poor testing accuracy       |

---

## Trade-off

```text
Model Complexity

Low ---------------------------- High

High Bias ---- Balanced ---- High Variance

Underfit                    Overfit
```

---

## Ideal Model

The best model has

* Low Bias
* Low Variance
* High Generalization

---

## How to Reduce Bias

* Increase model complexity
* Add more features
* Train longer
* Use better algorithms

---

## How to Reduce Variance

* Collect more training data
* Remove unnecessary features
* Use regularization
* Cross-validation
* Pruning (Decision Trees)

---

## Importance

* Prevents overfitting
* Prevents underfitting
* Improves testing accuracy
* Helps choose the best model

---

## Real-Life Example

### High Bias

A student studies only one chapter.

Fails the exam.

---

### High Variance

A student memorizes all previous question papers.

Fails when new questions appear.

---

### Balanced Model

A student understands concepts instead of memorizing.

Scores well in all exams.

---

## Viva Questions

### What is Bias?

Error due to overly simple assumptions, leading to underfitting.

---

### What is Variance?

Error due to learning noise from the training data, leading to overfitting.

---

### What is the Bias-Variance Trade-off?

The process of balancing bias and variance to achieve the best prediction performance on unseen data.

---

# Quick Revision

### Supervised Learning

* Uses labeled data
* Predicts output from input
* Two types: Classification and Regression

### Linear Regression

* Predicts continuous values
* Best-fit straight line
* Equation: $\hat{y}=b_0+b_1x$

### Bias

* Model too simple
* Underfitting

### Variance

* Model too complex
* Overfitting

### Ideal Model

* Low Bias
* Low Variance
* Good Generalization

---

# Expected University Exam Questions

## 2 Marks

1. Define Supervised Machine Learning.
2. What is Linear Regression?
3. Define Bias.
4. Define Variance.
5. What is Underfitting?

## 5 Marks

1. Explain Supervised Machine Learning with suitable examples.
2. Explain the working of Linear Regression.
3. Differentiate between Bias and Variance.

## 10 Marks

1. Explain Supervised Machine Learning with architecture, types, advantages, disadvantages, and applications.
2. Explain the Linear Regression algorithm with equation, working, advantages, disadvantages, and applications.
3. Explain the Bias-Variance Trade-off with suitable diagrams, examples, and comparison.
