# TO FILTER POSITIVE NUMBERS FROM A LIST:

li= [1,0,-2,34,-566,3,54,0]
filtered_li=[]
print("Before filtering the numbers are:",li)
for i in li:
    if i>0:
        filtered_li.append(i)
print("After the filtering the positive numbers are:",filtered_li)
