num1 = float(input("İlk sayiyi giriniz: "))
num2 = float(input("İkinci sayiyi giriniz: "))
operation = input("+ - x / işlemlerinden istediğinizi giriniz: ")

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



