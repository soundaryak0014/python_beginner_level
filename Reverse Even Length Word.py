# to reverse all words of even lengths

# Method 1: In a string

str_value=input("Enter the string value:")
print(str_value)
new_str=str_value.split()
for i in new_str:
    if len(i)%2==0:
        print(i[::-1], end=" ")
    else:
        print(i, end=" ")
print()

# Method 2: In a list

str_value=input("Enter the string value:")
new_str=str_value.split()
print(new_str)
list_str=[]
for i in new_str:
    if len(i)%2==0:
        list_str.append(i[::-1])

    else:
        list_str.append(i)

print(" ".join(list_str))
