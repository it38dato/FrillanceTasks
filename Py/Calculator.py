repeat="y"
while repeat == "y":
    numb1, numb2 = int(input("Enter number1: ")), int(input("Enter number2: "))
    operation = input("Enter the operation: ")
    if operation == '+':
        print(numb1 + numb2)
    elif operation == '-':
        print(numb1 - numb2)
    elif operation == '*':
        print(numb1 * numb2)
    elif operation == '/':
        if numb2 == 0:
            print('You cant divide by zero!')
        else:
            print(numb1 / numb2)
    else:
        print('Invalid operation')
    repeat = input("Do you want to continue? (y/n): ")
    if repeat == "n":
        break
    while (repeat!="y" and repeat!="n"):
        repeat = input("Please enter the correct answer (y/n): ")