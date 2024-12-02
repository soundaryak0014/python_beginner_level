# To check whether the average value of the elements of a given array of numbers is a whole number or not.

l=[1,3,5,7,9]
sum=0

for i in l:
    sum=sum+i
average=(sum/len(l))
print(sum)
print(average)
if average in l:
    print(True)
else:
    print(False)


