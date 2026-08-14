
---

# Artificial Neural Network (ANN)

> **Unit:** Deep Learning

---

# Table of Contents

1. Introduction
2. Definition
3. Biological Neuron vs Artificial Neuron
4. Structure of ANN
5. Working of ANN
6. Activation Functions
7. Types of ANN
8. Advantages & Disadvantages
9. Applications
10. Python Implementation
11. Comparison with Traditional ML
12. Viva Questions
13. University Questions
14. Quick Revision

---

# 1. Introduction

An **Artificial Neural Network (ANN)** is a machine learning model inspired by the **human brain**. It consists of interconnected nodes called **neurons**, which process information and learn patterns from data.

ANNs are the foundation of **Deep Learning**.

> ⭐ **Exam Point:** ANN mimics the working of biological neurons.

---

# 2. Definition

### Simple Definition

An ANN is a network of artificial neurons that learns from examples to make predictions.

### Technical Definition

> An **Artificial Neural Network (ANN)** is a computational model consisting of interconnected neurons organized into layers that learn complex relationships from data by adjusting weights and biases.

---

# 3. Biological Neuron vs Artificial Neuron

| Biological Neuron           | Artificial Neuron                    |
| --------------------------- | ------------------------------------ |
| Dendrites receive signals   | Inputs receive data                  |
| Cell Body processes signals | Summation computes weighted input    |
| Axon sends output           | Activation Function generates output |
| Synapse connects neurons    | Weights connect neurons              |

---

# 4. Structure of ANN

ANN consists of three main layers:

### A. Input Layer

Receives input features.

### B. Hidden Layer(s)

Processes the data.

### C. Output Layer

Produces the final prediction.

---

## Structure Diagram

```text
          Input Layer

      x1      x2      x3
       ●-------●-------●
        \      |      /
         \     |     /
          ▼    ▼    ▼

       Hidden Layer

        ●------●------●
          \     |     /
           \    |    /
            ▼   ▼   ▼

       Output Layer

             ●
```

---

# 5. Working of ANN

### Steps

1. Input data enters the network.
2. Each neuron multiplies inputs by weights.
3. Bias is added.
4. Activation function is applied.
5. Output is passed to the next layer.
6. Final prediction is generated.
7. Error is calculated.
8. Weights are updated using **Backpropagation**.

---

## Flow Diagram

```text
Input Data
      │
      ▼
Input Layer
      │
      ▼
Hidden Layer
      │
      ▼
Output Layer
      │
      ▼
Prediction
      │
      ▼
Error Calculation
      │
      ▼
Backpropagation
      │
      ▼
Updated Weights
```

---

# 6. Activation Functions

Activation functions decide whether a neuron should be activated.

## A. Sigmoid

Output range:

[
0 \text{ to } 1
]

Formula

[
\sigma(x)=\frac{1}{1+e^{-x}}
]

Used for binary classification.

---

## B. ReLU (Rectified Linear Unit)

Formula

[
f(x)=\max(0,x)
]

Advantages

* Faster training
* Most commonly used

---

## C. Tanh

Output range

[
-1 \text{ to } 1
]

Better than Sigmoid for many hidden-layer applications.

---

## Comparison

| Function | Output Range | Common Use            |
| -------- | ------------ | --------------------- |
| Sigmoid  | 0 to 1       | Binary Classification |
| Tanh     | -1 to 1      | Hidden Layers         |
| ReLU     | 0 to ∞       | Deep Neural Networks  |

---

# 7. Types of ANN

### Single Layer Perceptron

* One input layer
* One output layer
* No hidden layer

### Multi-Layer Perceptron (MLP)

* One or more hidden layers
* Most common ANN architecture

---

# 8. Advantages

* Learns complex patterns.
* Handles nonlinear problems.
* Automatic feature learning.
* High prediction accuracy.
* Can process large datasets.

---

# 9. Disadvantages

* Requires large datasets.
* Computationally expensive.
* Long training time.
* Difficult to interpret.

---

# 10. Applications

* Face Recognition
* Speech Recognition
* Medical Diagnosis
* Financial Prediction
* Fraud Detection
* Image Classification

---

# 11. Python Implementation

```python
from sklearn.neural_network import MLPClassifier

model = MLPClassifier(
    hidden_layer_sizes=(100,),
    max_iter=500,
    random_state=42
)

model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

---

# 12. ANN vs Traditional Machine Learning

| ANN                           | Traditional ML              |
| ----------------------------- | --------------------------- |
| Learns features automatically | Manual feature engineering  |
| Better for complex data       | Better for simpler problems |
| Needs more data               | Works with smaller datasets |
| Higher computation            | Lower computation           |

---

# 13. Viva Questions

* What is ANN?
* What are neurons?
* Explain hidden layers.
* What is Backpropagation?
* Why is ReLU popular?
* Difference between Sigmoid and ReLU?

---

# 14. University Questions

### 2 Marks

* Define ANN.
* What is an activation function?
* What is a hidden layer?

### 5 Marks

* Explain the architecture of ANN.
* Explain activation functions.

### 10 Marks

* Explain the working of ANN with a neat diagram.
* Compare ANN with traditional Machine Learning.

---

# Quick Revision

### Key Points

* Inspired by the human brain.
* Input → Hidden → Output layers.
* Uses weights and biases.
* Learns through Backpropagation.
* Common activation: **ReLU**.

### Memory Trick

Remember **"IHOAB"**

* **I** → Input Layer
* **H** → Hidden Layer
* **O** → Output Layer
* **A** → Activation Function
* **B** → Backpropagation

---

# Convolutional Neural Network (CNN)

> **Unit:** Deep Learning

---

# Table of Contents

1. Introduction
2. Definition
3. Why CNN?
4. Architecture of CNN
5. Working of CNN
6. Convolution Layer
7. Pooling Layer
8. Fully Connected Layer
9. Advantages & Disadvantages
10. Applications
11. Python Implementation
12. CNN vs ANN
13. Viva Questions
14. University Questions
15. Quick Revision

---

# 1. Introduction

A **Convolutional Neural Network (CNN)** is a specialized type of neural network designed for **image and video processing**.

Unlike a traditional ANN, CNN automatically extracts important image features such as edges, textures, and shapes.

> ⭐ **Exam Point:** CNN is mainly used for **Computer Vision** tasks.

---

# 2. Definition

### Simple Definition

CNN is a deep learning model used to recognize and classify images.

### Technical Definition

> A **Convolutional Neural Network (CNN)** is a deep neural network that uses convolution operations and pooling layers to automatically extract hierarchical features from image data.

---

# 3. Why CNN?

Traditional ANN treats every pixel independently.

CNN:

* Preserves spatial relationships.
* Learns features automatically.
* Requires fewer parameters than a fully connected ANN for image tasks.
* Provides higher accuracy for image recognition.

---

# 4. Architecture of CNN

```text
Input Image
      │
      ▼
Convolution Layer
      │
      ▼
Activation (ReLU)
      │
      ▼
Pooling Layer
      │
      ▼
Flatten
      │
      ▼
Fully Connected Layer
      │
      ▼
Output
```

---

# 5. Working of CNN

### Steps

1. Input image is provided.
2. Convolution filters detect features.
3. ReLU introduces non-linearity.
4. Pooling reduces image size.
5. Flatten converts the feature map into a vector.
6. Fully Connected Layer performs classification.
7. Output layer predicts the class.

---

# 6. Convolution Layer

The convolution layer applies **filters (kernels)** to detect features such as:

* Edges
* Corners
* Shapes
* Textures

Example:

```text
Original Image

⬜⬜⬛⬛

↓

Edge Detection Filter

↓

Feature Map
```

---

# 7. Pooling Layer

Pooling reduces the size of feature maps while retaining important information.

### Types

* Max Pooling ⭐ (Most Common)
* Average Pooling

Benefits:

* Reduces computation.
* Reduces overfitting.
* Makes the model faster.

---

# 8. Fully Connected Layer

The flattened features are passed to one or more fully connected layers to perform the final classification.

Example:

```text
Cat Image

↓

CNN

↓

Cat (98%)

Dog (2%)
```

---

# 9. Advantages

* Excellent for image recognition.
* Automatic feature extraction.
* High accuracy.
* Translation invariant.
* Reduces manual feature engineering.

---

# 10. Disadvantages

* Requires large datasets.
* Computationally intensive.
* Long training time.
* Difficult to interpret.

---

# 11. Python Implementation

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])
```

---

# 12. CNN vs ANN

| CNN                          | ANN                                  |
| ---------------------------- | ------------------------------------ |
| Image-specific               | General-purpose                      |
| Uses convolution layers      | Fully connected layers               |
| Automatic feature extraction | Limited automatic feature extraction |
| Fewer parameters for images  | More parameters for images           |

---

# 13. Viva Questions

* What is CNN?
* Why is CNN preferred for image processing?
* What is a convolution layer?
* What is pooling?
* Difference between Max Pooling and Average Pooling?
* What is flattening?

---

# 14. University Questions

### 2 Marks

* Define CNN.
* What is pooling?
* What is convolution?

### 5 Marks

* Explain the architecture of CNN.
* Explain convolution and pooling layers.

### 10 Marks

* Explain CNN with a neat diagram.
* Compare CNN and ANN with suitable examples.

---

# 15. Quick Revision

### Key Points

* Designed for image processing.
* Main layers:

  * Convolution
  * ReLU
  * Pooling
  * Flatten
  * Fully Connected
* Most common pooling: **Max Pooling**

### Memory Trick

Remember **"CRPFO"**

* **C** → Convolution
* **R** → ReLU
* **P** → Pooling
* **F** → Flatten
* **O** → Output

---


