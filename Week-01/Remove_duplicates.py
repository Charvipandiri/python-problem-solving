array = [2,3,1,5,1,6,2]
result = []
for i in array:
  if i not in result:
    result.append(i)
print(result)
