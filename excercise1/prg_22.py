class c1():
#this is constructor

    def __init__(self):
        print("init method")

#this is destructor

    def __del__(self):
        print("del method")


obj=c1()
del obj