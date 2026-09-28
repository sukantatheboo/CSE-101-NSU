import numpy as np
# Creating a 1D array (like a standard list)
my_list = [1, 2, 3, 4]
array_1d = np.array(my_list)
print(array_1d) 
# Output: [1 2 3 4]

# Creating a 2D array (like a matrix or a spreadsheet with rows and columns)
matrix = [[1, 2, 3], [4, 5, 6]]
array_2d = np.array(matrix)
print(array_2d)
# Output:
# [[1 2 3]
#  [4 5 6]]


# Array of five zeros
zeros = np.zeros(5)        # [0. 0. 0. 0. 0.]

# 2x3 matrix of ones
ones = np.ones((2, 3))     # [[1. 1. 1.]
                           #  [1. 1. 1.]]

# A range of numbers (start, stop, step)
range_arr = np.arange(0, 10, 2) # [0 2 4 6 8]

# Evenly spaced numbers over a specified interval
spaced = np.linspace(0, 1, 5)   # [0.   0.25 0.5  0.75 1.  ]


my_array = np.array([[1, 2, 3], [4, 5, 6]])

# What are the dimensions? (2D, 3D, etc.)
print(my_array.ndim)   # Output: 2

# What is the shape? (Rows, Columns)
print(my_array.shape)  # Output: (2, 3)

# How many total items are inside?
print(my_array.size)   # Output: 6



arr = np.array([1, 2, 3, 4])

# Basic math applies to everything in the array instantly
print(arr + 10)  # [11 12 13 14]
print(arr * 2)   # [2 4 6 8]

# You can also do math between two arrays of the same shape
arr2 = np.array([10, 10, 10, 10])
print(arr + arr2) # [11 12 13 14]