
---

# Recommender System

> **Unit:** Machine Learning Applications

---

# Table of Contents

1. Introduction
2. Definition
3. Need
4. Types
5. Working
6. Advantages & Disadvantages
7. Applications
8. Python Example
9. Comparison
10. Viva Questions
11. University Questions
12. Quick Revision

---

# 1. Introduction

A **Recommender System** suggests products, movies, songs, books, or other items to users based on their interests or behavior.

Examples:

* Netflix recommends movies.
* Amazon recommends products.
* Spotify recommends songs.
* YouTube recommends videos.

> ⭐ **Exam Point:** Recommender Systems improve user experience by providing personalized suggestions.

---

# 2. Definition

### Simple Definition

A Recommender System predicts what a user is likely to like.

### Technical Definition

> A **Recommender System** is an intelligent system that analyzes user preferences and item information to recommend relevant items.

---

# 3. Need for Recommender Systems

Without recommendations:

* Too many choices
* Difficult to find relevant items
* Poor user experience

With recommendations:

* Personalized suggestions
* Increased sales
* Better customer satisfaction
* Higher user engagement

---

# 4. Types of Recommender Systems

## A. Content-Based Filtering

Recommends items similar to those the user already likes.

### Example

```text
User Likes:
Action Movies

↓

Recommended

Mission Impossible
John Wick
Mad Max
```

---

## B. Collaborative Filtering

Recommends items liked by users with similar interests.

### Example

```text
User A → Movie X, Y

User B → Movie X

↓

Recommend Movie Y to User B
```

---

## C. Hybrid Recommendation

Combines **Content-Based** and **Collaborative Filtering**.

Examples:

* Netflix
* Amazon
* YouTube

---

# 5. Working

```text
User Data
     │
     ▼
Collect Preferences
     │
     ▼
Analyze Similarities
     │
     ▼
Generate Recommendations
     │
     ▼
Display Suggestions
```

---

# 6. Advantages

* Personalized recommendations
* Improves user satisfaction
* Increases revenue
* Saves users' time

---

# 7. Disadvantages

* Cold Start Problem (new users/items)
* Requires large datasets
* Privacy concerns
* Computationally expensive

---

# 8. Applications

* Netflix
* Amazon
* Flipkart
* Spotify
* YouTube
* Instagram
* Facebook

---

# 9. Simple Python Example

```python
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(user_item_matrix)
```

---

# 10. Content-Based vs Collaborative Filtering

| Content-Based              | Collaborative                  |
| -------------------------- | ------------------------------ |
| Uses item features         | Uses user behavior             |
| Doesn't require many users | Needs user interaction history |
| Good for new items         | Better personalization         |

---

# 11. Viva Questions

* What is a Recommender System?
* Name its types.
* What is Collaborative Filtering?
* What is Content-Based Filtering?
* What is the Cold Start Problem?

---

# 12. University Questions

### 2 Marks

* Define Recommender System.
* What is Collaborative Filtering?

### 5 Marks

* Explain different types of recommender systems.

### 10 Marks

* Explain the working of a recommender system with a diagram.

---

# Quick Revision

Remember **"CCH"**

* **C** → Content-Based
* **C** → Collaborative
* **H** → Hybrid

---

# Introduction to Deep Learning

> **Unit:** Deep Learning Basics

---

# Table of Contents

1. Introduction
2. AI vs ML vs DL
3. Definition
4. History
5. Turing Test
6. Learning Representations
7. Workflow of ML
8. ML Methods
9. Advantages & Disadvantages
10. Applications
11. Viva Questions
12. University Questions
13. Quick Revision

---

# 1. Introduction

**Deep Learning (DL)** is a subset of Machine Learning that uses **Artificial Neural Networks (ANNs)** with multiple hidden layers to learn complex patterns from data.

It is especially useful for:

* Image Recognition
* Speech Recognition
* Natural Language Processing (NLP)
* Autonomous Vehicles

> ⭐ **Exam Point:** Deep Learning is a **subset of Machine Learning**, which itself is a subset of **Artificial Intelligence**.

---

# 2. AI vs ML vs DL

```text
Artificial Intelligence (AI)
        │
        ▼
Machine Learning (ML)
        │
        ▼
Deep Learning (DL)
```

| AI                    | ML               | DL                                |
| --------------------- | ---------------- | --------------------------------- |
| Broad field           | Subset of AI     | Subset of ML                      |
| Rule-based & learning | Learns from data | Learns using deep neural networks |

---

# 3. Definition

### Simple Definition

Deep Learning uses neural networks with many hidden layers to learn automatically from data.

### Technical Definition

> **Deep Learning** is a branch of Machine Learning that trains multi-layer Artificial Neural Networks to learn hierarchical representations from large datasets.

---

# 4. Brief History

| Year    | Milestone                                        |
| ------- | ------------------------------------------------ |
| 1950    | Turing Test proposed                             |
| 1958    | Perceptron introduced                            |
| 1986    | Backpropagation popularized                      |
| 2012    | AlexNet revolutionized deep learning             |
| Present | ChatGPT, Gemini, autonomous vehicles, medical AI |

---

# 5. Turing Test

Proposed by **Alan Turing** in **1950**.

### Purpose

To determine whether a machine can exhibit intelligent behavior similar to a human.

### Simple Diagram

```text
 Human Judge
     │
 ┌───┴────┐
 │        │
Human   Computer
```

If the judge cannot reliably distinguish the computer from the human, the machine is said to have passed the Turing Test.

---

# 6. Learning Representations

Deep Learning automatically learns useful features from raw data.

Example:

```text
Image

↓

Edges

↓

Shapes

↓

Objects

↓

Prediction
```

Unlike traditional ML, manual feature engineering is often unnecessary.

---

# 7. Machine Learning Workflow

```text
Collect Data
      │
      ▼
Preprocess Data
      │
      ▼
Choose Algorithm
      │
      ▼
Train Model
      │
      ▼
Test Model
      │
      ▼
Evaluate Results
      │
      ▼
Deploy Model
```

---

# 8. Machine Learning Methods

| Method                 | Example                |
| ---------------------- | ---------------------- |
| Supervised Learning    | Decision Tree, SVM     |
| Unsupervised Learning  | K-Means, PCA           |
| Reinforcement Learning | Game Playing, Robotics |

---

# 9. Advantages

* Learns complex patterns
* High accuracy on large datasets
* Automatic feature extraction
* Excellent for images, speech, and text

---

# 10. Disadvantages

* Requires large amounts of data
* High computational cost
* Longer training time
* Less interpretable than simpler ML models

---

# 11. Applications

* Self-driving Cars
* Face Recognition
* Voice Assistants
* Medical Imaging
* Fraud Detection
* Machine Translation
* Chatbots

---

# 12. Viva Questions

* What is Deep Learning?
* Difference between AI, ML, and DL?
* Who proposed the Turing Test?
* What is representation learning?
* Why is Deep Learning powerful?

---

# 13. University Questions

### 2 Marks

* Define Deep Learning.
* What is the Turing Test?
* Differentiate AI and ML.

### 5 Marks

* Explain the ML workflow.
* Explain AI, ML, and DL.

### 10 Marks

* Explain Deep Learning with suitable examples.
* Explain the Turing Test and the evolution of Deep Learning.

---

# Quick Revision

### Key Points

* Deep Learning ⊂ Machine Learning ⊂ Artificial Intelligence
* Uses multi-layer neural networks
* Automatic feature learning
* Works best with large datasets
* Popular in computer vision, NLP, and speech processing

### Memory Trick

Remember **"DART"**

* **D** → Deep Neural Networks
* **A** → Artificial Intelligence
* **R** → Representation Learning
* **T** → Turing Test

---


