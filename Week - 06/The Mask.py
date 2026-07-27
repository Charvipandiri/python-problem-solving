Question:
Given an array of marks, return the array only containing elements with marks > 40?
Code:
import numpy as np
marks = np.array(list(map(int,input().split())))
mask = marks > 40
filtered_array = marks[mask]
print(filtered_array)
