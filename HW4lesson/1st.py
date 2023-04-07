a = int(input('enter 1st numb: '))
b = int(input('enter 2nd numb: '))
str_name = input('enter operation: ')

def func_1(*args):
    if str_name == '+':
        print(a+b)
    elif str_name == '-':
        print(a-b)
    elif str_name == '*':
        print(a*b)
    elif str_name == '/':
        if y ==0:
            print('На ноль делить нельзя')
        else:
            print(a/b)
    else:
        print('Чумачечий ввод')

func_1(a, b, str_name)


