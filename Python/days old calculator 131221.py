from datetime import date

print("Enter when you were born: ")
year = int(input('Year: '))
month = int(input('Month: '))
day = int(input('Day: '))
startdate = date(year, month, day)

print("Enter todays date: ")
year = int(input('Year: '))
month = int(input('Month: '))
day = int(input('Day: '))
enddate = date(year, month, day)
numdays = enddate - startdate

print ("you are" ,numdays, "old")