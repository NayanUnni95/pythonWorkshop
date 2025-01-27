num1 = 10  # integer
num2 = 10.5 # float
name1 = 'Nayan' # string
name2 = "Nayan SS" # string
isActive = True # boolean

# print(num1)

sum = num1 + num2
diff = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 % num2

# number1 = int(input("Enter first number : "))
# number2 = int(input("Enter second number : "))

# basic math operations
# print("Sum is ", (number1 + number2))
# print("Difference is ", (number1 - number2))
# print("Product is ", (number1 * number2))
# print("Quotient is ", (number1 / number2))
# print("Reminder is ", (number1 % number2))


#  list , tuple , set
names = ["Rahul", 'Amal', 'John']
# print(len(names))
names.append("Nayan")
# print(names)


# Dictionary
data = [
    {"name": "Nayan",
    "age": 20,
    "details" : {
        "gender" : "Male",
        "markInPer" : 89.9,
        "isStu" : True
    }},
    {"name": "Hari",
    "age": 20,
    "details" : {
        "gender" : "Male",
        "markInPer" : 99.9,
        "isStu" : True
    }}
]
# print(data[0]["name"])
# print(data[1]["name"])

# for details in data:
#     print(details)

age = input("Enter your name : ")
if int(age) > 18:
    print("your age is major")
else:
    print("Your are minor")