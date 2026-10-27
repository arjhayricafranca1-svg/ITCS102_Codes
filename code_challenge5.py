for x in range(5):
    for y in range(5):
        if x + y == 5-1 or x == y:
            print(x, end="")
        else:
            print(" ", end="")
    print()

for x in range(5):
    for y in range(5):
        if x + y == 4 or x == y:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n = int(input("Input size of x "))
for x in range(n):
    for y in range(n):
        if x + y == n-1 or x == y:
            print("*", end="")
        else:
            print(" ", end="")
    print()

    