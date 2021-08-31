import random

l1 = []
for i in range(15):
    l1.append(random.randint(1,100))

print(l1)
def evenno(num):
    if num%2==0:
        return True
filtered = filter(evenno,l1)

l2 = []
for s in filtered:
    l2.append(s)
print(l2)


def addfive(num):
    return num + 5

print(list(map(addfive,l2)))











