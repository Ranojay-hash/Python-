# Hollow Diamond Pattern

n = int(input("Enter the number of rows (half of diamond): "))

# Upper Half
for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")

    # Print stars
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower Half
for i in range(n - 2, -1, -1):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")

    # Print stars
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()