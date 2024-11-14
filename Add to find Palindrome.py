# Write a  Python program to reverse the digits of a given number and add them to the original.
# find it is a palindrome or not

# Method 1: Using if else statement
number= int(input("Enter the Number:"))
number2=str(number)[::-1]
print("The reversed number:",number2)
sum_numbers=number+int(number2)
reverse_sum=str(sum_numbers)[::-1]
if sum_numbers==reverse_sum:
    print(sum_numbers," is Palindrome")
else:
    print(sum_numbers, " not is Palindrome")

# Method 2:  Function to reverse a number and add it to the original number until a palindrome is obtained
def rev_number(n):
    s = 0
    while True:
        k = str(n)
        if k == k[::-1]:
            break
        else:
            m = int(k[::-1])
            n += m
            s += 1
    return n

# Test cases
print(rev_number(1234))
print(rev_number(1473))