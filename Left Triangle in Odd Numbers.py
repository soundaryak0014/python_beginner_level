# 1
# 3 3
# 5 5 5 
# 7 7 7 7
# 9 9 9 9 9

num=int(input("Enter the count:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print((i*2-1),end=" ")
    print()