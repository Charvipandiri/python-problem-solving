n = int(input())
for i in range(n):
  for j in range(i,n):
    print(" ",end = " ")
  for j in range(i+1):
    if i == n-1 or j == i or j == 0:
      print("*",end =" ")
    else:
      print(" ", end = " ")
  print()



