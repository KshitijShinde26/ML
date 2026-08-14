
# 📘 Pandas Notes – Part 1 (Topics 38–45)

# Main Topic: Pandas

## What is Pandas?

Before learning Pandas, let's understand **why it was created**.

Suppose you have the following student data:

| Roll No | Name  | Marks |
| ------- | ----- | ----- |
| 101     | Rahul | 85    |
| 102     | Priya | 90    |
| 103     | Amit  | 78    |

If this data is stored using normal Python lists, it becomes difficult to:

* Search students
* Calculate average marks
* Filter students with marks > 80
* Handle missing values
* Read Excel or CSV files

To solve these problems, Python provides the **Pandas** library.

---

# 38. Introduction to Pandas Library

## Definition

**Pandas** is an open-source Python library used for **data manipulation, analysis, and cleaning**. It provides powerful data structures like **Series** and **DataFrame** that make working with structured data easy.

---

## Why is Pandas Needed?

Imagine a company stores customer data in an Excel file.

Without Pandas:

* Reading data is difficult.
* Searching takes more code.
* Cleaning data is time-consuming.

With Pandas:

* Read Excel in one line.
* Filter records easily.
* Remove missing values.
* Perform statistical analysis.

---

## Features of Pandas

* Fast and efficient
* Easy data manipulation
* Reads CSV, Excel, JSON files
* Handles missing values
* Supports indexing and slicing
* Powerful grouping and aggregation
* Integrates with NumPy and Matplotlib

---

## Installation

```python
pip install pandas
```

Import Pandas

```python
import pandas as pd
```

---

## Pandas Data Structures

Pandas mainly provides two data structures:

### 1. Series

One-dimensional labeled array.

Example

```python
Marks

85
90
78
```

Think of it as **one column** of a table.

---

### 2. DataFrame

Two-dimensional table.

Example

| Name  | Marks |
| ----- | ----- |
| Rahul | 85    |
| Priya | 90    |
| Amit  | 78    |

Think of it as an **Excel sheet**.

---

## Applications

Pandas is used in

* Machine Learning
* Data Science
* Business Analytics
* Finance
* Healthcare
* Data Cleaning
* Artificial Intelligence

---

## Why Pandas is Important in Machine Learning

Machine Learning algorithms cannot directly use raw data.

The data first needs to be

* Loaded
* Cleaned
* Processed
* Filtered
* Converted into numerical format

Pandas performs all these tasks.

### ML Workflow

```
CSV File
     │
     ▼
Pandas
     │
Cleaning
     │
Feature Engineering
     │
NumPy
     │
Machine Learning Model
```

---

# 39. Creating a Pandas Series with a List

## What is a Series?

A **Series** is a **one-dimensional labeled array** capable of storing any data type.

It consists of

* Values
* Index

Example

```
Index    Value

0         85
1         90
2         78
```

---

## Syntax

```python
pd.Series(data)
```

---

## Example

```python
import pandas as pd

marks = pd.Series([85,90,78,92])

print(marks)
```

Output

```
0    85
1    90
2    78
3    92

dtype:int64
```

---

### Explanation

Pandas automatically assigns indexes

```
0
1
2
3
```

These indexes help access values quickly.

---

## Custom Index

```python
marks = pd.Series(
    [85,90,78],
    index=["Rahul","Priya","Amit"]
)

print(marks)
```

Output

```
Rahul    85
Priya    90
Amit     78
dtype:int64
```

---

### Real-Life Example

Temperature of cities

```python
temperature = pd.Series(
    [30,34,28],
    index=["Mumbai","Delhi","Pune"]
)
```

---

## Advantages

* Easy indexing
* Fast calculations
* Stores labels
* Supports missing values

---

# 40. Creating Pandas Series with Dictionary

Suppose we already have

```python
student = {
    "Rahul":85,
    "Priya":90,
    "Amit":78
}
```

Convert into Series

```python
import pandas as pd

s = pd.Series(student)

print(s)
```

Output

```
Rahul    85
Priya    90
Amit     78
dtype:int64
```

---

### Why Dictionary?

Keys become indexes.

Values become Series values.

```
Dictionary

Rahul → 85

↓

Series

Rahul    85
```

---

# 41. Creating Pandas Series with NumPy Array

Since Pandas is built on NumPy, we can directly create a Series from a NumPy array.

Example

```python
import numpy as np
import pandas as pd

arr=np.array([10,20,30])

s=pd.Series(arr)

print(s)
```

Output

```
0    10
1    20
2    30
dtype:int32
```

---

## Why use NumPy Arrays?

Machine Learning datasets are often stored as NumPy arrays. Converting them to a Series allows us to use Pandas' labeling and analysis features.

---

# 42. Object Types in Series

A Pandas Series can store many data types.

### Integer

```python
pd.Series([10,20,30])
```

dtype

```
int64
```

---

### Float

```python
pd.Series([1.5,2.3,5.8])
```

dtype

```
float64
```

---

### String

```python
pd.Series(["AI","ML","DL"])
```

dtype

```
object
```

---

### Boolean

```python
pd.Series([True,False,True])
```

dtype

```
bool
```

---

### Mixed Data

```python
pd.Series([10,"AI",3.5])
```

Output

```
object
```

---

### What is object?

In Pandas, **object** means the Series stores general Python objects, most commonly strings or mixed data types.

---

# 43. Examining the Primary Features of the Pandas Series

Consider

```python
import pandas as pd

s=pd.Series([10,20,30,40])
```

---

## dtype

Shows data type

```python
s.dtype
```

Output

```
int64
```

---

## size

Number of elements

```python
s.size
```

Output

```
4
```

---

## shape

Returns dimensions

```python
s.shape
```

Output

```
(4,)
```

---

## index

Displays indexes

```python
s.index
```

Output

```
RangeIndex(start=0, stop=4, step=1)
```

---

## values

Displays only values

```python
s.values
```

Output

```
array([10,20,30,40])
```

---

## ndim

Dimensions

```python
s.ndim
```

Output

```
1
```

---

# 44. Most Applied Methods on Pandas Series

Suppose

```python
s=pd.Series([15,40,10,35])
```

---

## max()

Largest value

```python
s.max()
```

Output

```
40
```

---

## min()

Smallest value

```python
s.min()
```

Output

```
10
```

---

## mean()

Average

```python
s.mean()
```

Output

```
25
```

---

## sum()

Total

```python
s.sum()
```

Output

```
100
```

---

## sort_values()

Ascending order

```python
s.sort_values()
```

---

## unique()

Unique values

```python
s.unique()
```

---

## count()

Counts non-null values

```python
s.count()
```

---

## isnull()

Checks missing values

```python
s.isnull()
```

---

# 45. Indexing and Slicing Pandas Series

Suppose

```python
s=pd.Series([100,200,300,400,500])
```

---

## Indexing

Access one element

```python
print(s[0])
```

Output

```
100
```

---

```python
print(s[3])
```

Output

```
400
```

---

## Slicing

Access multiple elements

```python
print(s[1:4])
```

Output

```
1    200
2    300
3    400
```

---

## Negative Indexing

```python
print(s[-1])
```

> **Note:** For a Series with the default integer index, `s[-1]` may raise a `KeyError` because Pandas treats `-1` as a label, not a position. To access the last element by position, use:

```python
print(s.iloc[-1])
```

Output

```
500
```

---

## iloc (Position-based Indexing)

```python
print(s.iloc[2])
```

Output

```
300
```

---

## loc (Label-based Indexing)

```python
s = pd.Series(
    [85,90,78],
    index=["Rahul","Priya","Amit"]
)

print(s.loc["Priya"])
```

Output

```
90
```

---

# Difference Between `loc` and `iloc`

| loc                       | iloc                   |
| ------------------------- | ---------------------- |
| Uses labels               | Uses integer positions |
| Example: `s.loc["Rahul"]` | Example: `s.iloc[0]`   |

---

# 📌 Summary of Part 1

You learned:

* ✔ What is Pandas?
* ✔ Why Pandas is important in AI & ML
* ✔ Pandas Series
* ✔ Creating Series from List, Dictionary, and NumPy Array
* ✔ Data types in a Series
* ✔ Series properties
* ✔ Common Series methods
* ✔ Indexing and slicing with `loc` and `iloc`

---

# 🎤 Viva Questions (Part 1)

1. What is Pandas?
2. Why is Pandas used in Machine Learning?
3. What is a Series?
4. What is the difference between a Series and a DataFrame?
5. How do you create a Series from a list?
6. How do you create a Series from a dictionary?
7. Why are NumPy and Pandas often used together?
8. What does `dtype` represent?
9. What is the difference between `loc` and `iloc`?
10. Name five commonly used methods of a Pandas Series.

---


# 📘 Pandas Viva Questions with Answers (Part 1: Topics 38–45)

---

# 1. What is Pandas?

### Answer:

**Pandas** is an open-source Python library used for **data manipulation, analysis, and cleaning**. It provides two main data structures: **Series** and **DataFrame**, which help in organizing and analyzing structured data efficiently.

**Example Use:** Reading CSV files, handling missing values, filtering data, and preparing datasets for Machine Learning.

---

# 2. Why is Pandas used in Machine Learning?

### Answer:

Pandas is used in Machine Learning because it helps to:

* Load datasets (CSV, Excel, etc.)
* Clean missing or incorrect data
* Filter and sort records
* Select useful features
* Prepare data before training ML models

### ML Workflow:

```text
Dataset
   ↓
Pandas
   ↓
Data Cleaning
   ↓
Feature Selection
   ↓
Machine Learning Model
```

---

# 3. What is a Series?

### Answer:

A **Series** is a **one-dimensional labeled array** in Pandas. It stores data along with an index.

### Example:

```python
import pandas as pd

s = pd.Series([10,20,30])
print(s)
```

Output:

```text
0    10
1    20
2    30
dtype: int64
```

---

# 4. What is the difference between a Series and a DataFrame?

| Series                | DataFrame                  |
| --------------------- | -------------------------- |
| One-dimensional       | Two-dimensional            |
| Single column of data | Multiple rows and columns  |
| Has one index         | Has row and column indexes |

### Example:

**Series**

```text
0    10
1    20
2    30
```

**DataFrame**

| Name  | Marks |
| ----- | ----- |
| Rahul | 85    |
| Priya | 90    |

---

# 5. How do you create a Series from a list?

### Answer:

Use the **`pd.Series()`** function with a Python list.

### Example:

```python
import pandas as pd

marks = pd.Series([85,90,78])

print(marks)
```

---

# 6. How do you create a Series from a dictionary?

### Answer:

Pass the dictionary to **`pd.Series()`**. The dictionary keys become the **index**, and the values become the **Series values**.

### Example:

```python
import pandas as pd

student = {
    "Rahul":85,
    "Priya":90,
    "Amit":78
}

s = pd.Series(student)

print(s)
```

Output:

```text
Rahul    85
Priya    90
Amit     78
dtype: int64
```

---

# 7. Why are NumPy and Pandas often used together?

### Answer:

Pandas is built on top of **NumPy**. NumPy provides fast numerical operations, while Pandas provides labeled data structures and data analysis features.

### Advantages:

* Faster calculations
* Efficient memory usage
* Easy data manipulation
* Better support for Machine Learning

---

# 8. What does `dtype` represent?

### Answer:

`dtype` stands for **Data Type**. It tells us what type of data is stored in a Series or DataFrame.

### Example:

```python
import pandas as pd

s = pd.Series([10,20,30])

print(s.dtype)
```

Output:

```text
int64
```

Other examples:

* `int64` → Integer
* `float64` → Decimal numbers
* `object` → Strings or mixed data
* `bool` → Boolean values

---

# 9. What is the difference between `loc` and `iloc`?

### Answer:

| `loc`                | `iloc`                  |
| -------------------- | ----------------------- |
| Uses labels          | Uses integer positions  |
| Label-based indexing | Position-based indexing |

### Example:

```python
import pandas as pd

s = pd.Series(
    [85,90,78],
    index=["Rahul","Priya","Amit"]
)
```

Using **`loc`**

```python
s.loc["Priya"]
```

Output:

```text
90
```

Using **`iloc`**

```python
s.iloc[1]
```

Output:

```text
90
```

---

# 10. Name five commonly used methods of a Pandas Series.

### Answer:

Some commonly used methods are:

| Method    | Purpose                  |
| --------- | ------------------------ |
| `max()`   | Finds the largest value  |
| `min()`   | Finds the smallest value |
| `mean()`  | Calculates the average   |
| `sum()`   | Calculates the total sum |
| `count()` | Counts non-null values   |

Other useful methods:

* `sort_values()`
* `unique()`
* `isnull()`
* `head()`
* `tail()`

---

# ⭐ Bonus Viva Questions (Frequently Asked)

## 11. What is the full form of Pandas?

### Answer:

**Pandas** does not officially stand for anything. It is derived from the term **Panel Data**, which refers to multidimensional structured datasets used in statistics and econometrics.

---

## 12. Which two main data structures are provided by Pandas?

### Answer:

1. **Series** – One-dimensional labeled array.
2. **DataFrame** – Two-dimensional table with rows and columns.

---

## 13. Which command is used to import Pandas?

### Answer:

```python
import pandas as pd
```

Here, `pd` is the standard alias for the Pandas library.

---

## 14. Can a Series contain different data types?

### Answer:

Yes, a Series can contain mixed data types. In such cases, the data type (`dtype`) is usually **object**.

### Example:

```python
import pandas as pd

s = pd.Series([10, "AI", 3.5])

print(s)
```

---

## 15. Why are indexes important in a Series?

### Answer:

Indexes help identify and access elements quickly. They allow users to retrieve data using labels or positions.

### Example:

```python
s = pd.Series([85,90], index=["Rahul","Priya"])

print(s["Rahul"])
```

Output:

```text
85
```

---

# 🎯 Most Important Viva Questions (Exam Focus)

1. What is Pandas?
2. What is a Series?
3. Difference between Series and DataFrame.
4. How do you create a Series from a list?
5. How do you create a Series from a dictionary?
6. What is `dtype`?
7. What is the difference between `loc` and `iloc`?
8. Why is Pandas important in Machine Learning?
9. Name five methods of a Series.
10. Why are NumPy and Pandas used together?



---

# 📘 Pandas Notes – Part 2
---

# Introduction to DataFrame

## What is a DataFrame?

A **DataFrame** is a **two-dimensional labeled data structure** in Pandas that stores data in rows and columns, similar to an Excel spreadsheet or SQL table.

Example:

| Roll No | Name  | Marks |
| ------- | ----- | ----- |
| 101     | Rahul | 85    |
| 102     | Priya | 90    |
| 103     | Amit  | 78    |

Each column can store different data types.

---

## Why DataFrames are Important?

DataFrames are widely used because they:

* Store tabular data efficiently.
* Support filtering and sorting.
* Handle missing values.
* Read and write CSV, Excel, and SQL data.
* Prepare datasets for Machine Learning.

---

# 46. Creating Pandas DataFrame with List

## Definition

A DataFrame can be created from a list of lists, where each inner list represents a row.

## Syntax

```python
pd.DataFrame(data, columns=column_names)
```

## Example

```python
import pandas as pd

data = [
    [101, "Rahul", 85],
    [102, "Priya", 90],
    [103, "Amit", 78]
]

df = pd.DataFrame(data, columns=["Roll No", "Name", "Marks"])

print(df)
```

### Output

```
   Roll No   Name  Marks
0      101  Rahul     85
1      102  Priya     90
2      103   Amit     78
```

### Explanation

* Each inner list becomes one row.
* `columns` assigns column names.

---

# 47. Creating DataFrame with NumPy Array

Since Pandas is built on NumPy, NumPy arrays can be directly converted into DataFrames.

Example

```python
import numpy as np
import pandas as pd

arr = np.array([
    [1,2],
    [3,4],
    [5,6]
])

df = pd.DataFrame(arr, columns=["A","B"])

print(df)
```

Output

```
   A  B
0  1  2
1  3  4
2  5  6
```

---

# 48. Creating DataFrame with Dictionary

Dictionary keys become column names.

Example

```python
import pandas as pd

student = {
    "Name":["Rahul","Priya","Amit"],
    "Marks":[85,90,78],
    "City":["Pune","Delhi","Mumbai"]
}

df = pd.DataFrame(student)

print(df)
```

Output

| Name  | Marks | City   |
| ----- | ----- | ------ |
| Rahul | 85    | Pune   |
| Priya | 90    | Delhi  |
| Amit  | 78    | Mumbai |

---

# Which Method is Best?

| Method      | Best Use           |
| ----------- | ------------------ |
| List        | Small datasets     |
| Dictionary  | Most common        |
| NumPy Array | Numerical datasets |

---

# 49. Properties of DataFrame

Consider

```python
df = pd.DataFrame({
    "Name":["Rahul","Priya","Amit"],
    "Marks":[85,90,78]
})
```

---

## shape

Returns rows and columns.

```python
df.shape
```

Output

```
(3,2)
```

---

## size

Returns total elements.

```python
df.size
```

Output

```
6
```

---

## columns

Returns column names.

```python
df.columns
```

Output

```
Index(['Name','Marks'])
```

---

## index

Returns row indexes.

```python
df.index
```

---

## dtypes

Returns datatype of each column.

```python
df.dtypes
```

Output

```
Name     object
Marks     int64
```

---

## values

Returns NumPy array.

```python
df.values
```

---

## ndim

Returns number of dimensions.

```
2
```

---

# 50. Element Selection Operations (Lesson 1)

Selecting a single column.

Example

```python
df["Marks"]
```

Output

```
0    85
1    90
2    78
```

Notice the output is a **Series**.

---

Selecting multiple columns.

```python
df[["Name","Marks"]]
```

Output

| Name  | Marks |
| ----- | ----- |
| Rahul | 85    |
| Priya | 90    |
| Amit  | 78    |

Output is a **DataFrame**.

---

# 51. Element Selection Operations (Lesson 2)

Selecting rows using `iloc`.

```python
df.iloc[1]
```

Output

```
Name     Priya
Marks       90
```

Selecting multiple rows.

```python
df.iloc[0:2]
```

---

Selecting specific rows and columns.

```python
df.iloc[0:2,0:2]
```

---

# 52. Top Level Element Selection – Lesson 1

Selecting one column.

```python
df.Name
```

or

```python
df["Name"]
```

Both return the same result.

**Recommendation:** Prefer `df["Name"]` because it works with all column names.

---

# 53. Top Level Element Selection – Lesson 2

Using `loc`.

```python
df.loc[1]
```

Returns

```
Name     Priya
Marks       90
```

Selecting specific row and column.

```python
df.loc[1,"Marks"]
```

Output

```
90
```

---

# 54. Top Level Element Selection – Lesson 3

Selecting multiple rows and columns.

```python
df.loc[0:2,["Name","Marks"]]
```

Output

| Name  | Marks |
| ----- | ----- |
| Rahul | 85    |
| Priya | 90    |
| Amit  | 78    |

---

# Difference Between `loc` and `iloc`

| loc                                       | iloc                                      |
| ----------------------------------------- | ----------------------------------------- |
| Uses labels                               | Uses integer positions                    |
| Includes end label in slices              | Excludes end position like Python slicing |
| Example: `df.loc[0:2]` returns rows 0,1,2 | `df.iloc[0:2]` returns rows 0,1           |

---

# 55. Conditional Selection

Suppose

```python
df
```

| Name  | Marks |
| ----- | ----- |
| Rahul | 85    |
| Priya | 90    |
| Amit  | 78    |

Students with marks above 80.

```python
df[df["Marks"]>80]
```

Output

| Name  | Marks |
| ----- | ----- |
| Rahul | 85    |
| Priya | 90    |

---

Multiple Conditions

```python
df[(df["Marks"]>80) & (df["Marks"]<90)]
```

Output

| Name  | Marks |
| ----- | ----- |
| Rahul | 85    |

---

# Why Conditional Selection?

Useful in:

* Finding top-performing students.
* Filtering customers.
* Selecting specific records.
* Preparing ML datasets.

---

# 56. Adding Columns

Suppose

```python
df
```

| Name  | Marks |
| ----- | ----- |
| Rahul | 85    |
| Priya | 90    |

---

Add Age

```python
df["Age"]=[20,21]
```

Output

| Name  | Marks | Age |
| ----- | ----- | --- |
| Rahul | 85    | 20  |
| Priya | 90    | 21  |

---

Derived Column

```python
df["Result"]=df["Marks"]>=40
```

Output

| Name  | Marks | Result |
| ----- | ----- | ------ |
| Rahul | 85    | True   |
| Priya | 90    | True   |

---

# 57. Removing Rows and Columns

Using `drop()`.

Remove Column

```python
df.drop("Age",axis=1)
```

* `axis=1` → column
* `axis=0` → row

---

Remove Row

```python
df.drop(1)
```

---

Permanent Removal

```python
df.drop("Age",axis=1,inplace=True)
```

`inplace=True` modifies the original DataFrame.

---

# 58. Null Values

## What are Null Values?

Null values represent missing or unavailable data.

Example

| Name  | Marks |
| ----- | ----- |
| Rahul | 85    |
| Priya | NaN   |
| Amit  | 78    |

Here, **NaN (Not a Number)** indicates missing data.

---

## Why Do Null Values Occur?

* User skipped entering data.
* Sensor failure.
* Data corruption.
* Missing information in surveys.
* Import errors.

---

## Detecting Null Values

```python
df.isnull()
```

Output

```
Name   Marks
False  False
False   True
False  False
```

---

Count Null Values

```python
df.isnull().sum()
```

Output

```
Name     0
Marks    1
```

---

## Why Handle Null Values?

Machine Learning algorithms generally cannot process missing values directly. Detecting and handling them is an important preprocessing step.

---

# 📌 Summary of Part 2

You learned:

* ✔ Creating DataFrames using lists, NumPy arrays, and dictionaries
* ✔ DataFrame properties (`shape`, `size`, `columns`, `dtypes`, etc.)
* ✔ Selecting rows and columns using `[]`, `loc`, and `iloc`
* ✔ Conditional filtering
* ✔ Adding new columns
* ✔ Removing rows and columns with `drop()`
* ✔ Understanding and detecting null values

---

# 🎤 Viva Questions (Part 2)

1. What is a DataFrame?
2. What is the difference between a Series and a DataFrame?
3. How do you create a DataFrame from a dictionary?
4. What does `shape` return?
5. What is the difference between `loc` and `iloc`?
6. How do you select multiple columns?
7. How do you filter rows based on a condition?
8. How do you add a new column to a DataFrame?
9. What is the purpose of the `drop()` function?
10. What are null values, and why should they be handled?




---

# 📘 Pandas Viva Questions with Answers (Part 2)

---

# 1. What is a DataFrame?

### Answer

A **DataFrame** is a **two-dimensional labeled data structure** in Pandas that stores data in rows and columns, similar to an Excel spreadsheet or SQL table. Each column can have a different data type.

### Example

| Roll No | Name  | Marks |
| ------- | ----- | ----- |
| 101     | Rahul | 85    |
| 102     | Priya | 90    |

---

# 2. What is the difference between a Series and a DataFrame?

### Answer

| Series                  | DataFrame                                         |
| ----------------------- | ------------------------------------------------- |
| One-dimensional         | Two-dimensional                                   |
| Single column           | Multiple columns                                  |
| Stores one type of data | Stores multiple columns with different data types |
| Example: Marks          | Example: Student Table                            |

---

# 3. How do you create a DataFrame from a dictionary?

### Answer

Use the **`pd.DataFrame()`** function and pass a dictionary where:

* Keys become column names.
* Values become column data.

### Example

```python
import pandas as pd

student = {
    "Name": ["Rahul", "Priya"],
    "Marks": [85, 90]
}

df = pd.DataFrame(student)

print(df)
```

---

# 4. What does `shape` return?

### Answer

The **`shape`** property returns the number of **rows and columns** in a DataFrame.

### Syntax

```python
df.shape
```

### Example

If a DataFrame has 5 rows and 3 columns:

```text
(5, 3)
```

* First number → Rows
* Second number → Columns

---

# 5. What is the difference between `loc` and `iloc`?

### Answer

| loc                           | iloc                             |
| ----------------------------- | -------------------------------- |
| Label-based indexing          | Position-based indexing          |
| Uses row/column labels        | Uses integer positions           |
| Includes end label in slicing | Excludes end position in slicing |

### Example

```python
df.loc[1]
```

Returns row with label `1`.

```python
df.iloc[1]
```

Returns the second row by position.

---

# 6. How do you select multiple columns?

### Answer

Use double square brackets.

### Example

```python
df[["Name", "Marks"]]
```

This returns only the selected columns as a DataFrame.

---

# 7. How do you filter rows based on a condition?

### Answer

Use conditional selection inside square brackets.

### Example

```python
df[df["Marks"] > 80]
```

This returns only rows where the Marks are greater than 80.

---

# 8. How do you add a new column to a DataFrame?

### Answer

Assign values to a new column name.

### Example

```python
df["Age"] = [20, 21]
```

A new column named **Age** is added.

---

# 9. What is the purpose of the `drop()` function?

### Answer

The **`drop()`** function removes rows or columns from a DataFrame.

### Example

Remove a column:

```python
df.drop("Age", axis=1)
```

Remove a row:

```python
df.drop(1)
```

---

# 10. What are null values, and why should they be handled?

### Answer

**Null values** represent missing or unavailable data. In Pandas, they are usually shown as **NaN (Not a Number)**.

Null values should be handled because:

* They can cause errors in data analysis.
* Most Machine Learning algorithms cannot process missing values directly.
* They may reduce the accuracy of predictions.

Common methods:

* `dropna()` → Remove missing values.
* `fillna()` → Replace missing values.

---

# ⭐ Additional Viva Questions

## 11. What does `axis=0` mean?

### Answer

`axis=0` refers to **rows**.

Example:

```python
df.drop(1, axis=0)
```

Removes row number 1.

---

## 12. What does `axis=1` mean?

### Answer

`axis=1` refers to **columns**.

Example

```python
df.drop("Age", axis=1)
```

Removes the Age column.

---

## 13. What does `inplace=True` mean?

### Answer

It modifies the original DataFrame permanently without creating a new one.

Example

```python
df.drop("Age", axis=1, inplace=True)
```

---

## 14. What is conditional selection?

### Answer

Conditional selection means selecting rows based on one or more conditions.

Example

```python
df[df["Marks"] > 80]
```

---

## 15. Why are DataFrames important in Machine Learning?

### Answer

DataFrames help to:

* Load datasets.
* Clean and preprocess data.
* Handle missing values.
* Select useful features.
* Prepare data before training Machine Learning models.

---

# 🎯 Most Important Viva Questions

1. What is a DataFrame?
2. Difference between Series and DataFrame.
3. Difference between `loc` and `iloc`.
4. Difference between `axis=0` and `axis=1`.
5. How do you add a column?
6. How do you remove a column?
7. What are null values?
8. What is conditional selection?
9. What is the use of `shape`?
10. What is the use of `drop()`?

---

# 📘 Pandas Notes – Part 3 (Topics 59–70)

## Topics Covered

59. Dropping Null Values: `dropna()`
60. Filling Null Values: `fillna()`
61. Setting Index in Pandas DataFrames
62. Multi-Index and Index Hierarchy
63. Element Selection in Multi-Indexed DataFrames
64. Selecting Elements Using the `xs()` Function
65. Concatenating DataFrames: `concat()`
    66–69. Merging DataFrames: `merge()`
66. Joining DataFrames: `join()`

---

# 59. Dropping Null Values: `dropna()`

## What is `dropna()`?

The `dropna()` function removes rows or columns that contain missing (`NaN`) values.

### Why is it Needed?

Missing values can:

* Cause errors in analysis.
* Affect machine learning models.
* Produce incorrect statistics.

---

## Syntax

```python
df.dropna(axis=0, how='any', inplace=False)
```

### Parameters

* **axis=0** → Remove rows (default)
* **axis=1** → Remove columns
* **how='any'** → Remove if at least one null exists
* **how='all'** → Remove only if all values are null
* **inplace=True** → Modify original DataFrame

---

## Example

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit"],
    "Marks": [85, np.nan, 78]
})

print(df.dropna())
```

### Output

| Name  | Marks |
| ----- | ----: |
| Rahul |    85 |
| Amit  |    78 |

The row containing `NaN` is removed.

---

# 60. Filling Null Values: `fillna()`

## What is `fillna()`?

Instead of deleting data, `fillna()` replaces missing values with a specified value.

### Syntax

```python
df.fillna(value)
```

### Example

```python
df.fillna(0)
```

### Output

| Name  | Marks |
| ----- | ----: |
| Rahul |    85 |
| Priya |     0 |
| Amit  |    78 |

You can also replace with:

```python
df.fillna(df["Marks"].mean())
```

This fills missing values with the average of the `Marks` column.

---

# Difference Between `dropna()` and `fillna()`

| `dropna()`                               | `fillna()`              |
| ---------------------------------------- | ----------------------- |
| Removes rows/columns with missing values | Replaces missing values |
| May reduce dataset size                  | Preserves dataset size  |

---

# 61. Setting Index in DataFrames

## What is an Index?

An **index** uniquely identifies each row in a DataFrame.

By default, Pandas uses numeric indexes: `0, 1, 2, ...`

You can set another column as the index.

### Example

```python
df.set_index("Name")
```

### Output

| Name  | Marks |
| ----- | ----: |
| Rahul |    85 |
| Priya |    90 |
| Amit  |    78 |

Now **Name** becomes the row label.

---

# 62. MultiIndex and Index Hierarchy

## What is a MultiIndex?

A **MultiIndex** uses more than one column as the row index, creating a hierarchical index.

### Example

| Department | Year | Student | Marks |
| ---------- | ---- | ------- | ----: |
| IT         | TY   | Rahul   |    85 |
| IT         | TY   | Priya   |    90 |
| CS         | TY   | Amit    |    78 |

```python
df.set_index(["Department", "Year"])
```

This creates two index levels: **Department** and **Year**.

---

# 63. Element Selection in Multi-Indexed DataFrames

Once a MultiIndex is created, rows can be selected using tuples.

### Example

```python
df.loc[("IT", "TY")]
```

This returns all records belonging to the IT department in TY.

---

# 64. Selecting Elements Using the `xs()` Function

## What is `xs()`?

`xs()` stands for **Cross Section**. It selects data from a particular level of a MultiIndex.

### Example

```python
df.xs("IT", level="Department")
```

This retrieves all rows where the **Department** is IT.

---

# 65. Concatenating DataFrames: `concat()`

## What is `concat()`?

The `concat()` function combines two or more DataFrames either vertically or horizontally.

### Vertical Concatenation (default)

```python
pd.concat([df1, df2])
```

Rows from `df2` are added below `df1`.

### Horizontal Concatenation

```python
pd.concat([df1, df2], axis=1)
```

Columns from `df2` are placed beside `df1`.

---

# 66–69. Merging DataFrames: `merge()`

## What is `merge()`?

The `merge()` function combines DataFrames based on one or more common columns, similar to SQL JOIN operations.

### Syntax

```python
pd.merge(df1, df2, on="ID")
```

---

## Types of Merge

### Inner Merge

Returns only matching records.

```python
pd.merge(df1, df2, on="ID", how="inner")
```

---

### Left Merge

Returns all rows from the left DataFrame and matching rows from the right.

```python
pd.merge(df1, df2, on="ID", how="left")
```

---

### Right Merge

Returns all rows from the right DataFrame.

```python
pd.merge(df1, df2, on="ID", how="right")
```

---

### Outer Merge

Returns all rows from both DataFrames, filling unmatched values with `NaN`.

```python
pd.merge(df1, df2, on="ID", how="outer")
```

---

# Difference Between `concat()` and `merge()`

| `concat()`                      | `merge()`                           |
| ------------------------------- | ----------------------------------- |
| Stacks DataFrames               | Combines using a common key         |
| Doesn't require a common column | Requires one or more common columns |
| Similar to appending            | Similar to SQL JOIN                 |

---

# 70. Joining DataFrames: `join()`

## What is `join()`?

The `join()` function combines DataFrames based on their indexes.

### Example

```python
df1.join(df2)
```

If both DataFrames have the same index, they are joined together.

---

## Difference Between `join()` and `merge()`

| `join()`                | `merge()`                                     |
| ----------------------- | --------------------------------------------- |
| Joins using indexes     | Joins using columns (or indexes if specified) |
| Simpler syntax          | More flexible with join keys                  |
| Best when indexes match | Best when using common columns                |

---

# 📌 Summary of Part 3

You learned:

* ✔ Handling missing values with `dropna()` and `fillna()`
* ✔ Setting a custom index with `set_index()`
* ✔ Creating and using MultiIndex
* ✔ Selecting data with `loc` and `xs()`
* ✔ Combining DataFrames using `concat()`
* ✔ Merging DataFrames with different join types
* ✔ Joining DataFrames based on indexes


Great! You're building a solid set of notes. Let's continue.

---

# 📘 Pandas Notes – Part 4 (Topics 71–81)

---

# 71. Loading a Dataset from the Seaborn Library

## What is Seaborn?

**Seaborn** is a Python library mainly used for **data visualization**. It also provides many built-in datasets for learning and practicing data analysis.

Some popular datasets are:

* tips
* iris
* titanic
* flights
* diamonds
* penguins

---

## Why Use Seaborn Datasets?

Instead of creating your own data, you can use ready-made datasets to:

* Practice Pandas
* Learn Machine Learning
* Perform Data Analysis
* Create Charts

---

## Installation

```python
pip install seaborn
```

Import Libraries

```python
import seaborn as sns
import pandas as pd
```

---

## Load Dataset

Example

```python
tips = sns.load_dataset("tips")
```

---

## Display Dataset

```python
print(tips)
```

Output (first few rows)

| total_bill | tip  | sex    | smoker | day | time   | size |
| ---------- | ---- | ------ | ------ | --- | ------ | ---- |
| 16.99      | 1.01 | Female | No     | Sun | Dinner | 2    |
| 10.34      | 1.66 | Male   | No     | Sun | Dinner | 3    |

---

## Applications

* Machine Learning
* Data Analysis
* Data Visualization
* Statistics

---

# 72. Examining the Dataset - 1

After loading a dataset, we need to understand it.

---

## head()

Displays first 5 rows.

```python
tips.head()
```

---

## tail()

Displays last 5 rows.

```python
tips.tail()
```

---

## sample()

Displays random rows.

```python
tips.sample(5)
```

---

## info()

Shows:

* Number of rows
* Number of columns
* Data types
* Missing values

```python
tips.info()
```

Example Output

```text
<class 'DataFrame'>
244 entries
7 columns
```

---

## describe()

Provides statistical summary.

```python
tips.describe()
```

Output includes

* Count
* Mean
* Standard Deviation
* Minimum
* Maximum
* Quartiles

---

## columns

```python
tips.columns
```

Returns all column names.

---

## shape

```python
tips.shape
```

Example Output

```text
(244,7)
```

---

## dtypes

```python
tips.dtypes
```

Shows data type of every column.

---

# Why Examine Dataset First?

Before building an ML model, we must know:

* Number of rows
* Number of columns
* Missing values
* Data types
* Statistics

This process is called **Exploratory Data Analysis (EDA)**.

---

# 73. Aggregation Functions

## What are Aggregation Functions?

Aggregation functions combine multiple values into a **single summary value**.

Example:

Marks

```text
70
80
90
```

Average

```text
80
```

---

## Common Aggregation Functions

### sum()

```python
tips["tip"].sum()
```

Returns total tips.

---

### mean()

```python
tips["tip"].mean()
```

Returns average tip.

---

### max()

```python
tips["tip"].max()
```

Largest tip.

---

### min()

```python
tips["tip"].min()
```

Smallest tip.

---

### count()

```python
tips["tip"].count()
```

Counts non-null values.

---

### median()

```python
tips["tip"].median()
```

Middle value.

---

### std()

Standard deviation.

```python
tips["tip"].std()
```

---

### var()

Variance.

```python
tips["tip"].var()
```

---

# Applications

Used in

* Business reports
* Sales analysis
* Student results
* Machine Learning preprocessing

---

# 74. Examining Dataset - 2

After basic analysis, examine unique values.

---

## unique()

```python
tips["day"].unique()
```

Output

```text
['Sun','Sat','Thur','Fri']
```

---

## value_counts()

Counts frequency.

```python
tips["day"].value_counts()
```

Output

```text
Sat 87
Sun 76
Thur 62
Fri 19
```

---

## nunique()

Number of unique values.

```python
tips["day"].nunique()
```

Output

```text
4
```

---

# 75. Grouping and Aggregation (groupby())

## What is groupby()?

It divides data into groups and performs calculations on each group.

Example:

Restaurant wants

Average tip by gender.

Instead of calculating manually,

Pandas does it automatically.

---

## Syntax

```python
df.groupby(column)
```

---

## Example

```python
tips.groupby("sex")["tip"].mean()
```

Output

```text
Female 2.83
Male   3.09
```

---

Another Example

Average total bill by day.

```python
tips.groupby("day")["total_bill"].mean()
```

---

Group by multiple columns

```python
tips.groupby(["sex","day"])["tip"].mean()
```

---

# Why groupby()?

Very useful in

* Business reports
* Banking
* Healthcare
* Machine Learning
* Data Analytics

---

# 76. aggregate() / agg()

## What is agg()?

`agg()` allows multiple aggregation functions together.

Example

```python
tips["tip"].agg(["mean","max","min"])
```

Output

| mean | max | min |
| ---- | --- | --- |
| 2.99 | 10  | 1   |

---

Groupby with agg()

```python
tips.groupby("day")["tip"].agg(["mean","sum","max"])
```

---

# Why agg()?

Instead of writing

```python
mean()

sum()

max()
```

three times,

write once.

---

# 77. filter()

## What is filter()?

Keeps only groups satisfying a condition.

Example

```python
tips.groupby("day").filter(lambda x: len(x)>50)
```

Meaning

Keep only days having more than 50 records.

---

Applications

* Remove small groups
* Clean data
* Business analytics

---

# 78. transform()

## What is transform()?

Returns transformed values while keeping the **same DataFrame size**.

Example

Normalize tips.

```python
tips["Normalized Tip"]=tips.groupby("day")["tip"].transform("mean")
```

Each row gets the average tip of its group.

---

Difference

| agg()           | transform()                |
| --------------- | -------------------------- |
| Returns summary | Returns transformed column |
| Output smaller  | Output same size           |

---

# 79. apply()

## What is apply()?

Used to apply **custom functions**.

Example

```python
tips["tip"].apply(lambda x:x*2)
```

Output

Every tip becomes double.

---

Example

Convert names to uppercase.

```python
tips["day"].apply(str.upper)
```

Output

```text
SUN
SAT
THUR
```

---

Why use apply()?

Whenever built-in functions are not enough.

---

# 80. Examining Dataset - 3

More useful functions.

---

## sort_values()

Sort data.

```python
tips.sort_values("tip")
```

Ascending.

---

Descending.

```python
tips.sort_values("tip",ascending=False)
```

---

## sort_index()

Sort by index.

```python
tips.sort_index()
```

---

## duplicated()

Find duplicate rows.

```python
tips.duplicated()
```

---

## drop_duplicates()

Remove duplicate rows.

```python
tips.drop_duplicates()
```

---

# 81. Pivot Tables

## What is Pivot Table?

A Pivot Table summarizes large datasets into meaningful reports.

Suppose a restaurant wants

Average tip by day.

Instead of manually calculating,

Pivot Table creates it instantly.

---

## Syntax

```python
pd.pivot_table(
    tips,
    values="tip",
    index="day"
)
```

Output

| Day | Average Tip |
| --- | ----------- |
| Fri | 2.73        |
| Sat | 2.99        |
| Sun | 3.25        |

---

Multiple Aggregations

```python
pd.pivot_table(
    tips,
    values="tip",
    index="day",
    aggfunc=["mean","max"]
)
```

---

Applications

* Business Intelligence
* Sales Reports
* Finance
* Healthcare
* Machine Learning Data Analysis

---

# Difference Between groupby() and Pivot Table

| groupby()           | Pivot Table              |
| ------------------- | ------------------------ |
| Flexible            | Easy summary reports     |
| Programmer-oriented | Business-oriented        |
| More coding         | Less coding              |
| More customizable   | Easy visualization-ready |

---

# Summary of Part 4

You learned

✔ Loading datasets from Seaborn

✔ Exploring datasets

✔ Statistical summaries

✔ Aggregation functions

✔ groupby()

✔ agg()

✔ filter()

✔ transform()

✔ apply()

✔ Pivot Tables

---

# 🎤 Viva Questions (Part 4)

1. What is Seaborn?
2. Why do we use built-in datasets?
3. What is Exploratory Data Analysis (EDA)?
4. Difference between `head()` and `tail()`.
5. Difference between `unique()` and `nunique()`.
6. What is `groupby()`?
7. Difference between `agg()` and `transform()`.
8. What is `apply()`?
9. What is a Pivot Table?
10. Difference between `groupby()` and a Pivot Table.

---


# 📘 Pandas Notes – Part 5 (Topics 82–86) **Final Part**

---

# 82. Reading CSV Files

## What is a CSV File?

**CSV** stands for **Comma-Separated Values**. It is one of the most common file formats used to store tabular data.

Example (`students.csv`):

```text
RollNo,Name,Marks
101,Rahul,85
102,Priya,90
103,Amit,78
```

Each row represents one record, and commas separate the values.

---

## Why are CSV Files Important?

CSV files are widely used because they are:

* Easy to create and edit.
* Supported by Excel, Google Sheets, and databases.
* Commonly used in Data Science and Machine Learning.

---

## Reading a CSV File

### Syntax

```python
pd.read_csv("filename.csv")
```

### Example

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df)
```

### Output

| RollNo | Name  | Marks |
| -----: | ----- | ----: |
|    101 | Rahul |    85 |
|    102 | Priya |    90 |
|    103 | Amit  |    78 |

---

## Reading Specific Number of Rows

```python
df = pd.read_csv("students.csv", nrows=2)
```

Output

| RollNo | Name  | Marks |
| -----: | ----- | ----: |
|    101 | Rahul |    85 |
|    102 | Priya |    90 |

---

## Reading Selected Columns

```python
df = pd.read_csv("students.csv", usecols=["Name", "Marks"])
```

Output

| Name  | Marks |
| ----- | ----: |
| Rahul |    85 |
| Priya |    90 |
| Amit  |    78 |

---

## Setting an Index While Reading

```python
df = pd.read_csv("students.csv", index_col="RollNo")
```

Output

| RollNo | Name  | Marks |
| -----: | ----- | ----: |
|    101 | Rahul |    85 |
|    102 | Priya |    90 |
|    103 | Amit  |    78 |

Here, **RollNo** becomes the row index.

---

# 83. Writing CSV Files

## What is `to_csv()`?

The `to_csv()` function saves a DataFrame as a CSV file.

---

## Syntax

```python
df.to_csv("filename.csv")
```

---

## Example

```python
import pandas as pd

student = {
    "Name": ["Rahul", "Priya"],
    "Marks": [85, 90]
}

df = pd.DataFrame(student)

df.to_csv("output.csv")
```

A new file named **output.csv** is created.

---

## Save Without Index

```python
df.to_csv("output.csv", index=False)
```

This prevents the row numbers from being saved.

---

# 84. Reading Excel Files

## Why Read Excel Files?

Many companies store data in **Microsoft Excel (.xlsx)** files.

Pandas can directly read Excel files.

---

## Install Required Library

```bash
pip install openpyxl
```

---

## Syntax

```python
pd.read_excel("students.xlsx")
```

---

## Example

```python
import pandas as pd

df = pd.read_excel("students.xlsx")

print(df)
```

---

## Read a Specific Sheet

```python
df = pd.read_excel("students.xlsx", sheet_name="Sheet1")
```

---

## Read Multiple Sheets

```python
all_sheets = pd.read_excel("students.xlsx", sheet_name=None)
```

This returns a **dictionary** where each key is a sheet name and each value is a DataFrame.

---

# 85. Writing Excel Files

## What is `to_excel()`?

The `to_excel()` function saves a DataFrame as an Excel file.

---

## Syntax

```python
df.to_excel("filename.xlsx")
```

---

## Example

```python
df.to_excel("students.xlsx", index=False)
```

A new Excel file named **students.xlsx** is created.

---

## Writing to a Specific Sheet

```python
df.to_excel("students.xlsx", sheet_name="StudentData", index=False)
```

---

# Difference Between CSV and Excel

| CSV               | Excel                     |
| ----------------- | ------------------------- |
| Plain text format | Spreadsheet format        |
| Faster to read    | Slightly slower           |
| Stores one sheet  | Can store multiple sheets |
| Smaller file size | Larger file size          |
| Extension: `.csv` | Extension: `.xlsx`        |

---

# Best Practices While Working with Files

* Check the file path before reading.
* Use `index=False` when saving if row numbers are not needed.
* Handle missing values before saving.
* Verify column names after reading.
* Use Excel files for multiple sheets and CSV for simple datasets.

---

# 86. Complete Pandas Revision

## Main Data Structures

1. **Series** – One-dimensional labeled array.
2. **DataFrame** – Two-dimensional table.

---

## Commonly Used Functions

| Function        | Purpose                    |
| --------------- | -------------------------- |
| `head()`        | First 5 rows               |
| `tail()`        | Last 5 rows                |
| `info()`        | Dataset information        |
| `describe()`    | Statistical summary        |
| `shape`         | Number of rows and columns |
| `columns`       | Column names               |
| `dtypes`        | Data types                 |
| `isnull()`      | Detect missing values      |
| `dropna()`      | Remove missing values      |
| `fillna()`      | Fill missing values        |
| `groupby()`     | Group data                 |
| `agg()`         | Multiple aggregations      |
| `apply()`       | Apply custom functions     |
| `concat()`      | Combine DataFrames         |
| `merge()`       | Merge DataFrames           |
| `join()`        | Join using indexes         |
| `pivot_table()` | Create summary tables      |
| `read_csv()`    | Read CSV file              |
| `to_csv()`      | Save CSV file              |
| `read_excel()`  | Read Excel file            |
| `to_excel()`    | Save Excel file            |

---

# Pandas Workflow in Machine Learning

```text
CSV / Excel File
        │
        ▼
Read using Pandas
        │
        ▼
Explore Dataset
(head(), info(), describe())
        │
        ▼
Clean Data
(dropna(), fillna())
        │
        ▼
Feature Selection
(loc, iloc, groupby())
        │
        ▼
Convert to NumPy (if required)
        │
        ▼
Train Machine Learning Model
```

---

# Real-Life Applications of Pandas

* Data Cleaning
* Data Analysis
* Machine Learning
* Artificial Intelligence
* Banking
* Healthcare
* Sales and Marketing
* Financial Analysis
* Business Intelligence
* Research

---

# 🎯 Important Viva Questions (Topics 82–86)

### 1. What does CSV stand for?

**Answer:** CSV stands for **Comma-Separated Values**, a text file format used to store tabular data.

---

### 2. Which function is used to read a CSV file?

**Answer:** `pd.read_csv()`

Example:

```python
df = pd.read_csv("students.csv")
```

---

### 3. Which function is used to save a DataFrame as a CSV file?

**Answer:** `to_csv()`

Example:

```python
df.to_csv("students.csv", index=False)
```

---

### 4. Which function is used to read an Excel file?

**Answer:** `pd.read_excel()`

---

### 5. Which function is used to save a DataFrame as an Excel file?

**Answer:** `to_excel()`

---

### 6. Why is `index=False` used while saving files?

**Answer:** It prevents the row index from being written to the file, making the output cleaner.

---

### 7. Which library is required to read and write Excel files in Pandas?

**Answer:** `openpyxl`

Installation:

```bash
pip install openpyxl
```

---

### 8. What is the difference between CSV and Excel?

| CSV          | Excel           |
| ------------ | --------------- |
| Text file    | Spreadsheet     |
| Single sheet | Multiple sheets |
| Smaller size | Larger size     |
| Faster       | Slightly slower |

---

### 9. Why is Pandas important in Data Science?

**Answer:** Pandas helps in loading, cleaning, transforming, analyzing, and preparing data before building Machine Learning models.

---

### 10. Name the two main data structures in Pandas.

**Answer:**

1. **Series**
2. **DataFrame**

---

# ⭐ Top 20 Pandas Interview Questions

1. What is Pandas?
2. What are Series and DataFrame?
3. Difference between `loc` and `iloc`.
4. Difference between `merge()` and `join()`.
5. Difference between `concat()` and `merge()`.
6. What is `groupby()`?
7. What is a Pivot Table?
8. What is `agg()`?
9. What is `apply()`?
10. What is `transform()`?
11. How do you handle missing values?
12. What is `dropna()`?
13. What is `fillna()`?
14. What is `isnull()`?
15. Difference between `head()` and `tail()`.
16. What is `describe()`?
17. What is `info()`?
18. How do you read a CSV file?
19. How do you write an Excel file?
20. Why is Pandas used in Machine Learning?

---

# 📌 Final Revision Tips

For exams, make sure you're comfortable with:

* **Series and DataFrame creation**
* **Indexing (`loc` and `iloc`)**
* **Filtering data**
* **Handling missing values**
* **Grouping and aggregation**
* **`merge()`, `join()`, and `concat()`**
* **Pivot tables**
* **Reading and writing CSV/Excel files**

This completes the **entire Pandas syllabus (Topics 38–86)** with concepts, syntax, examples, and viva preparation.
