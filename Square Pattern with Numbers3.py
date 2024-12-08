# 1 0 0 0 0
# 0 2 0 0 0
# 0 0 3 0 0
# 0 0 0 4 0
# 0 0 0 0 5

num=int(input("Enter the count:"))
for i in range(1,num+1):
    n=0
    for j in range(1,num+1):
        if i==j:
            print(i,end=" ")
        else:
            print(n,end=" ")

    print()