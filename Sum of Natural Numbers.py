# SUM OF NATURAL NUMBERS:

#METHOD 1: USING FOR LOOP

value=int(input("Enter the Value:"))
sum=0
for i in range(1,value+1):
    sum=sum+i
    i = i + 1
print(f"The sum is {sum}")

# METHOD 2: USING WHILE LOOP

value=int(input("Enter the Value:"))
sum=0
i=1
while i<=value:
    sum=sum+i
    i=i+1
print(f"THe sum is {sum}")

