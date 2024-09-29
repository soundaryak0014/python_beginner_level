#ANAGRAM FOR STRING AND INTEGER:

#METHOD 1: USING STRING

first_value=input("Enter the first input value:")
second_value=input("Enter the second input value:")
str1=sorted(first_value)
str2=sorted(second_value)
print("First word=",str1)
print("Second word=",str2)
if str1==str2:
    print("It is Anagram")
else:
    print("It is not Anagram")

#METHOD 2: USING INTEGERS

first_value=int(input("Enter the first input value:"))
second_value=int(input("Enter the second input value:"))
num1=sorted(str(first_value))
num2=sorted(str(second_value))
print("First word=",num1)
print("Second word=",num2)
if num1==num2:
    print("It is Anagram")
else:
    print("It is not Anagram")