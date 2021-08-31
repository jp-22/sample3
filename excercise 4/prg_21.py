import random

l1 = []
for i in range(10):
    l1.append(random.randint(1,100))

print(l1)
def evenno(num):
    if num%2==0:
       return True

def oddno(num2):
    if num2%2!=0:
        return True


filtered1 = filter(oddno,l1)
filtered2 = filter(evenno,l1)
c = list(filtered1)
d = list(filtered2)
print("list of odd nos.",c)
print("list of even nos.",d)