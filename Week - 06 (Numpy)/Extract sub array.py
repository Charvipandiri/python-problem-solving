Question:
Given a 2d array, write a program to return a subarray such that the subarray consists of the elements from:
1. the second to the fourth row of the original array,
2. the elements in these rows should be from the last three columns of the corresponding rows of the original array,
3. the rows should be in reversed order.
Code:
import numpy as np
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the elements row-wise:")
arr = []
for i in range(rows):
    row = list(map(int, input().split()))
    arr.append(row)

# Convert to NumPy array
arr = np.array(arr)

# 2nd to 4th rows
row_array = arr[1:4]

# Last 3 columns
cols_array = row_array[:, -3:]

# Reverse the rows
result = cols_array[::-1]

print("\nOriginal Array:")
print(arr)

print("\nResult:")
print(result)
