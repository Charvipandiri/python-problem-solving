n = int(input())

# Upper half
for i in range(n):
    # Left stars
    for j in range(i + 1):
        print("*", end="")
    # Spaces
    for j in range(2 * (n - i - 1)):
        print(" ", end="")
    # Right stars
    for j in range(i + 1):
        print("*", end="")
    print()


# Lower half
for i in range(n - 2, -1, -1):
    # Left stars
    for j in range(i + 1):
        print("*", end="")
    # Spaces
    for j in range(2 * (n - i - 1)):
        print(" ", end="")
    # Right stars
    for j in range(i + 1):
        print("*", end="")
    print()

