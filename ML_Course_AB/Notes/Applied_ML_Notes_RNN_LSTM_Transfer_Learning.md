# Applied Machine Learning Notes (Part)

# Recurrent Neural Network (RNN) & LSTM

## Definition

RNN is a neural network designed for sequential data. It remembers
previous information using feedback connections.

## Applications

-   Language Translation
-   Speech Recognition
-   Time Series Forecasting
-   Chatbots

## RNN Architecture

``` text
Input → Hidden → Output
          ▲
          │
    Previous State
```

## Working

1.  Receive current input.
2.  Combine with previous hidden state.
3.  Produce output.
4.  Pass hidden state to next time step.

## Limitation of RNN

-   Vanishing Gradient Problem
-   Difficulty learning long-term dependencies.

# Long Short-Term Memory (LSTM)

## Definition

LSTM is an improved RNN architecture that can remember information for
long periods.

## Gates in LSTM

-   Forget Gate
-   Input Gate
-   Output Gate

``` text
Input
  │
Forget Gate
  │
Input Gate
  │
Cell State
  │
Output Gate
  │
Output
```

## Advantages

-   Learns long-term dependencies
-   Better than RNN
-   Handles sequential data efficiently

## Python Example

``` python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

model = Sequential([
    LSTM(64, input_shape=(100,1)),
    Dense(1)
])
```

------------------------------------------------------------------------

# Transfer Learning

## Definition

Transfer Learning is a technique where a pre-trained model is reused for
a new but related task.

## Working

1.  Choose a pre-trained model.
2.  Replace the final layer.
3.  Fine-tune on the new dataset.

``` text
Pretrained Model
      │
 Remove Last Layer
      │
 Add New Layer
      │
 Fine Tune
      │
 New Task
```

## Popular Pre-trained Models

-   VGG16
-   ResNet50
-   InceptionV3
-   MobileNet

## Advantages

-   Less training time
-   High accuracy
-   Requires less data

## Applications

-   Medical Imaging
-   Face Recognition
-   Object Detection
-   Image Classification

## Python Example

``` python
from tensorflow.keras.applications import ResNet50

model = ResNet50(weights="imagenet", include_top=False)
```

## Quick Revision

### RNN

-   Sequential data
-   Hidden state
-   Vanishing gradient

### LSTM

-   Forget, Input, Output gates
-   Long-term memory

### Transfer Learning

-   Reuse pretrained model
-   Fine tuning
-   Less data, faster training
