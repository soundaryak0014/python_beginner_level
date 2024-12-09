# *
# * *
# * * *
# * * * *
# * * * * *

#Method 1:

num=int(input("Enter the count:"))
for i in range(num):
    for j in range(i+1):
        print("*",end=" ")
    print()

# Method 2:
n=int(input("Enter the count:"))
for i in range(1,n+1):
    print("* "*i)