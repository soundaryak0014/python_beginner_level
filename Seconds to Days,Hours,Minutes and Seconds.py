# CONVERTS SECONDS INTO DAYS,HOURS,MINUTES AND SECONDS:

# METHOD 1: IF ELSE ELIF STATEMENT:

Sec= int(input("Enter the seconds:"))
convert_to_other=input("choose the convertion type(Days,Hours,Minutes,Sec):")
if convert_to_other == "Days":
    Days = Sec // (60 * 60 * 24)
    print("The convertion seconds to Days are:",format(Days,".2f"))
elif convert_to_other == "Hours":
    Hours = Sec / (60 * 60)
    print("The convertion seconds to Hours are:",format(Hours,".2f"))
elif convert_to_other == "Minutes":
    Minutes = Sec/ 60
    print("The convertion seconds to Minutes are:",format(Minutes,".2f"))
else:
    print("The convertion seconds to Seconds are:",format(Sec,".2f"))

# METHOD 2:

time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
