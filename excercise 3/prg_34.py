from tabulate import tabulate
class student:
    name = False
    regno = False
    rollno = False
    std = False
    admission_year = False
    marks = []
    result = False
    endresult = False

    def __init__(self,name,regno,rollno,std,admission_year):
        if type(name) == str and type(regno)== str and type(rollno)== str and  type(std)== str and type(admission_year)== str:
            if name.isalpha():
                self.name = name
            else:
                print("name must be in alphabets")

            if regno.isalnum():
                self.regno = regno
            else:
                print("regno shuld be alphanumeric")

            if rollno.isnumeric():
                self.rollno = rollno
            else:
                print("roll number should be numeric")

            if std.isnumeric():
                self.std = std
            else:
                print("std should be numeric")

            if admission_year.isnumeric():
                self.admission_year = admission_year
            else:
                print("admission year should be numeric")


        else:
            print("all inputs must be in string")

    def markgain(self,marks_dict):

        for key,val in marks_dict.items():

            res = {}
            if val<=100:
                if val < 40:
                    res[key] = (val,'fail')
                    # self.marks.append(res)
                else:
                    res[key] = (val,'pass')
                    # self.marks.append(res)
            else:
                print("marks should be less than 100")
            self.marks.append(res)


        reslis = []
        for mark in self.marks:
            for key_marks,val_marks in mark.items():
                reslis.append(val_marks[1])

        if 'fail' in reslis:
            self.result = "Fail"
        else:
            self.result = "Pass"



        if self.result== "Fail":
            self.percentage = '----'
        else:
            v = []
            for mark in self.marks:
                for key_mark,val_mark in mark.items():
                    v.append(val_mark[0])
                    self.percentage = sum(v) / len(self.marks)


    def gradecalc(self): #65
        if self.percentage == '----':
            self.grade = "F"
        elif self.percentage < 50:
            self.grade = "E"
        elif int(self.percentage) < 60:
            self.grade = "D"
        elif int(self.percentage) < 70:
            self.grade = "C"
        elif int(self.percentage) < 75:
            self.grade = "B"
        elif int(self.percentage) < 80:
            self.grade = "B+"
        elif int(self.percentage) < 85:
            self.grade = "A"
        elif int(self.percentage) < 90:
            self.grade = "A+"
        elif int(self.percentage) < 95:
            self.grade = "O"
        elif int(self.percentage) < 100:
            self.grade = "O+"

    def generateresult(self):
        v = []
        for mark in self.marks:
            for key_mark, val_mark in mark.items():
                v.append(val_mark[0])
        tm = 100
        pm = 40

        print("*"*100,"\n")

        print("Name :",(self.name),"\n")

        print("Roll No :", self.rollno ,            (" "*30),                        "Standard :", (self.std),"\n")

        print("*" * 100,"\n")

        data = []
        for mark in self.marks:
            for key_mark,val_mark in mark.items():
                data.append([key_mark,tm,pm,val_mark[0],val_mark[1]])

        data.append([])

        data.append(['Total',(tm*len(self.marks)),pm*len(self.marks),sum(v)])

        print(tabulate(data,headers=["Subject","Total marks","Passing marks","Obtained marks","Result"]))

        print("*" * 100, "\n")

        print("Result :" , (self.result),          (" "*30),           "Percentage :", (self.percentage),"\n")

        print("Grade  :", (self.grade))




obj = student("jay",'32','43','12','2001')
obj.markgain({'maths':14})
obj.markgain({'sci':76})
obj.gradecalc()
obj.generateresult()