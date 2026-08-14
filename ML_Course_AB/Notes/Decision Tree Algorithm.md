# Decision Tree Algorithm

> **Unit:** Supervised Machine Learning

---

# Table of Contents

1. Introduction
2. Definition
3. Terminology
4. Working of Decision Tree
5. Entropy
6. Information Gain
7. Gini Index
8. Types of Decision Trees
9. Advantages & Disadvantages
10. Applications
11. Python Implementation
12. Complexity Analysis
13. Comparison with KNN
14. Viva Questions
15. University Questions
16. Quick Revision

---

# 1. Introduction

A **Decision Tree** is one of the most popular supervised machine learning algorithms used for **Classification** and **Regression**.

It makes decisions by asking a sequence of questions and dividing the dataset into smaller subsets until a prediction is made.

Think of it like a flowchart where every question narrows down the answer.

> ⭐ **Exam Point:** Decision Tree is easy to understand because its structure resembles human decision-making.

---

# 2. Definition

### Simple Definition

A Decision Tree predicts the output by repeatedly splitting the dataset based on feature values.

### Technical Definition

> A **Decision Tree** is a supervised learning algorithm that recursively splits a dataset into subsets based on the feature that best separates the data, forming a tree-like structure for classification or regression.

---

# 3. Terminology

| Term          | Meaning                          |
| ------------- | -------------------------------- |
| Root Node     | Starting node of the tree        |
| Decision Node | Node where data is split         |
| Leaf Node     | Final prediction/output          |
| Branch        | Connection between nodes         |
| Split         | Dividing data based on a feature |
| Parent Node   | Node before splitting            |
| Child Node    | Node created after splitting     |

---

# 4. Working of Decision Tree

### Steps

1. Start with the complete dataset.
2. Calculate the best feature for splitting.
3. Split the dataset into subsets.
4. Repeat the process for each subset.
5. Stop when all records belong to the same class or another stopping condition is met.
6. The final nodes become **Leaf Nodes**.

---

### Flow Diagram

```text
                    Root Node
                   (Dataset)
                      │
         ┌────────────┴────────────┐
         │                         │
      Feature A               Feature B
         │                         │
    ┌────┴────┐              ┌─────┴─────┐
   Yes        No           Yes         No
   │           │            │            │
 Leaf        Decision      Leaf        Leaf
```

---

# Example

Suppose a bank wants to decide whether to approve a loan.

```text
               Income > ₹50,000?
                  /         \
               Yes           No
               /              \
      Credit Score > 700?     Reject
           /      \
        Yes        No
        |          |
     Approve    Reject
```

The tree asks simple questions until it reaches a decision.

---

# 5. Entropy

## Definition

Entropy measures the **impurity or randomness** of a dataset.

* High Entropy → Mixed classes
* Low Entropy → Pure classes

### Formula

[
Entropy(S)=-\sum_{i=1}^{n}p_i\log_2(p_i)
]

Where:

* (p_i) = Probability of class *i*

---

### Interpretation

| Entropy | Meaning                              |
| ------: | ------------------------------------ |
|       0 | Completely Pure                      |
|       1 | Maximum Uncertainty (Binary Classes) |

---

### Example

Dataset

| Yes | No |
| --: | -: |
|   5 |  5 |

Entropy = High

Dataset

| Yes | No |
| --: | -: |
|  10 |  0 |

Entropy = 0 (Pure)

> ⭐ **Exam Tip:** Lower entropy indicates a better split.

---

# 6. Information Gain

## Definition

Information Gain measures how much uncertainty is reduced after splitting the dataset.

The feature with the **highest Information Gain** is selected for splitting.

### Formula

[
Information\ Gain = Entropy(Parent)-Weighted\ Entropy(Children)
]

### Example

Suppose

Initial Entropy = 0.90

Entropy after split = 0.30

Then

[
IG=0.90-0.30=0.60
]

A higher value indicates a better split.

---

# 7. Gini Index

## Definition

The Gini Index is another measure of impurity.

It is commonly used in the **CART (Classification and Regression Tree)** algorithm.

### Formula

[
Gini = 1-\sum p_i^2
]

### Interpretation

| Gini Value   | Meaning     |
| ------------ | ----------- |
| 0            | Pure Node   |
| Higher Value | More Impure |

---

# Entropy vs Gini Index

| Feature     | Entropy         | Gini         |
| ----------- | --------------- | ------------ |
| Formula     | Logarithm Based | Square Based |
| Speed       | Slower          | Faster       |
| Used In     | ID3, C4.5       | CART         |
| Computation | Complex         | Simple       |

> ⭐ **Interview Point:** CART uses **Gini Index**, while ID3 uses **Entropy**.

---

# 8. Types of Decision Trees

### Classification Tree

Used when the output is categorical.

Examples:

* Spam / Not Spam
* Pass / Fail
* Yes / No

---

### Regression Tree

Used when the output is numerical.

Examples:

* House Price
* Temperature
* Salary Prediction

---

# 9. Advantages

* Easy to understand and visualize.
* Works with numerical and categorical data.
* Requires little data preprocessing.
* Performs feature selection automatically.
* Can handle nonlinear relationships.

---

# 10. Disadvantages

* Can overfit the training data.
* Sensitive to noisy data.
* Small changes in data may produce a different tree.
* Large trees become difficult to interpret.

---

# 11. Applications

* Loan Approval
* Medical Diagnosis
* Fraud Detection
* Customer Churn Prediction
* Email Spam Detection
* Employee Performance Analysis
* Stock Market Prediction
* Credit Risk Analysis

---

# 12. Python Implementation

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=5
)

model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

---

# 13. Complexity Analysis

| Operation  | Complexity                   |
| ---------- | ---------------------------- |
| Training   | O(N × D × log N) *(approx.)* |
| Prediction | O(tree depth)                |
| Space      | O(Number of Nodes)           |

Where:

* **N** = Number of training samples
* **D** = Number of features

> ⭐ Decision Trees are slower to train than KNN but much faster during prediction.

---

# 14. Overfitting in Decision Trees

A very deep tree may memorize the training data instead of learning general patterns.

### Solutions

* Limit maximum depth
* Pruning
* Minimum samples per leaf
* Random Forest

---

# 15. Pruning

Pruning removes unnecessary branches from a decision tree.

### Types

### Pre-Pruning

Stops tree growth early.

Examples:

* Maximum depth
* Minimum samples split

### Post-Pruning

Build the complete tree first, then remove unnecessary branches.

### Benefits

* Reduces overfitting
* Improves generalization
* Produces a simpler model

---

# 16. Comparison with KNN

| Feature          | Decision Tree | KNN            |
| ---------------- | ------------- | -------------- |
| Learning Type    | Eager         | Lazy           |
| Training         | Slower        | Very Fast      |
| Prediction       | Fast          | Slow           |
| Model Storage    | Tree          | Entire Dataset |
| Feature Scaling  | Not Required  | Required       |
| Interpretability | High          | Lower          |

---

# 17. Viva Questions

1. What is a Decision Tree?
2. Define Root Node.
3. What is a Leaf Node?
4. What is Entropy?
5. What is Information Gain?
6. What is the Gini Index?
7. Difference between Entropy and Gini?
8. What is Pruning?
9. Why do Decision Trees overfit?
10. Difference between Classification Tree and Regression Tree?

---

# 18. University Questions

### 2 Marks

* Define Decision Tree.
* What is Entropy?
* What is Information Gain?
* What is the Gini Index?

### 5 Marks

* Explain the working of a Decision Tree.
* Explain Entropy and Information Gain.
* Explain Pruning.

### 10 Marks

* Explain the Decision Tree algorithm with a neat diagram.
* Compare Entropy and Gini Index.
* Explain overfitting and pruning in Decision Trees.

---

# 19. Quick Revision

### Key Points

* **Algorithm Type:** Supervised Learning
* **Uses:** Classification & Regression
* **Root Node:** Starting point
* **Leaf Node:** Final prediction
* **Entropy:** Measures impurity
* **Information Gain:** Chooses the best split
* **Gini Index:** Used in CART
* **Pruning:** Reduces overfitting

### Memory Trick

**"R-E-G-P"**

* **R** → Root Node
* **E** → Entropy
* **G** → Gini Index
* **P** → Pruning

Remember this sequence when explaining the Decision Tree algorithm in exams.

---

