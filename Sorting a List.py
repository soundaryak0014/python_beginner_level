# SORTING A LIST:

# METHOD 1: USING IF CONDITIONS AND LOOPS

num = [12,9,15,2, 4, 5, 3, 7, 6, 8, 10,1]
sorted_num = []
for i in num:
    inserted = False
    for j in range(len(sorted_num)):
        if i < sorted_num[j]:
            sorted_num.insert(j, i)
            inserted = True
            break
    if not inserted:
        sorted_num.append(i)
print(sorted_num)

# METHOD 2: USING NESTED FOR LOOP

num = [12,9,15,2, 4, 5, 3, 7, 6, 8, 10,1]
for i in range(len(num)):
    min_index = i
    for j in range(i + 1, len(num)):
        if num[j] < num[min_index]:
            min_index = j
    num[i], num[min_index] = num[min_index], num[i]
print(num)


