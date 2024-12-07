# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

num=int(input("Enter the count:"))
for i in range(num+1,0,-1):
    for j in range(i-1,0,-1):
        print(j, end=" ")
    print()