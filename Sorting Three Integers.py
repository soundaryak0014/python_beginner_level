# SORTING THREE INTEGERS:

# METHOD 1: SORTING THREE INTEGERS WITHOUT USING CONDITIONAL STATEMENTS AND LOOPS

num1= int(input("Enter number 1:"))
num2= int(input("Enter number 2:"))
num3= int(input("Enter number 3:"))
a1=min(num1,num2,num3)
a3=max(num1,num2,num3)
a2=(num1+num2+num3-a1-a3)
print("Sort the Integers:",a1,a2,a3)

# METHOD 2: USING CONDITIONAL STATEMENTS

a, b, c = input("Enter the values:").split()
a = int (a)
b = int (b)
c = int (c)
if a < b and a < c:
   smallest = a
elif b < a and b < c:
   smallest = b
else:
   smallest = c
if a > b and a < c:
   middle = a
elif a < b and a > c:
   middle = a
elif b > a and b < c:
   middle = b
elif b < a and b > c:
   middle = b
else:
   middle = c
if a > b and a > c:
   largest = a
elif b > a and b > c:
   largest = b
else:
   largest = c
print("Sort the values:",smallest, middle, largest)

