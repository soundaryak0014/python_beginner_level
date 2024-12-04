# To convert the letters of a given string (same case-upper/lower) into alphabetical order:

str_value=input("Enter the string value:")
con_str_value=sorted(str_value.lower())
new_value=("".join(con_str_value))
print(new_value)