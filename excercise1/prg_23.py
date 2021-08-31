class c1():

    def eval(self,x,y):
        print(x+y)

    def eval(self,a,b):
        print(a*b)

# method overloading complete

class c2(c1):

    def eval(self,x,y):      #method overriding
        print(x-y)

obj= c1()     #overloading
# obj= c2()   ----->> overriding
obj.eval(5,2)
