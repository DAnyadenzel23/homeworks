q = int(input('Вводим имена: '))

list_names =[]
for i in range(q):
    list_names.append(input())
sort_list_names =sorted(list_names)
print(sort_list_names)

w = int(input('Вводим марки автомобилей: '))

list_cars =[]
for i in range(w):
    list_cars.append(input())
sort_list_cars = sorted(list_cars)
print(sort_list_cars)

from itertools import zip_longest
result = list(zip_longest(sort_list_cars, sort_list_names,fillvalue='Пролетел с машиной'))
print(result)