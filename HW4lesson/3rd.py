'''Напишите функцию, которая принимает на вход список, а на выходе даёт список с поменяными местами
   первым и последним элементами списка, в списке минимум 2 элемента'''
lst =list(map(int, input('введите список: ').split()))
print(lst)
def change_lst(lst):
    lst[0],lst[-1] = lst[-1],lst[0]
    print(lst)
    return
change_lst(lst)
