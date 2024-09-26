# FACTORIAL OF GIVEN NUMBER

num=int(input("Enter the number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
    i=i+1
print("The Factorial is :",fact)
