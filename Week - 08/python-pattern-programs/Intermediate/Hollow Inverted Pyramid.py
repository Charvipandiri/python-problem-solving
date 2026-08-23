n = int(input())
for i in range(n):
  for j in range(i+1):
    print(" ",end = " ")
  for j in range(2*(n-i)-1):
    if j == 0 or i == 0 or j == 2*(n-i)-2:
      print("*", end = " ")
    else:
      print(" ", end = " ")  
  
  print()
