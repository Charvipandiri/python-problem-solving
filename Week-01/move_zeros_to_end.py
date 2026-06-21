array = list(map(int, input().split()))
pos = 0
for i in range(len(array)):
    if array[i] != 0:
        array[pos], array[i] = array[i], array[pos]
        pos += 1
print(array)
