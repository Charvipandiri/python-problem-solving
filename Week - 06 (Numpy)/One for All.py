Question:
Given a numpy array and target value k,Return True if all elements of array satisfy all below given conditions
(i) Multiple of 2 and (ii) Greater than k
Code:
import numpy as np
arr = np.array(list(map(int,input().split())))
k = int(input())
flag = True 
for i in arr:
  if not(i>k and i%2==0):
    flag = False
    break
print(flag)    
