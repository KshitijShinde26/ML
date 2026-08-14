import numpy as np
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a[1][0:2])
print(a[0:2][1])



# 1D array
a1 = np.array([10, 20, 30, 40, 50])

# 2D array
a2 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

# Fancy indexing for 1D array
print("1D fancy indexing:", a1[[0, 2, 4]])

# Fancy indexing for 2D array
print("2D fancy indexing with row selection:")
print(a2[[0, 2]])

print("2D fancy indexing with element-wise indices:")
print(a2[[0, 2], [1, 2]])



# 1D array
a3 = np.array([10, 20, 30, 40, 50])

# 2D array
a4 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

# Combine fancy indexing with normal indexing
new3 = a3[[0, 2, 4]][1:3]   # fancy indexing + normal slicing
new4 = a4[[0, 2], 1:3]     # fancy indexing rows + normal slicing columns

print("new3:", new3)
print("new4:\n", new4)