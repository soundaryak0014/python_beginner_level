# Write a Python program to find common divisors between two numbers in a given pair:

# Method 1:

n1= int(input("Enter the number 1:"))
n2= int(input("Enter the number 2:"))
for i in range(2,100):
    if n1%i==0 and n2%i==0:
        break
print("The common divisors is:", i)

# Method 2: # Function to calculate the greatest common divisor (GCD) of two numbers

def ngcd(x, y):
    i = 1
    while(i <= x and i <= y):
        if(x % i == 0 and y % i == 0):
            gcd = i
        i += 1
    return gcd
print("Number of common divisors: ", ngcd(2, 4))
print("Number of common divisors: ", ngcd(2, 8))
print("Number of common divisors: ", ngcd(12, 24))

# Method 3:# Function to calculate the greatest common divisor (GCD) of two numbers

def num_comm_div(x, y):
    n = ngcd(x, y)
    result = 0
    z = int(n ** 0.5)
    i = 1
    while(i <= z):
        if(n % i == 0):
            result += 2
            if(i == n/i):
                result -= 1
        i += 1
    return result
print("Number of common divisors: ", num_comm_div(2, 4))
print("Number of common divisors: ", num_comm_div(2, 8))
print("Number of common divisors: ", num_comm_div(12, 24))
