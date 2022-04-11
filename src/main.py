from datetime import datetime 
Christmas = datetime(month = 12,day = 25,year = 1)
today = datetime.today()
Christmas= Christmas.replace(year = datetime.today().year)
count = Christmas- today
print("There are ",count.days,"remaining till Christmas!")


