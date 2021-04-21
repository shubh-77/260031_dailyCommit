def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0:
            leap = True
        elif year % 400 == 0:
            leap = True
    return leap

#this is the sample input
year = int(input())
#printing function
print(is_leap(year))
