# Unsupervised Machine Learning

> **Unit:** Unsupervised Learning

---

# Table of Contents

1. Introduction
2. Definition
3. Characteristics
4. Working of Unsupervised Learning
5. Types of Unsupervised Learning
6. Supervised vs Unsupervised Learning
7. Advantages & Disadvantages
8. Applications
9. Python Example
10. Viva Questions
11. University Questions
12. Quick Revision

---

# 1. Introduction

In many real-world situations, data **does not have labels**. For example, a company may have customer information but not know which customers belong to which group.

**Unsupervised Learning** helps discover hidden patterns, relationships, or groups from such unlabeled data.

> ⭐ **Exam Point:** Unsupervised Learning works on **unlabeled data**.

---

# 2. Definition

### Simple Definition

Unsupervised Learning is a machine learning technique in which the algorithm learns patterns from data **without knowing the correct output**.

### Technical Definition

> **Unsupervised Learning** is a machine learning approach in which the model analyzes **unlabeled data** to identify hidden structures, clusters, or relationships without predefined target labels.

---

# 3. Characteristics

* Uses **unlabeled data**
* No target/output variable
* Finds hidden patterns
* Discovers groups (clusters)
* Can reduce data dimensions
* Learns without human supervision

---

# 4. Working of Unsupervised Learning

### Steps

1. Collect unlabeled data.
2. Preprocess the data (cleaning, scaling).
3. Select an unsupervised algorithm.
4. Find hidden patterns or clusters.
5. Analyze the discovered groups.

---

### Flow Diagram

```text
          Unlabeled Dataset
                  │
                  ▼
          Data Preprocessing
                  │
                  ▼
      Apply ML Algorithm
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
   Clustering        Dimensionality
                        Reduction
        │                   │
        └─────────┬─────────┘
                  ▼
          Hidden Patterns
```

---

# 5. Types of Unsupervised Learning

## A. Clustering

Groups similar data points together.

### Popular Algorithms

* K-Means
* Hierarchical Clustering
* DBSCAN

### Example

Customer Segmentation

```text
Customers

↓

Group A → Students

Group B → Professionals

Group C → Senior Citizens
```

---

## B. Association Rule Learning

Finds relationships between items.

### Example

Customers buying

```text
Bread

↓

Butter

↓

Jam
```

This information helps supermarkets recommend products.

Example Algorithms

* Apriori
* FP-Growth

---

## C. Dimensionality Reduction

Reduces the number of features while preserving important information.

Example Algorithm

* Principal Component Analysis (PCA)

Applications

* Data Visualization
* Faster Training
* Noise Removal

---

# 6. Supervised vs Unsupervised Learning

| Feature         | Supervised              | Unsupervised                          |
| --------------- | ----------------------- | ------------------------------------- |
| Data            | Labeled                 | Unlabeled                             |
| Target Variable | Present                 | Absent                                |
| Goal            | Prediction              | Pattern Discovery                     |
| Output          | Class/Value             | Clusters/Relationships                |
| Examples        | KNN, SVM, Decision Tree | K-Means, PCA, Hierarchical Clustering |

---

# 7. Advantages

* Works without labeled data.
* Finds hidden patterns.
* Useful for exploratory data analysis.
* Helps in customer segmentation.
* Reduces data complexity.

---

# 8. Disadvantages

* Difficult to evaluate accuracy.
* Results may be difficult to interpret.
* Sensitive to algorithm selection.
* May identify meaningless patterns.

---

# 9. Applications

* Customer Segmentation
* Recommendation Systems
* Market Basket Analysis
* Fraud Detection
* Image Compression
* Social Network Analysis
* Anomaly Detection
* Document Clustering

---

# 10. Python Example

```python
from sklearn.cluster import KMeans

model = KMeans(
    n_clusters=3,
    random_state=42
)

model.fit(X)
```

---

# 11. Real-Life Example

Suppose an online shopping company has data about customers but does not know their categories.

The algorithm automatically creates groups based on shopping behavior.

```text
Customer Data

↓

Machine Learning

↓

Cluster 1 → Students

Cluster 2 → Professionals

Cluster 3 → Premium Customers
```

The company can now provide personalized offers to each group.

---

# 12. Comparison of Unsupervised Learning Techniques

| Technique                | Purpose            | Example Algorithm |
| ------------------------ | ------------------ | ----------------- |
| Clustering               | Group similar data | K-Means           |
| Association              | Find relationships | Apriori           |
| Dimensionality Reduction | Reduce features    | PCA               |

---

# 13. Viva Questions

1. What is Unsupervised Learning?
2. What type of data does it use?
3. What is clustering?
4. Give two clustering algorithms.
5. What is PCA?
6. What is Association Rule Learning?
7. Give applications of Unsupervised Learning.
8. Difference between supervised and unsupervised learning?
9. What is customer segmentation?
10. Name two dimensionality reduction techniques.

---

# 14. University Questions

### 2 Marks

* Define Unsupervised Learning.
* What is clustering?
* What is PCA?
* Name two clustering algorithms.

### 5 Marks

* Explain the working of Unsupervised Learning.
* Explain different types of Unsupervised Learning.
* Compare Supervised and Unsupervised Learning.

### 10 Marks

* Explain Unsupervised Learning with a neat diagram.
* Discuss clustering, association rule learning, and dimensionality reduction.
* Compare Supervised and Unsupervised Learning with examples.

---

# 15. Quick Revision

### Key Points

* **Data:** Unlabeled
* **Goal:** Discover hidden patterns
* **Main Tasks:**

  * Clustering
  * Association Rule Learning
  * Dimensionality Reduction
* **Popular Algorithms:**

  * K-Means
  * Hierarchical Clustering
  * PCA
  * Apriori

---

### Memory Trick

Remember **"CAD"**

* **C** → Clustering
* **A** → Association Rules
* **D** → Dimensionality Reduction

This helps recall the three main categories of Unsupervised Learning in exams.

---


