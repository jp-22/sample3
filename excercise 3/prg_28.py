import datetime
x = datetime.datetime.today().replace(day=1)
y = datetime.datetime.today().replace(day=31)

print(x.strftime("%d %b %y %H : %M : %S"))
print(y.strftime("%d %b %y %H : %M : %S"))