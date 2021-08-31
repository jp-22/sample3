class c1():

    def __init__(self,a,b):
        print(f'''this is original constructor with parameters {a} and {b}''')
    def __init__(self,x,y):         #overloaded constructor
        print(f'''this is overloaded constructor with parameters {x} and {y}''')

    def orimethod(self,r,s):
        print(f'''this is original method with parameters {r} and {s}''')

    def orimethod(self,t,u):           #this is overloaded method
        print(f'''this is overloaded method with parameters {t} and {u}''')

obj = c1(1,2)

obj.orimethod("d","l")
