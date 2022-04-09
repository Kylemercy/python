from datetime import datetime
 
# Getting current date and time

now = datetime.now()
 

string = datetime.ctime(now)
# representation of date and time
print (string)
