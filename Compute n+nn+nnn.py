# INPUT AN INTEGER(n) AND COMPUTES THE VALUE OF n+nn+nnn:

#METHOD 1:

num = int(input("Enter the number: "))
num_times = int(input("Enter number of times: "))
times = []
for i in range(1, num_times + 1):
    term = int(str(num) * i)
    times.append(term)
con_times = sum(times)

print(f"The result of n + nn + nnn is: {con_times}")

#METHOD 2:

num=int(input("Enter the number:"))
n1=int("%s" %num)
n2=int("%s%s" %(num,num))
n3=int("%s%s%s" %(num,num,num))
print(n1+n2+n3)

#METHOD 3:

num = int(input("Enter the Number:"))
count=""
count1=0
for i in range(1,4):
    b=i*str(num)
    count=count+b+"+"
    count1=count1+int(b)
print(count)
print(count1)