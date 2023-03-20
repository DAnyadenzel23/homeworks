'''2. Напишите программу принимающую на вход список [1,2,3] и выводящую все возможные комбинации его членов.:
Ответ: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)'''

x = [1, 2, 3]
def perturbator(x):
    blank_lst = []
    blank_lst.append([x[0], x[1], x[2]])
    blank_lst.append([x[0], x[2], x[1]])
    blank_lst.append([x[1], x[2], x[0]])
    blank_lst.append([x[1], x[0], x[2]])
    blank_lst.append([x[2], x[0], x[1]])
    blank_lst.append([x[2], x[1], x[0]])
    return blank_lst
print(perturbator(x))

'''3. Изучите функцию permutations из itertools. Напишите программу выводящую все возможные варианты для списка [1,2,3]'''

from itertools import permutations
lst = [1, 2, 3]
print(list(permutations(lst)))


