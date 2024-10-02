# FIND MULTIPLICATION TABLE:

#METHOD 1:USING FOR LOOP

num=int(input("Enter the Table number:"))
end_num=int(input("Enter the range:"))
for i in range(1,end_num+1):
    print(i,'x',num,'=',i*num)

#METHOD 2:USING WHILE LOOP

num=int(input("Enter the Table number:"))
end_num=int(input("Enter the range:"))
i=1
while i<=end_num:
    print(i,'x',num,'=',i*num)
    i=i+1

