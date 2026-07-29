Question:
Given an MxN 2D array (M >= 4),Split the array column wise such that,
-> 1st sub array contains the first 2 columns
-> 2nd sub array contains the 3rd column
-> 3rd sub array contains the rest of the columns
code:
import numpy as np
m, n = map(int, input("Enter number of rows and columns: ").split())
print("Enter the matrix elements row by row:")
arr = []
for i in range(m):
    row = list(map(int, input().split()))
    arr.append(row)
arr = np.array(arr)

print("\nOriginal Matrix:")
print(arr)
result = np.split(arr, [2, 3], axis=1)

print("\nSplit Arrays:")
for i, sub_array in enumerate(result, start=1):
    print(f"\nSub Array {i}:")
    print(sub_array)
