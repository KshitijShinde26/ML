

# Hyperparameter Optimization

> **Unit:** Supervised Machine Learning

---

# Table of Contents

1. Introduction
2. What are Parameters and Hyperparameters?
3. Need for Hyperparameter Optimization
4. Common Hyperparameters
5. Hyperparameter Optimization Techniques
6. Grid Search
7. Random Search
8. Bayesian Optimization (Overview)
9. Advantages & Disadvantages
10. Python Implementation
11. Comparison of Techniques
12. Viva Questions
13. University Questions
14. Quick Revision

---

# 1. Introduction

Machine Learning models have settings that control how they learn. These settings are called **Hyperparameters**.

Choosing the right hyperparameters improves the model's accuracy and reduces overfitting or underfitting.

> ⭐ **Exam Point:** Hyperparameters are set **before** training starts.

---

# 2. Parameters vs Hyperparameters

| Parameters                          | Hyperparameters                  |
| ----------------------------------- | -------------------------------- |
| Learned during training             | Set before training              |
| Model updates them automatically    | User chooses them                |
| Example: Weights in Neural Networks | Example: Learning Rate, K in KNN |

### Examples

| Algorithm      | Hyperparameter                    |
| -------------- | --------------------------------- |
| KNN            | K (number of neighbors)           |
| Decision Tree  | Maximum depth                     |
| Random Forest  | Number of trees                   |
| SVM            | Kernel type                       |
| Neural Network | Learning rate, Epochs, Batch size |

---

# 3. Need for Hyperparameter Optimization

Selecting inappropriate hyperparameters can lead to poor performance.

### If Hyperparameters are Poorly Chosen

* Low Accuracy
* Overfitting
* Underfitting
* Longer Training Time
* Poor Generalization

### Goal

Find the combination of hyperparameters that gives the **best model performance**.

---

# 4. Common Hyperparameters

| Hyperparameter        | Purpose                       |
| --------------------- | ----------------------------- |
| Learning Rate         | Controls learning speed       |
| K                     | Number of neighbors in KNN    |
| Epochs                | Number of training iterations |
| Batch Size            | Samples processed at once     |
| Max Depth             | Maximum tree depth            |
| Number of Trees       | Used in Random Forest         |
| Regularization (C, λ) | Controls overfitting          |

---

# 5. Hyperparameter Optimization Techniques

The three most common techniques are:

1. Grid Search
2. Random Search
3. Bayesian Optimization

---

# 6. Grid Search

## Definition

Grid Search tries **every possible combination** of hyperparameter values.

### Example

Suppose

```text
K = {3,5,7}

Weight = {uniform,distance}
```

Grid Search checks:

| K | Weight   |
| - | -------- |
| 3 | uniform  |
| 3 | distance |
| 5 | uniform  |
| 5 | distance |
| 7 | uniform  |
| 7 | distance |

It evaluates all combinations and selects the best one.

### Advantages

* Easy to understand
* Finds the best combination within the search space
* Good for small datasets

### Disadvantages

* Slow
* Computationally expensive
* Doesn't scale well

---

# 7. Random Search

## Definition

Random Search selects **random combinations** instead of testing every combination.

### Example

Possible combinations = 100

Random Search may evaluate only 20 random combinations.

### Advantages

* Faster than Grid Search
* Efficient for large search spaces
* Often achieves similar performance

### Disadvantages

* May miss the optimal combination
* Results vary between runs

---

# 8. Bayesian Optimization (Overview)

## Definition

Bayesian Optimization uses the results of previous trials to intelligently choose the next hyperparameter values.

Instead of random guessing, it learns which regions of the search space are more promising.

### Advantages

* Very efficient
* Requires fewer evaluations
* Best for expensive models

### Disadvantages

* More complex
* Harder to implement

> ⭐ For most university exams, knowing the concept is sufficient; detailed mathematics is usually not required.

---

# 9. Comparison of Optimization Techniques

| Feature            | Grid Search        | Random Search       | Bayesian Optimization |
| ------------------ | ------------------ | ------------------- | --------------------- |
| Search Method      | All combinations   | Random combinations | Intelligent search    |
| Speed              | Slow               | Fast                | Moderate              |
| Accuracy           | High (within grid) | Good                | Very High             |
| Computational Cost | High               | Medium              | Low–Medium            |
| Best For           | Small datasets     | Large search spaces | Complex models        |

---

# 10. Python Implementation

### Grid Search

```python
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

parameters = {
    'n_neighbors': [3,5,7,9]
}

grid = GridSearchCV(
    KNeighborsClassifier(),
    parameters,
    cv=5
)

grid.fit(X_train, y_train)

print(grid.best_params_)
```

---

### Random Search

```python
from sklearn.model_selection import RandomizedSearchCV

random = RandomizedSearchCV(
    KNeighborsClassifier(),
    parameters,
    n_iter=3,
    cv=5
)

random.fit(X_train, y_train)

print(random.best_params_)
```

---

# 11. Advantages & Disadvantages

## Advantages

* Improves model accuracy
* Helps reduce overfitting
* Finds better-performing models
* Automates parameter tuning

## Disadvantages

* Time-consuming
* Computationally expensive
* Requires validation data
* Bayesian Optimization is more difficult to implement

---

# 12. Applications

* Machine Learning Model Tuning
* Deep Learning
* Recommendation Systems
* Image Classification
* Medical Diagnosis
* Fraud Detection
* Financial Prediction

---

# 13. Viva Questions

1. What is a hyperparameter?
2. What is the difference between a parameter and a hyperparameter?
3. Why is hyperparameter optimization required?
4. What is Grid Search?
5. What is Random Search?
6. Which technique is faster: Grid Search or Random Search?
7. What is Bayesian Optimization?
8. Give two examples of hyperparameters.
9. Is K in KNN a parameter or a hyperparameter?
10. Why is Cross Validation often used with Grid Search?

---

# 14. University Questions

### 2 Marks

* Define Hyperparameter.
* What is Grid Search?
* What is Random Search?

### 5 Marks

* Explain Hyperparameter Optimization.
* Compare Grid Search and Random Search.
* Explain common hyperparameters used in ML.

### 10 Marks

* Explain Hyperparameter Optimization techniques with suitable examples.
* Compare Grid Search, Random Search, and Bayesian Optimization.

---

# 15. Quick Revision

### Hyperparameter Optimization

* Hyperparameters are set **before training**.
* Goal: Find the best values to improve model performance.

### Techniques

* **Grid Search** → Tests every combination.
* **Random Search** → Tests random combinations.
* **Bayesian Optimization** → Uses previous results to guide future searches.

### Examples of Hyperparameters

* K (KNN)
* Learning Rate
* Max Depth
* Number of Trees
* Epochs
* Batch Size

### Memory Trick

**"GRB"**

* **G** → Grid Search (checks **G**rid of all values)
* **R** → Random Search (chooses **R**andom values)
* **B** → Bayesian Optimization (**B**uilds on previous results)

---


