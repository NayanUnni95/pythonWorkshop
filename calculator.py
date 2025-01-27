# sample calculator project

number1 = float(input("Enter first number : "));
number2 = float(input("Enter second number : "));
symbol = input("Enter the operator : ");

if symbol == '+':
    print('Sum is', (number1 + number2));
elif symbol == '-':
    print('Difference is', (number1 - number2));
elif symbol == '*':
    print('Product is', (number1 * number2));
elif symbol == '/':
    print('Quotient is', (number1 / number2));
elif symbol == '%':
    print('Reminder is', (number1 % number2));
else:
    print("Invalid Operator");