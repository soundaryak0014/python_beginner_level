# Method 1:

num=int(input("Enter the count:"))
b=0
for i in range(num,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b, end=" ")
    print()


# Method 2:

num = int(input("Enter the count:"))
for i in range(1, num + 1):
    for j in range(num - i+1):
        print(i, end=" ")

    print()