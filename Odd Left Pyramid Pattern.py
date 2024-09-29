# ODD LEFT PYRAMID PATTERN:

#METHOD 1:
num=int(input("Enter the number:"))
for i in range(1,num+1,2):
    for j in range(1,i+1):
        print("*",end='')
    print()

# METHOD 2: USING IF ELSE STATEMENT
num=int(input("Enter the number:"))
for i in range(1,num+1):
    if i%2==0:
        continue
    else:
        for j in range(1,i+1):
            print("*",end='')
        print()

