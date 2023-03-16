a = int(input('enter 1st numb: '))
b = int(input('enter 2nd numb: '))
str_name = input('enter operation: ')

def func_1():
    if str_name == '+':
        print(a+b)
    elif str_name == '-':
        print(a-b)
    elif str_name == '*':
        print(a*b)
    elif str_name == '/':
        print(a/b)
    else:
        print('Чумачечий ввод')

func_1()


