from datetime import datetime
 
# Getting current date and time

now = datetime.now()
 

string = datetime.timetuple(now)
#Returns an object of type time.struct_time
print (string)
