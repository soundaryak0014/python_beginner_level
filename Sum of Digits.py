# SUM OF DIGITS :

# METHOD 1: USING FOR LOOP

n=int(input("Enter the number:"))
n2=str(n)
sum=0
for i in n2:
    sum=sum+int(i)
print("The sum of digits:",sum)

# METHOD 2: USING WHILE LOOP

num=int(input("Enter the number:"))
sum=0
while num>0:
    last_digit=num%10
    sum=sum+last_digit
    num=num//10
print("The sum of digits:",sum)
