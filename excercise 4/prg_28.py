
l1 = ['a','b','c','d','e']
l2 = [1,2,3,4,5]
def createdict():
    d1 = {}
    for num1,num2 in zip(l1,l2):
        d1[num1] = num2


    print(d1)

createdict()












