
def sum(num1,num2):
    if (isinstance(num1,int) and isinstance(num2,int)) or (isinstance(num1,float) and isinstance(num2,float)):
        print(num1+num2)
    else:
        print("both values should either be int or float")
sum(5,6.5)