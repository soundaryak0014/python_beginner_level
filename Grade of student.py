#THE GRADE OF STUDENT:

#METHOD 1: USING FIXED NUMBER OF SUBJECTS

stu_id=int(input("Enter Student ID:"))
stu_name=input("Enter Student Name:")
subject1=int(input("Enter Subject1 mark:"))
subject2=int(input("Enter Subject2 mark:"))
subject3=int(input("Enter Subject3 mark:"))
Total_mark=subject1+subject2+subject3
Average=Total_mark/3
print(format(Average,".2f"))
if Average>=90 and Average<=99:
    print("The Grade is:A+")
elif Average>=80 and Average<=89:
    print("The Grade is:A")
elif Average>=70 and Average<=79:
    print("The Grade is:B+")
elif Average>=60 and Average<=69:
    print("The Grade is:B")
elif Average>=50 and Average<=59:
    print("The Grade is:C+")
else:
    print("The Grade is:E")

#METHOD 2: USING NUMBER OF SUBJECTS

stu_id=int(input("Enter Student ID:"))
stu_name=input("Enter Student Name:")
num=int(input("Enter number of subjects:"))
subjects=[]
for i in range(0,num):
    count_sub=int(input("Enter subject marks:"))
    subjects.append(count_sub)
Average=sum(subjects)/num
print(format(Average,".2f"))
if Average>=90 and Average<=99:
    print("The Grade is:A+")
elif Average>=80 and Average<=89:
    print("The Grade is:A")
elif Average>=70 and Average<=79:
    print("The Grade is:B+")
elif Average>=60 and Average<=69:
    print("The Grade is:B")
elif Average>=50 and Average<=59:
    print("The Grade is:C+")
else:
    print("The Grade is:E")
