import random
l1 = []
for i in range(10):
    l1.append(chr(random.randint(97,123)))

print(l1)
print("".join(l1))