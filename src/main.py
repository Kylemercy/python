import datetime
tday = datetime.date.today()
tdelta = datetime.timedelta(days = 7)
bday = datetime.date(2022,5,14)
till_bday = (bday-tday)
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())