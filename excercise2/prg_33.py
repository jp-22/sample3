class student():
    def __init__(self):
        self.name = input("enter your name : ")
        if self.name.isalpha()== False:
            print("invalid name")
        self.regno = input("enter yor regno. : ")
        if self.regno.isalnum()== False:
            print("invalid regno.")
        self.rollno = input("enter your rollno. : ")
        if self.rollno.isnumeric()== False:
            print("invalid rollno.")
        self.std = input("enter your std : ")
        if self.std.isnumeric()== False:
            print("invalid std.")
        self.admission_year = input("enter your admission year : ")
        if self.admission_year.isnumeric()== False:
            print("invalid admission year")
        self.marks = list()
        self.subjects = list()
        self.result = list()
        self.endresult= False

    def markgain(self):
        dic = {}
        for x in range(4):
            i = input("enter subjects : ")
            j = input("enter marks  : ")
            dic[i]=j

        self.subjects = list(dic.keys())
        self.marks = list(dic.values())

        print(dic)

        for i in (self.marks):
            if int (i)< 40:
                self.result.append("fail")
            else:
                self.result.append("pass")
            #print(self.result)

        if "fail" in self.result:
            self.endresult= "fail"
        else:
            self.endresult= "pass"

    def generateresult(self):
        print(f''' **************************************************************************************************
        Name : {self.name}
        Roll No : {self.rollno}                                      Standard : {self.std}
    ****************************************************************************************************
        Subject     Total marks     Passing marks        Obtained marks          Result
        {self.subjects[0]}          100             40                  {self.marks[0]}                   {self.result[0]}
        {self.subjects[1]}        100             40                  {self.marks[1]}                   {self.result[1]}
        {self.subjects[2]}            100             40                  {self.marks[2]}                   {self.result[2]}
        {self.subjects[3]}          100             40                  {self.marks[3]}                   {self.result[3]}

        ************************************************************************************************
        Total            400            160                {int(self.marks[0])+int(self.marks[1])+int(self.marks[2])+int(self.marks[3])}

        Result : {self.endresult}                     Percentage : {(int(self.marks[0])+int(self.marks[1])+int(self.marks[2])+int(self.marks[3]))/4}
''')
obj = student()
obj.markgain()
obj.generateresult()