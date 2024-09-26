# FACTORIAL OF GIVEN NUMBER:

#METHOD 1: USING FOR LOOP

num=int(input("Enter the number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("The Factorial is :",fact)

#METHOD 2: USING WHILE LOOP

num=int(input("Enter the number:"))
fact=1
i=1
while i<=num:
    fact=fact*i
    i=i+1
print("The Factorial is :",fact)


