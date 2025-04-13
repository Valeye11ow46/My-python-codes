num1 = input('Enter a number: ')
num2 = input('Enter a second number: ')
if not num1.isdigit() or not num2.isdigit():
    print(ValueError)
multiply =int(num1) * int(num2)
print(f'Here is the answer: {multiply}')
