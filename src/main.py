from datetime import datetime
tday = datetime.now()
m_day = datetime.time(tday)
print(m_day,m_day.strftime("%p"))
#p help it shows either pm or am