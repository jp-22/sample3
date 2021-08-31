class father():
    def a(self):
        print("this is parent 1")

class mother():
    def b(self):
        print("this is parent 2")


class child(father,mother):
    def c(self):
        print("this is child")

obj = child()
obj.a()




print("multi level")

class gr():
    def x(self):
        print("this is grandfather")

class fa(gr):
    def y(self):
        print("this is father")

class ch(fa):
    def z(self):
        print("this is child")


obje= ch()
obje.y()

