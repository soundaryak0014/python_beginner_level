#REMOVE DUPLICATES IN A LIST:

#METHOD 1: USING EMPTY LIST
dup_list=[1,2,3,2,4,6,5,6,4]
non_dup_list=[]
for i in dup_list:
    if i in non_dup_list:
        continue
    else:
        non_dup_list.append(i)
print(non_dup_list)

#METHOD 2: LIST IS CONVERT AS SET
dup_list=[1,2,3,2,4,6,5,6,4]
non_dup_list=set(dup_list)
print(non_dup_list)