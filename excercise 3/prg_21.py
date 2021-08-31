import datetime
from dateutil import relativedelta


date = datetime.date.today()
delta = date+relativedelta.relativedelta(days=+7)


print(delta)

