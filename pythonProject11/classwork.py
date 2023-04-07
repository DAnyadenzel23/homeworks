x = 0
def outer():
    x = 1
    def inner():
        nonlocal x # nonlocal делает значение х релевантным не только для inner, но и для outer(global пользоваться нельзя!)
        x = 2
        print('inner: ',x)
    inner()
    print('outer: ',x)
outer()
print('global: ',x)
##inner:  2
##outer:  2
##global:  0

###Функции с аргументами
def hello(name, prefix = 'Hello, ', suffix = '!!!'):
    print('{}{}{}'.format(prefix, name, suffix))

hello(name='World')
##Hello, World!!!
hello('danya', 'hauhai, ','!)')# при неявном указании аргументов , сначала передастся значение пустому аргументу, а потом по очереди неуказанным
##hauhai, danya!)
hello(prefix = 'goodbay, ',name = 'world')# при явном указании аргументов очередность неважна
##goodbay, world!!!
def append_func(element,lst=[]):# с изменяемыми переменными типа списка и прочее при каждом вызове функции будет сохраняться измененная переменная

    lst.append(element)
    print(lst)
    return lst # return возвращает значение лст и при следующем выполнении функции на месте лст будет уже новый список
append_func('1')
append_func('2')
append_func('string')
##['1']
##['1', '2']
##['1', '2', 'string']

'''поозиционные и опциональные аргументы'''
#*args - позиционные
#**kwargs - опциональные
def print_c(arg1, arg2,*args,**kwargs):
    print(' '.join([arg1]+[arg2]+list(args)+list(kwargs.values())))
print_c('2', 'string4', '4', '6', key1 = 'bublik', key2 = 'korzhik')
##2 string4 4 6 bublik korzhik

'''Рекурсия - '''
def fact(n):#факториал
    return 1 if n==0 else n*fact(n-1)
print(fact(4))
##24

'''Напишите функцию, которая на входе принимает число, а на выходе возвращает ответ положительное, отрицательно или ноль'''

'''n = int(input('ввод числа: '))
def func(n):
    if n>0:
        print('Положительное')
    elif n<0:
        print('отрицательная')
    else:
        print('ноль')
    return
print(func(n))'''

