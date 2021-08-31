def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ or 1 for addition
- or 2 for subtraction
* or 3 for multiplication
/ or 4 for division
// or 5 for floor division
** or 6 for exponent

''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))
    number_3 = int(input('please enter the third number: '))

    if operation == '+' or operation == '1':
        add(number_1,number_2,number_3)

    elif operation == '-' or operation == '2':
        sub(number_1,number_2,number_3)

    elif operation == '*' or operation == '3':
        mul(number_1,number_2,number_3)

    elif operation == '/' or operation == '4':
        div(number_1,number_2)

    elif operation == '//' or operation == '5':
        fldiv(number_1,number_2)

    elif operation == '**' or operation == '6':
        exp(number_1,number_2)

    else:
        print('invalid argument')

def add(number_1,number_2,number_3):
    print(number_1+number_2+number_3)
def  sub(number_1,number_2,number_3):
    print(number_1-number_2-number_3)
def  mul(number_1,number_2,number_3):
    print (number_1*number_2*number_3)
def  div(number_1,number_2):
    print (number_1/number_2)
def fldiv(number_1,number_2):
    print (number_1//number_2)
def  exp(number_1,number_2):
    print (number_1**number_2)


calculate()