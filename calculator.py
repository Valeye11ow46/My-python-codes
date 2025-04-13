def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def square(x,y):
    return x ** y
print('your choice')
print('1:add')
print('2:subtract')
print('3:multiply')
print('4:divide')
print('5:square')
while True:
    choice = input('select choice 1/2/3/4/5: ')
    if choice in ('1', '2', '3', '4','5'):
        try:
            num1=float(input('enter first number: '))
            num2=float(input('enter second number: '))
        except ValueError:
            print('enter a number')
            continue
        if choice =='1':
            print(num1,  '+',  num2,  '=',  add(num1, num2))
        elif choice =='2':
            print(num1,  '-', num2, '=', subtract(num1, num2))
        elif choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))
        elif choice == '4':
            print(num1, '/', num2, '=', divide(num1, num2))
        elif choice == '5':
            print(num1, '**', num2, '=',square(num1, num2))
        next_calculation= input('do you want to do another calulation (yes/no): ')
        if next_calculation == 'no':
            break
        else:
            print('next calculation')

