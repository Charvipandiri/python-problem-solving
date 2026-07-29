Question:
Given two 2D arrays, row and column ranges Perform the following operations:
* Find the matrix multiplication of the given two matrices and
* Extract the elements from the output of above step using the given ranges
* If matrix multiplication is not possible, return -1
Code:

import numpy as np
r1 = int(input("Enter rows of Matrix 1: "))
c1 = int(input("Enter columns of Matrix 1: "))
print("Enter the elements of Matrix 1:")
mat1 = np.array([list(map(int, input().split())) for _ in range(r1)])

r2 = int(input("Enter rows of Matrix 2: "))
c2 = int(input("Enter columns of Matrix 2: "))
print("Enter the elements of Matrix 2:")
mat2 = np.array([list(map(int, input().split())) for _ in range(r2)])

row_start, row_end = map(int, input("Enter row range (start end): ").split())
col_start, col_end = map(int, input("Enter column range (start end): ").split())


if c1 != r2:
    print(-1)
else:
    product = np.matmul(mat1, mat2)

    print("\nProduct Matrix:")
    print(product)

    result = product[row_start:row_end, col_start:col_end]

    print("\nRequired Output:")
    print(result)
