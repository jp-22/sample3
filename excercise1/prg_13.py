i = 0
lis=[]

for i in range(1,10):
    if i % 2 != 0:
        lis.append(i)
    i = i + 1
lis.reverse()
print(lis)