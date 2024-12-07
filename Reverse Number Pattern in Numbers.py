# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

num = int(input("Enter the count:"))
for i in range(num, 0, -1):
    for j in range(i):
        print(i, end=" ")

    print()