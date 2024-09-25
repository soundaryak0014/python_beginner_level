#VOWELS OR NOT

#METHOD 1: Charater is vowel or not

character=input("enter the character:")
vowels="AEIOUaeiou"
if character in vowels:
    print("The value is vowels")
else:
    print("The value is not vowels")



#METHOD 2:Word is vowel or not

word=input("enter the word:")
vowels="AEIOUaeiou"
for i in word:
    if i in vowels:
        print(i,"is vowel")
    else:
        print(i,"is not vowel")
print("program is end")

#METHOD 3:

character=input("enter the character:")
if(character=='a' or character=='e' or character=='i' or character=='o' or character=='u'):
    print(character, "is vowels")

elif(character=='A' or character=='E' or character=='I' or character=='O' or character=='U'):
    print(character, "is vowels")
else:
    print(character, "is not vowels")





