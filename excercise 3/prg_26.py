import datetime,calendar

c = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
l1= []
l3 = []
l4 = []
x,y = calendar.monthrange(2021,9)
for i in range(x-1,y+1):
    j = int(datetime.date(2021,9,i).weekday())
    l1.append(j)



for i in l1:
    l3.append(c[i])





monday = l3.index("monday")
l4.append(f'''monday {monday+1}''')

tuesday = l3.index("tuesday")
l4.append(f'''tuesday {tuesday+1}''')

wednesday = l3.index("wednesday")
l4.append(f'''wednesday {wednesday+1}''')

thursday = l3.index("thursday")
l4.append(f'''thursday {thursday+1}''')

friday = l3.index("friday")
l4.append(f'''friday {friday+1}''')

saturday = l3.index("saturday")
l4.append(f'''saturday {saturday+1}''')

sunday = l3.index("sunday")
l4.append(f'''sunday {sunday+1}''')


print(l4)













# monday = 1
# tuesday = 2
# wednesday = 3
# thursday = 4
# friday = 5
# saturday = 6
# sunday = 7


