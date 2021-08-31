l1=[]
l2=[]
l3=[]

for i in range(1,9):
    l1.append(i)

print(l1)

for j in range(4,11):
    l2.append(j)

print(l2)

for i in l1:
    if i in l2:
        l3.append(i)

print(l3)

