import datetime
from dateutil import relativedelta

date_1 = datetime.date(2021, 7, 2)
date_2 = datetime.date(2032, 3, 24)


difference = relativedelta.relativedelta(date_2, date_1)

print('Complete Difference between two dates: ')
print(difference.years , ' years, ', difference.months, ' months and ', difference.days, ' days')