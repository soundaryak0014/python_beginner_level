# GENERATE A LIST AND TUPLE WITH COMMA- SEPARATED NUMBERS:

#METHOD 1:

numbers=int(input("Enter the range of value:"))
values=[]
for i in range(numbers):
    value=int(input("Enter the Number:"))
    values.append(value)
print("List:",values)
con_tuple=tuple(values)
print("Tuple:",con_tuple)

#METHOD 2:

values = input("Input some comma- seperated numbers:")
con_list=values.split(",")
con_tuple=tuple(con_list)
print("List:",con_list)
print("Tuple:",con_tuple)

