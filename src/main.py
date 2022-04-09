from datetime import datetime
 
# Getting current date and time

now = datetime.now()
 

string = datetime.isocalendar(now)
# Returns a tuple year, week, and weekday
print (string)
