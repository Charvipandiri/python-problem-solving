Question:
Given an 1D array and an integer k that specifies the number of equal parts to split the array into,Perform the following operations:
Split the array into k number of equal parts.Return the list of split arrays.
code:
import numpy as np
arr = np.array(list(map(int, input("Enter array elements: ").split())))
k = int(input("Enter the value of k: "))
result = np.split(arr, k)
print("\nSplit Arrays:")
for i, sub_array in enumerate(result, start=1):
    print(f"Part {i}: {sub_array}")
