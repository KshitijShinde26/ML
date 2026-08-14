

---

# Principal Component Analysis (PCA)

> **Unit:** Unsupervised Learning (Dimensionality Reduction)

---

# Table of Contents

1. Introduction
2. Definition
3. Need for PCA
4. Terminology
5. Working of PCA
6. Mathematical Concept
7. Advantages & Disadvantages
8. Applications
9. Python Implementation
10. Complexity Analysis
11. Comparison with Feature Selection
12. Viva Questions
13. University Questions
14. Quick Revision

---

# 1. Introduction

Modern datasets often contain **many features (dimensions)**. Some features may be redundant or highly correlated, increasing computation time and model complexity.

**Principal Component Analysis (PCA)** reduces the number of features while preserving as much information as possible.

> ⭐ **Exam Point:** PCA is mainly used for **Dimensionality Reduction**.

---

# 2. Definition

### Simple Definition

PCA converts many correlated features into a smaller number of new features called **Principal Components**.

### Technical Definition

> **Principal Component Analysis (PCA)** is an unsupervised dimensionality reduction technique that transforms correlated variables into a smaller set of uncorrelated variables called principal components while preserving maximum variance.

---

# 3. Need for PCA

Without PCA:

* High computation time
* More memory usage
* Redundant features
* Risk of overfitting
* Difficult visualization

With PCA:

* Faster training
* Less storage
* Better visualization
* Reduced noise
* Improved efficiency

---

# 4. Terminology

| Term                | Meaning                       |
| ------------------- | ----------------------------- |
| Dimension           | Feature/Attribute             |
| Variance            | Spread of data                |
| Principal Component | New transformed feature       |
| Eigenvector         | Direction of maximum variance |
| Eigenvalue          | Amount of variance captured   |

---

# 5. Working of PCA

### Steps

1. Collect data.
2. Standardize the data.
3. Compute the covariance matrix.
4. Calculate eigenvalues and eigenvectors.
5. Sort principal components by eigenvalues.
6. Select top principal components.
7. Transform the original data.

---

### Flow Diagram

```text
Original Dataset
       │
       ▼
 Standardization
       │
       ▼
Covariance Matrix
       │
       ▼
Eigenvalues &
Eigenvectors
       │
       ▼
Select Top Components
       │
       ▼
Reduced Dataset
```

---

# 6. Mathematical Concept

### Covariance Matrix

Shows how features vary together.

### Eigenvectors

Represent the **direction** of maximum variance.

### Eigenvalues

Represent the **amount of variance** explained.

> ⭐ Higher Eigenvalue → More important Principal Component.

---

### Example

Suppose a dataset has **10 features**.

After PCA,

```text
10 Features

↓

PCA

↓

3 Principal Components
```

Now the model works with **3 features instead of 10**.

---

# 7. Advantages

* Reduces dimensions.
* Removes redundant information.
* Faster model training.
* Helps visualization.
* Reduces overfitting.

---

# 8. Disadvantages

* Reduced interpretability.
* Possible information loss.
* Difficult mathematical concepts.
* Assumes linear relationships.

---

# 9. Applications

* Face Recognition
* Image Compression
* Medical Data Analysis
* Financial Data Analysis
* Gene Expression Analysis
* Data Visualization

---

# 10. Python Implementation

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_new = pca.fit_transform(X)
```

---

# 11. Complexity

| Operation            | Complexity            |
| -------------------- | --------------------- |
| Training             | O(n × d²) *(approx.)* |
| Prediction/Transform | O(n × d × k)          |

Where:

* **n** = Samples
* **d** = Features
* **k** = Principal Components

---

# 12. PCA vs Feature Selection

| PCA                         | Feature Selection                 |
| --------------------------- | --------------------------------- |
| Creates new features        | Keeps original features           |
| Feature transformation      | Feature removal                   |
| Unsupervised                | Can be supervised or unsupervised |
| May reduce interpretability | Easier to interpret               |

---

# 13. Viva Questions

* What is PCA?
* Why is PCA used?
* What is dimensionality reduction?
* What are Principal Components?
* What are Eigenvalues and Eigenvectors?
* Why is data standardized before PCA?

---

# 14. University Questions

### 2 Marks

* Define PCA.
* What is dimensionality reduction?
* What is a Principal Component?

### 5 Marks

* Explain the working of PCA.
* Explain Eigenvalues and Eigenvectors.

### 10 Marks

* Explain PCA with a neat diagram.
* Compare PCA and Feature Selection.

---

# Quick Revision

### Key Points

* Unsupervised Learning
* Dimensionality Reduction
* Principal Components
* Covariance Matrix
* Eigenvalues
* Eigenvectors

### Memory Trick

Remember **"SCEPT"**

* **S** → Standardize
* **C** → Covariance Matrix
* **E** → Eigenvalues
* **P** → Principal Components
* **T** → Transform Data

---

# Association Rule Learning (Apriori Algorithm)

> **Unit:** Unsupervised Learning

---

# Table of Contents

1. Introduction
2. Definition
3. Key Terminology
4. Working of Apriori
5. Support, Confidence & Lift
6. Advantages & Disadvantages
7. Applications
8. Python Implementation
9. Comparison with Clustering
10. Viva Questions
11. University Questions
12. Quick Revision

---

# 1. Introduction

**Association Rule Learning** discovers relationships between items in large datasets.

The **Apriori Algorithm** is the most widely used algorithm for market basket analysis.

Example:

A supermarket may find that customers who buy **Bread** also often buy **Butter**.

---

# 2. Definition

### Simple Definition

Apriori finds frequently occurring item combinations in a dataset.

### Technical Definition

> **Apriori** is an unsupervised learning algorithm that identifies frequent itemsets and generates association rules using Support, Confidence, and Lift.

---

# 3. Key Terminology

| Term             | Meaning                      |
| ---------------- | ---------------------------- |
| Itemset          | Collection of items          |
| Frequent Itemset | Itemset appearing frequently |
| Rule             | Relationship between items   |
| Support          | Frequency of an itemset      |
| Confidence       | Reliability of a rule        |
| Lift             | Strength of association      |

---

# 4. Working of Apriori

### Steps

1. Scan the dataset.
2. Find frequent single items.
3. Generate larger itemsets.
4. Remove infrequent itemsets.
5. Generate association rules.

---

### Flow Diagram

```text
Transaction Dataset
        │
        ▼
Find Frequent Itemsets
        │
        ▼
Generate Candidate Itemsets
        │
        ▼
Prune Infrequent Itemsets
        │
        ▼
Generate Association Rules
```

---

# 5. Support, Confidence & Lift

### Support

Frequency of an itemset in the dataset.

[
Support(A)=\frac{\text{Transactions containing A}}{\text{Total Transactions}}
]

---

### Confidence

Probability that item **B** is purchased when **A** is purchased.

[
Confidence(A\rightarrow B)=
\frac{Support(A\cap B)}{Support(A)}
]

---

### Lift

Measures the strength of the association.

[
Lift(A\rightarrow B)=
\frac{Confidence(A\rightarrow B)}
{Support(B)}
]

### Interpretation

| Lift Value | Meaning              |
| ---------- | -------------------- |
| = 1        | No relationship      |
| > 1        | Positive association |
| < 1        | Negative association |

---

# Example

| Customer | Items Purchased     |
| -------- | ------------------- |
| 1        | Bread, Butter       |
| 2        | Bread, Milk         |
| 3        | Bread, Butter, Milk |
| 4        | Butter, Milk        |

Possible rule:

```text
Bread → Butter
```

Meaning: Customers buying bread are likely to buy butter.

---

# 6. Advantages

* Finds hidden buying patterns.
* Easy to understand.
* Useful in recommendation systems.
* Helps increase sales.

---

# 7. Disadvantages

* Slow for very large datasets.
* Generates many candidate itemsets.
* High memory usage.
* Performance decreases with many items.

---

# 8. Applications

* Market Basket Analysis
* Product Recommendation
* Online Shopping
* Medical Diagnosis
* Fraud Detection
* Website Clickstream Analysis

---

# 9. Python Implementation

```python
from mlxtend.frequent_patterns import apriori

frequent_itemsets = apriori(
    df,
    min_support=0.2,
    use_colnames=True
)
```

---

# 10. Apriori vs Clustering

| Apriori                   | Clustering               |
| ------------------------- | ------------------------ |
| Finds relationships       | Finds groups             |
| Market Basket Analysis    | Customer Segmentation    |
| Uses Support & Confidence | Uses Similarity Measures |
| Association Rules         | Clusters                 |

---

# 11. Viva Questions

* What is Apriori?
* What is Association Rule Learning?
* Define Support.
* Define Confidence.
* What is Lift?
* Give applications of Apriori.

---

# 12. University Questions

### 2 Marks

* Define Apriori Algorithm.
* What is Support?
* What is Confidence?

### 5 Marks

* Explain the working of Apriori.
* Explain Support, Confidence, and Lift.

### 10 Marks

* Explain the Apriori Algorithm with a neat diagram.
* Discuss market basket analysis using Apriori.

---

# Quick Revision

### Key Points

* Unsupervised Learning
* Association Rule Learning
* Frequent Itemsets
* Support
* Confidence
* Lift
* Market Basket Analysis

### Memory Trick

Remember **"SCL"**

* **S** → Support
* **C** → Confidence
* **L** → Lift

---

