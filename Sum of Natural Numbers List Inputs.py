#SUM OF NATURAL NUMBERS BASED ON LIST INPUTS:

#METHOD 1: SUM OF NATURAL NUMBERS IN FIXED LIST VALUES

list= [1,2,3,4,5]
sum0=0
sum1=0
sum2=0
sum3=0
sum4=0
for i in range(list[0]+1):
    sum0=sum0+i
print(sum0)
for i in range(list[1]+1):
    sum1=sum1+i
print(sum1)
for i in range(list[2]+1):
    sum2=sum2+i
print(sum2)
for i in range(list[3]+1):
    sum3=sum3+i
print(sum3)
for i in range(list[4]+1):
    sum4=sum4+i
print(sum4)

#METHOD 2: SUM OF NATURAL NUMBERS USING NESTED FOR LOOP

list=[1,2,3,4,5]
for i in list:
    sum=0
    for j in range(1,i+1):
        sum=sum+j
    print(i,'=',sum)

#METHOD 3:FINDING SUM OF NATURAL NUMBERS IN A EMPTY LIST

list=[]
while True:
    add=input("Enter a value:")
    if add =='done':
        break
    list.append(add)
for i in list:
    sum=0
    for j in range(1,int(i)+1):
        sum=sum+j
    print(i,'=',sum)

