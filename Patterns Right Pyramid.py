# RIGHT SIDE PYRAMID PATTERN USING NESTED LOOP:

n=int(input("Enter the Number:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n,1,-1):
    for j in range(i-1):
        print("*",end=" ")
    print()