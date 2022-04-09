from datetime import datetime
 
# Getting current date and time

now = datetime.now()
 

string = datetime.replace(now,2017,3,25)
print(string.weekday())
print(string.ctime())
print (string)
