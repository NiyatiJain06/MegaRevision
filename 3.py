year = int(input("Enter a year:"))
if ((year % 4 == 0)and(year % 100 != 0)) or (year % 400 == 0):
    print("Its is leap year:",year)
else:
    print("Its is not a leap year",year)    