n = int(input())

# Upper half
for i in range(n):   
    # Spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Stars
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# Lower half
for i in range(n - 2, -1, -1):
    # Spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Stars
    for j in range(2 * i + 1):
        print("*", end="")
    print()
