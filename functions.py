condition = input("Please enter the operation: ")
num1 = int(input("Please enter num1: "))
num2 = int(input("Please enter num2: "))


def add(num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1-num2


def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2


def operation(cond, a, b):
    if cond == "add":
        result = add(a, b)
    elif cond == "sub":
        result = sub(a, b)
    elif cond == "mul":
        result = mul(a, b)
    elif cond == "div":
        result = div(a, b)
    else:
        result = "Error, please enter valid operation" 
    
    return result


print(operation(condition, num1, num2))
