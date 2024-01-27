def add(x, y):

    print(x+y)

def subtract(x, y):

    print(x-y)

def multiply(x, y):

    print(x*y)

def divide(x, y):

    result = 0

    try:
        result = x/y
    except ZeroDivisionError:
        result = 0
    print(result)

Continue = False

while Continue == False:

    first = input('Input first number: ')
    second = input('Input second number: ')

    if first.isdigit() == False:
        break
    
    if second.isdigit() == False:
        break

    print("Please enter an operator:\n 1) + \n 2) - \n 3) * \n 4) /")

    operator_answer = input()

    match operator_answer:
        case '+':
            add(float(first), float(second))
            break
        case '-':
            subtract(float(first), float(second))
            break
        case '*':
            multiply(float(first), float(second))
            break
        case '/':
            divide(float(first), float(second))
            break
        case _:
            print("Not an operator")
            Continue == True