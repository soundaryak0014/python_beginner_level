# PALINDROME:

#METHOD 1:
value=int(input("Enter the value:"))
value2=value
rev=0
while value>0:
    digit=value%10          
    rev=rev*10+digit    
    value=value//10             
if value2==rev:
    print(rev, "is PALINDROME")
else:
    print(rev, "is NOT PALINDROME")

#METHOD 2:
value=input("Enter the value:")
value2=value[::-1]
print(value2)
if value==value2:
    print("palindrome")
else:
    print("not palindrome")
