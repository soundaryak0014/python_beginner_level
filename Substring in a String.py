# FIND THE NUMBER OF OCCURRENCES OF A SUBSTRING IN A STRING:

#METHOD 1: BASIC USER INPUTS METHOD

str_x=input("Enter the string:")
sub_str=input("Enter the substring:")
count_str=str_x.count(sub_str)
print(f"{sub_str} is {count_str} times occur")

#METHOD 2: USING FUNCTION

def count_emma(str_x):
    print("Given string:",str_x)
    count=0
    for i in range(len(str_x)-1):
        count+=str_x[i:i+4]=='Emma'
    return count
count=count_emma("Emma is a good developer. Emma is a good writer")
print("Emma appeared",count,'times')

#METHOD 3:USING SPLIT() FUNCTION

str_x=input("Enter the string:")
str_y=str_x.split()
sub_string=input("Enter the substring:")
count=0
for i in str_y:
    if i==sub_string:
        count=count+1
print(f"{sub_string} is {count} times occur ")