# Method 1:

str_value=input("Enter the string value:")
str_value2=str_value.split()
new_list=" "
for i in str_value2:
    if len(i) > len(new_list):
        new_list=i
print(new_list,len(new_list))

#Method 2:

a = input("Enter the string value:")
b = a.split()
lst = []
for i in b:
    lst.append(len(i))
max_length = max(lst)
for i in b:
    if len(i) == max_length:
        print(i, len(i))
        break