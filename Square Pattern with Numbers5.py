# 1 0 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0
# 0 0 0 0 1

num=int(input("Enter the count:"))
n = int(input("Enter diagonal Value:"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==j:
            print(n,end=" ")
        else:
            print("0",end=" ")

    print()