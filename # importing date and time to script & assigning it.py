# importing date and time to script & assigning it ot variable a 

from datetime import datetime
Date = datetime.now()
print(Date)

# assigning year month and day to variable
year = Date.year
month = Date.month
day = Date.day

# printing the required values
print(year)
print(month)
print(day)

# Printing in required format 
print(year,month,day,Date.hour,Date.minute,Date.second)