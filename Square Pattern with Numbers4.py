# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5

num = int(input("Enter the count:"))
for i in range(1, num + 1):
    for j in range(1, num + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()