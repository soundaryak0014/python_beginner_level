# SUM OF THREE GIVEN INTEGERS. HOWEVER, IF TWO VALUES ARE EQUAL SUM WILL BE ZERO:

# METHOD 1: USING USER INPUTS

n1= int(input("Enter first number1:"))
n2= int(input("Enter second number2:"))
n3= int(input("Enter third number3:"))
if (n1==n2) or (n2==n3) or (n1==n3):
    print ("The sum is: 0")
else:
    print("The sum is:",n1+n2+n3)

# METHOD 2: USING FUNCTION

def sum_three(x,y,z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum=x+y+z
    return sum
print(sum_three(2,1,2))

