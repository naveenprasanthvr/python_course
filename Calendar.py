import calendar
y =  int(input("Enter the Year:"))
m = 1
print("\n******CALENDER******")
Cal = calendar.TextCalendar(calendar.SUNDAY)
i = 1
while i<=12:
    Cal.prmonth(y,i)
    i+=1