#EVEN OR ODD IN RANGE

n=int(input("Enter the number"))
for i in range(1,n+1):
    if i%2==0:
        print(i,"Even")
    else:
        print(i,"Odd")
