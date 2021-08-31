
i = 0
lis = []
while i < 10:
    if i % 2 != 0:
        lis.append(i)
    i = i+1
lis.reverse()
print(lis)