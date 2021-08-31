import datetime,calendar
l1 = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
c,d =calendar.monthrange(2021,8)
i = c
j = int(datetime.date(2021,8,d).weekday())


x = l1[i]
y = l1[j]
print(f'''first day of month is {x}''')
print(f'''last day of the month is {y}''')
