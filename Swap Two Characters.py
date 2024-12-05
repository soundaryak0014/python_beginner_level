# To get a single string from two given strings, separated by a space and swap the first two characters of each string.

str1=input("Enter the String value1:")
str2=input("Enter the string value2:")
print(str1,str2)
new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]
print(new_str1,new_str2)