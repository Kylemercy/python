from datetime import datetime
 
# Getting current date and time

now = datetime.now()
 

string = datetime.astimezone(now)
# Returns the DateTime object containing
# timezone information.
print (string)
