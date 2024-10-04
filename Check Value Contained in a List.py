# CHECK WHETHER A SPECIFIED VALUE IS CONTAINED IN A GROUP OF VALUES:

#METHOD 1: USING FIXED VALUE

list_value=[3,4,5,6]
specific_value=int(input("Enter specific value contained in a list:"))
if specific_value in list_value:
    print(True)
else:
    print(False)

#METHOD 2: USING USER INPUTS

n=int(input("Enter the range:"))
list_value=[]
specific_value=int(input("Enter specific value contained in a list:"))
for i in range(n):
    values=int(input("Enter the list values:"))
    list_value.append(values)
if specific_value in list_value:
    print(True)
else:
    print(False)

#METHOD 3: USING FUNCTION

def is_group_member(group_data,n):
    for value in group_data:
        if n==value:
            return True
    return False
print(is_group_member([1,2,3,4,5,7],3))
print(is_group_member([1,2,3,4,5,7],-1))



