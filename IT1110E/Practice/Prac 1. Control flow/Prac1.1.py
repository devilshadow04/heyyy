# Write a program to display the number of days in a month, given the month and the year
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    result = 31
elif month in [4, 6, 9, 11]:
    result = 30
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        result = 29
    else:
        result = 28
print(result)
