# CALCULATE THE SUM OF ALL ITEMS OF A SET AND DICTIONARY:

# METHOD 1: BY SET

set_value = {100,200,300,400,500}
set_sum = 0
for i in set_value:
    set_sum = set_sum+i
print("The sum is:",set_sum)

# METHOD 2: BY DICTIONARY

dict_value= {"a":100,"b":200,"c":300,"d":400,"e":500}
dict_sum=0
for i in dict_value.values():
    dict_sum=dict_sum+i
print("The sum is:",dict_sum)