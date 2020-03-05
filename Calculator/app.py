# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion


while True:
    which_function = input("Would you like to use the calculator or the converter or neither?")
    if which_function.lower() == 'calculator':
        while True:
            while True:
                num1 = (input('Enter first number: '))
                if num1.isdigit():
                    num1 = float(num1)
                    break
                else:
                    print('Make sure your first number is a number...')

            operator = (input('Enter operator: '))

            while True:
                num2 = (input('Enter second number: '))
                if num2.isdigit():
                    num2 = float(num2)
                    break
                else:
                    print('Make sure your second number is a number...')

            if operator == '+':
                print(num1 + num2)
                break
            elif operator == '-':
                print(num1 - num2)
                break
            elif operator == '*':
                print(num1 * num2)
                break
            elif operator == '/':
                print(num1 / num2)
                break
            else:
                print('Invalid Operator')

    elif which_function.lower() == 'converter':
        while True:
            c = (input('Temperature in celsius: '))
            if c.isdigit():
                c = float(c)
                print(str(c * 9 / 5 + 32) + ' degrees fahrenheit')
                break
            else:
                print('Please enter a number...')

    elif which_function.lower() == 'neither':
        print("Goodbye!")
        exit()

    else:
        print("Please answer with either 'calculator' or 'converter' or 'neither'")
