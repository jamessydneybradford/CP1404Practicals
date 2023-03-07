for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number = int(input("Enter a number:"))
for i in range(1, number+1, 1):
    for j in range(1, i+1, 1):
        print("*", end="")
    print()
