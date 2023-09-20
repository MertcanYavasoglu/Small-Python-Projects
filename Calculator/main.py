num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("+ - x / Enter any of the given operations: ")

if (operation == '+'):
    output = num1 + num2
elif (operation == '-'):
    output = num1 - num2
elif (operation == 'x'):
    output = num1 * num2
elif (operation == '/'):
    output = num1 / num2
else:
    output = "Error"

print(output)



