import datetime
from dateutil import relativedelta


date = datetime.date.today()
delta = date+relativedelta.relativedelta(months=+1)


print(delta)
