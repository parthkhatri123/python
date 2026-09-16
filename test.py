num1  = int(input('Enter number 1 = '))
num2  = int(input('Enter number 2 = '))

choice = input('Enter choice (+, -, *, /): ')

if choice == '+':
    result = num1 + num2
    print(f'The sum of {num1} and {num2} is: {result}')
elif choice == '-':
    result = num1 - num2
    print(f'The difference of {num1} and {num2} is: {result}')  
elif choice == '*':
    result = num1 * num2
    print(f'The product of {num1} and {num2} is: {result}') 
elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        print(f'The quotient of {num1} and {num2} is: {result}')
    else:
        print('Error: Division by zero is not allowed.')    
else:
    print('Invalid choice. Please enter a valid operator (+, -, *, /).')