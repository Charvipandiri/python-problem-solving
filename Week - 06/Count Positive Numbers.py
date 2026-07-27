Question:
Take space-separated integers as input and count how many positive numbers are present.
Code:
import numpy as np
arr = np.array(list(map(int, input("Enter numbers: ").split())))
print(np.sum(arr > 0))
