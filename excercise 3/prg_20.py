import datetime
from dateutil import relativedelta

curr_date = datetime.date.today()
date_2 = datetime.date(2001, 2, 22)


difference = relativedelta.relativedelta(curr_date, date_2)

print('your age :  ')
print(difference.years , ' years, ', difference.months, ' months and ', difference.days, ' days')