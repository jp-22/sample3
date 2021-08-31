
l1 = []
a = int(input("tell the no. of elements you want to enter : "))
for i in range(a):
    j = int(input("enter value : "))
    l1.append(j)



if len(l1)<5:
    raise Exception("list length should be minimum 5")
else:
    print(l1)











