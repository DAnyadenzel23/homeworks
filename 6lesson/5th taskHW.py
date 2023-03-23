'''Напишите функцию которая принимает на вход неограниченное количество аргументов, а на выходе возвращает их сумму.
 Используйте *args.'''
def sumatra(*args):
    ammount = 0
    for elem in args:
            ammount += elem
    return ammount

lst = []
a = int(input('enter numbs: '))
while a != 0:
    lst.append(a)
    a = int(input('enter numbs: '))
print(lst)

result = sumatra(*lst)
print('Result of ammount: ', result)
