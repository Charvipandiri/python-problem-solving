array = list(map(int, input().split()))
result = []
for num in array:
    if num != 0:
        result.append(num)
zero_count = len(array) - len(result)
for i in range(zero_count):
    result.append(0)

print(result)
