# Random Forest Algorithm

> **Unit:** Supervised Machine Learning

---

# Table of Contents

1. Introduction
2. Definition
3. Why Random Forest?
4. Working of Random Forest
5. Bootstrap Sampling
6. Feature Randomness
7. Voting & Averaging
8. Advantages & Disadvantages
9. Applications
10. Python Implementation
11. Complexity Analysis
12. Comparison with Decision Tree
13. Viva Questions
14. University Questions
15. Quick Revision

---

# 1. Introduction

A **Random Forest** is an **ensemble learning algorithm** that combines multiple Decision Trees to improve prediction accuracy and reduce overfitting.

Instead of relying on a single Decision Tree, Random Forest makes predictions using the combined output of many trees.

> ⭐ **Exam Point:** Random Forest = **Many Decision Trees working together.**

---

# 2. Definition

### Simple Definition

Random Forest is a machine learning algorithm that builds multiple Decision Trees and combines their predictions.

### Technical Definition

> **Random Forest** is a supervised ensemble learning algorithm that constructs multiple Decision Trees using randomly selected training samples and features, then combines their predictions using **majority voting (classification)** or **averaging (regression).**

---

# 3. Why Random Forest?

A single Decision Tree can **overfit** the training data.

Random Forest solves this problem by:

* Building many Decision Trees.
* Training each tree on different data samples.
* Combining predictions.

This leads to:

* Higher accuracy
* Better generalization
* Lower overfitting

---

# 4. Working of Random Forest

### Step-by-Step

1. Select random samples from the training dataset (**Bootstrap Sampling**).
2. Build multiple Decision Trees.
3. At each split, consider only a random subset of features.
4. Each tree makes its own prediction.
5. Combine all predictions.

* **Classification → Majority Voting**
* **Regression → Average Prediction**

---

### Flow Diagram

```text
                Training Dataset
                        │
        ┌───────────────┼───────────────┐
        │               │               │
   Random Sample    Random Sample   Random Sample
        │               │               │
      Tree 1          Tree 2          Tree 3
        │               │               │
     Predict         Predict         Predict
        └───────────────┼───────────────┘
                        │
       Majority Voting / Average
                        │
                 Final Prediction
```

---

# 5. Bootstrap Sampling

## Definition

Bootstrap Sampling is the process of creating multiple datasets by **randomly selecting samples from the original dataset with replacement**.

### With Replacement

If one record is selected, it **can be selected again**.

Example

Original Dataset

```text
A B C D E
```

Random Sample

```text
A C B A E
```

Notice that:

* **A** appears twice.
* **D** is missing.

This is valid because sampling is done **with replacement**.

---

## Advantages

* Produces different datasets.
* Increases model diversity.
* Reduces overfitting.

---

# 6. Feature Randomness

Random Forest does not use all features at every split.

Instead,

it randomly selects a subset of features.

### Example

Suppose there are **8 features**.

Decision Tree

```text
Uses all 8 features.
```

Random Forest

```text
Tree 1 → Features 1,4,7

Tree 2 → Features 2,3,5

Tree 3 → Features 1,6,8
```

Each tree learns differently.

This improves generalization.

---

# 7. Voting & Averaging

## Classification

Each tree predicts a class.

Example

| Tree   | Prediction |
| ------ | ---------- |
| Tree 1 | Cat        |
| Tree 2 | Dog        |
| Tree 3 | Cat        |
| Tree 4 | Cat        |
| Tree 5 | Dog        |

Majority Vote

```text
Cat
```

Final Prediction = **Cat**

---

## Regression

Each tree predicts a numerical value.

Example

| Tree | House Price (₹ Lakh) |
| ---- | -------------------: |
| 1    |                   48 |
| 2    |                   50 |
| 3    |                   52 |

Average

[
\frac{48+50+52}{3}=50
]

Final Prediction = **₹50 Lakh**

---

# 8. Advantages

* High accuracy.
* Reduces overfitting.
* Handles missing values better than a single tree.
* Works with large datasets.
* Handles both classification and regression.
* Robust to noise.

---

# 9. Disadvantages

* Slower than a single Decision Tree.
* Requires more memory.
* Difficult to interpret.
* Large models may consume more computational resources.

---

# 10. Applications

* Medical Diagnosis
* Credit Card Fraud Detection
* Loan Approval
* Customer Churn Prediction
* Stock Market Analysis
* Recommendation Systems
* Weather Prediction
* Image Classification

---

# 11. Python Implementation

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

### Important Parameters

| Parameter    | Meaning                        |
| ------------ | ------------------------------ |
| n_estimators | Number of Decision Trees       |
| max_depth    | Maximum depth of each tree     |
| random_state | Ensures reproducible results   |
| criterion    | Split criterion (gini/entropy) |

---

# 12. Complexity Analysis

| Operation  | Complexity                       |
| ---------- | -------------------------------- |
| Training   | O(T × N × D × log N) *(approx.)* |
| Prediction | O(T × tree depth)                |
| Space      | O(Number of Trees × Tree Size)   |

Where:

* **T** = Number of trees
* **N** = Training samples
* **D** = Features

---

# 13. Random Forest vs Decision Tree

| Feature          | Decision Tree | Random Forest   |
| ---------------- | ------------- | --------------- |
| Trees            | One           | Multiple        |
| Accuracy         | Moderate      | Higher          |
| Overfitting      | High          | Low             |
| Speed (Training) | Faster        | Slower          |
| Prediction       | Fast          | Slightly Slower |
| Interpretability | Easy          | Difficult       |

---

# 14. Random Forest vs KNN

| Feature         | Random Forest        | KNN            |
| --------------- | -------------------- | -------------- |
| Training        | Slower               | Very Fast      |
| Prediction      | Fast                 | Slow           |
| Feature Scaling | Usually Not Required | Required       |
| Overfitting     | Low                  | Depends on K   |
| Large Dataset   | Good                 | Less Efficient |

---

# 15. Common Interview Questions

### Why is it called Random Forest?

Because it creates a **forest (collection) of Decision Trees** using **random samples and random features**.

---

### What is Bootstrap Sampling?

Random sampling **with replacement** to create multiple training datasets.

---

### What is Majority Voting?

The class predicted by the majority of trees becomes the final prediction.

---

### Why is Random Forest more accurate than a Decision Tree?

Because combining multiple trees reduces variance and overfitting.

---

### Can Random Forest perform regression?

Yes, by averaging the predictions of all trees.

---

# 16. University Questions

## 2 Marks

* Define Random Forest.
* What is Bootstrap Sampling?
* What is Majority Voting?
* Give two applications of Random Forest.

### 5 Marks

* Explain the working of Random Forest.
* Explain Bootstrap Sampling.
* Compare Decision Tree and Random Forest.

### 10 Marks

* Explain the Random Forest algorithm with a neat diagram.
* Discuss the advantages and disadvantages of Random Forest.
* Compare Random Forest with Decision Tree and KNN.

---

# 17. Quick Revision

### Key Points

* **Type:** Supervised Learning
* **Method:** Ensemble Learning
* **Base Model:** Decision Tree
* **Bootstrap Sampling:** Sampling with replacement
* **Random Features:** Different features at each split
* **Classification:** Majority Voting
* **Regression:** Average Prediction
* **Overfitting:** Much lower than a single Decision Tree

### Memory Trick

**"BRAVE"**

* **B** → Bootstrap Sampling
* **R** → Random Features
* **A** → Average (Regression)
* **V** → Voting (Classification)
* **E** → Ensemble Learning

Remember **BRAVE** to quickly recall the main concepts of Random Forest during exams.

---

