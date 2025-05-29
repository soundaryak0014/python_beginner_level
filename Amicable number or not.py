def check_amicable(a,b):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum=sum+i

    if sum==b:
        print("amicable",sum)
    else:
        print("not amicable",sum)
a=int(input())
b=int(input())
check_amicable(a,b)

