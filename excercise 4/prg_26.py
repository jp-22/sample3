class student():

    rollno = 21
    std = 12
    name = "jay"

    def marks(self):
        marks = 54            #local
        print("std is",self.std)                      #global
        print("rollno is", self.rollno)                 #global
        print("name is ", self.name)                 #global
        print("marks is ",marks)               #global

obj = student()
obj.marks()

