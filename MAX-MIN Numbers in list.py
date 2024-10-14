# MAXIMUM - MINIMUM NUMBERS FROM A LIST:

li=[23,4,1,44,0,34,-2,55]
min_li=li[0]
max_li=li[0]
for i in li:
    if i>min_li:
        max_li=i
    else:
        min_li=i
print("The maximum number is:",max_li)
print("The minimum number is:",min_li)