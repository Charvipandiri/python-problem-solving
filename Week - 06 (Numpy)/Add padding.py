Question:
Given a NumPy array of shape (n,m). Add padding of a layer of 0’s on all 4 boundaries of the matrix.
Code:
import numpy as np
arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print("Original Matrix:\n")
print(arr)
padded_arr = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
print("\nPadded Matrix:\n")
print(padded_arr)
