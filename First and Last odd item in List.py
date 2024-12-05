# Find the first and Last odd item in the list

num=[2,4,6,3,79,10,4,67,68,70]
num2=[]
for i in num:
    if i%2!=0:
        num2.append(i)


print("the first number is :",num2[0])
print("the last number is:",num2[-1])
