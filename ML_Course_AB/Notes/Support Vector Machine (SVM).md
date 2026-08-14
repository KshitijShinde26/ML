# Support Vector Machine (SVM)

> **Unit:** Supervised Machine Learning

---

# Table of Contents

1. Introduction
2. Definition
3. Terminology
4. Working of SVM
5. Hyperplane
6. Support Vectors
7. Margin
8. Types of SVM
9. Kernel Trick
10. Advantages & Disadvantages
11. Applications
12. Python Implementation
13. Complexity Analysis
14. Comparison with KNN & Decision Tree
15. Viva Questions
16. University Questions
17. Quick Revision

---

# 1. Introduction

**Support Vector Machine (SVM)** is a powerful **Supervised Machine Learning** algorithm mainly used for **Classification**, but it can also perform **Regression (SVR)**.

The main objective of SVM is to find the **best decision boundary (Hyperplane)** that separates different classes with the **maximum margin**.

> ⭐ **Exam Point:** SVM selects the hyperplane with the **maximum margin**, leading to better generalization.

---

# 2. Definition

### Simple Definition

SVM separates different classes by drawing the best possible boundary between them.

### Technical Definition

> **Support Vector Machine (SVM)** is a supervised learning algorithm that finds the optimal hyperplane to separate data points of different classes while maximizing the margin between them.

---

# 3. Terminology

| Term            | Meaning                                               |
| --------------- | ----------------------------------------------------- |
| Hyperplane      | Decision boundary separating classes                  |
| Support Vectors | Data points closest to the hyperplane                 |
| Margin          | Distance between support vectors and hyperplane       |
| Kernel          | Function that transforms data into a higher dimension |
| Linear SVM      | Used when data is linearly separable                  |
| Non-Linear SVM  | Used when data cannot be separated by a straight line |

---

# 4. Working of SVM

### Steps

1. Load the training dataset.
2. Find the possible hyperplanes.
3. Calculate the margin for each hyperplane.
4. Select the hyperplane with the **maximum margin**.
5. Classify new data based on its position relative to the hyperplane.

---

## Flow Diagram

```text
              Training Dataset
                     │
                     ▼
         Find Possible Hyperplanes
                     │
                     ▼
          Calculate Margins
                     │
                     ▼
      Select Maximum Margin Plane
                     │
                     ▼
            Classify New Data
```

---

# 5. Hyperplane

## Definition

A **Hyperplane** is the decision boundary that separates different classes.

### Example

Suppose we have:

* Class A (○)
* Class B (●)

```text
○ ○ ○ ○

────────────── Hyperplane

● ● ● ●
```

The line separating the two classes is called the **Hyperplane**.

### Mathematical Equation

For two features:

[
w_1x_1+w_2x_2+b=0
]

Where:

* (w) = Weights
* (x) = Features
* (b) = Bias

---

# 6. Support Vectors

## Definition

Support Vectors are the **closest data points** to the hyperplane.

These points determine the position of the hyperplane.

### Illustration

```text
○    ○   ○

○  |-----------|  ●

○                ●

──────── Hyperplane

●                ●

●   |-----------|  ○

●     ●    ●
```

The nearest points (shown close to the boundary) are the **Support Vectors**.

> ⭐ If support vectors change, the hyperplane also changes.

---

# 7. Margin

## Definition

Margin is the **distance between the hyperplane and the nearest support vectors**.

### Types

### Small Margin

```text
○ ○

──────

● ●
```

More chances of classification errors.

---

### Large Margin

```text
○ ○ ○

────────────

● ● ●
```

Better separation and better generalization.

> ⭐ SVM always tries to maximize the margin.

---

# 8. Types of SVM

## Linear SVM

Used when data can be separated using a straight line.

Example:

```text
○ ○ ○

────────

● ● ●
```

---

## Non-Linear SVM

Used when data cannot be separated by a straight line.

Example:

```text
○   ○

●  ○  ●

○   ●
```

In this case, SVM uses the **Kernel Trick**.

---

# 9. Kernel Trick

## Definition

A **Kernel** transforms data into a higher-dimensional space where it becomes easier to separate.

Instead of explicitly converting the data, SVM uses kernel functions to compute the separation efficiently.

### Common Kernels

| Kernel                      | Use                        |
| --------------------------- | -------------------------- |
| Linear                      | Linearly separable data    |
| Polynomial                  | Curved decision boundaries |
| RBF (Radial Basis Function) | Complex non-linear data    |
| Sigmoid                     | Similar to Neural Networks |

---

# Linear vs Non-Linear SVM

| Linear SVM          | Non-Linear SVM           |
| ------------------- | ------------------------ |
| Straight hyperplane | Curved boundary          |
| Faster              | Slower                   |
| Simple datasets     | Complex datasets         |
| Linear Kernel       | RBF, Polynomial, Sigmoid |

---

# 10. Advantages

* Effective for high-dimensional data.
* Works well with small and medium-sized datasets.
* Maximizes margin, improving generalization.
* Less prone to overfitting.
* Can handle non-linear problems using kernels.

---

# 11. Disadvantages

* Slow for very large datasets.
* Kernel selection can be difficult.
* Sensitive to parameter tuning.
* Less interpretable than Decision Trees.

---

# 12. Applications

* Face Recognition
* Text Classification
* Spam Detection
* Image Classification
* Handwriting Recognition
* Bioinformatics
* Medical Diagnosis
* Fraud Detection

---

# 13. Python Implementation

```python
from sklearn.svm import SVC

model = SVC(
    kernel="rbf",
    C=1.0
)

model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

### Important Parameters

| Parameter | Meaning                                                        |
| --------- | -------------------------------------------------------------- |
| kernel    | Type of kernel (linear, rbf, poly, sigmoid)                    |
| C         | Regularization parameter                                       |
| gamma     | Controls influence of training points (for RBF, Poly, Sigmoid) |

---

# 14. Complexity Analysis

| Operation  | Complexity                     |
| ---------- | ------------------------------ |
| Training   | High (depends on dataset size) |
| Prediction | Fast                           |
| Space      | Moderate                       |

> ⭐ SVM performs best on **small to medium-sized datasets** with many features.

---

# 15. Comparison

## SVM vs KNN

| Feature               | SVM      | KNN       |
| --------------------- | -------- | --------- |
| Learning              | Eager    | Lazy      |
| Training              | Slow     | Very Fast |
| Prediction            | Fast     | Slow      |
| Feature Scaling       | Required | Required  |
| High-Dimensional Data | Better   | Poorer    |

---

## SVM vs Decision Tree

| Feature           | SVM          | Decision Tree    |
| ----------------- | ------------ | ---------------- |
| Decision Boundary | Hyperplane   | Tree Structure   |
| Interpretability  | Lower        | High             |
| Overfitting       | Lower        | Higher           |
| Non-linear Data   | Uses Kernels | Uses Tree Splits |

---

# 16. Viva Questions

1. What is SVM?
2. What is a Hyperplane?
3. What are Support Vectors?
4. What is Margin?
5. Why does SVM maximize the margin?
6. What is the Kernel Trick?
7. Name different kernel functions.
8. Difference between Linear and Non-Linear SVM.
9. What is the role of parameter **C**?
10. Where is SVM commonly used?

---

# 17. University Questions

### 2 Marks

* Define SVM.
* What is a Hyperplane?
* What are Support Vectors?
* What is the Kernel Trick?

### 5 Marks

* Explain the working of SVM.
* Explain Hyperplane and Margin.
* Explain Linear and Non-Linear SVM.

### 10 Marks

* Explain the SVM algorithm with a neat diagram.
* Explain different kernel functions.
* Compare SVM with KNN and Decision Tree.

---

# 18. Quick Revision

### Key Points

* **Type:** Supervised Learning
* **Uses:** Classification & Regression (SVR)
* **Decision Boundary:** Hyperplane
* **Nearest Points:** Support Vectors
* **Goal:** Maximize Margin
* **Non-Linear Data:** Kernel Trick
* **Popular Kernel:** RBF

### Memory Trick

**"HSMK"**

* **H** → Hyperplane
* **S** → Support Vectors
* **M** → Maximum Margin
* **K** → Kernel Trick

Remember **HSMK** to quickly recall the four core concepts of SVM during exams.

---


