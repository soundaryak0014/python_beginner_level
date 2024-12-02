# To identify non-prime numbers between 1 and 100 (integers). Print the non-prime numbers.

#Method 2:

for i in range(1, 101):
    is_nonprime = False
    for j in range(2, i):
        if i % j == 0:
            is_nonprime = True
            break
    if is_nonprime:
        print(i, end=", ")


# Method 1:

print("\n")
for i in range(1,101):
    a=0
    for j in range(2,i):
        if i%j==0:
            a=a+i
    if a>0:
        print(i,end=", ")