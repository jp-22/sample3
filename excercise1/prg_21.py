class c1():

    def sum(self,n1,n2):
        print(n1+n2)
    def minus(self,n1,n2):
        print(n1-n2)
class c2(c1):
    def multi(self,n1,n2):
        print(n1*n2)

obj = c2()
obj.sum(5,4)
# if object is created of child class then it can access every method of parent class but the visa versa is not true