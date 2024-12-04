# To check whether a given number is odd or even.

num=abs(int(input("Enter the number:")))
new_num=str(num)
sum=0
for i in new_num:
    sum=sum+int(i)
if sum%2==0:
    print(sum,"is Even")
else:
    print(sum,"is Odd")

