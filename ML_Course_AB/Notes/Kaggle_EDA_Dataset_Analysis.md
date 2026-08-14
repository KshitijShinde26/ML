# Applied Machine Learning Notes

# Part: Kaggle, Dataset Analysis & EDA

# 1. Kaggle Tutorials

## Definition

Kaggle is an online platform for Data Science and Machine Learning that
provides datasets, notebooks, competitions, and learning courses.

## Features

-   Datasets
-   Competitions
-   Notebooks
-   Learn Courses
-   Discussion Forums

## Workflow

1.  Create Account
2.  Select Dataset
3.  Explore Data
4.  Build Model
5.  Submit Results

## Advantages

-   Free datasets
-   Practical learning
-   Community support

------------------------------------------------------------------------

# 2. Dataset Analysis and Visualization

## Definition

Dataset analysis is the process of understanding data before building a
machine learning model.

## Steps

1.  Load Dataset
2.  View Shape
3.  Check Data Types
4.  Find Missing Values
5.  Statistical Summary
6.  Visualize Data

## Python Example

``` python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.shape)
print(df.info())
print(df.describe())
```

## Common Visualizations

-   Line Plot
-   Bar Chart
-   Histogram
-   Scatter Plot
-   Box Plot
-   Heatmap

------------------------------------------------------------------------

# 3. Exploratory Data Analysis (EDA)

## Definition

EDA is the process of analyzing and summarizing datasets using
statistics and visualization before model building.

## Objectives

-   Understand dataset
-   Detect missing values
-   Detect outliers
-   Find relationships
-   Select useful features

## Types

### Univariate Analysis

Study of one variable.

### Bivariate Analysis

Relationship between two variables.

### Multivariate Analysis

Relationship among multiple variables.

## EDA Workflow

``` text
Collect Data
      │
Clean Data
      │
Statistics
      │
Visualization
      │
Insights
      │
Feature Selection
```

## Python Example

``` python
import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(df)
plt.show()

sns.heatmap(df.corr(), annot=True)
```

## Advantages

-   Better understanding of data
-   Improves model accuracy
-   Finds hidden patterns

## Viva Questions

1.  What is Kaggle?
2.  What is EDA?
3.  Why is visualization important?
4.  Difference between Dataset Analysis and EDA?
5.  What is Pairplot?
