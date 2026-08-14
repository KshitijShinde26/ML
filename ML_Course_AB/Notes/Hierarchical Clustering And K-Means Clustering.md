

---

# K-Means Clustering

> **Unit:** Unsupervised Learning

---

# Table of Contents

1. Introduction
2. Definition
3. Terminology
4. Working of K-Means
5. Choosing K
6. Advantages & Disadvantages
7. Applications
8. Python Implementation
9. Complexity Analysis
10. Comparison with KNN
11. Viva Questions
12. University Questions
13. Quick Revision

---

# 1. Introduction

**K-Means Clustering** is one of the most popular **unsupervised learning** algorithms used to divide data into **K clusters** based on similarity.

Each cluster contains data points that are similar to each other and different from those in other clusters.

> ⭐ **Exam Point:** K-Means groups **unlabeled data** into **K clusters**.

---

# 2. Definition

### Simple Definition

K-Means divides a dataset into **K groups** by assigning each data point to the nearest cluster center.

### Technical Definition

> **K-Means** is an iterative unsupervised learning algorithm that partitions a dataset into **K clusters**, where each data point belongs to the cluster with the nearest **centroid**.

---

# 3. Terminology

| Term      | Meaning                      |
| --------- | ---------------------------- |
| Cluster   | Group of similar data points |
| K         | Number of clusters           |
| Centroid  | Center point of a cluster    |
| Iteration | One complete update cycle    |

---

# 4. Working of K-Means

### Algorithm

1. Choose the value of **K**.
2. Select **K random centroids**.
3. Calculate the distance of every data point from each centroid.
4. Assign each point to the nearest centroid.
5. Calculate new centroids.
6. Repeat Steps 3–5 until centroids no longer change.

---

### Flow Diagram

```text
          Dataset
             │
             ▼
      Choose K Value
             │
             ▼
   Initialize Centroids
             │
             ▼
 Assign Points to Clusters
             │
             ▼
 Recalculate Centroids
             │
             ▼
 Converged?
      │
  No──┘
      │
     Yes
      ▼
 Final Clusters
```

---

# Example

Suppose there are **30 students**.

Choose

```text
K = 3
```

Output

```text
Cluster 1 → High Performers

Cluster 2 → Average Students

Cluster 3 → Beginners
```

---

# 5. Choosing K

Choosing the correct value of **K** is important.

### Elbow Method

The Elbow Method helps find the optimal number of clusters.

* Plot **K** vs **WCSS (Within-Cluster Sum of Squares)**.
* Select the point where the graph bends like an elbow.

> ⭐ **Exam Point:** The Elbow Method is the most common technique for selecting **K**.

---

# 6. Advantages

* Simple and easy to implement.
* Fast for medium-sized datasets.
* Works well with numerical data.
* Scalable.

---

# 7. Disadvantages

* Need to specify K in advance.
* Sensitive to initial centroid selection.
* Poor performance with irregular clusters.
* Sensitive to outliers.

---

# 8. Applications

* Customer Segmentation
* Image Compression
* Market Analysis
* Document Clustering
* Recommendation Systems

---

# 9. Python Implementation

```python
from sklearn.cluster import KMeans

model = KMeans(
    n_clusters=3,
    random_state=42
)

model.fit(X)

labels = model.labels_
```

---

# 10. Complexity

| Operation | Complexity       |
| --------- | ---------------- |
| Training  | O(n × k × i × d) |

Where

* **n** = Samples
* **k** = Clusters
* **i** = Iterations
* **d** = Features

---

# 11. K-Means vs KNN

| K-Means                | KNN                       |
| ---------------------- | ------------------------- |
| Unsupervised           | Supervised                |
| Clustering             | Classification/Regression |
| Uses unlabeled data    | Uses labeled data         |
| K = Number of Clusters | K = Number of Neighbors   |

---

# 12. Viva Questions

* What is K-Means?
* What is a centroid?
* What is the Elbow Method?
* Why is K-Means unsupervised?
* What is the role of K?

---

# 13. University Questions

### 2 Marks

* Define K-Means.
* What is a centroid?
* What is clustering?

### 5 Marks

* Explain the K-Means algorithm.
* Explain the Elbow Method.

### 10 Marks

* Explain K-Means with a neat diagram, algorithm, and applications.

---

# Quick Revision

* Unsupervised Learning
* Groups similar data
* Uses Centroids
* Elbow Method selects K
* Sensitive to Outliers

---

# Hierarchical Clustering

> **Unit:** Unsupervised Learning

---

# Table of Contents

1. Introduction
2. Definition
3. Types
4. Working
5. Dendrogram
6. Linkage Methods
7. Advantages & Disadvantages
8. Applications
9. Python Implementation
10. Comparison with K-Means
11. Viva Questions
12. University Questions
13. Quick Revision

---

# 1. Introduction

**Hierarchical Clustering** creates a hierarchy of clusters represented as a **tree-like structure (Dendrogram)**.

Unlike K-Means, the number of clusters does **not** need to be specified at the beginning.

---

# 2. Definition

### Simple Definition

Hierarchical Clustering groups similar data points into a hierarchy of clusters.

### Technical Definition

> **Hierarchical Clustering** is an unsupervised learning algorithm that builds a hierarchy of clusters by repeatedly merging or splitting data points based on similarity.

---

# 3. Types

## A. Agglomerative (Bottom-Up)

Each data point starts as its own cluster.

Clusters are merged until one large cluster remains.

```text
A   B   C   D

↓

AB

↓

ABC

↓

ABCD
```

> ⭐ **Most commonly used**.

---

## B. Divisive (Top-Down)

Start with one large cluster.

Split it repeatedly.

```text
ABCD

↓

AB   CD

↓

A B C D
```

---

# 4. Working (Agglomerative)

1. Treat every data point as a separate cluster.
2. Calculate distances between clusters.
3. Merge the closest clusters.
4. Repeat until only one cluster remains.
5. Cut the dendrogram at the desired level to obtain clusters.

---

# 5. Dendrogram

A **Dendrogram** is a tree diagram showing how clusters are merged.

```text
          ───────
         /       \
     ────         ────
    /   \         /   \
   A     B       C     D
```

> ⭐ **Exam Point:** A dendrogram helps determine the number of clusters.

---

# 6. Linkage Methods

| Method           | Description                             |
| ---------------- | --------------------------------------- |
| Single Linkage   | Minimum distance                        |
| Complete Linkage | Maximum distance                        |
| Average Linkage  | Average distance                        |
| Ward Linkage     | Minimizes variance (most commonly used) |

---

# 7. Advantages

* Number of clusters not required initially.
* Produces a dendrogram.
* Works well with small datasets.
* Easy to visualize.

---

# 8. Disadvantages

* Slow for large datasets.
* High memory usage.
* Difficult to modify once clusters are formed.

---

# 9. Applications

* Gene Analysis
* Customer Segmentation
* Social Network Analysis
* Document Clustering
* Image Processing

---

# 10. Python Implementation

```python
from sklearn.cluster import AgglomerativeClustering

model = AgglomerativeClustering(
    n_clusters=3
)

labels = model.fit_predict(X)
```

---

# 11. Comparison with K-Means

| K-Means          | Hierarchical             |
| ---------------- | ------------------------ |
| Centroid-based   | Tree-based               |
| Need K initially | K not required initially |
| Fast             | Slower                   |
| Large datasets   | Small datasets           |
| No Dendrogram    | Uses Dendrogram          |

---

# 12. Viva Questions

* What is Hierarchical Clustering?
* What is a Dendrogram?
* Difference between Agglomerative and Divisive?
* What is Ward Linkage?
* Why doesn't Hierarchical Clustering require K initially?

---

# 13. University Questions

### 2 Marks

* Define Hierarchical Clustering.
* What is a Dendrogram?
* What is Agglomerative Clustering?

### 5 Marks

* Explain Agglomerative Clustering.
* Explain different linkage methods.

### 10 Marks

* Explain Hierarchical Clustering with a neat diagram.
* Compare Hierarchical Clustering and K-Means.

---

# Quick Revision

### Key Points

* Unsupervised Learning
* Tree-based clustering
* Dendrogram visualization
* Agglomerative (Bottom-Up)
* Divisive (Top-Down)
* Ward Linkage is commonly used

### Memory Trick

Remember **"A-D-W-D"**

* **A** → Agglomerative
* **D** → Divisive
* **W** → Ward Linkage
* **D** → Dendrogram

---

