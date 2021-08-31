import random
def generator(n):
    g = random.sample(range(n), 10)
    yield g

s = generator(100)
print(list(s))





