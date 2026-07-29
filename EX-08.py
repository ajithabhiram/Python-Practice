#Inverted Triangle (Stars)
for i in range(4, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()

#Floyd's Triangle (Numbers)
x = 1
for i in range(1, 5):
    for j in range(i):
        print(x, end=' ')
        x = x + 1
    print()

#Floyd's Triangle (Alphabets)
x = 65
for i in range(1, 5):
    for j in range(i):
        print(chr(x), end=' ')
        x = x + 1
    print()

