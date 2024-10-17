# FUNCTION THAT TAKES A SEQUENCE OF NUMBERS AND DETERMINES WHETHER ALL ARE DIFFERENT FROM EACH OTHER:

# METHOD 1: USING FUNCTION

def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False
print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))

# METHOD 2: WITHOUT USING FUNCTION

data = [1, 5, 7, 9]
if len(data) == len(set(data)):
    print(True)
else:
    print(False)
