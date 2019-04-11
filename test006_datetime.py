# importing date and time to script & assigning it ot variable a

import datetime
Date = datetime.datetime.now()
print(Date)

# assigning year month and day to variable
year = Date.year
month = Date.month
day = Date.day
hour = Date.hour
minute = Date.minute
second = Date.second

# printing the required values
print('This is year',year)
print('and month is',month)
print('and date is ',day)

