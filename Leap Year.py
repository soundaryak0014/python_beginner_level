#FIND THE LEAP YEAR

year=int(input("Enter the year:"))
if (year%4==0 or year%400==0) and (year%100!=0):
    print(year,"is Leap Year")
else:
    print(year,"is not Leap Year")