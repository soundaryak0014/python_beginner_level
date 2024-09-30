# CHECK FIRST AND LAST NUMBER OF A LIST IS SAME OR NOT:

#METHOD 1: USING FIXED VALUE

value=[10,3,5,3,10]
if value[0]==value[-1]:
    print("The Result is ",True)
else:
    print("The Result is ",False)

#METHOD 2: USING USER INPUT

elements=[]
no_of_elements=int(input("Enter required number of elements:"))
for i in range(no_of_elements):
    value=int(input("Enter value:"))
    elements.append(value)
if elements[0] == elements[-1]:
    print("The Result is ",True)
else:
    print("The Result is ",False)
