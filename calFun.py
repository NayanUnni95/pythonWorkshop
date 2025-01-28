# sample calculator project
def calculation(number1, number2, symbol):
    if symbol == '+':
        return (number1 + number2)
    elif symbol == '-':
        return (number1 - number2)
    elif symbol == '*':
        return (number1 * number2)
    elif symbol == '/':
        return (number1 / number2)
    elif symbol == '%':
        return (number1 % number2)
    else:
         return ("Invalid Operator...")


number1 = float(input("Enter first number : "));
number2 = float(input("Enter second number : "));
symbol = input("Enter the operator : ");
result = calculation(number1, number2, symbol)
print(result)
