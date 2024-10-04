# CONCATENATE ALL ELEMENTS IN A LIST INTO A STRING:

#METHOD 1: USING FIXED VALUE

list_value=[1,5,55,12]
for i in list_value:
    str_value=str(i)
    print(str_value,end="")
print()

#METHOD 2: USING FUNCTION

def concatenate_list_data(lst):
    result=""
    for element in lst:
        result+=str(element)
    return result
print(concatenate_list_data([1,5,55,12]))