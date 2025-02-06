# Program to Display a Specific Month's Calendar
import calendar
# Taking year input from the user
year = int(input('enter the year: '))
month = int(input('enter the month (1-12): '))

#Displaying the calender
print(calendar.month(year, month))