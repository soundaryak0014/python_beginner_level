#  To check if a given string contains only lowercase or uppercase

# Method 1:

str_value=input("Enter the string value:")
if str_value in str_value.upper():
    print(True)
elif str_value in str_value.lower():
    print(True)
else:
    print(False)


# METHOD 2:

str_value=input("Enter the string value:")
if str_value.isupper() or str_value.islower():
    print(True)
else:
    print(False)