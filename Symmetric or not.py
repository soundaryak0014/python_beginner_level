#Symmetric or not:

value = input("Enter the value:") # amaama
value2=int(len(value)/2)
print(value2)
f_value=value[value2:]
l_value=value[:value2]
if f_value==l_value:
    print(value,"is symmetric")
else:
    print(value, "is not symmetric")