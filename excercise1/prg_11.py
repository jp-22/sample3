var = input("enter three numbers with , :")
var2 = var.split(',')
num1 = var2[0]
num2 = var2[1]
num3 = var2[2]


def maxnum(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("the largest number is ",num1)
    elif num2>num3 and num2>num1:
        print("the largest number is ",num2)
    else:
        print("the largest number is ", num3)


def minnum(num1,num2,num3):
    if num1<num2 and num1<num3:
        print("the smallest number is ",num1)
    elif num2<num3 and num2<num1:
        print("the smallest number is ",num2)
    else:
        print("the smallest number is ", num3)

maxnum(num1,num2,num3)

minnum(num1,num2,num3)