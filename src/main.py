import datetime
b_day = datetime.date(year= 2000,month = 3,day = 24)
b_day2 = datetime.date(year = 1988,month= 5,day = 27)

if b_day < b_day2:
  print("Person one is older")
elif b_day > b_day2:
  print("Person two is older")
else:
  print("The ae both the same age")

