# STRONG NUMBERS USING NESTED LOOP:

n = int(input("enter the number:"))
n2 = n
sum = 0

while (n > 0):
    digit = n % 10
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i
    sum = sum + fact
    n = n // 10
print(sum)
if (sum == n2):
    print("It is strong number")
else:
    print("It is not strong number")
