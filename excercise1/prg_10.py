num1 = int(input("enter number 1 :"))
num2 = int(input("enter number 2 :"))
num3 = int(input("enter number 3 :"))

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