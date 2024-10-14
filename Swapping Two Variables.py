# SWAPPING TWO VARIABLES:

# METHOD 1: USING THIRD VALUE

a=int(input("Enter a value:")) #10
b=int(input("Enter b value:")) #20
c=0
print("Before swapping:",a,b)
c=a  #c=10
a=b  #a=20
b=c  #b=10
print("After swapping:",a,b)

# METHOD 2: WITHOUT THIRD VALUE

a=int(input("Enter a value:")) #10
b=int(input("Enter b value:")) #20
print("Before swapping:",a,b)
a,b=b,a
print("After swapping:",a,b)



