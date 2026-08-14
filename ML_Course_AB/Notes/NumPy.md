# 6. Introduction to NumPy Library

## Definition

**NumPy (Numerical Python)** is a Python library used for performing numerical computations efficiently. It provides support for **multi-dimensional arrays**, **mathematical operations**, **linear algebra**, and **statistical functions**.

## Why NumPy?

* Faster than Python lists
* Less memory usage
* Easy mathematical calculations
* Used in AI, ML, Data Science, Deep Learning

## Installation

```python
pip install numpy
```

## Import

```python
import numpy as np
```

## Example

```python
import numpy as np

arr = np.array([10,20,30])
print(arr)
```

**Output**

```
[10 20 30]
```

### Applications

* Machine Learning
* Deep Learning
* Image Processing
* Data Analysis
* Scientific Computing

⭐ **Exam Point:** NumPy stands for **Numerical Python**.

---

# 7. The Power of NumPy

## Advantages

* Faster execution
* Vectorized operations
* Supports N-dimensional arrays
* Memory efficient
* Built-in mathematical functions
* Easy reshaping and indexing

### Python List vs NumPy

| Python List             | NumPy Array             |
| ----------------------- | ----------------------- |
| Slow                    | Fast                    |
| More memory             | Less memory             |
| Limited math operations | Powerful math functions |
| No vectorization        | Vectorization supported |

Example

```python
import numpy as np

a=np.array([1,2,3])
print(a+5)
```

Output

```
[6 7 8]
```

---

# 8. Creating NumPy Array using array()

## Syntax

```python
np.array(object)
```

Example

```python
import numpy as np

a=np.array([10,20,30,40])
print(a)
```

2D Array

```python
a=np.array([[1,2],[3,4]])
print(a)
```

---

# 9. Creating Array using zeros()

Creates an array filled with **0**.

Syntax

```python
np.zeros(shape)
```

Example

```python
np.zeros(5)
```

Output

```
[0. 0. 0. 0. 0.]
```

2D

```python
np.zeros((2,3))
```

Output

```
[[0. 0. 0.]
 [0. 0. 0.]]
```

---

# 10. Creating Array using ones()

Creates array filled with **1**.

```python
np.ones(4)
```

Output

```
[1. 1. 1. 1.]
```

2D

```python
np.ones((3,2))
```

---

# 11. Creating Array using full()

Creates an array filled with a specified value.

Syntax

```python
np.full(shape,value)
```

Example

```python
np.full((2,3),7)
```

Output

```
[[7 7 7]
 [7 7 7]]
```

---

# 12. Creating Array using arange()

Creates evenly spaced numbers.

Syntax

```python
np.arange(start,stop,step)
```

Example

```python
np.arange(1,10,2)
```

Output

```
[1 3 5 7 9]
```

---

# 13. Creating Array using eye()

Creates an Identity Matrix.

Syntax

```python
np.eye(n)
```

Example

```python
np.eye(3)
```

Output

```
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

---

# 14. Creating Array using linspace()

Creates equally spaced numbers.

Syntax

```python
np.linspace(start,stop,num)
```

Example

```python
np.linspace(0,10,5)
```

Output

```
[0. 2.5 5. 7.5 10.]
```

---

# 15. Creating Array using random()

Generate random numbers.

Example

```python
np.random.random(5)
```

Random Integers

```python
np.random.randint(1,10,5)
```

Output Example

```
[3 8 1 5 6]
```

---

# 16. Properties of NumPy Array

| Property | Meaning                    |
| -------- | -------------------------- |
| shape    | Number of rows and columns |
| size     | Total elements             |
| ndim     | Number of dimensions       |
| dtype    | Data type                  |
| itemsize | Size of one element        |
| nbytes   | Total memory               |

Example

```python
a=np.array([[1,2],[3,4]])

print(a.shape)
print(a.size)
print(a.ndim)
print(a.dtype)
```

---

# 17. Largest Element

```python
np.max(a)
```

or

```python
a.max()
```

Example

```python
a=np.array([5,8,2,10])

print(np.max(a))
```

Output

```
10
```

---

# 18. Least Element

```python
np.min(a)
```

Index of minimum

```python
np.argmin(a)
```

Example

```python
a=np.array([12,4,7,20])

print(np.min(a))
print(np.argmin(a))
```

Output

```
4
1
```

---

# 19. Reshape()

Changes array dimensions.

Syntax

```python
reshape(rows,columns)
```

Example

```python
a=np.arange(6)

a.reshape(2,3)
```

Output

```
[[0 1 2]
 [3 4 5]]
```

---

# 20. Concatenate()

Joins arrays.

```python
np.concatenate((a,b))
```

Example

```python
a=np.array([1,2])

b=np.array([3,4])

np.concatenate((a,b))
```

Output

```
[1 2 3 4]
```

---

# 21. Split One-Dimensional Array

```python
np.split(a,2)
```

Example

```python
a=np.array([1,2,3,4])

np.split(a,2)
```

Output

```
[array([1,2]), array([3,4])]
```

---

# 22. Split Two-Dimensional Array

```python
np.vsplit()
```

Vertical split

```python
np.hsplit()
```

Horizontal split

Example

```python
a=np.arange(16).reshape(4,4)

np.vsplit(a,2)
```

---

# 23. Sort()

```python
np.sort(a)
```

Example

```python
a=np.array([8,2,7,4])

np.sort(a)
```

Output

```
[2 4 7 8]
```

---

# 24. Indexing

Example

```python
a=np.array([10,20,30,40])

print(a[2])
```

Output

```
30
```

2D

```python
a[1][0]
```

---

# 25. Slicing 1D Array

Syntax

```python
a[start:stop:step]
```

Example

```python
a[1:4]
```

Output

```
[20 30 40]
```

---

# 26. Slicing 2D Array

Example

```python
a[:,1]
```

Second column

```python
a[1,:]
```

Second row

---

# 27. Assigning Values to 1D Array

```python
a[2]=100
```

Example

```
Before

[1 2 3 4]

After

[1 2 100 4]
```

---

# 28. Assigning Values to 2D Array

```python
a[1][1]=50
```

Output

```
[[1 2]
 [3 50]]
```

---

# 29. Fancy Indexing (1D)

Selecting multiple elements.

```python
a[[0,2,4]]
```

Example

```
[10 30 50]
```

---

# 30. Fancy Indexing (2D)

```python
a[[0,2],[1,0]]
```

Output

```
[2 7]
```

---

# 31. Combining Fancy Index with Normal Indexing

Example

```python
a[[0,2],1]
```

Output

```
[2 8]
```

---

# 32. Combining Fancy Index with Slicing

Example

```python
a[1:3,[0,2]]
```

---

# 33. Comparison Operators

Example

```python
a>5
```

Output

```
[False False True True]
```

Other Operators

* >
* <
* > =
* <=
* ==
* !=

Filtering

```python
a[a>5]
```

---

# 34. Arithmetic Operations

Example

```python
a+b
```

```python
a-b
```

```python
a*b
```

```python
a/b
```

Example

```python
a=np.array([1,2,3])

b=np.array([4,5,6])

print(a+b)
```

Output

```
[5 7 9]
```

---

# 35. Statistical Operations

| Function    | Work               |
| ----------- | ------------------ |
| np.mean()   | Average            |
| np.median() | Median             |
| np.std()    | Standard Deviation |
| np.var()    | Variance           |
| np.sum()    | Sum                |

Example

```python
a=np.array([10,20,30])

print(np.mean(a))
print(np.sum(a))
```

Output

```
20

60
```

---

# 36. Solving Second-Degree Equations with NumPy

Quadratic Equation

[
ax^2+bx+c=0
]

Using NumPy

```python
import numpy as np

coeff=[1,-5,6]

roots=np.roots(coeff)

print(roots)
```

Output

```
[3. 2.]
```

---

# Viva Questions

1. What is NumPy?
2. Why is NumPy faster than Python lists?
3. Difference between array() and arange()?
4. Difference between zeros() and ones()?
5. What is reshape()?
6. Difference between split() and concatenate()?
7. What is fancy indexing?
8. Difference between indexing and slicing?
9. Explain ndarray.
10. What is an identity matrix?
11. Difference between mean() and median()?
12. What is the use of `np.random`?
13. Explain `linspace()`.
14. Explain `argmin()` and `argmax()`.
15. How do you solve a quadratic equation using NumPy?

---

# Quick Revision (2 Minutes Before Exam)

* **NumPy** = Numerical Python library for fast numerical computation.
* **array()** → Create an array from a list or tuple.
* **zeros()** → Array of all 0s.
* **ones()** → Array of all 1s.
* **full()** → Array filled with a specified value.
* **arange()** → Evenly spaced values with a step size.
* **eye()** → Identity matrix.
* **linspace()** → Fixed number of evenly spaced values.
* **random() / randint()** → Generate random numbers.
* **shape** → Rows and columns.
* **size** → Total elements.
* **ndim** → Number of dimensions.
* **dtype** → Data type of elements.
* **reshape()** → Change array dimensions without changing data.
* **concatenate()** → Join arrays.
* **split() / hsplit() / vsplit()** → Divide arrays.
* **sort()** → Arrange elements in ascending order.
* **Indexing** → Access a single element.
* **Slicing** → Access a range of elements.
* **Fancy Indexing** → Select multiple elements using index arrays.
* **Comparison Operators** → Filter elements based on conditions.
* **Arithmetic Operations** → `+`, `-`, `*`, `/` performed element-wise.
* **Statistical Functions** → `mean()`, `median()`, `sum()`, `std()`, `var()`.
* **Quadratic Equation** → Solve using `np.roots([a, b, c])`.

# **NumPy Viva Questions with Answers **

---

# 1. What is NumPy?

**Answer:**
NumPy (Numerical Python) is an open-source Python library used for performing fast numerical and mathematical computations. It provides support for multi-dimensional arrays, matrices, and various mathematical functions.

---

# 2. Why is NumPy faster than Python lists?

**Answer:**
NumPy is faster because:

* It stores data in continuous memory locations.
* It uses optimized C language implementation internally.
* It supports vectorized operations, eliminating the need for loops.
* It consumes less memory than Python lists.

---

# 3. What is an ndarray?

**Answer:**
An **ndarray (N-dimensional array)** is the main data structure of NumPy. It stores elements of the same data type in one or more dimensions.

**Example:**

```python
import numpy as np
a = np.array([1,2,3])
```

---

# 4. What is the difference between Python List and NumPy Array?

| Python List                     | NumPy Array                    |
| ------------------------------- | ------------------------------ |
| Slower                          | Faster                         |
| Uses more memory                | Uses less memory               |
| Stores different data types     | Stores same data type          |
| Limited mathematical operations | Supports vectorized operations |

---

# 5. What is the purpose of `np.array()`?

**Answer:**
The `np.array()` function is used to create a NumPy array from a Python list, tuple, or other iterable.

**Example**

```python
np.array([10,20,30])
```

---

# 6. What is the difference between `zeros()` and `ones()`?

**Answer:**

* `zeros()` creates an array filled with **0**.
* `ones()` creates an array filled with **1**.

**Example**

```python
np.zeros(3)
```

Output

```python
[0. 0. 0.]
```

```python
np.ones(3)
```

Output

```python
[1. 1. 1.]
```

---

# 7. What is `full()`?

**Answer:**
`full()` creates an array where every element has the same specified value.

**Example**

```python
np.full((2,2),5)
```

Output

```python
[[5 5]
 [5 5]]
```

---

# 8. What is the use of `arange()`?

**Answer:**
`arange()` creates an array of evenly spaced values within a given range using a specified step size.

**Example**

```python
np.arange(1,10,2)
```

Output

```python
[1 3 5 7 9]
```

---

# 9. What is the difference between `arange()` and `linspace()`?

| arange()                    | linspace()             |
| --------------------------- | ---------------------- |
| Uses step size              | Uses number of values  |
| Stop value usually excluded | Stop value included    |
| Interval based              | Number of points based |

Example

```python
np.arange(0,10,2)
```

```python
np.linspace(0,10,5)
```

---

# 10. What is an Identity Matrix?

**Answer:**
An identity matrix is a square matrix in which all diagonal elements are **1** and all other elements are **0**.

It is created using:

```python
np.eye(3)
```

---

# 11. What is the use of `np.random`?

**Answer:**
It is used to generate random numbers for simulations, machine learning, testing, and data analysis.

Example

```python
np.random.randint(1,10,5)
```

---

# 12. What are the properties of a NumPy array?

**Answer:**

* **shape** → Number of rows and columns
* **size** → Total number of elements
* **ndim** → Number of dimensions
* **dtype** → Data type
* **itemsize** → Memory occupied by one element
* **nbytes** → Total memory occupied

---

# 13. What is `reshape()`?

**Answer:**
`reshape()` changes the dimensions (shape) of an array without changing its data.

Example

```python
a=np.arange(6)
a.reshape(2,3)
```

Output

```python
[[0 1 2]
 [3 4 5]]
```

---

# 14. What is `concatenate()`?

**Answer:**
`concatenate()` joins two or more arrays into a single array.

Example

```python
np.concatenate((a,b))
```

---

# 15. What is the difference between `split()` and `concatenate()`?

| split()                  | concatenate()      |
| ------------------------ | ------------------ |
| Divides an array         | Joins arrays       |
| Produces multiple arrays | Produces one array |

---

# 16. What is indexing?

**Answer:**
Indexing is used to access a **single element** of an array using its position.

Example

```python
a[2]
```

---

# 17. What is slicing?

**Answer:**
Slicing is used to access a **range of elements** from an array.

Example

```python
a[1:4]
```

---

# 18. What is Fancy Indexing?

**Answer:**
Fancy indexing is a method of selecting multiple elements from an array using a list or array of indices.

Example

```python
a[[0,2,4]]
```

---

# 19. What is the difference between Indexing and Slicing?

| Indexing               | Slicing                    |
| ---------------------- | -------------------------- |
| Accesses one element   | Accesses multiple elements |
| Returns a single value | Returns a new array        |

---

# 20. What is `np.sort()`?

**Answer:**
`np.sort()` arranges array elements in ascending order.

Example

```python
np.sort(a)
```

---

# 21. How do you find the maximum element?

**Answer:**

Using

```python
np.max(a)
```

or

```python
a.max()
```

---

# 22. How do you find the minimum element?

**Answer:**

Using

```python
np.min(a)
```

---

# 23. What is `argmin()`?

**Answer:**
`argmin()` returns the **index (position)** of the smallest element in the array.

Example

```python
a=np.array([5,2,8])

np.argmin(a)
```

Output

```python
1
```

---

# 24. What is `argmax()`?

**Answer:**
`argmax()` returns the **index (position)** of the largest element.

Example

```python
np.argmax(a)
```

---

# 25. What are Arithmetic Operations in NumPy?

**Answer:**
NumPy performs element-wise arithmetic operations.

They include:

* Addition (+)
* Subtraction (-)
* Multiplication (*)
* Division (/)
* Modulus (%)
* Power (**)

---

# 26. What are Comparison Operators?

**Answer:**
Comparison operators compare array elements and return Boolean values (`True` or `False`).

Operators include:

* >
* <
* > =
* <=
* ==
* !=

---

# 27. What are Statistical Functions in NumPy?

**Answer:**

Some commonly used statistical functions are:

* `mean()` → Average
* `median()` → Middle value
* `sum()` → Total
* `std()` → Standard deviation
* `var()` → Variance
* `min()` → Smallest value
* `max()` → Largest value

---

# 28. What is vectorization?

**Answer:**
Vectorization means performing operations on the entire array at once without using loops. It makes NumPy code faster and more efficient.

Example

```python
a=np.array([1,2,3])

a+5
```

Output

```python
[6 7 8]
```

---

# 29. Why is NumPy important in Machine Learning?

**Answer:**
NumPy is important because it:

* Stores datasets efficiently.
* Performs fast mathematical computations.
* Supports matrix and vector operations.
* Is used by libraries like **Pandas**, **Scikit-learn**, **TensorFlow**, and **PyTorch**.

---

# 30. How do you solve a quadratic equation using NumPy?

**Answer:**
The `np.roots()` function is used to find the roots of a quadratic equation.

Example

```python
import numpy as np

coeff=[1,-5,6]

print(np.roots(coeff))
```

Output

```python
[3. 2.]
```

This gives the roots of the equation:

[
x^2-5x+6=0
]

---

# ⭐ Most Frequently Asked Viva Questions

1. What is NumPy?
2. Why is NumPy faster than Python?
3. What is an `ndarray`?
4. Difference between `arange()` and `linspace()`.
5. Difference between indexing and slicing.
6. Difference between `split()` and `concatenate()`.
7. What is `reshape()`?
8. Explain `argmax()` and `argmin()`.
9. Explain vectorization.
10. Why is NumPy used in Machine Learning?


