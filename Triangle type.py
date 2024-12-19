# Triangle type using input value:

# Method 1:

x=int(input("Enter the first side:"))
y=int(input("Enter the second side:"))
z=int(input("Enter the third side:"))
if x==y and y==z:
    print("The Triangle :Equilateral")
elif x!=y and y!=z and x!=z:
    print("The Triangle :Scalene")
else:
    print("The Triangle :Isosceles")


# Method 2:
def triangle_type(a,b,c):
    if x == y and y == z:
        print("The Triangle :Equilateral")
    elif x != y and y != z and x != z:
        print("The Triangle :Scalene")
    else:
        print("The Triangle :Isosceles")
x=int(input("Enter the first side:"))
y=int(input("Enter the second side:"))
z=int(input("Enter the third side:"))
triangle_type(x,y,z)