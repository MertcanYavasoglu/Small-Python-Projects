num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

if (num1 < 0 or num2 < 0):
    print("Error")
    quit()

if (num1 < num2):
    min = num1
    max = num2
elif (num2 < num1):
    min = num2
    max = num1
else:
    print("Error")
    quit()

for i in range(min+1, max):
    for j in range (1, i+1):
        if (j*j == i):
            print(i)
            break;


