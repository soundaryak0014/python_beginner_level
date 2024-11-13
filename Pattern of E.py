# PRINT PATTERN 'E' USING FOR LOOP:

# METHOD1:

n = int(input("Enter the number: "))
for i in range(n):
    print("*", end="")
print()
for j in range(n-3):
    print("*")
for k in range(n):
    print("*", end="")
print()
for l in range(n-3):
    print("*")
for m in range(n):
    print("*", end="")
print()

# METHOD 2:

result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (
                row == 3 and column > 1 and column < 5)):
            result_str = result_str + "*"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n"
print(result_str)

'''
*****
*
*
*****
*
*
*****
'''