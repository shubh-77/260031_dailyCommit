# Soln:
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

month,day,year=input().split()
# print(type(month))
month= int(month)
day= int(day)
year= int(year)
result =  calendar.weekday(year,month,day)
# print(result)
if result ==0:
    print("MONDAY")
elif result == 1:
    print("TUESDAY")
elif result == 2:
    print("WEDNESDAY")
elif result == 3:
    print("THURSDAY")
elif result == 4:
    print("FRIDAY")
elif result == 5:
    print("SATURDAY")
else:
    print("SUNDAY")



    





    
