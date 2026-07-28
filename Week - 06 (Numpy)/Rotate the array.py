Question:
Given an array in form of a matrix of size (n, n), rotate the matrix clockwise by 90º.
Code:

import numpy as np
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print(f"Enter {rows * cols} elements separated by space:")
elements = list(map(int, input().split()))
mat = np.array(elements).reshape(rows, cols)
print("\nOriginal Matrix:")
print(mat)
rev = mat.T
rotated_matrix = rev[:, ::-1]
print("\nRotated Matrix (90° Clockwise):")
print(rotated_matrix)
