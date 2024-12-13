#Assignment #1
size = int(input("Enter the size of the pattern: "))

for i in range(1, size + 1):
    print("*" * i)

print("\n")
#Assignment #2

for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n")

#Assignment #3
for i in range(size, 0, -1):
    for j in range(1, i + 1):
        print(chr(j+64), end=" ")
    print()
