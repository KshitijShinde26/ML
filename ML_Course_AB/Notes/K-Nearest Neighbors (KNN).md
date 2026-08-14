
---

# K-Nearest Neighbors (KNN) Algorithm

> **Unit:** Supervised Machine Learning

---

# Table of Contents

1. Introduction
2. Definition
3. Terminology
4. Working of KNN
5. Distance Metrics
6. Choosing K Value
7. Feature Scaling
8. Advantages & Disadvantages
9. Applications
10. Python Implementation
11. Complexity Analysis
12. Comparison with Other Algorithms
13. Viva Questions
14. University Questions
15. Quick Revision

---

# 1. Introduction

K-Nearest Neighbors (**KNN**) is one of the simplest **Supervised Machine Learning** algorithms used for **Classification** and **Regression** problems.

Unlike many machine learning algorithms, KNN **does not build a mathematical model** during training. It stores the training data and predicts the output of a new data point based on its nearest neighbors.

> ⭐ **Exam Point:** KNN is called a **Lazy Learning** and **Instance-Based Learning** algorithm.

---

# 2. Definition

### Simple Definition

KNN predicts the class or value of a new data point by looking at the **K nearest data points** in the training dataset.

### Technical Definition

> **K-Nearest Neighbors (KNN)** is a **non-parametric**, **instance-based**, supervised learning algorithm that classifies a new sample using the majority class (classification) or average value (regression) of its **K nearest neighbors**.

---

# 3. Key Terminology

| Term            | Meaning                             |
| --------------- | ----------------------------------- |
| K               | Number of nearest neighbors         |
| Neighbor        | Closest training data point         |
| Query Point     | New data point to be predicted      |
| Training Data   | Known labeled dataset               |
| Test Data       | Data used to evaluate the model     |
| Majority Voting | Most frequent class among neighbors |

---

# 4. Working of KNN

## Steps

1. Choose the value of **K**.
2. Store the training dataset.
3. Calculate the distance between the query point and all training samples.
4. Sort the distances.
5. Select the **K nearest neighbors**.
6. Use **majority voting** (classification) or **average** (regression).
7. Predict the output.

### Flow Diagram

```text
          Training Dataset
                 │
                 ▼
          New Query Point
                 │
                 ▼
      Calculate Distances
                 │
                 ▼
        Sort Distances
                 │
                 ▼
      Select K Neighbors
                 │
                 ▼
 Majority Voting / Average
                 │
                 ▼
         Predicted Output
```

---

# 5. Distance Metrics

Distance metrics determine how "close" two data points are.

| Metric                | Formula                        | Best Used For                 |                   |                      |
| --------------------- | ------------------------------ | ----------------------------- | ----------------- | -------------------- |
| **Euclidean**         | ( d=\sqrt{\sum(x_i-y_i)^2} )   | Continuous numerical data     |                   |                      |
| **Manhattan**         | ( d=\sum                       | x_i-y_i                       | )                 | Grid-like movement   |
| **Minkowski**         | ( d=\left(\sum                 | x_i-y_i                       | ^p\right)^{1/p} ) | Generalized distance |
| **Hamming**           | Count of differing positions   | Binary/Categorical data       |                   |                      |
| **Cosine Similarity** | Measures angle between vectors | Text & Recommendation Systems |                   |                      |

> ⭐ **Most commonly used:** Euclidean Distance.

---

# 6. Choosing the Value of K

The choice of **K** affects model performance.

| K Value | Effect                             |
| ------- | ---------------------------------- |
| Small K | Overfitting, sensitive to noise    |
| Large K | Underfitting, smoother predictions |

### Rule of Thumb

[
K \approx \sqrt{N}
]

where **N** is the number of training samples.

### Why use an odd K?

Odd values (3, 5, 7...) reduce the chance of ties during majority voting.

---

# 7. Feature Scaling

KNN relies on **distance calculations**, so features with larger values can dominate.

### Example

| Feature |  Value |
| ------- | -----: |
| Age     |     25 |
| Salary  | 500000 |

Without scaling, **Salary** has much more influence than **Age**.

### Common Techniques

* **Min-Max Scaling**

[
x'=\frac{x-x_{min}}{x_{max}-x_{min}}
]

* **Standardization**

[
z=\frac{x-\mu}{\sigma}
]

---

# Curse of Dimensionality

As the number of features increases:

* Distance calculations become less meaningful.
* Prediction accuracy may decrease.
* Computation time increases.

### Solutions

* Feature Selection
* PCA (Principal Component Analysis)
* Remove irrelevant features

---

# 8. Advantages & Disadvantages

## Advantages

* Simple and easy to implement.
* No training phase.
* Works for classification and regression.
* Good accuracy for small datasets.
* Naturally supports multi-class classification.

## Disadvantages

* Slow prediction on large datasets.
* High memory usage.
* Sensitive to feature scaling.
* Performance depends on choosing the correct K.
* Affected by the curse of dimensionality.

---

# 9. Applications

* Image Classification
* Face Recognition
* Handwriting Recognition
* Recommendation Systems
* Medical Diagnosis
* Fraud Detection
* Customer Segmentation
* Credit Risk Analysis

---

# 10. Python Implementation

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

---

# 11. Complexity Analysis

| Operation  | Complexity             |
| ---------- | ---------------------- |
| Training   | **O(1)** (stores data) |
| Prediction | **O(N × D)**           |
| Space      | **O(N × D)**           |

Where:

* **N** = Number of training samples
* **D** = Number of features

> ⭐ Since KNN checks all training samples during prediction, it is fast to train but slow to predict.

---

# 12. Comparison with Other Algorithms

| Feature        | KNN       | Logistic Regression | Decision Tree |
| -------------- | --------- | ------------------- | ------------- |
| Learning       | Lazy      | Eager               | Eager         |
| Model          | No        | Yes                 | Yes           |
| Training       | Very Fast | Medium              | Slow          |
| Prediction     | Slow      | Fast                | Fast          |
| Classification | ✅         | ✅                   | ✅             |
| Regression     | ✅         | ❌                   | ✅             |

---

# 13. Viva Questions

1. What is KNN?
2. Why is KNN called Lazy Learning?
3. What is the role of K?
4. Why is feature scaling important?
5. Which distance metric is commonly used?
6. Why are odd values of K preferred?
7. What is the Curse of Dimensionality?
8. Can KNN perform regression?
9. Is KNN parametric or non-parametric?
10. What is majority voting?

---

# 14. University Questions

### 2 Marks

* Define KNN.
* What is majority voting?
* What is the role of K?
* List two applications of KNN.

### 5 Marks

* Explain the working of KNN.
* Explain different distance metrics.
* Explain feature scaling in KNN.

### 10 Marks

* Explain KNN with algorithm, diagram, advantages, disadvantages, and applications.
* Explain the effect of K and the curse of dimensionality.
* Compare KNN with Logistic Regression and Decision Tree.

---

# 15. Quick Revision

## Remember These Points

* **Type:** Supervised Learning
* **Nature:** Non-Parametric, Instance-Based, Lazy Learning
* **Uses:** Classification & Regression
* **Most Used Distance:** Euclidean Distance
* **Small K:** Overfitting
* **Large K:** Underfitting
* **Feature Scaling:** Required
* **Training Complexity:** O(1)
* **Prediction Complexity:** O(N × D)

### Memory Trick

**KNN = "Keep Nearby Neighbors"**

Think of asking your **nearest neighbors** for advice before making a decision. The majority opinion becomes the prediction.

---


