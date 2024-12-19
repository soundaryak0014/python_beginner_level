# Count Character in Dictionary

string_value=input("Enter the String value:")
dict_value={}
for i in string_value:
    if i in dict_value:
        dict_value[i]+=1
    else:
        dict_value[i]=1
print(dict_value)