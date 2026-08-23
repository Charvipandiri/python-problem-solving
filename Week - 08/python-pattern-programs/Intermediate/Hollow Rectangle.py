rows = int(input("enter no.of rows"))
cols = int(input("enter no.of cols"))

for i in range(rows):
  for j in range(cols):
    if i == 0 or i == rows-1 or j == 0 or j == cols-1:
      print("*",end = " ")
    else:
      print(" ", end = " ")
  print()
