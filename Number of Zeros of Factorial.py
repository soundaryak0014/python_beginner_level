#  Find the number of zeros at the end of a factorial of a given positive number:

# Method 1: Sum of total Zero in the Factorial

n=int(input("Enter the Number:"))
fact=1
count=0
for i in range(1,n+1):
    fact=fact*i
print(f"factorial of {n} is {fact}")
for j in str(fact):
    if int(j)==0:
        count=count+1
print(count)

# Method 2: Using Function sum last zero of the given factorial

def factendzero(n):
    x = n // 5
    y = x

    while x > 0:
        x /= 5
        y += int(x)

    return y
print(factendzero(5))
print(factendzero(12))
print(factendzero(100))
