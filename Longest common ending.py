# find the longest common ending between two given strings.

# Method1: While Loop

str1=input("Enter the string1:")
str2=input("Enter the string2:")
i, j = len(str1) - 1, len(str2) - 1
common_ending = ""

while i >= 0 and j >= 0:
    if str1[i] == str2[j]:
        common_ending = str1[i] + common_ending
    else:
        break
    i -= 1
    j -= 1

if common_ending:
    print("Longest common ending:", common_ending)
else:
    print("Longest common ending: Null")


# Method2: Nested Loop

def test(str1, str2):
    for i in range(len(str2)):
        while str2[i:] in str1 and str2[-1] == str1[-1]:
            return str2[i:]
    return ""
str1_1 = "running"
str2_1 = "ruminating"
print("Original strings: " + str1_1 + "  " + str2_1)
print("Common ending between said two strings: " + test(str1_1, str2_1))
