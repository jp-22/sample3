import datetime
import calendar


i = calendar.day_name[datetime.date.today().replace(day=1).weekday()]


print(i)

