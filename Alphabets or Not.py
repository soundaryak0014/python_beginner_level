#ALPHABETS OR NOT

letter = input("Enter the letter:")
if(letter>='a' and letter<='z') or (letter>='A' and letter<='Z'):
    print(f"{letter} is alphabet")

else:
    print(f"{letter} is not alphabet")
