import datetime
import time 
print( f"Today date and time is: \n{datetime.datetime.today()}")
print ("The current year is",datetime.date.today().strftime("%Y"))
print("The current month is:",datetime.date.today().strftime("%B"))
print("week number of the year is:",datetime.date.today().strftime("%W"))
print("weekday of the week is: ",datetime.date.today().strftime("%w"))
print("Day of the year is :", datetime.date.today().strftime("%j")," days")
print("Day in of the month is;",datetime.date.today().strftime("%D"))
print("Day in of the month is;",datetime.date.today().strftime("%d"))
print("Day in the week",datetime.date.today().strftime("%A"))