r = int(input("Enter number of rows: "))
print("\nPattern 4")
# Upper Part
for a in range(1, r + 1):
    for b in range(r - a):
        print(" ", end="")
    for c in range(a):
        print("*", end=" ")
    print()
# Lower Part
for a in range(r - 1, 0, -1):
    for b in range(r - a):
        print(" ", end="")
    for c in range(a):
        print("*", end=" ")
    print()
