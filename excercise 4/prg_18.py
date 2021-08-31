import random
l1 = []
for i in range(10):
    l1.append(random.randint(0, 1))

print(l1)

if all(l1):
    print("all")
if any(l1):
    print("any")
else:
    print("none")




