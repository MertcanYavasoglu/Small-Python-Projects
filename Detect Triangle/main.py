num1 = int(input("Enter first edge of the triangle: "))
num2 = int(input("Enter second edge of the triangle: "))
num3 = int(input("Enter third edge of the triangle: "))

if(num1+num2 > num3 > abs(num1-num2)):
    if(num1 == num2 == num3):
        print("The triangle you entered is an equilateral triangle!")
    elif(num1 == num2 or num1 == num3 or num2 == num3):
        print("The triangle you entered is an isosceles triangle!")
    else:
        print("The triangle you entered is a scalene triangle!")
else:
    print("A triangle cannot be formed with the numbers you entered.")
