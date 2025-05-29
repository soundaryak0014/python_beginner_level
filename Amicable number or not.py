def check_amicable(a,b):
    sum1=0
    sum2=0
    for i in range(1,a):
        if a%i==0:
            sum1=sum1+i
    for j in range(1,a):
        if b%j==0:
            sum2=sum2+j
    if sum1==b and sum2==a:
        print("amicable",sum1,sum2)
    else:
        print("not amicable",sum1,sum2)
a=int(input())
b=int(input())
check_amicable(a,b)

