number1 = eval(input("Enter first number"))
number2 = eval(input("Entersecond number"))

operator = input("Enter operator")


def add(number1, number2):
    result = number1 + number2
    return result

def subtract(number1, number2):
    result = number1 - number2
    return result

def divide(number1, number2):
    result = number1 / number2
    return result
def multiply(number1, number2):
    result = number1 * number2
    return result
if operator == "+":
    add(number1, number2)
elif operator == "-":
    subtract(number1, number2)
elif operator == "/":
    divide(number1, number2)
elif operator == "x" or operator == "x" or operator == "x":
    multiply(number1, number2)



 
