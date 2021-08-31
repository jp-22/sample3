class c1:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b
    def result(self):
        print(self.a+self.b)

obj = c1(2,3)
obj.result()

